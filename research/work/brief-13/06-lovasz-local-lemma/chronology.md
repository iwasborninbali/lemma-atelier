# Кейс 06. Локальная лемма Ловаса (Эрдёш–Ловас, 1975)
## Стадия 2 регламента: лента, противоречия, «за неделю до», черновик таблицы брифа, ответ на kill-gate

Дата сборки: 2026-09-03. Вход: проверенные факты стадии 1 (три сборщика + сверяющий агент).
Регламент: `/Users/iwasborninbali/projects/moves/research/00-PROTOCOL.md`, §3–§4, §8 (стадия 2).
Правило стадии: **противоречия помечаются, не разрешаются**; **пустое записывается как пустое**
и не заполняется из ретроспективы (§8, абзац о стадиях).

**Состав ленты.** Включены факты со статусом `verified` (20) и `corrected` (12); один факт со статусом
`unverified` включён с явной пометкой. Фактов со статусом `refuted` во входе **нет ни одного** — см. §1.4.

**Границы источниковой базы (важно для чтения всей ленты).** Вся контемпоральная база кейса до 1977 года
держится на **одном** документе — печатной статье 1975 года. Черновиков, переписки, тетрадей, стенограммы
доклада 1973 года не найдено (см. §3). Всё, что в ленте датировано ранее 1975 года, — это либо ссылки
внутри самой статьи 1975 года, либо каталожные записи, либо позднейшие ретроспективы.

**Условные обозначения.** `kind`: `contemporaneous` — документ времени описываемого события;
`retrospective` — рассказ участника задним числом; `secondary` — позднейшая работа/каталог о событии.
`status`: `verified` — проверено сверяющим независимо; `corrected` — проверено и исправлено против
версии сборщика; `unverified` — не проверено по существу. Локальные копии — в
`/private/tmp/claude-501/-Users-iwasborninbali-saturation/e5097638-8685-4abc-aa31-61c23e004964/scratchpad/b13/sources/`.
Ниже эта директория сокращается до `sources/`.
Скан первоисточника: `sources/EL75_original.pdf` (MD5 a0183f21fb05c8d7621b78b48442ad30, 19 стр. = стр. 609–627,
OCR OmniPage 12), OCR — `sources/EL75_original.txt`.

---

# 1. Лента по датам

## 1.1. До статьи (1936–1974) — всё известно только через ссылки статьи 1975 года и каталоги

**L01 — 1936 (анонс) и 1937 (полная статья). Miller вводит property B.**
Факт: работа E. W. Miller, «On a property of families of sets», C. R. Soc. Sci. Lett. Varsovie, Cl. III 30,
31–38 (1937) (Zbl 0017.30003 / JFM 63.0832.01), предварительный анонс того же названия — Bull. Amer. Math.
Soc. 42, 333 (1936) (JFM 62.0048.23). Это та работа, на которую EL75 ссылается как на первое систематическое
изучение семейств множеств с хроматическим числом 2.
Источник/локатор: zbMATH Open, записи Zbl 0017.30003, JFM 63.0832.01, JFM 62.0048.23; поиск
`au:Miller ti:"property" py:1930-1945` (3 документа). Копия: `sources/lll_zbmath_miller_search.html`.
kind: `secondary` · status: `verified`
Оговорка сверяющего: сама статья Миллера не открывалась; это каталожная запись, не первоисточник.
Прямые запросы к zbmath.org сегодня дают 403.

**L02 — 1961, 1963, 1964. Предшествующая линия Эрдёша по property B (изложена в докладе Спенсера).**
Факт: [3] P. Erdős, «On a combinatorial problem I», Nordisk Mat. Tidskr. 11 (1963), 5–10 — Theorem 1:
«Let {A_i}, 1 ⩽ i ⩽ k be a family F of finite sets, |A_i| = α_i ⩾ 2. If Σ_{i=1}^{k} 1/2^(α_i) ⩽ 1/2 …
holds, then F has property B» — простой просеивающий довод (union bound), структуру зависимостей не
учитывающий; отсюда m(n) > 2^(n−1). [4] P. Erdős, «On a combinatorial problem II», Acta Math. Acad. Sci.
Hungar. 15 (1964), 445–447 — верхняя граница m(n) < n²·2^(n+1), откуда lim m(n)^(1/n) = 2. Вопрос о m(p)
Эрдёш ставит, ссылаясь на совместную с Хайналом работу о property B.
Источник/локатор: J. Spencer, доклад памяти Эрдёша «erdos99mytalk», §4 «On a Combinatorial Problem, 1963,
1964», с. 7–8 документа; References [2],[3],[4]. `https://cs.nyu.edu/~spencer/papers/erdos99mytalk.pdf`;
копии `sources/e99p6-06.png`, `sources/lll_spencer_erdos99.txt`.
kind: `retrospective` · status: `corrected`
Что исправлено: (а) «Graph Theory and Probability II», Canad. J. Math. 13 (1961), 346–352 значится у
Спенсера ([2]) за одним Эрдёшем, не за парой Erdős–Hajnal (сборщик 1 ошибся); фраза «Hajnal and I [2]» —
цитата Эрдёша с его собственной нумерацией; (б) условие теоремы напечатано Σ 1/2^(α_i) ⩽ 1/2, а не
«Σ 1/2^{|A_i|−1} < 1»; (в) слова Эрдёша и комментарий Спенсера разделены.
Датировка самого документа: имя файла `erdos99mytalk`, но `pdfinfo` даёт CreationDate 26.06.2003.

**L03 — 1964. Год статьи Erdős II по независимому каталогу.**
Факт: P. Erdős, «On a combinatorial problem. II», Acta Math. Acad. Sci. Hung. 15, 445–447 датируется
zbMATH 1964 годом (Zbl 0201.33704), а не 1969, как напечатано в библиографии EL75 (ссылка [5]). Тот же
1964 год независимо даёт Спенсер ([4] его списка литературы).
Источник/локатор: zbMATH Open, Zbl 0201.33704; Spencer, erdos99mytalk, References [4]. Копии:
`sources/lll_zbmath_erdos_search.html`, `sources/lll_spencer_erdos99.txt`.
kind: `secondary` · status: `verified`
→ противоречие C04.
Побочная деталь сверяющего: в том же поиске есть отдельная Erdős, «On a combinatorial problem. III»,
Can. Math. Bull. 12, 413–416 (1969) (Zbl 0199.31801) — вероятный источник смешения годов.

**L04 — 1964 (Erdős) и 1964 (Schmidt). Непосредственные предшественники количественных границ.**
Факт: EL75 приводит границы для m_2(r) (общий, не simple случай) со ссылками [5] и [9]:
[5] P. Erdős, «On a combinatorial problem II», Acta Math. Hung. 15 (1969), 445–447 — **так напечатано**;
[9] W. M. Schmidt, «Ein kombinatorisches Problem von P. Erdős and A. Hajnal», ibid, 373–374 (тот же том 15).
Источник/локатор: EL75, стр. 610 (текст «It is known [5], [9]») и стр. 627 (список литературы).
Скан стр. 627 — `sources/pref-19.png`, сверен визуально при 150 dpi.
kind: `contemporaneous` · status: `verified`

**L05 — 1966–1974. Прочие предшественники, процитированные статьёй.**
Факт: полный список литературы EL75 — девять позиций (стр. 626–627): [1] M. Calczynska-Karlovicz,
«Theorem on families of finite sets», Bull. Acad. Polon. Sci. 12 (1964), 87–89; [2] D. Lubell, «A short
proof of Sperner's Lemma», J. Comb. Th. 1 (1966), 1299; [3] P. Erdős – S. Shelah, «Separability properties
of almost disjoint families of sets», Israel J. of Math. 12 (1972), 207–214; [4] P. Erdős – A. Hajnal,
«On chromatic number of graphs and finite set-systems», Acta Math. Acad. Sci. Hung. 17 (1966), 61–99;
[6] L. Lovász, «Graphs and hypergraphs», Beiträge zur Graphentheorie, Leipzig, 1967, 99–106;
[7] D. R. Woodall, «Property B and the four colour problem», to appear (на момент печати не вышла);
[8] M. Deza, «Solution d'un problème de Erdős – Lovász», J. Comb. Theory 16 (1974), 166–167.
Источник/локатор: EL75, стр. 626 ([1]–[4]) и 627 ([5]–[9]); сканы `sources/pref-18.png`, `sources/pref-19.png`.
kind: `contemporaneous` · status: `verified`

**L06 — начало 1970-х (ТОЛЬКО по свидетельству 2014/2015; документа нет). Неопубликованная записка Ловаса.**
Факт: «The idea of the Local Lemma was first circulated by Lovász in the early 1970s in an unpublished note.
It was published by Erdős and Lovász in [10]. The general form below is also due in unpublished form to
Lovász and was given by Spencer in [27].»
Источник/локатор: D. Achlioptas, F. Iliopoulos, arXiv:1406.0242v3, Introduction, с. 1 (строки 39–41
извлечённого текста); References [10] = EL75, [27] = Spencer 1977. Копия: `sources/achlioptas_iliopoulos.txt`.
kind: `secondary` (работа 2014/2015 года о событии начала 1970-х) · status: `verified`
**Пометка ленты:** в ленте эта запись стоит на месте события ради читаемости, но **документом времени
работы не является**. Самой записки не найдено ни сборщиками, ни сверяющим (см. §3 и §5). Год у
Achlioptas–Iliopoulos не назван вовсе. → противоречие C09.

## 1.2. Конференция и статья (1973–1975)

