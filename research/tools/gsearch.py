#!/usr/bin/env python3
"""gsearch — веб-поиск для агентов, когда встроенный WebSearch недоступен (лимит или запрет хуком).

Движок: Tavily (с 3.09.2026 вечера; до этого — Groq compound, снят по решению владельца: его синтезированный
ответ выдумывал источники). Печатает ТОЛЬКО сырые результаты (title / url / snippet / score). Сниппет — указатель:
цитировать можно то, что затем открыто по URL (curl / rfetch) и прочитано.

Использование:
  python3 gsearch.py "запрос" [--include arxiv.org github.com '*.edu'] [--exclude wikipedia.org]
                     [--n 10] [--depth basic|advanced] [--days N] [--json]
Ключи: TAVILY_API_KEY, TAVILY_API_KEY_2, TAVILY_API_KEY_3 — из окружения, иначе ~/.config/deep-research-atelier/env,
иначе ~/.config/saturation/env (строки `export KEY=...`). Ротация при 401/403/429/432/433.
"""
import argparse, json, os, sys, time, urllib.request, urllib.error
from pathlib import Path

ENV_FILES = (Path.home()/".config"/"deep-research-atelier"/"env", Path.home()/".config"/"saturation"/"env")

def load_keys():
    keys = []
    for name in ("TAVILY_API_KEY", "TAVILY_API_KEY_2", "TAVILY_API_KEY_3"):
        v = os.environ.get(name)
        if v: keys.append(v)
    if keys: return keys
    for p in ENV_FILES:
        if not p.exists(): continue
        for line in p.read_text().splitlines():
            line = line.strip()
            if line.startswith("export "): line = line[7:].strip()
            if line.startswith("TAVILY_API_KEY"):
                k, _, v = line.partition("=")
                v = v.strip().strip('"').strip("'")
                if v: keys.append(v)
        if keys: return keys
    sys.exit("gsearch: нет TAVILY_API_KEY (окружение или ~/.config/deep-research-atelier/env)")

def search(query, include=None, exclude=None, n=10, depth="basic", days=None):
    body = {"query": query, "max_results": max(1, min(int(n), 20)), "search_depth": depth}
    if include: body["include_domains"] = include
    if exclude: body["exclude_domains"] = exclude
    if days:
        body["time_range"] = "day" if days <= 1 else "week" if days <= 7 else "month" if days <= 31 else "year"
    last = None
    for key in load_keys():
        req = urllib.request.Request("https://api.tavily.com/search", data=json.dumps(body).encode(), method="POST",
                                     headers={"Content-Type": "application/json", "Authorization": "Bearer " + key,
                                              "User-Agent": "Mozilla/5.0 (compatible; deep-research-atelier/0.1)"})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                resp = json.load(r)
            out = [{"title": x.get("title", ""), "url": x.get("url", ""), "snippet": (x.get("content") or "")[:600],
                    "score": x.get("score"), "date": x.get("published_date")} for x in resp.get("results", [])]
            return out
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}"
            if e.code in (401, 403, 429, 432, 433):
                time.sleep(1); continue
            sys.exit(f"gsearch: {last}: {e.read().decode(errors='replace')[:300]}")
        except Exception as e:
            last = str(e)[:200]; time.sleep(2)
    sys.exit(f"gsearch: все ключи Tavily отказали ({last})")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--include", nargs="*"); ap.add_argument("--exclude", nargs="*")
    ap.add_argument("--n", type=int, default=10); ap.add_argument("--depth", default="basic", choices=["basic", "advanced"])
    ap.add_argument("--days", type=int); ap.add_argument("--json", action="store_true")
    ap.add_argument("--model", help="игнорируется (совместимость со старым интерфейсом)")
    ap.add_argument("--country", help="игнорируется (совместимость)")
    a = ap.parse_args()
    res = search(a.query, a.include, a.exclude, a.n, a.depth, a.days)
    if a.json:
        print(json.dumps({"query": a.query, "engine": "tavily", "results": res}, ensure_ascii=False, indent=1))
    else:
        print(f"# gsearch (tavily/{a.depth}): {len(res)} результатов — сниппет лишь указатель; открывай URL и цитируй источник")
        for i, x in enumerate(res, 1):
            sc = f"{x['score']:.2f} " if isinstance(x.get('score'), (int, float)) else ""
            print(f"{i}. {sc}{x['title']}\n   {x['url']}\n   {x['snippet'][:300].replace(chr(10), ' ')}")
    sys.exit(0 if res else 2)
