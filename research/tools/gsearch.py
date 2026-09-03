#!/usr/bin/env python3
"""gsearch — веб-поиск для агентов через Groq compound (движок Tavily), когда лимит WebSearch исчерпан.

Печатает ТОЛЬКО сырые результаты поиска (title / url / snippet). Синтезированный ответ модели
намеренно не печатается: в пробе 3.09.2026 он выдумал препринт и слайды. Цитировать можно только то,
что затем открыто по URL (curl / WebFetch) и прочитано.

Использование:
  python3 gsearch.py "запрос" [--include arxiv.org github.com '*.edu'] [--exclude wikipedia.org]
                     [--model compound-mini|compound] [--json] [--n 10]
Ключ: переменная GROQ_API_KEY, иначе ~/.config/saturation/env (строка `export GROQ_API_KEY=...`; права 600, вне всех
репозиториев — решение коллеги saturation-cf 3.09.2026: файлов .env в рабочих каталогах не держим).
"""
import argparse, json, os, sys, urllib.request, urllib.error
from pathlib import Path

def load_key():
    k = os.environ.get("GROQ_API_KEY")
    if k: return k
    p = Path.home()/".config"/"saturation"/"env"
    if p.exists():
        for line in p.read_text().splitlines():
            line = line.strip()
            if line.startswith("export "): line = line[7:].strip()
            if line.startswith("GROQ_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("gsearch: нет GROQ_API_KEY (переменная окружения или ~/.config/saturation/env)")

def search(query, include=None, exclude=None, model="compound-mini", country=None):
    body = {"model": f"groq/{model}",
            "messages": [{"role": "user", "content":
                "Use the web search tool for exactly this query and then reply with the single word DONE: " + query}]}
    ss = {}
    if include: ss["include_domains"] = include
    if exclude: ss["exclude_domains"] = exclude
    if country: ss["country"] = country
    if ss: body["search_settings"] = ss
    req = urllib.request.Request("https://api.groq.com/openai/v1/chat/completions",
                                 data=json.dumps(body).encode(), method="POST",
                                 headers={"Content-Type": "application/json", "Authorization": "Bearer " + load_key(),
                                          "User-Agent": "curl/8.7.1", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            resp = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"gsearch: HTTP {e.code}: {e.read().decode()[:500]}")
    if "error" in resp:
        sys.exit("gsearch: " + json.dumps(resp["error"]))
    msg = resp["choices"][0]["message"]
    out = []
    for t in msg.get("executed_tools") or []:
        sr = t.get("search_results") or {}
        res = sr.get("results") if isinstance(sr, dict) else sr
        for x in res or []:
            out.append({"title": x.get("title", ""), "url": x.get("url", ""),
                        "snippet": (x.get("content") or "")[:600], "score": x.get("score")})
    usage = resp.get("usage") or {}
    return out, usage.get("total_tokens")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--include", nargs="*")
    ap.add_argument("--exclude", nargs="*")
    ap.add_argument("--model", default="compound-mini", choices=["compound-mini", "compound"])
    ap.add_argument("--country")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--n", type=int, default=10)
    a = ap.parse_args()
    res, tok = search(a.query, a.include, a.exclude, a.model, a.country)
    res = res[:a.n]
    if a.json:
        print(json.dumps({"query": a.query, "results": res, "groq_tokens": tok}, ensure_ascii=False, indent=1))
    else:
        print(f"# gsearch: {len(res)} результатов (groq tokens {tok}); текст модели отброшен намеренно — открывай URL и цитируй источник")
        for i, x in enumerate(res, 1):
            print(f"{i}. {x['title']}\n   {x['url']}\n   {x['snippet'][:300].replace(chr(10),' ')}")