**L07 — 1973 (конференция) / 1975 (публикация). Выходные данные.**
Факт: титульный лист — «COLLOQUIA MATHEMATICA SOCIETATIS JÁNOS BOLYAI 10. INFINITE AND FINITE SETS,
KESZTHELY (HUNGARY), 1973.» Сборник посвящён 60-летию Пала Эрдёша (род. 1913); издание North-Holland, 1975;
редакторы A. Hajnal, R. Rado, V. T. Sós; статья на стр. 609–627 — во второй части (Vol. II).
Источник/локатор: EL75, стр. 609 (шапка), скан `sources/lll_page01-01.png`; библиозаписи Moser–Tardos
(arXiv:0903.0544v3, References [EL75]) и Achlioptas–Iliopoulos (arXiv:1406.0242v3, References [10]).
kind: `contemporaneous` (титульный лист) + `secondary` (библиозаписи) · status: `verified`
Доработка сверяющего: запись A–I снимает мнимое противоречие «том 10 против Vol. II» — 10 это номер тома
серии Bolyai, Vol. II — вторая часть сборника (в третьей части, стр. 1051–1079, вышла Lovász–Plummer).
Не согласуется только «11» → противоречие C03.
**Пустое:** точная дата (день/месяц) конференции в источниках не указана.

**L08 — 1975, стр. 609. Названный концептуальный предшественник.**
Факт: «As far as we know families of sets with chromatic number 2 were first investigated systematically by
M i l l e r (who used the term property B) in the case of infinite edges. There now is a large literature of
this subject both for finite and infinite sets.» Ссылка дана только по фамилии (набранной вразрядку), без
номера в библиографии и без года.
Источник/локатор: EL75, стр. 609, третий абзац; скан `sources/lll_page01-01.png`, OCR `sources/EL75_original.txt`.
kind: `contemporaneous` · status: `verified` → противоречие C10 (дата Миллера).

**L09 — 1975, стр. 610. Постановка: что известно и где разрыв (клетка «нужда»).**
Факт: введены m_k(r) — минимальное число рёбер (k+1)-хроматического r-однородного гиперграфа, и n*_k(r),
m*_k(r) — то же для **простого** (любые два ребра пересекаются не более чем по одной точке) гиперграфа.
Известное ДО статьи для непростого случая: (r/(r+2))·2^(r−1) ⩽ m_2(r) ⩽ r²·2^r (ссылки [5],[9]).
Theorem 1: lim r-корень из n*_k(r) = k, lim r-корень из m*_k(r) = k²; «Thus in particular,
c₁·4^r/r³ < m*_2(r) < c₂·r⁴·4^r, i.e. m*_2(r) is much larger then m_2(r)» (печатная опечатка «larger then»
сохранена).
Источник/локатор: EL75, стр. 610 (Theorem 1 и следующая за ней формула); скан `sources/lll_page02-02.png`,
сверен визуально при 150 dpi.
kind: `contemporaneous` · status: `corrected`
Что исправлено: у сборщика 2 стояло «Mk(r)/mk(r)» — в оригинале m_k(r) и n*_k(r), m*_k(r), заглавной M нет;
у сборщика 1 неравенство с c₁,c₂ выдано за саму Theorem 1 — оно идёт после неё как следствие
(«Thus in particular»). → противоречие C05 (расхождение с авторским рефератом).

**L10 — 1975, стр. 616. Сама лемма (клетка «модель»).**
Факт: раздел «2.» (без названия) содержит безымянную «Lemma»: G — конечный граф с максимальной степенью d
и вершинами v_1,…,v_n; с v_i связано событие A_i; при (3) P(A_i) ⩽ 1/(4d) следует (4) P(Ā_1…Ā_n) > 0.
Доказательство — индукция по n с усилением (5) P(A_1 | Ā_2…Ā_n) ⩽ 1/(2d); в индукционном шаге v_2,…,v_q —
вершины, смежные с v_1 (q ⩽ d+1), и оценка снизу 1 − (q−1)/(2d) ⩾ 1/2.
Дословно: «2. Lemma. Let G be a (finite) graph with maximum degree d and vertices v_1, . . . , v_n. Let us
associate an event A_i with v_i (i = 1, . . . , n) and suppose that A_i is independent of the set
{A_j: (v_i, v_j) ∈ E(G)}. Also suppose (3) P(A_i) ⩽ 1/4d. Then (4) P(Ā_1 . . . Ā_n) > 0. Proof. We prove
more, namely that (5) P(A_1 | Ā_2 . . . Ā_n) ⩽ 1/2d.»
Источник/локатор: EL75, стр. 616–617, раздел «2.», формулы (3)–(5); сканы `sources/lll_lemma_page-08.png`
(616), `sources/lll_lemma_page-09.png` (617).
kind: `contemporaneous` · status: `corrected`
Что исправлено: оба сборщика пересказали условие как «независимость от всех НЕсоседних по G событий»,
тогда как оригинал печатает «∈ E(G)» (соседних) — см. L11.

**L11 — 1975, стр. 616 против 617–618. ВНУТРЕННЕЕ ПРОТИВОРЕЧИЕ ПЕРВОИСТОЧНИКА.**
Факт: в формулировке леммы (стр. 616) напечатано, что A_i независимо от {A_j : (v_i,v_j) ∈ E(G)} — то есть
от событий в **соседних** вершинах; но и доказательство (стр. 617: «P(A_1 Ā_2…Ā_q | Ā_{q+1}…Ā_n) ⩽
P(A_1 | Ā_{q+1}…Ā_n) = P(A_1)», где v_2,…,v_q — соседи v_1), и применение (стр. 618: «A_i is independent of
the set of all A_j's such that E_i ∩ E_j = φ, i.e. (v_i,v_j) ∉ E(G)») требуют независимости от **НЕсоседних**.
В печатной формулировке стоит «∈» там, где по смыслу «∉» — опечатка первоисточника.
Источник/локатор: EL75, стр. 616 против 617–618; перерендер строки при 400 dpi — `sources/lemma_zoom2-08.png`
(на 616 знак ∈ без косой черты), `sources/p618-10.png` (на 618 знак ∉ с чертой).
kind: `contemporaneous` · status: `verified`
Пометка: находка сверяющего агента; ни один из трёх сборщиков её не заметил, современные пересказы молча
исправляют «∈» на «∉». → противоречие C01 (главное).

**L12 — 1975, стр. 617–618. Первое применение леммы: Theorem 2 и Corollary 1 (клетка «нужда»).**
Факт: при случайной равновероятной k-раскраске точек r-однородного гиперграфа событие A_i = «ребро E_i
монохромно» имеет P(A_i) = 1/k^(r−1); G — рёберный граф (line-graph) H, максимальная степень d ⩽ k^(r−1)/4,
условие (3) выполнено, лемма даёт P(Ā_1…Ā_m) > 0, значит H k-раскрашиваем. Отсюда «Corollary 1. If each
point of an r-uniform hypergraph H has degree ⩽ k^(r−1)/4r then the chromatic number of H is ⩽ k.»
Источник/локатор: EL75, стр. 617 (Proof of Theorem 2) — 618 (Corollary 1); сканы
`sources/lll_lemma_page-09.png`, `sources/p618-10.png`.
kind: `contemporaneous` · status: `corrected`
Что исправлено: сборщик 1 привёл Corollary 1 как «has degree ≤ kr^{-1}/4r then the chromatic number of H
is < k» — в оригинале «⩽ k^(r−1)/4r … is ⩽ k» (нестрогие неравенства, показатель r−1).

**L13 — 1975, стр. 616. Форма леммы в статье — только симметричная (клетка «нужда»).**
Факт: формула (3) — P(A_i) ⩽ 1/(4d) — симметричная невзвешенная версия: одна и та же граница p и одна и та
же максимальная степень d для всех событий. Никакой весовой функции x: A → (0,1), никакой асимметричной
формулировки, никакой константы e в контексте леммы в полном тексте статьи 1975 года нет.
Источник/локатор: EL75, стр. 616, формула (3); проверка по всему OCR `sources/EL75_original.txt`.
kind: `contemporaneous` · status: `verified`
Проверка при сборке ленты (повторена мной): `grep -ic "Gamma"` по OCR → 0.
**Это ключевой факт для разбора атрибуций** → противоречие C02.

**L14 — 1975, стр. 617–619. Лемма применяется в статье трижды; оформлена как рядовая вспомогательная.**
Факт: применения — Theorem 2 (стр. 617–618), Theorem 3 (стр. 618: «holds, and the lemma implies that
P(Ā_1…Ā_m) > 0»), Theorem 4 (стр. 619: «then we can conclude as in the two previous cases»). При этом слово
«Lemma» встречается в статье 7 раз и относится к ТРЁМ разным безымянным вспомогательным леммам:
вероятностной (стр. 616), лемме о клике-заострении теоремы Calczynska-Karlowicz (стр. 621) и ещё одной
технической (стр. ~624).
Источник/локатор: EL75, стр. 616, 617, 618, 619, 621, ~624; `grep -in "lemma"` по полному OCR — 7 вхождений.
kind: `contemporaneous` · status: `corrected`
Что исправлено: сборщик 1 утверждал, что лемма «вынесена как отдельный инструмент общего назначения» —
формально она оформлена ровно так же, как две другие безымянные вспомогательные леммы статьи; выделяет её
только кратность применения. Сборщик 2 писал «все три появления 'Lemma' безымянны» — вхождений 7,
а безымянных лемм три разных.
Проверка при сборке ленты (повторена мной): `grep -ic "lemma"` по OCR → 7. → противоречие C12.

**L15 — 1975, стр. 619. Третье применение: гипотеза Штрауса на решётке (клетка «носитель 2», внутренний).**
Факт: «Theorem 4. Let ε > 0, k ⩾ 2, n ⩾ 1. Then there is an r_0 = r_0(k, ε) such that if S is any set of
lattice points in the n-dimensional space with |S| = r ⩾ r_0 then the lattice points can be k-colored so
that each set S + a obtained by translating S with an integer vector a contains at least (1 − ε) r/k points
of any given color.» В доказательстве P(A_i) < (1−δ)^r, каждая копия S пересекается менее чем с r² другими,
и «Thus if (1 − δ)^r < 1/4r² then we can conclude as in the two previous cases».
Источник/локатор: EL75, стр. 619 (Theorem 4 и доказательство); постановка задачи Штрауса и анонс
(«We also prove the stronger version of Strauss' conjecture (Theorem 4.)») — стр. 611. Скан `sources/p619-11.png`.
kind: `contemporaneous` · status: `corrected`
Что исправлено (у сборщика 2): (а) Theorem 4 на стр. 619, не 618; (б) это ТРЕТЬЕ применение, не второе;
(в) цитата «contains at least (1 − e) k/… points» искажена — в оригинале (1−ε)r/k; (г) неравенство строгое.

**L16 — 1975, весь текст. Имени «локальная лемма» в первоисточнике нет (клетка «опознание»).**
Факт: словосочетание «local lemma» в тексте 1975 года не встречается ни разу; утверждение называется просто
«Lemma». Современного имени «Lovász Local Lemma» в первоисточнике нет.
Источник/локатор: EL75, стр. 609–627; `grep -i "local"` по полному OCR — 0 вхождений.
kind: `contemporaneous` · status: `verified`
Проверка при сборке ленты (повторена мной): `grep -ic "local"` по `sources/EL75_original.txt` → **0**.

**L17 — 1975, весь текст. Ни заявления о новизне приёма, ни атрибуции, ни благодарностей.**
Факт: полный текст не содержит ни заявления о новизне вероятностной техники раздела «2.», ни ссылки на чужую
работу как на источник самого приёма, ни благодарностей — лемма вводится без пояснений о происхождении.
Контраст: там, где авторы опираются на чужой метод, они это пишут прямо (стр. 621: «This is a sharpening of
a theorem of Calczynska-Karlowicz. The proof uses a method due to Lubell [2].»).
Источник/локатор: EL75, стр. 609–627 (полный текст), контрольный пример — стр. 621;
`sources/EL75_original.txt`, строки 561–567.
kind: `contemporaneous` · status: `verified`

**L18 — 1975, стр. 626. «Added in proof»: устное сообщение Бека.**
Факт: «Added in proof. Recently J. Beck (Budapest) proved that m(r)/2^r → ∞ (oral communication).» На момент
печати Й. Бек устно улучшил асимптотику для m(r) (общий, не simple случай); использовал ли он ту же лемму —
статья не говорит.
Источник/локатор: EL75, стр. 626, между концом текста и REFERENCES; скан `sources/pref-18.png`.
kind: `contemporaneous` · status: `verified`
Проверка при сборке ленты (повторена мной): строка 813 OCR — «Added in proof. Recently J . Beck (Budapest)
proved that m(r)/2 r». Перекличка: тот же Й. Бек в 1991 г. даст первую алгоритмическую версию (L24).

**L19 — 1975. Авторский реферат (Autorreferat) в Zentralblatt даёт ДРУГУЮ форму главной границы.**
Факт: реферат Zbl 0315.05117, подписанный «Autorreferat» (то есть написанный самими авторами), печатает
симметризованное «We prove (1) c₁ 4ⁿ/n⁴ < f(n) < c₂ 4ⁿ n⁴. It would be desirable to have an asymptotic
formula for f(n).» — f(n) вместо m*_2(r), n⁴ в обеих частях, тогда как в самой статье в нижней части r³.
Источник/локатор: Zentralblatt für Mathematik, Zbl 0315.05117; скан оригинальной страницы Zentralblatt,
с. 46, поз. 05117, подпись «Autorreferat». Копии: `sources/lll_zbmath_scan046.gif`, `sources/lll_zbmath_0315.05117.html`.
kind: `contemporaneous` · status: `verified` → противоречие C05.

## 1.3. После статьи (1977–2020)

**L20 — 1977. Spencer, «Asymptotic lower bounds for Ramsey functions» — первое чужое применение
(клетки «носитель 2» и «проигрыш» одновременно).**
Факт: авторский реферат: «A probability theorem, due to Lovasz, is used to derive lower bounds for various
Ramsey functions. A short proof of the known result R(3, t) ⩾ ct²/(ln t)² is given.» Отсюда: (а) Спенсер
приписывает вероятностную теорему **Ловасу одному**, не Эрдёшу–Ловасу; (б) применяет её к нижним границам
рамсеевских функций; (в) для R(3,t) получает не новую границу, а **короткое доказательство уже известного**
результата ct²/(ln t)².
Источник/локатор: Discrete Mathematics 20 (1977), 69–76, DOI 10.1016/0012-365X(77)90044-9; Abstract на
странице ScienceDirect, архивная копия Wayback от 21.04.2024. Копия: `sources/spencer1977_sciencedirect_wayback20240421.html`
(дробь ct²/(ln t)² восстановлена из встроенного JSON: «nu»=ct², «de»=(ln t)²).
kind: `contemporaneous` · status: `verified`
Пометка: находка сверяющего; все три сборщика записали Spencer 1977 в not_found. **Полный текст статьи
по-прежнему не получен** (403 и на ScienceDirect, и через Wayback) — дословной формулировки «ep(d+1) ⩽ 1»
в её первой публикации никто не читал. → снимает противоречие C08.

**L21 — 1977 (год не подтверждён независимо). Усиленная симметричная форма с константой e.**
Факт: по вторичному изложению — «Lemma I (Lovász and Erdős 1973; published 1975) If 4 p d ≤ 1 then there is
a nonzero probability that none of the events occurs. || Lemma II (Lovász 1977; published by Joel Spencer)
If e p (d+1) ≤ 1 … || Lemma II today is usually referred to as "Lovász local lemma".» Библиореквизиты статьи
Спенсера подтверждены его собственным CV: «35. Asymptotic Lower Bounds for Ramsey Functions, Discrete Math
20 (1977), 69-76.»
Источник/локатор: Wikipedia, «Lovász local lemma», сырой wikitext (загружен 2026-09-03), раздел «Statements
of the lemma (symmetric version)»; J. Spencer, vita.pdf, п. 35. Копии: `sources/lll_wiki.txt`,
`sources/lll_spencer_vita.txt` (строка 160).
kind: `secondary` · status: `verified` (цитата), но **содержание — medium**
Оговорка: формулировка «Lovász 1977» на Wikipedia не подкреплена сноской на источник даты — только на
статью Спенсера; независимого подтверждения года «1977» для самого Ловаса не найдено. → противоречие C09.

**L22 — 1985 (сентябрь). Ширер: оптимальный порог (клетка «проигрыш»).**
Факт: James B. Shearer, «On a problem of Spencer», Combinatorica 5(3), 241–245. По вторичному изложению —
оптимальный порог симметричной версии: p < (d−1)^(d−1)/d^d при d > 1 (и p < 1/2 при d = 1); отсюда следует,
что достаточно и границы epd ⩽ 1. Само название («проблема Спенсера») указывает, что вопрос о точном пороге
поставил Спенсер. Achlioptas–Iliopoulos независимо называют критерий Ширера «самым щедрым условием» для
симметричных графов зависимостей.
Источник/локатор: Wikipedia «Lovász local lemma», Lemma III; Crossref DOI 10.1007/BF02579368 (Combinatorica
5(3):241–245, issued 1985-09); A–I, References [26]. Копии: `sources/lll_wiki.txt` (строки 19–25), `sources/dblp_shearer2.json`.
kind: `secondary` · status: `verified` (библиография), содержание — medium
Оговорка: полный текст Ширера не получен (Springer — «Client Challenge»); формула порога известна только по
вторичному изложению.

**L23 — 1991, 28 февраля. Erdős–Spencer: lopsided-версия и латинские трансверсали (клетки «отказ»/«носитель 2»).**
Факт: P. Erdős, J. Spencer, «Lopsided Lovász Local Lemma and Latin transversals», Discrete Applied
Mathematics 30 (2–3), 151–154. Реферат: «A new version of the Lovász Local lemma is used to prove the
existence of Latin transversals in matrices where no symbol appears too often.» Существо ослабления (по
позднейшему изложению A–I): требование «каждое плохое событие зависит лишь от немногих других» заменено
более слабым «каждое плохое событие **отрицательно коррелировано** лишь с немногими другими»; это
понадобилось для задач о перестановках, где события типично плотно зависимы.
Источник/локатор: страница ScienceDirect (архивная копия Wayback от 28.11.2022), DOI 10.1016/0166-218X(91)90040-4;
пересказ — A–I, arXiv:1406.0242, с. 2, абзац о [11]. Копии: `sources/es91_sd_wayback.html`,
`sources/achlioptas_iliopoulos.txt` (строки 64–70).
kind: `contemporaneous` (реферат и выходные данные) · status: `verified`
Пометка: находка сверяющего (сборщики 2 и 3 писали not_found). Полный текст статьи не получен; точного
определения lopsided-условия из первоисточника никто не читал. → противоречие C06 (год 1990 у ATS1995).

**L24 — 1991 (декабрь). Beck: первая алгоритмическая версия (клетка «проигрыш» — разрыв порогов).**
Факт: József Beck, «An algorithmic approach to the Lovász local lemma. I», Random Structures and Algorithms
2(4), 343–365. По описанию Мозера–Тардоша: Бек сформулировал стратегию в терминах 2-раскраски гиперграфа и
доказал, что если каждое ребро содержит ⩾ k вершин и пересекается не более чем примерно с **2^(k/48)**
другими рёбрами, то полиномиальный алгоритм даёт 2-раскраску без монохромного ребра; существованческая же
версия допускает примерно **2^k/e** соседей.
Источник/локатор: Moser–Tardos, arXiv:0903.0544v3, Introduction, с. 2 (строки 56–66); Crossref DOI
10.1002/rsa.3240020402; Wikipedia «Algorithmic Lovász local lemma», History. Копии: `sources/moser_tardos.txt`,
`sources/algo_lll_wiki.txt` (строки 39–43).
kind: `secondary` · status: `verified`
Оговорка: первоисточник (текст Бека) не открыт (Wiley). → противоречие C07 (страницы 343–365 vs 343–366).

**L25 — 1991 (декабрь). Alon: параллельная версия, порог поднят до 2^(k/8).**
Факт: Noga Alon, «A parallel algorithmic version of the local lemma», RSA 2(4), 367–378. «Alon improved the
threshold to essentially 2^(k/8) using a simpler and randomized variant of Beck's algorithm [Alo91].»
Источник/локатор: Moser–Tardos, arXiv:0903.0544v3, Introduction (строка 67); Crossref DOI 10.1002/rsa.3240020403.
Копия: `sources/moser_tardos.txt`.
kind: `secondary` · status: `corrected`
Что исправлено: сборщики 2 и 3 записали порог как «~2^k/8» — в оригинале 2^(k/8) (показатель k/8), как и
2^(k/48) у Бека; в pdftotext верхние индексы теряются. Первоисточник (текст Алона) не открыт.

**L26 — 1991 (1-е изд.) / 2000 (2-е изд.). Alon–Spencer, «The Probabilistic Method» — [!] UNVERIFIED.**
Факт (только как библиографическое упоминание): стандартное изложение симметричной и асимметричной форм
леммы, на которое ссылаются позднейшие работы: ATS1995, ref [2] — «N. Alon and J. Spencer, The Probabilistic
Method, John-Wiley, New York (1991)»; Wikipedia — «For other versions, see Alon & Spencer 2000».
Источник/локатор: `sources/latintransv_raw.txt` (строка 32); `sources/lll_wiki.txt` (строка 4).
kind: `secondary` · status: **`unverified`**
**Пометка ленты:** текст самой книги не открыт ни сборщиками, ни сверяющим (экземпляры на archive.org —
«Item not available»). Проверены только УПОМИНАНИЯ книги в двух источниках; **никакого утверждения о
содержании книги эта запись не делает**.

**L27 — 1995, 1 марта. Спенсер: рекорд по R(3,k) берётся НЕ леммой (клетка «проигрыш»).**
Факт: J. Spencer, «Maximal Triangle Free Graphs and Ramsey R(3,k)» — неопубликованные заметки, датированные
1 марта 1995, улучшают классическую нижнюю границу Эрдёша 1961 года не локальной леммой, а «случайным
динамическим алгоритмом» (жадный треугольник-свободный процесс). Прямая проверка полного текста:
словосочетание «local lemma» в нём не встречается.
Источник/локатор: `https://cs.nyu.edu/~spencer/papers/ramsey3k.pdf`, титульный лист («March 1, 1995»);
собственная аннотация Спенсера на papers.html. Копии: `sources/spencer_ramsey3k.txt`, `sources/spencer_papers.html`.
kind: `contemporaneous` (заметки 1995) · status: `verified`
Оговорка: аннотация на papers.html — `retrospective` и недатирована (см. L34).

**L28 — 1995. Alon–Tetali–Spencer: лемма цитируется в форме с e и приписывается [EL75] (клетка «опознание»).**
Факт: «Lemma 1 (The local lemma [7]) … If ep(b + 1) < 1 then with positive probability none of the events
A_i holds.», где [7] = EL75 — но скалярной формы с константой e в статье 1975 года нет. То есть сам Спенсер,
участник передачи 1977 года, двадцать лет спустя атрибутирует сильную форму первоисточнику 1975 года. В их
списке литературы [7] указан том серии Bolyai «11».
Источник/локатор: N. Alon, P. Tetali, J. Spencer, «Covering with Latin Transversals», Discrete Applied
Mathematics 57 (1995), 1–10, раздел 3, Lemma 1; References [7]. `https://cs.nyu.edu/~spencer/papers/latintransv.pdf`;
копии `sources/alon_tetali_spencer_latintransv.txt` (строки 411–416), `sources/latintransv_raw.txt`.
kind: `secondary` · status: `corrected`
Что исправлено: (а) порядок авторов и выходные данные — Alon, Tetali, Spencer, DAM 57 (1995), 1–10;
(б) kind — secondary, не contemporaneous; (в) локатор «стр. 10» сборщика — нумерация внутри PDF, не журнала.
→ противоречия C02, C03.

**L29 — 1995 (октябрь). Ким закрывает R(3,t) — треугольник-свободным процессом, не леммой (клетка «проигрыш»).**
Факт: Jeong Han Kim, «The Ramsey Number R(3,t) has order of magnitude t²/log t», RSA 7(3), 173–207. По
вторичному изложению нижняя граница получена анализом специального **треугольник-свободного процесса**, а не
локальной леммы; неявная константа позднее уточнена независимо Fiz Pontiveros–Griffiths–Morris и Bohman–Keevash.
Источник/локатор: Wikipedia «Ramsey's theorem», раздел «Bounds for R(3, s)», сноска на Kim 1995;
Crossref DOI 10.1002/rsa.3240070302 (issued 1995-10). Копия: `sources/ramsey_wiki.txt` (строка 268).
kind: `secondary` · status: `corrected`
Что исправлено: сборщик 2 предполагал метод «semi-random / Rödl nibble» — по вторичным источникам это
«triangle-free process» (тот же класс, что у Спенсера 1995). Первоисточник не открыт (Wiley).

**L30 — 1998, 2000, 2008, 2009. Цепь ослаблений алгоритмической версии (клетка «проигрыш»).**
Факт: Molloy–Reed (STOC 1998) — общий каркас условий, при которых применимы инструменты Бека и Алона
(в нём позднее найдена и исправлена ошибка, [PT09]); Czumaj–Scheideler (SODA 2000) — распространение на
гиперграфы с рёбрами неодинакового размера; Srinivasan (2008) — порог ~2^(k/4); Moser (2008) — ~2^(k/2);
Moser (2009) — ~2^k/32.
Источник/локатор: Moser–Tardos, arXiv:0903.0544v3, Introduction, с. 2 (строки 66–76). Копия: `sources/moser_tardos.txt`.
kind: `secondary` · status: `corrected`
Что исправлено: показатели степеней (2^(k/4), 2^(k/2), 2^k/32 вместо «2^k/4» и т.п.) и добавлена фраза про
исправленную ошибку в Molloy–Reed, опущенная сборщиком 2.

**L31 — PDF датирован 26 июня 2003; описывает середину/конец 1970-х. Ретроспектива Спенсера: «duplicate».**
Факт: «The story has a coda: the Lovasz Local Lemma, developed in the mid-1970s, gave a new sieve method for
showing that a set of bad events could simultaneously not hold. This author applied it to the random graph
G(n; p) with p = cn^(−1/2) with the bad events being the existence of the various potential triangles and the
independence of the various x-sets. The conditions of the Local Lemma made for some calculations but it was
relatively straightforward to **duplicate** this result. Still, the ideas behind this proof, the subtle
extension of the Deletion Method notion, are too beautiful to be forgotten.»
Источник/локатор: J. Spencer, «The Erdos Existence Argument» (неопубликованная заметка, сайт NYU; PDF
CreationDate 26.06.2003), раздел 4 «1961: Ramsey R(3,k)», последний абзац (строки 168–180).
`https://cs.nyu.edu/~spencer/papers/erdosex.pdf`; копия `sources/erdosex.txt`.
kind: `retrospective` · status: `verified`
Пометка: слово «duplicate» точно соответствует реферату 1977 года («A short proof of the KNOWN result») —
два независимых свидетельства, что лемма здесь ничего не улучшила.

**L32 — 2009 (arXiv v3, 20 мая) / 2010 (J. ACM 57(2)) / 2020 (премия Гёделя). Moser–Tardos.**
Факт (а), клетка «опознание»: полностью общая (асимметричная, взвешенная функцией x: A → (0,1)) форма
приводится как «Theorem 1.1. [EL75]» — то есть атрибутируется напрямую статье 1975 года. Библиозапись [EL75]
у них — «volume II, pages 609–627. North-Holland, 1975» (без номера тома серии).
Факт (б), клетка «проигрыш»: разрыв между алгоритмической и существованческой версиями закрыт («directly
apply to almost all known applications of the general Local Lemma»), но ценой единственного ограничения:
события должны определяться подмножествами конечного набора взаимно независимых случайных переменных, а
Γ(A) — состоять из событий, зависящих от тех же переменных («variable setting»). Такого условия в
абстрактной формулировке 1975 года нет.
Факт (в): в 2020 году Робин Мозер и Габор Тардош получили за эту работу премию Гёделя.
Источник/локатор: R. A. Moser, G. Tardos, «A constructive proof of the general Lovász Local Lemma»,
arXiv:0903.0544v3 [cs.DS], 20 May 2009, с. 1 (Theorem 1.1), с. 1–2 (Abstract/Introduction), References [EL75];
Wikipedia «Gödel Prize» (сырой wikitext), строка таблицы 2020. Копии: `sources/moser_tardos.txt`,
`sources/godel_prize_wiki.txt` (строки 125–128).
kind: `secondary` · status: `corrected`
Что исправлено: сборщик 2 пометил kind как contemporaneous — по отношению к событию 1975 года работа 2009
года является secondary. → противоречие C02.

**L33 — 2010 (публикация; заметки 1995 года). Ретроспектива Спенсера, где леммы нет вовсе (клетка «проигрыш»).**
Факт: «Current Day Annotation. These notes were written in 1995. Since 1961 the best lower bound on R(3, k)
had been ck² ln⁻² k. Building on a paper of Erdős, Winkler and Suen I was able to show that c could be made
arbitrarily large. Why didn't I publish? Only a few weeks later Jeong-Han Kim found that R(3, k) =
Ω(k² ln⁻¹ k), matching the upper bound of Ajtai, Komlós and Szemerédi, so that R(3, k) = Θ(k² ln⁻¹ k). …»
Локальная лемма Ловаса в этом тексте не упоминается ни разу.
Источник/локатор: Joel Spencer, «Potpourri», Journal of Combinatorics 1 (2010), 237–264, §1 «Maximal
TriangleFree Graphs and Ramsey R(3,k)», начало (строки 10–17). `https://cs.nyu.edu/~spencer/papers/potpourri.pdf`;
копия `sources/spencer_potpourri.txt`.
kind: `retrospective` · status: `verified`
Проверка сверяющего: `grep -i "local lemma|lovasz"` по всему извлечённому тексту — 0 вхождений.

**L34 — дата не установлена (страница правилась не ранее 2010 года). Аннотация Спенсера: где от леммы
отказались в требовании независимости (клетка «отказ»).**
Факт: «Noga Alon, Prasad Tetali and Joel Spencer, Covering with Latin Transversals … Description: Features
an intriguing extension of the Lovasz Local Lemma in which one doesn't require full independence but rather
only that the correlations are going in the correct way. Appeared in Disc Appl Math, vol 57 (1995), 1-10.»
Источник/локатор: страница публикаций Joel Spencer, NYU (papers.html), раздел «Probabilistic Methods».
`https://cs.nyu.edu/~spencer/papers/papers.html`; копия `sources/spencer_papers.html`.
kind: `retrospective` · status: `corrected`
Что исправлено: сборщик 2 датировал аннотацию «около 1995». На странице дат нет; она заведомо правилась
позже — в описании соседнего пункта стоит «[In 2008, Tom Bohman gave …]», а в списке есть работы 2010 года.
Датировать аннотацию 1995 годом нельзя. → противоречие C11(3).

**L35 — 2011 (о границе 1991 года). Bissacot и др. улучшают исходную lopsided-границу (клетка «проигрыш»).**
Факт: исходная граница Эрдёша–Спенсера для латинских квадратов (каждый цвет встречается не более
Δ ⩽ n/(4e) раз) улучшена Bissacot, Fernández, Procacci, Scoppola (Combin. Probab. Comput. 20(5), 2011,
709–719) до Δ ⩽ (27/256)·n за счёт учёта локальной плотности lopsided-графа зависимостей.
Источник/локатор: A–I, arXiv:1406.0242v3, §1.1, с. 2 (строки 124–127), ссылки [4] и [11]. Копия:
`sources/achlioptas_iliopoulos.txt`.
kind: `secondary` · status: `verified`

**L36 — 2011 и 2012 (о критерии 1985 года). Колипака–Сегеди(–Сюй) (клетка «проигрыш»).**
Факт: «Kolipaka and Szegedy in [17] showed that the algorithm of Moser and Tardos, in fact, converges in
polynomial time under the criterion of Shearer [26], the most generous condition under which Pr[∩_i Ā_i] > 0
for symmetric dependency graphs. As the criterion of Shearer is not efficiently verifiable, Kolipaka, Szegedy
and Xu [16] gave a series of intermediate conditions, between the general LLL and Shearer's criterion, for the
algorithm of [22] to terminate, most notably the efficiently verifiable Clique LLL.»
Источник/локатор: A–I, arXiv:1406.0242v3, §1.1 «Constructive Versions», с. 2–3 (строки 116–120). Копия:
`sources/achlioptas_iliopoulos.txt`.
kind: `secondary` · status: `verified`

**L37 — 2014. Harris–Srinivasan: lopsided-версия становится конструктивной, но только для перестановок
(клетка «проигрыш»).**
Факт: «On the other hand, with the notable exception of CNF-SAT, none of these results applies to the lopsided
LLL which remained non-constructive. Very recently Harris and Srinivasan [14] made the lopsided LLL
constructive for the uniform measure on Cartesian products of permutations. … In particular, they left as a
canonical open problem whether the results of Dudek, Frieze and Ruciński [9] regarding Hamilton Cycles in
edge colored hypergraphs can be made constructive.» (SODA 2014, 907–925.)
Источник/локатор: A–I, arXiv:1406.0242v3, §1.1, с. 2 (строки 120–131), References [9], [14].
kind: `secondary` · status: `verified`

**L38 — 2014/2015. «Одна из старейших и самых досадных претензий к LLL»: Δ+1 раскраска (клетка «проигрыш»).**
Факт: «This allows us to address one of the oldest and most vexing concerns about the LLL (see the survey of
Szegedy [29]), exemplified by the LLL's inability to establish the elementary fact that a graph with maximum
degree ∆ can be colored with q = ∆ + 1 colors. … Specifically, the LLL can only work when q > e∆.» Причина —
обязательный равномерный выбор нового цвета в «переменной» постановке Мозера–Тардоша: лемма требует примерно
в e раз больше цветов, чем нужно на самом деле.
Источник/локатор: A–I, arXiv:1406.0242v3, §2 «A New Framework», с. 3 (строки 436–446), References [29] =
M. Szegedy, «The Lovász Local Lemma — A Survey», CSR 2013.
kind: `secondary` · status: `verified`
Оговорка: сам обзор Сегеди недоступен (404 по двум доменам Rutgers) — см. §6.

**L39 — 2014/2015. Названная граница применимости ВСЕХ конструктивных версий (клетка «проигрыш»).**
Факт: «Both the set of objects Ω and every flaw f ⊆ Ω can be entirely amorphous. That is, Ω does not need to
have product form Ω = D_1 × · · · × D_n, as in the work of Moser and Tardos [22], or any form of symmetry, as
in the work of Harris and Srinivasan [14]. For example, Ω can be the set of all Hamiltonian cycles of a graph,
a set of very high complexity.» То есть и подход Мозера–Тардоша (пространство-произведение), и подход
Харриса–Шринивасана (требующий симметрии) не работают на бесструктурном Ω.
Источник/локатор: A–I, arXiv:1406.0242v3, §2, с. 3 (строки 143–147).
kind: `secondary` · status: `verified`

## 1.4. Факты со статусом `refuted`

**Пусто.** Ни один факт входа не помечен статусом `refuted`. Записываю это как результат, а не как пропуск.

Отдельно — **опровергнутые утверждения сборщиков**, поглощённые статусом `corrected` соответствующих фактов
(они не факты ленты, но их полезно иметь списком, чтобы они не всплыли обратно на стадии 3):
1. «Обозначения EL75 — M_k(r)/m_k(r)» → в оригинале m_k(r) и n*_k(r), m*_k(r) (L09).
2. «Theorem 1 = неравенство c₁·4^r/r³ < m*_2(r) < c₂·r⁴·4^r» → это следствие после Theorem 1 (L09).
3. «В лемме требуется независимость от несоседних (так напечатано)» → напечатано «∈ E(G)», то есть от
   соседних; расхождение внутристочниковое (L10, L11).
4. «Corollary 1: degree ≤ kr^{-1}/4r … chromatic number < k» → «⩽ k^(r−1)/4r … ⩽ k» (L12).
5. «Вероятностная лемма вынесена как отдельный инструмент общего назначения» → оформлена как две другие
   безымянные вспомогательные леммы статьи (L14).
6. «Все три появления слова "Lemma" безымянны» → вхождений 7, безымянных лемм три разных (L14).
7. «Theorem 4 на стр. 618, второе применение леммы, (1−ε)k/…» → стр. 619, третье применение, (1−ε)r/k (L15).
8. «Moser–Tardos 2009 — contemporaneous источник» → secondary (L32).
9. «Alon–Tetali–Spencer — contemporaneous; Spencer, Alon, Tetali; стр. 10» → secondary; ATS; DAM 57, 1–10 (L28).
10. «Пороги 2^k/48, 2^k/8, 2^k/4» → 2^(k/48), 2^(k/8), 2^(k/4) (L24, L25, L30).
11. «Ким использовал semi-random / Rödl nibble» → triangle-free process (L29).
12. «Аннотация Спенсера к Latin Transversals — около 1995» → страница недатирована, правилась не ранее 2010 (L34).
13. «Эрдёш–Хайнал, Graph Theory and Probability II, 1961» → у Спенсера значится за одним Эрдёшем (L02).
14. «Доклад Спенсера памяти Эрдёша — 1999» → 1999 по имени файла, CreationDate PDF — 26.06.2003 (L02, C11(4)).

---

# 2. Противоречия между источниками (помечены, НЕ разрешены)

**C01 — ГЛАВНОЕ, ВНУТРИ ПЕРВОИСТОЧНИКА.** Формулировка леммы (стр. 616): «A_i is independent of the set
{A_j: (v_i,v_j) **∈** E(G)}» — независимость от СОСЕДНИХ; доказательство (стр. 617) и применение (стр. 618:
«i.e. (v_i,v_j) **∉** E(G)») требуют независимости от НЕСОСЕДНИХ. Перерендер при 400 dpi: на стр. 616 знак
∈ без косой, на стр. 618 — ∉ с косой. Опечатка первоисточника; современные пересказы (включая пересказы
сборщиков 1 и 2) молча её исправляют. **Не разрешено:** оставляю как расхождение внутри одного документа.

**C02 — Какая форма леммы приписывается статье 1975 года.** В полном тексте EL75 есть ТОЛЬКО симметричная
невзвешенная форма P(A_i) ⩽ 1/(4d) (проверено по всему OCR: ни x(A), ни произведения по Γ(A), ни константы e).
При этом: (а) Moser–Tardos 2009 приводят общую асимметричную взвешенную форму как «Theorem 1.1 [EL75]»;
(б) Alon–Tetali–Spencer 1995 приводят скалярную форму ep(b+1)<1 как «Lemma 1 (The local lemma [7])» — и это
делает в том числе сам Спенсер, участник передачи 1977 года. Против них: Wikipedia относит форму с e к
«Lovász 1977; published by Joel Spencer», а Achlioptas–Iliopoulos пишут «The general form below is also due
in unpublished form to Lovász and was given by Spencer in [27]». **Не разрешено:** атрибуция «[EL75]» у MT и
ATS — принятое в поле округление цитирования, а не буквальное соответствие тексту 1975 года.

**C03 — Номер тома серии сборника.** «Colloq. Math. Soc. J. Bolyai **10**» — титульный лист самой статьи,
скан Zentralblatt (Zbl 0315.05117), Achlioptas–Iliopoulos (ref [10]). ПРОТИВ: «Bolyai **11**» — собственный
публикационный список Л. Ловаса (public23.pdf от 04.03.2023, п. 43, и п. 44 для Lovász–Plummer) И список
литературы ATS1995 (ref [7]). Третий вариант — «volume II» без номера серии (Wikipedia, Moser–Tardos) —
первому не противоречит: 10 — том серии, Vol. II — часть сборника. **Не разрешено формально**, хотя
первоисточник печатает «10»; отмечаю, что у Ловаса «11» стоит систематически (два пункта подряд).

**C04 — Год статьи Erdős «On a combinatorial problem II», Acta Math. Hung. 15, 445–447.** «1969» — как
напечатано в библиографии самой EL75 (ссылка [5], сверено по скану стр. 627) против «1964» по zbMATH
(Zbl 0201.33704) и по списку литературы Спенсера ([4]). Том и страницы совпадают. Дополнительно существует
Erdős «On a combinatorial problem III», Can. Math. Bull. 12, 413–416 (1969) — вероятный источник смешения.
**Не разрешено.**

**C05 — Формула главной границы Theorem 1.** В самой статье — c₁·4^r/r³ < m*_2(r) < c₂·r⁴·4^r (r³ в
знаменателе нижней части, r⁴ в верхней); в авторском реферате (Autorreferat) той же статьи в Zentralblatt —
симметризованная c₁·4ⁿ/n⁴ < f(n) < c₂·4ⁿ·n⁴ (n⁴ в обеих частях). Обе версии сверены визуально (стр. 610
скана статьи и с. 46 скана Zentralblatt). **Не разрешено.** Замечание для стадии 3: это расхождение авторов
с самими собой в двух документах одного года.

**C06 — Год Erdős–Spencer «Lopsided Lovász Local Lemma and Latin transversals».** «1990» в списке литературы
ATS1995 (ref [5]) против «1991» по странице ScienceDirect самой статьи (28 February 1991), Crossref
(issued 1991-02), CV Спенсера (vita.pdf, п. 108) и A–I (ref [11]). **Не разрешено формально**, перевес
решительно за 1991.

**C07 — Страницы Beck 1991** («An algorithmic approach to the Lovász local lemma. I», RSA 2(4)): 343–365 по
Crossref против 343–366 по Wikipedia («Algorithmic Lovász local lemma»). Первоисточник не открыт.
**Не разрешено.**

**C08 — Нарратив «Spencer 1977 = LLL → нижние границы Рамсея» против умолчания о лемме в ретроспективе
Спенсера про R(3,k) (Potpourri 2010).** Сверяющий агент считает это противоречие **снятым** найденным
рефератом Spencer 1977: «A probability theorem, due to Lovasz, is used to derive lower bounds for various
Ramsey functions. A short proof of the **known** result R(3, t) ⩾ ct²/(ln t)² is given» — то есть лемма
применялась к R(3,t), но давала лишь короткое доказательство уже известной границы Эрдёша 1961 года, а не
улучшение, и потому в рассказе о рекордах законно не упоминается; согласуется с «relatively straightforward
to duplicate this result» (L31). **Привожу как есть, с пометкой: разрешение выполнено на стадии 1, не мной;
стадия 2 его не подтверждает и не отменяет.** Оговорка, которая остаётся: полного текста Spencer 1977 никто
не читал.

**C09 — Хронология неопубликованной формы Ловаса.** Wikipedia: «Lemma I (Lovász and Erdős 1973; published
1975)» и «Lemma II (**Lovász 1977**; published by Joel Spencer)» — год привязан к самому Ловасу, без сноски
на источник даты. Achlioptas–Iliopoulos: идея леммы «первоначально распространялась Ловасом в начале 1970-х
в неопубликованной записке», общая форма «также принадлежит в неопубликованном виде Ловасу» — **без года**.
Никакого документа (записки, письма, препринта) в подтверждение ни одной из версий не найдено. **Не разрешено.**

**C10 — Дата работы Миллера.** Сама статья 1975 года ссылается на Миллера без года и без номера в
библиографии; zbMATH/JFM дают 1937 (полная статья) и 1936 (анонс). Каталожные записи первоисточником не
являются; статья Миллера не открыта. **Не разрешено.**

**C11 — Расхождения между самими сборщиками** (наблюдения сверяющего; см. также §1.4):
(1) локатор Theorem 4 — стр. 618 у сборщика 2 против стр. 619 на скане;
(2) порядковый номер применения леммы в Theorem 4 — «второе» против «as in the two previous cases» (третье);
(3) датировка аннотации Спенсера к «Covering with Latin Transversals» — «около 1995» против недатированной
страницы, правившейся не ранее 2010;
(4) дата доклада Спенсера памяти Эрдёша — «1999» (по имени файла) против CreationDate 26.06.2003;
(5) обозначения EL75 — «Mk(r)/mk(r)» против m_k(r), n*_k(r), m*_k(r);
(6) пороги Бека/Алона/Шринивасана — «2^k/48, 2^k/8, 2^k/4» против 2^(k/48), 2^(k/8), 2^(k/4)
(только моseровский порог действительно 2^k/32).

**C12 — Статус вероятностной леммы в структуре статьи 1975 года.** Сборщик 1: «вынесена как отдельный
инструмент общего назначения, не зарыта внутри доказательства». Сборщик 2: «сама лемма безымянна». Проверка
сверяющего: в статье ТРИ разных безымянных «Lemma» (стр. 616, 621, ~624), то есть оформление вероятностной
леммы ничем не выделено; выделяет её только трёхкратное применение. **Не разрешено:** это спор об
интерпретации одного и того же текста, и он прямо влияет на стадию 3 (был ли инструмент осознан как
инструмент в момент печати).

**C13 — Целостность одной из локальных копий (техническое).** Файл `sources/LocalLem_original1975.pdf`
(сборщик 3) размером 5433 байта — это HTML-страница ошибки error.elte.hu, не PDF; при этом одноимённый .txt
идентичен корректному OCR. Годным первоисточником считается `sources/EL75_original.pdf`.

---

# 3. «За неделю до»: в каком виде задача лежала на столе непосредственно перед изобретением

## 3.1. Ответ

**Документов времени работы, по которым можно было бы восстановить «за неделю до», НЕТ.**

Единственный контемпоральный документ кейса — уже напечатанная статья 1975 года, в которой лемма присутствует
в готовом виде, без единого слова о своём происхождении (L17: ни заявления о новизне, ни ссылки на источник
приёма, ни благодарностей — при том что в других местах той же статьи авторы источник метода называют прямо:
«The proof uses a method due to Lubell [2]»).

Не найдено (§6 даёт полный список с адресами поиска):
- черновиков, переписки, рабочих тетрадей Эрдёша и Ловаса за 1973–1975 годы;
- набросков доказательства до печатной формы;
- «неопубликованной записки» Ловаса начала 1970-х, о которой пишут Achlioptas–Iliopoulos (L06) — ни
  скана, ни каталожной записи, ни ссылки с реквизитами в других работах;
- стенограммы или отдельного текста устного доклада 1973 года в Кестхее (и даже точной даты конференции);
- указания самих авторов на то, кто из двоих предложил вероятностную технику раздела «2.».

**Какое вычисление не проходило — по документам времени работы неизвестно.** Заполнять это поле из
ретроспективы регламент запрещает (§8: «Стадия, вернувшая пустое, записывает пустое как результат»;
§4: «"Озарение" — почти всегда сжатие месяцев. Спрашивайте, что было за неделю до»). Отвечаю: спросили —
документа нет.

## 3.2. Что МОЖНО сказать по документам, не выходя за них

Это не «за неделю до», а состояние задачи в момент печати; отделяю явно.

1. **Разрыв, ради которого лемма понадобилась, в статье назван численно** (L09, стр. 610): для непростых
   гиперграфов известно (r/(r+2))·2^(r−1) ⩽ m_2(r) ⩽ r²·2^r (то есть порядка 2^r); Theorem 1 даёт для простых
   c₁·4^r/r³ < m*_2(r) < c₂·r⁴·4^r (порядка 4^r) и заканчивается словами «i.e. m*_2(r) is much larger then
   m_2(r)». То есть на столе стоял вопрос о величине порядка 4^r там, где старая техника давала 2^r.
2. **Старая техника, дававшая 2^r, документирована — но только ретроспективно** (L02): просеивающий довод
   Эрдёша 1963 года «Σ 1/2^(α_i) ⩽ 1/2 ⟹ property B», не учитывающий, какие рёбра пересекаются, а какие нет.
   Документ — доклад Спенсера (kind `retrospective`, PDF 2003), а не бумага 1970-х.
3. **Первое, к чему лемма применена в самой статье** (L12), — ровно место, где глобальный union bound не
   работает: r-однородный гиперграф с ограниченной локальной степенью, d ⩽ k^(r−1)/4, событие «ребро
   монохромно» с вероятностью 1/k^(r−1); сумма вероятностей по всем m рёбрам ничем не ограничена, а
   поштучное условие P(A_i) ⩽ 1/(4d) выполняется.

**Чем это НЕ является.** Пункты 1–3 — реконструкция по печатному тексту и по одной ретроспективе; они
показывают, какой разрыв лемма закрывает, но **не** свидетельствуют, что именно этот счёт «не проходил» на
столе у авторов за неделю, месяц или год до леммы. Документа с несошедшимся вычислением нет. Порядок
изложения в статье (сначала общая лемма, потом три применения) — свойство печатного текста, а не
свидетельство о порядке открытия.

---

# 4. Черновик таблицы брифа

Формат клетки: **содержание** — далее адрес (источник + локатор + `status`), либо «не найдено, искали там-то».
Клетки заполнены только тем, что есть в ленте; пустые оставлены пустыми.

| клетка | содержание | адрес |
|---|---|---|
| **нужда** | Порядок 4^r для простых гиперграфов против известного 2^r для непростых; «m*_2(r) is much larger then m_2(r)» | EL75, стр. 610 (Theorem 1 + следствие), `sources/lll_page02-02.png` · `corrected` (L09) |
| нужда | Задача, где глобальный union bound не работает: k-раскраска r-однородного гиперграфа с локальной степенью d ⩽ k^(r−1)/4; Corollary 1 | EL75, стр. 617–618, `sources/lll_lemma_page-09.png`, `sources/p618-10.png` · `corrected` (L12) |
| нужда | Предшествующая техника (union bound Эрдёша 1963: Σ 1/2^(α_i) ⩽ 1/2 ⟹ property B, m(n) > 2^(n−1)) | Spencer, erdos99mytalk, §4, с. 7–8; `sources/e99p6-06.png` · `corrected`, kind `retrospective` (L02) |
| нужда | Названные предшественники: Miller (property B, без года); [5] Erdős 1964/«1969», [9] Schmidt; полный список [1]–[9] | EL75, стр. 609, 610, 626–627; `sources/lll_page01-01.png`, `sources/pref-18.png`, `sources/pref-19.png` · `verified` (L04, L05, L08) |
| нужда | Форма леммы в статье — только симметричная P(A_i) ⩽ 1/(4d); ни x(A), ни Γ(A), ни e | EL75, стр. 616 + весь OCR · `verified` (L13) |
| **отказ** | *На момент изобретения (1973–1975): «не найдено».* Искали: полный текст EL75 (нет заявления о новизне, нет атрибуции приёма, нет благодарностей — L17); архив Эрдёша renyi.hu/~p_erdos; lovasz.web.elte.hu и CV Ловаса; MacTutor. Что именно авторы сознательно отвергли (глобальную сумму? полную независимость? безусловную оценку?), ни один документ времени работы не говорит | «не найдено» — адреса поиска: §6 п. 1, 4, 5, 6 |
| отказ | *Задокументированный отказ есть только на стадии переноса, у другого человека, 1991/после:* от требования полной независимости — к однонаправленному условию на корреляции («one doesn't require full independence but rather only that the correlations are going in the correct way») | Spencer, papers.html, аннотация к ATS «Covering with Latin Transversals» · `corrected`, kind `retrospective`, **страница недатирована** (L34); первоисточник отказа — Erdős–Spencer 1991, реферат, `sources/es91_sd_wayback.html` · `verified` (L23) |
| **модель** (первая реализация непротиворечивости) | Сама лемма с доказательством: индукция по n с усилением (5) P(A_1 \| Ā_2…Ā_n) ⩽ 1/(2d), q ⩽ d+1, оценка 1 − (q−1)/(2d) ⩾ 1/2 — то есть «модель» здесь есть само доказательство, а не отдельная конструкция | EL75, стр. 616–617, `sources/lll_lemma_page-08.png`, `sources/lll_lemma_page-09.png` · `corrected` (L10) |
| модель | Первая конкретная реализация условия: line-graph гиперграфа, P(A_i)=1/k^(r−1), d ⩽ k^(r−1)/4 — но в печатном тексте она идёт ПОСЛЕ общей леммы | EL75, стр. 617–618 · `corrected` (L12) |
| модель | *Конкретный частный случай, найденный ДО общей формулировки: «не найдено».* Искали: полный текст EL75 (порядок изложения — общее→частное), черновики и переписку (нет), «неопубликованную записку» Ловаса (нет документа) | «не найдено» — адреса поиска: §6 п. 1, 2; свидетельство без документа — L06 (A–I, arXiv:1406.0242v3, с. 1) · `verified` как цитата, kind `secondary` |
| модель (дефект) | Внутреннее противоречие модели: в формулировке ∈ E(G), в доказательстве и применении ∉ E(G) | EL75, стр. 616 против 617–618; `sources/lemma_zoom2-08.png` (400 dpi), `sources/p618-10.png` · `verified` (L11) |
| **опознание** | В 1975 году имени нет: «local lemma» — 0 вхождений, утверждение называется просто «Lemma», оформлено как две другие безымянные вспомогательные леммы статьи | EL75, весь текст, `grep -i "local"` по `sources/EL75_original.txt` → 0 · `verified` (L16); оформление — `corrected` (L14) |
| опознание | Первое имя-атрибуция в чужой печати (1977): «A probability theorem, **due to Lovasz**» — Эрдёш не назван | Spencer, Discrete Math 20 (1977), 69–76, Abstract; `sources/spencer1977_sciencedirect_wayback20240421.html` · `verified` (L20) |
| опознание | «Lemma II (Lovász 1977; published by Joel Spencer) … Lemma II today is usually referred to as "Lovász local lemma"» | Wikipedia «Lovász local lemma», раздел Statements; `sources/lll_wiki.txt` · `verified` как цитата, содержание medium, год не подтверждён (L21) |
| опознание | Обратная проекция имени на 1975 год: «Lemma 1 (The local lemma [7])» с ep(b+1)<1 (ATS 1995) и «Theorem 1.1. [EL75]» с весами x: A → (0,1) (Moser–Tardos 2009) — обеих форм в статье 1975 года нет | ATS1995, раздел 3, `sources/alon_tetali_spencer_latintransv.txt` (строки 411–416) · `corrected` (L28); Moser–Tardos, arXiv:0903.0544v3, с. 1, `sources/moser_tardos.txt` · `corrected` (L32) |
| **носитель 2** | *Внутри статьи (тот же носитель, те же авторы, третье применение):* гипотеза Штрауса на решётке n-мерного пространства — k-раскраска точек решётки так, что всякий сдвиг S+a содержит ⩾ (1−ε)r/k точек каждого цвета | EL75, стр. 619 (Theorem 4), стр. 611 (анонс); `sources/p619-11.png` · `corrected` (L15) |
| носитель 2 | *Первый чужой перенос (другой человек, 1977):* нижние границы рамсеевских функций, R(3,t) ⩾ ct²/(ln t)² | Spencer, Discrete Math 20 (1977), Abstract · `verified` (L20); ретроспективное описание механики (G(n,p), p = cn^(−1/2), плохие события = потенциальные треугольники и независимость x-множеств) — Spencer, «The Erdos Existence Argument», раздел 4, `sources/erdosex.txt` · `verified`, kind `retrospective` (L31) |
| носитель 2 | *Перенос с изменением формулировки (1991):* латинские трансверсали через lopsided-версию (независимость → отрицательная корреляция) | Erdős–Spencer, DAM 30 (1991), 151–154, Abstract; `sources/es91_sd_wayback.html` · `verified` (L23) |
| носитель 2 | *Перенос в другую грубую область реестра (программирование/вычисления):* алгоритмические версии — Beck 1991 (RSA 2(4)), затем Moser–Tardos (J. ACM 57(2), 2010; премия Гёделя 2020) | Moser–Tardos, arXiv:0903.0544v3, Introduction, `sources/moser_tardos.txt` · `verified` (L24) / `corrected` (L32); премия — `sources/godel_prize_wiki.txt` · `verified` |
| носитель 2 | **Оговорка для §5 регламента (реестр областей):** все переносы, кроме алгоритмического, остаются внутри одной грубой области (математика). Второй области, кроме «программирования» через алгоритмическую версию, в ленте нет; физика/химия/биология/статистика **не искались** | пометка стадии 2, не источник |
| **проигрыш** | Первое же чужое применение не улучшило результат: «A short proof of the **known** result R(3,t) ⩾ ct²/(ln t)²»; ретроспективно — «relatively straightforward to **duplicate** this result» | Spencer 1977, Abstract · `verified` (L20); Spencer, erdosex.pdf, раздел 4 · `verified` (L31) |
| проигрыш | Рекорд по R(3,k) взят другим методом: заметки Спенсера 01.03.1995 (жадный треугольник-свободный процесс, «local lemma» — 0 вхождений) и Ким 1995 (Θ(k² ln⁻¹ k), triangle-free process); в ретроспективе Спенсера 2010 года о R(3,k) лемма не упоминается ни разу | `sources/spencer_ramsey3k.txt` · `verified` (L27); Wikipedia «Ramsey's theorem» + Crossref · `corrected` (L29); Spencer, «Potpourri», J. Combin. 1 (2010), 237–264, §1 · `verified` (L33) |
| проигрыш | Существованческая версия не даёт алгоритма: разрыв порогов 2^(k/48) (Бек) против 2^k/e; далее 2^(k/8), 2^(k/4), 2^(k/2), 2^k/32 — восемнадцать лет закрывания разрыва | Moser–Tardos, arXiv:0903.0544v3, Introduction · `verified` (L24), `corrected` (L25, L30) |
| проигрыш | Цена конструктивности: ограничение «variable setting» (события определяются подмножествами независимых переменных) — условия, которого в формулировке 1975 года нет | Moser–Tardos, arXiv:0903.0544v3, с. 1–2 · `corrected` (L32) |
| проигрыш | Граница симметричной формы: оптимальный порог Ширера p < (d−1)^(d−1)/d^d (d>1) — то есть 4pd ⩽ 1 и ep(d+1) ⩽ 1 не точны; критерий Ширера при этом не проверяем эффективно | Wikipedia «Lovász local lemma», Lemma III + Crossref DOI 10.1007/BF02579368 · `verified` (библиография), содержание medium (L22); Kolipaka–Szegedy(–Xu) — A–I, §1.1 · `verified` (L36) |
| проигрыш | Лемма не доказывает элементарного факта: граф с максимальной степенью Δ раскрашивается в Δ+1 цвет; она работает лишь при q > eΔ — «одна из старейших и самых досадных претензий к LLL» | A–I, arXiv:1406.0242v3, §2, с. 3 (строки 436–446) · `verified` (L38) |
| проигрыш | Lopsided-версия оставалась неконструктивной до 2014 года, и сделана конструктивной лишь для равномерной меры на произведениях перестановок; бесструктурное Ω (например, множество гамильтоновых циклов) не покрыто ничем | A–I, §1.1 и §2 · `verified` (L37, L39) |
| проигрыш | Исходная lopsided-граница Δ ⩽ n/(4e) не была точной: Bissacot и др. 2011 подняли до Δ ⩽ (27/256)·n | A–I, §1.1, с. 2 (строки 124–127) · `verified` (L35) |

**Пустые клетки таблицы, названные явно:**
- «отказ» на момент изобретения — не найдено (адреса поиска даны в клетке и в §6);
- «модель» в смысле «частный случай, найденный ДО общей теории» — не найдено;
- второй носитель вне математики и вычислений — **не искали** (это не отрицательный результат, а
  неисследованная область; отмечаю для стадии 3).

---

# 5. Ответ на kill-gate ставки (стадия 0, `b13/stake.md`)

**Вопрос kill-gate (п. 1 ставки + раздел «Чем опровергается»):** есть ли для этого кейса датированный
документ времени работы с несходящимся (не проходящим или повторяющимся) вычислением **ДО** изобретения?

## **ОТВЕТ: НЕТ.**

**Адрес отрицательного результата (что именно проверено):**
1. Единственный контемпоральный документ кейса — P. Erdős, L. Lovász, Colloq. Math. Soc. J. Bolyai 10 (1975),
   609–627; полный скан `sources/EL75_original.pdf` (19 стр., MD5 a0183f21fb05c8d7621b78b48442ad30), OCR
   `sources/EL75_original.txt`, ключевые страницы (609, 610, 616, 617, 618, 619, 626, 627) сверены визуально.
   В нём лемма напечатана **в готовом виде**; нет ни заявления о новизне, ни атрибуции приёма, ни
   благодарностей, ни описания неудавшихся попыток (L17, стр. 609–627, `verified`).
2. Черновики, переписка, рабочие тетради Эрдёша и Ловаса за 1973–1975 годы — **не найдены**. Искали:
   открытый архив Rényi Institute (renyi.hu/~p_erdos; библиография обрывается около 1966 года), личная
   страница Ловаса (lovasz.web.elte.hu) и его CV (public23.pdf, vita22.pdf), MacTutor, archive.org.
3. «Неопубликованная записка» Ловаса начала 1970-х — **документа нет**; существует только свидетельство
   вторичного источника 2014/2015 года: Achlioptas–Iliopoulos, arXiv:1406.0242v3, Introduction, с. 1,
   «first circulated by Lovász in the early 1970s in an unpublished note» (L06, `secondary`, `verified` как
   цитата; года у них не названо, ссылки на документ нет).
4. Стенограмма/текст доклада 1973 года в Кестхее — **не найдена**; в открытом доступе сведений о её
   существовании нет. Точная дата конференции нигде не указана.
5. Полный текст сборника «Infinite and Finite Sets» на archive.org (identifier `infinitefinitese0000unse`) —
   controlled digital lending, полнотекстовый поиск и скачивание заблокированы.

**Что есть вместо документа (и почему оно не засчитывается):**
- Ретроспектива: доклад Спенсера о технике Эрдёша (`erdos99mytalk`, PDF CreationDate 26.06.2003) с
  формулировкой старого просеивающего довода Σ 1/2^(α_i) ⩽ 1/2 (L02, kind `retrospective`) — это рассказ
  третьего лица через 30–40 лет, а не рабочая бумага.
- Реконструкция по печатному тексту: разрыв 2^r против 4^r назван в самой статье (L09), и первое применение
  леммы стоит ровно там, где сумма вероятностей по всем рёбрам не ограничена (L12). Это показывает, **какой**
  счёт не проходил старой техникой, но **не** является датированным документом времени работы и не говорит,
  что этот счёт кто-то пробовал и бросил.

**Формулировка для сводки kill-gate по брифу 13:** кейс «Локальная лемма Ловаса» идёт в **отрицательный**
столбец п. 1 ставки — датированного документа времени работы с несходящимся вычислением до изобретения нет,
есть только печатный результат и ретроспективы. Если такой же ответ получится ещё для двух кейсов из пяти,
премисса брифа «структура рождается из вычисления, которое не проходит» опровергнута для этого набора
(`b13/stake.md`, раздел «Чем опровергается», первый пункт).

**Что при этом kill-gate НЕ опровергает** (фиксирую, чтобы стадия 3 не растащила): п. 5 ставки («для
лемм-инструментов первое чужое применение изменило формулировку») по этому кейсу **подтверждается
документами**: первое чужое применение (Spencer 1977, L20) сменило атрибуцию и, по вторичным источникам,
принесло форму с константой e (L21, medium); второй перенос (Erdős–Spencer 1991, L23) прямо ослабил условие
независимости до отрицательной корреляции; алгоритмические версии сменили условие на «variable setting»
(L32). Ни одна из этих формулировок не совпадает с напечатанной в 1975 году (L13).

---

# 6. Осталось непроверенным (адреса для стадии 3 и дальнейшего поиска)

1. Черновики/переписка/тетради Эрдёша и Ловаса 1973–1975. Искали: renyi.hu/~p_erdos, lovasz.web.elte.hu, CV.
   Не найдено.
2. «Неопубликованная записка» Ловаса начала 1970-х. Следов документа нет ни в каталогах, ни в ссылках.
3. Стенограмма доклада 1973 года в Кестхее; точная дата конференции.
4. Указание авторов, кто из двоих предложил технику раздела «2.».
5. Прямые ретроспективы самого **Ловаса** о происхождении/ограничениях леммы (интервью, лекция, предисловие;
   в том числе к Абелевской премии 2021 года). Искали в MacTutor, lovasz.web.elte.hu, vita22.pdf — не найдены;
   отмечено, что это скорее **неисследованная тема**, чем отрицательный результат.
6. Прямые ретроспективы самого **Эрдёша** о локальной лемме. Искали в MacTutor и в библиографии на renyi.hu.
   Не найдены.
7. **Полный текст Spencer 1977** (Discrete Math 20, 69–76): реферат добыт, полного текста нет (ScienceDirect
   403 напрямую и через Wayback; Elsevier full-text API требует ключ; core.ac.uk — Cloudflare). Дословная
   формулировка «ep(d+1) ⩽ 1» в первой публикации никем не прочитана.
8. Полный текст Beck 1991 (RSA 2(4):343–365) — Wiley, закрытый доступ; сайт автора без списка публикаций.
9. Полный текст Alon 1991 (RSA 2(4):367–378) — Wiley; сайт автора недоступен из среды (сетевая ошибка).
10. Полный текст Shearer 1985 (Combinatorica 5(3):241–245) — Springer «Client Challenge»; zbMATH 403.
11. Полный текст Kim 1995 (RSA 7(3):173–207) — Wiley.
12. Полный текст Erdős–Spencer 1991 (DAM 30:151–154) — реферат добыт, текста нет; точного определения
    lopsided-условия из первоисточника никто не читал.
13. Обзор M. Szegedy, «The Lovász Local Lemma — A Survey», CSR 2013, LNCS 7913, 1–11 — 404 по двум доменам
    Rutgers, Springer закрыт. Именно он, по ссылке A–I, документирует «старейшие проблемы LLL».
14. N. Alon, J. Spencer, «The Probabilistic Method» (1991/2000) — archive.org «Item not available»;
    единственный `unverified` факт ленты (L26).
15. M. Molloy, B. Reed, «Graph Colouring and the Probabilistic Method» (2002) — **не искали**.
16. Второй носитель линзы вне математики и вычислений — **не искали**.
17. Бюджет веб-поиска сессии стадии 1 исчерпан (200/200) до начала сверки; часть отрицательных результатов
    получена прямыми HTTP-запросами, а archive.org в день сверки был частично «Temporarily Offline» —
    отрицательные результаты по нему могут быть временными.
