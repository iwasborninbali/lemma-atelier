# Бриф 13, кейс 03: Куммер — идеальные числа (1847) → Дедекинд — идеалы (1871)
## Стадия 2 регламента: лента, противоречия, «за неделю до», черновик таблицы, ответ на kill-gate

Составлено 2026-09-03 по проверенному своду фактов (стадия 1: пять сборщиков + сверка).
Регламент: `/Users/iwasborninbali/projects/moves/research/00-PROTOCOL.md`, §3–§4, §8.
Правило §8: «Стадия, вернувшая пустое, записывает пустое как результат, а не заполняет его из ретроспективы».
Правило §4: противоречия не сглаживаются; ниже они помечены, но НЕ разрешаются мной — там, где сверка
стадии 1 уже разрешила противоречие, это указано отдельной строкой «разрешено на стадии 1».

Обозначения: `kind` — contemporaneous (документ времени работы) / retrospective (позднее самоописание) /
secondary (вторичный источник). `status` — verified / corrected (локатор или атрибуция исправлены при сверке) /
unverified. Записи со `status: refuted` в своде отсутствуют; опровергнутые УТВЕРЖДЕНИЯ (не факты) вынесены
в §1.1 и в ленту не входят.

Сокращения источников:
- **CR t.24** — Comptes rendus hebdomadaires des séances de l'Académie des sciences, t. 24 (1847).
  `archive.org/details/comptesrendusheb24acad`; локальный полнотекст `…/b13/sources/cr_v24_1847_djvu.txt`.
- **JMPA t.12** — Journal de mathématiques pures et appliquées, 1re série, t. 12 (1847), numdam.org.
- **Crelle 35** — Journal für die reine und angewandte Mathematik, Bd. 35 (1847), GDZ `PPN243919689_0035`.
- **Crelle 92** — то же, Bd. 92 (1882), GDZ `PPN243919689_0092`.
- **VZT 1871 / 1879 / 1894** — Dirichlet, Vorlesungen über Zahlentheorie, 2./3./4. Aufl., изд. Дедекинда.
- **Grundzüge** — Kronecker, Grundzüge einer arithmetischen Theorie der algebraischen Grössen (1882).
- **Avigad 2005** — J. Avigad, «Methodology and metaphysics in the development of Dedekind's theory of ideals»,
  препринт 13.04.2005, `andrew.cmu.edu/user/avigad/Papers/dedekind.pdf`.

Все локальные файлы — в `/private/tmp/claude-501/-Users-iwasborninbali-saturation/e5097638-8685-4abc-aa31-61c23e004964/scratchpad/b13/sources/`
(наличие 18 ключевых файлов перепроверено при составлении ленты).

---

# 1. Лента по датам

## 1844 — Куммер, «De numeris complexis, qui radicibus unitatis et numeris integris realibus constant», Бреслау
Печатная программа Бреславльского университета, адресованная Кёнигсбергскому университету к его
трёхсотлетнему юбилею. Переиздана целиком: JMPA t. 12 (май 1847), pp. 185–212. Точный день 1844 г.
источниками не установлен.

**Л-01 · 1844 · опознание.** В открывающем абзаце Куммер признаёт приоритет Якоби: тот первым доказал, что
всякое простое вида mλ+1 разлагается на два комплексных множителя этого рода, и первым довёл разложение до
простых множителей для корней 5-й, 8-й и 12-й степени, сообщив об этом Берлинской академии. В том же абзаце —
описание сбоя: «Quod idem numerus primus p pluribus modis diversis in factores duos diffinditur, et quod
producta certa ex iis factoribus formata per alios factores divisibilia fiunt, neque tamen hi ipsi factores
cum illis compensari possunt, res maximi momenti, indicat hos factores non esse primos sed compositos».
*Источник:* JMPA t. 12, pp. 185–186 (первый абзац). *kind:* contemporaneous. *status:* verified.

**Л-02 · 1844 · опознание.** § IV: Дирихле, находящийся в Италии, разработал основополагающие теоремы о
комплексных единицах, ещё не опубликованные; отдельно отмечен «geometram juvenilem Leopoldum Kronecker,
qui nunc Vratislaviae litteris mathematicis studet», нашедший тонкий метод для единиц при λ = 7.
*Источник:* JMPA t. 12, pp. 193–194 (конец § IV). *kind:* contemporaneous. *status:* verified.

**Л-03 · 1844 · нужда.** Прямая формулировка нужды за три года до парижской дискуссии: «Maxime dolendum
videtur, quod haec numerorum realium virtus, ut in factores primos dissolvi possint, qui pro eodem numero
semper iidem sint, non eadem est numerorum complexorum, quae si esset, tota haec doctrina, quae magnis adhuc
difficultatibus laborat, facile absolvi et ad finem perduci posset. Eam ipsam ob causam numeri complexi, quos
hic tractamus, imperfecti esse videntur, et dubium inde oriri posset, utrum hi numeri complexis ceteris qui
fingi possint praeferendi, an alii quaerendi essent, qui in hac re fundamentali analogiam cum numeris integris
realibus servarent». Непосредственно перед этим пассажем — вывод несостоявшегося счёта: «Inde sequeretur ut
quilibet numerus primus p = mλ + 1 esset productum λ − 1 factorum complexorum conjunctorum, quod in universum
non pro omnibus valoribus numerorum p et λ valere supra demonstravimus».
*Источник:* JMPA t. 12, p. 203 (перед § IX). *kind:* contemporaneous. *status:* verified.

**Л-04 · 1844 · модель.** § IX открывается постановкой нерешённой задачи: «Quum numerorum primorum formae
mλ + 1 alii in λ − 1 factores complexos discerpi possint, alii non possint, e re est ut inveniatur qui et
quales sint ii numeri λ et p, pro quibus talis repraesentatio locum habet, atque ut pro iis qui minorem tantum
numerum factorum primorum habent, horum factorum numerus et forma propria indagetur, quod vero problema
ulterioribus virorum doctorum perscrutationibus relinquendum est». Далее — заявленная вычислительная база:
«Ipse ut hanc rem accuratius cognoscerem, et ut exemplis docerer, omnium numerorum primorum infra mille, qui
formas habent 5m+1, 7m+1, 11m+1, 13m+1, 17m+1, 19m+1 et 23m+1, factores primos computavi, et methodos quibus
usus sum, et ipsos factores primos computatos hoc loco in publicum edam».
*Источник:* JMPA t. 12, pp. 203–204 (§ IX). *kind:* contemporaneous. *status:* verified.

**Л-05 · 1844 · модель.** В таблицах § X случай λ = 23 выглядит резко иначе соседних: для λ = 13, 17, 19 —
длинные списки простых p < 1000, представимых нормой, для λ = 23 (группа 7) — только три (599, 491, 829),
после чего идёт отдельная ремарка «Reliqui numeri primi formae 23m + 1 infra mille undecim factoribus primis
constant» со списком 47, 139, 277, 461, 967. Интерпретации Куммер этому НЕ даёт; слов о том, что λ = 23 —
первый случай нарушения единственности, в тексте нет.
*Источник:* JMPA t. 12, pp. 207–208 (группы (4)–(7) § X и следующая ремарка). *kind:* contemporaneous.
*status:* corrected (исправляет утверждение сборщика 1, что признака нет), *confidence:* medium (OCR таблиц повреждён).

## 1847-03-01 — заседание Парижской академии наук, понедельник

**Л-06 · 1847-03-01 · нужда.** Ламе представил «Démonstration générale du théorème de Fermat…» и сам сообщил,
что несколько месяцев назад говорил об этом с Лиувиллем, который был убеждён, что отрицательное свойство
Ферма должно зависеть от комплексных множителей: «il me parut convaincu que la propriété négative, énoncée
par Fermat, devait dépendre de certains facteurs complexes… C'était une nouvelle voie que je n'avais pas
explorée; je l'ai suivie…».
*Источник:* CR t. 24, séance du 1er mars 1847, мемуар pp. 310–314; цитата на p. 310. *kind:* contemporaneous.
*status:* verified (пагинация уточнена по печатным колонтитулам).

**Л-07 · 1847-03-01 · нужда.** Сразу после Ламе Лиувилль в «Observations» называет пробел публично:
«il faudrait d'abord chercher à établir pour les nouveaux nombres complexes un théorème analogue à la
proposition élémentaire pour les nombres entiers ordinaires, qu'un produit ne peut être décomposé en facteurs
premiers que d'une seule manière. L'analyse de M. Lamé me confirme dans ce sentiment; elle a besoin, ce me
semble, du théorème dont je parle… N'y a-t-il pas là une lacune à remplir?»
*Источник:* CR t. 24, «Observations de M. Liouville», pp. 314–315; цитата на p. 315. *kind:* contemporaneous.
*status:* verified. **Ключевой документ клетки «нужда»: пробел назван в день доклада.**

**Л-08 · 1847-03-01 · опознание.** Там же Лиувилль указывает адреса материала: большая работа Коши в
т. XVII Мемуаров Академии о числах, связанных с r^n − 1 = 0, и «surtout dans un article de M. Jacobi
(Journal de Mathématiques, tome VIII, page 268)».
*Источник:* CR t. 24, p. 315. *kind:* contemporaneous. *status:* verified.

**Л-09 · 1847-03-01 · опознание.** Следом Коши напоминает о мемуаре, представленном Академии в запечатанном
виде 19 октября 1846 г., с методом и формулами, которые, как ему казалось, могли привести к доказательству
теоремы Ферма; признаёт, что отвлёкся и не успел проверить гипотезу, и что его метод «très-différente» от
метода Ламе.
*Источник:* CR t. 24, pp. 316–317. *kind:* contemporaneous. *status:* verified (клетка изменена сборщиками с
«прочее»/«нужда» на «опознание»: по содержанию это заявка на приоритет).

## 1847-03-15 — заседание, понедельник

**Л-10 · 1847-03-15 · проигрыш.** Ванцель представил «Note sur la théorie des nombres complexes» (комиссары:
Коши, Лиувилль, Ламе), прямо отвечая на замечание Лиувилля: через евклидов алгоритм доказал единственность
для чисел вида a+br и a+br+cr², затем **без доказательства** распространил на все n: «On voit facilement que
le même mode de démonstration s'applique aux nombres complexes… qui dépendent des racines de r^n = 1 pour n
quelconque. Il suffira d'établir que le module de l'expression α + βr + … + μr^(n−1) est toujours moindre que 1
quand α, β, …, μ sont compris entre 0 et 1; ce qui se vérifie de plusieurs manières».
*Источник:* CR t. 24, pp. 430–434; цитируемый пассаж на p. 434. *kind:* contemporaneous.
*status:* corrected (пагинация обоих сборщиков исправлена; буква переменной μ, а не ρ; клетка изменена на
«проигрыш», так как утверждение опровергнуто через семь дней — см. Л-12).

## 1847-03-22 — заседание, понедельник

**Л-11 · 1847-03-22 · нужда.** В «Préliminaire» Коши воспроизводит возражение Лиувилля как уже установленный
факт дискуссии: «Le mode de démonstration, proposé par l'un de nos confrères… exigerait, comme l'a remarqué
M. Liouville, que l'on établît d'abord, pour les polynômes appelés complexes, des propositions analogues à
celles sur lesquelles repose, en arithmétique, la décomposition d'un nombre en facteurs premiers».
*Источник:* CR t. 24, p. 469. *kind:* contemporaneous. *status:* verified.

**Л-12 · 1847-03-22 · проигрыш.** В том же мемуаре («Sur de nouvelles formules relatives à la théorie des
polynômes radicaux, et sur le dernier théorème de Fermat») Коши прямо опровергает Ванцеля, адресуясь к
«l'auteur d'une Note insérée dans le Compte rendu de la dernière séance»: для корня 7-й степени из единицы
произведение сопряжённых триномов «sera égal au nombre 8, notablement supérieur à l'unité»; далее — «ce
produit surpasserait l'unité pour toute valeur du nombre premier n, égale ou supérieure à 17»; вывод:
«On voit, par ce qui précède, que la théorie générale des nombres complexes est encore à établir».
*Источник:* CR t. 24: начало на p. 469, контрпример p. 470, вывод p. 471. *kind:* contemporaneous.
*status:* verified. **Датированное опровержение через 7 дней после датированного заявления.**

## 1847-04-28 — Бреслау, письмо Куммера Лиувиллю

**Л-13 · 1847-04-28 · отказ.** Куммер отвечает на парижскую дискуссию: единственность разложения «n'a pas
lieu généralement tant qu'il s'agit de nombres complexes de la forme a0 + a1r + … + a(n−1)r^(n−1), mais qu'on
peut la sauver en introduisant un nouveau genre de nombres complexes que j'ai appelé nombre complexe idéal».
Сообщает, что результаты доложены Берлинской академии и напечатаны в её отчётах (**mars 1846**), мемуар
готовится у Крелле; и что он свёл невозможность x^n − y^n = z^n к двум свойствам простого n.
*Источник:* «Sur la théorie des nombres complexes. (Extrait d'une Lettre de M. Kummer à M. Liouville.)»,
JMPA t. 12, p. 136; параллельно CR t. 24, pp. 899–900 (оглашено 24 мая 1847). Письмо датировано
«Breslau, le 28 avril 1847». *kind:* contemporaneous. *status:* corrected (место публикации: письмо ЕСТЬ в CR,
pp. 899–900, вопреки утверждению сборщика 1; страницы уточнены с «898–899»).

**Л-14 · 1847-04-28 · опознание.** В начале того же письма: «Engagé par mon ami M. Lejeune-Dirichlet, je prends
la liberté de vous envoyer quelques exemplaires d'une Dissertation que j'ai écrite, il y a trois ans, à
l'occasion du jubilé séculaire de l'Université de Kœnigsberg, et d'une autre Dissertation d'un de mes amis et
disciples, M. Kronecker, jeune géomètre distingué».
*Источник:* JMPA t. 12, p. 136, первые строки / CR t. 24, p. 899. *kind:* contemporaneous. *status:* verified.
*Примечание:* опровергает посылку брифа о «письме Кронекеру» — речь о пересылке ЛИУВИЛЛЮ диссертации Кронекера.

## 1847-05-17 — заседание Парижской академии

**[событие без собственного документа] · 1847-05-17 · опознание.** Лиувилль устно сообщил Академии о работах
Куммера. Печатной стенограммы НЕТ: по полнотексту CR t. 24 в выпуске от 17.05.1847 слово «Kummer» не
встречается ни разу. Само событие засвидетельствовано ДВУМЯ независимыми документами выпуска от 24 мая —
Л-16 и Л-18. В ленту внесено как выводимое из двух verified-фактов; отдельного факта в своде не имеет.

## 1847-05-24 — заседание, понедельник

**Л-15 · 1847-05-24 · опознание.** Коши, читая «Mémoire sur les lieux analytiques», говорит: «Dans la dernière
séance, M. Liouville a parlé de travaux de M. Kummer, relatifs aux polynômes complexes… Si M. Kummer a fait
faire à la question quelques pas de plus, si même il était parvenu à lever tous les obstacles, j'applaudirais
le premier au succès de ses efforts».
*Источник:* CR t. 24, p. 887. *kind:* contemporaneous. *status:* verified.

**Л-16 · 1847-05-24 · прочее.** Ламе представил «Troisième Mémoire sur le dernier théorème de Fermat»,
сославшись на свой второй мемуар от 5 апреля 1847 г. (показатель 5), и свёл теорему к двум условиям на простой
показатель, перечислив 11, 17, 23, 29, 41 как простые, для которых выполнено первое.
*Источник:* CR t. 24, p. 888. *kind:* contemporaneous. *status:* corrected (дата: мемуар читан 24 мая и лишь
ссылается назад на 5 апреля, вопреки датировке сборщика 5). *Примечание:* λ = 23 стоит здесь у Ламе в списке,
где условие ВЫПОЛНЕНО, — не как исключение.

**Л-17 · 1847-05-24 · отказ.** В выпуске напечатано само письмо Куммера (см. Л-13) под заголовком
«THÉORIE DES NOMBRES. — Sur la théorie des nombres complexes. (Extrait d'une Lettre de M. Kummer à
M. Liouville.)».
*Источник:* CR t. 24, pp. 899–900 (заголовок заседания «SÉANCE DU LUNDI 24 MAI 1847»). *kind:* contemporaneous.
*status:* corrected.

**Л-18 · 1847-05-24 · опознание.** Редакционная сноска Лиувилля к письму, ОТСУТСТВУЮЩАЯ в версии JMPA:
«M. Liouville a remis aujourd'hui pour la Bibliothèque un exemplaire de chacun de ces deux Mémoires dont il
avait déjà dit quelques mots à la séance précédente».
*Источник:* CR t. 24, p. 899, сноска (1). *kind:* contemporaneous. *status:* verified.
*Примечание:* факт не найден ни одним из пяти сборщиков; второе, независимое от Коши свидетельство о 17 мая.

## 1847, май — JMPA, t. 12 (1re série)

**Л-19 · 1847 · опознание.** Редакционная «Note de M. Liouville» сразу после письма: работа Куммера датирована
1844 г., по-латыни, «De numeris complexis qui radicibus unitatis et numeris integris realibus constant»;
работа Кронекера «De unitatibus complexis» о комплексных делителях единицы вышла в 1845 г.; Лиувилль обещает
напечатать текст Куммера целиком и демонстративно уклоняется от суждения о приоритете: «Nous n'avons pas à
examiner ici en quoi les auteurs que nous citons s'accordent ou diffèrent, ni quels sont les droits de chacun
à l'antériorité… C'est au temps à fixer la valeur de leurs travaux».
*Источник:* JMPA t. 12, p. 136, вторая половина. *kind:* contemporaneous. *status:* verified.

**Л-20 · 1847-05 · опознание.** Сноска [*] Лиувилля к публикации латинского мемуара: он «imprimé pour la
première fois… en 1844, à Breslau… et adressé par l'Université de Breslau à l'Université de Kœnigsberg, à
l'occasion du **troisième** jubilé séculaire de cette dernière Université. Nous donnons ici le texte latin.
Nous n'avons pas eu le temps d'en faire la traduction».
*Источник:* JMPA t. 12, p. 185, сноска [*]. *kind:* contemporaneous. *status:* verified (локатор исправлен:
сведения на p. 185, а не на p. 136, как писал сборщик 1).

**Л-21 · 1847 · прочее.** Мемуар Ламе, напечатанный в JMPA сразу вслед за письмом Куммера, трактует разложение
на простые множители как установленный факт, не возвращаясь к возражению Лиувилля: «La décomposition d'un
nombre complexe en ses facteurs premiers, et la détermination du plus grand commun diviseur entre deux nombres
complexes, résultent de ces diverses propositions».
*Источник:* G. Lamé, «Mémoire sur la résolution, en nombres complexes, de l'équation A^n + B^n + C^n = 0»,
JMPA t. 12, pp. 172–184; цитата p. 176. *kind:* contemporaneous. *status:* verified.
*Примечание:* документ инерции — через два месяца после публичного указания на пробел он не закрыт.

## 1847 — Crelle, Bd. 35 (месяц выхода не установлен)

**Л-22 · 1847 · прочее.** Подзаголовок статьи «Zur Theorie der complexen Zahlen»: «(Auszug aus den Berichten
der Königl. Akad. der Wiss. zu Berlin vom **März 1845**.)» — расходится с «mars 1846» письма Куммера (Л-13).
*Источник:* Crelle 35, S. 319, строка под заглавием. *kind:* contemporaneous. *status:* verified
(сборщик 5 сверил визуально по скану высокого разрешения; ошибка OCR исключена). См. противоречие П-1.

**Л-23 · 1847 · отказ.** Первое печатное определение термина: «durch Einführung einer eigenthümlichen Art
imaginärer Divisoren, welche ich ideale complexe Zahlen nenne… Es haben vielmehr solche Zahlen f(a), wenn
gleich sie nicht in complexe Factoren zerlegbar sind, dennoch die Natur der zusammengesetzten Zahlen; die
Factoren aber sind alsdann nicht wirkliche, sondern ideale complexe Zahlen».
*Источник:* Crelle 35, S. 319. *kind:* contemporaneous. *status:* verified.

**Л-24 · 1847 · модель.** Формальное определение идеального простого множителя ЧЕРЕЗ ДЕЛИМОСТЬ: «Wenn f(a) die
Eigenschaft hat, dafs das Product f(a)·Ψ(η_r) durch q theilbar ist, so soll dies so ausgedrückt werden: Es
enthält f(a) den idealen Primfactor von q, welcher zu u = η_r gehört». Кратность — через делимость на q^μ;
условие эквивалентно системе из f сравнений.
*Источник:* Crelle 35, S. 322 (колонтитул «322 Kummer, zur Theorie der complexen Zahlen»). *kind:* contemporaneous.
*status:* corrected (локатор сужен с «S.321–324»; печатный текст даёт «u = η_r», Ψ(η) = ψ(η₁)…ψ(η_{e−1});
более ранний частный случай — на S. 321).

**Л-25 · 1847 · отказ.** Куммер сам цитирует по-латыни свою жалобу 1844 г. и объявляет её снятой: «Es erledigt
sich somit die Klage, welche ich in dem Breslauer Programm zur Jubelfeier der Universität Königsberg S. 18
aussprach: Maxime dolendum videtur… Auch sieht man, dafs die idealen Primfactoren die innere Natur der
complexen Zahlen aufschliefsen, sie gleichsam durchsichtig machen und das innere crystallinische Gefüge
derselben zeigen».
*Источник:* Crelle 35, S. 323. *kind:* contemporaneous. *status:* verified.
**Документ, прямо связывающий нужду 1844 г. с отказом 1847 г.; даёт независимую сверку чтения Л-03.**

**Л-26 · 1847 · опознание.** Сноска: «Ein Beweis dieses wichtigen Satzes, wenn gleich in weit geringerer
Allgemeinheit und in ganz anderer Form, findet sich in der Dissertation: De unitatibus complexis von
L. Kronecker, Berlin 1845».
*Источник:* Crelle 35, S. 324, сноска. *kind:* contemporaneous. *status:* verified.

**Л-27 · 1847 · опознание.** Там же: классификация идеальных чисел по классам совпадает с исследованием форм
λ−1-й степени, «über welche Dirichlet die Hauptresultate gefunden, aber noch nicht veröffentlicht hat, so dafs
ich nicht genau weifs, ob sein Princip der Classification mit diesem… genau übereinstimmt».
*Источник:* Crelle 35, S. 324. *kind:* contemporaneous. *status:* verified.
*Примечание:* факт не отмечен ни одним сборщиком; второй документированный случай признания Куммером
параллельной неопубликованной работы современника.

**Л-28 · 1847 · модель.** Следом в том же томе — большой мемуар «Über die Zerlegung der aus Wurzeln der Einheit
gebildeten complexen Zahlen in ihre Primfactoren» (S. 327–367, 41 страница): «In dem vorstehenden Aufsatze,
welchen ich als Einleitung zu dem hier folgenden anzusehen bitte, habe ich… die Resultate meiner
Untersuchungen… niedergelegt. Die Entwickelung und Begründung derselben soll nun der Gegenstand der
gegenwärtigen Abhandlung sein».
*Источник:* Crelle 35, S. 327. *kind:* contemporaneous. *status:* corrected (объём разрешён по IIIF-манифесту
GDZ: canvas 339–379 = S. 327–367; прав сборщик 1, ошибся сборщик 5).

**Л-29 · 1847 · модель.** § 2 большого мемуара: идеальные множители строятся алгоритмически — система уравнений
для периодов переистолковывается как система сравнений: «Wir fassen jetzt das System der in (1.) enthaltenen
Gleichungen als ein System von Congruenzen auf, für den Modul q; wo q eine Primzahl sein soll, welche der
Bedingung q^f ≡ 1 mod. λ genügt. Anstatt der Perioden η, η₁, …, η_(e−1) setzen wir die unbestimmten ganzen
Zahlen u, u₁, …, u_(e−1)».
*Источник:* Crelle 35, S. 329 (canvas 00000341). *kind:* contemporaneous. *status:* verified.
**Фиксирует: модель Куммера — вычислительно-конгруэнтная; ровно это станет предметом отказа Дедекинда (Л-38).**

## 1850-е — 1870

**Л-30 · 1859 · опознание.** «Towards the end of the 1850's, both Dedekind and Leopold Kronecker aimed to extend
Ernst Kummer's theory of ideal divisors from cyclotomic cases to arbitrary algebraic number fields. Dedekind
published such a theory in 1871, but he continued to modify and revise it over the next 23 years… Kronecker's
theory was published in 1882, although it seems to have been developed, for the most part, as early as 1859».
*Источник:* Avigad 2005, стр. 3. *kind:* secondary. *status:* verified, *confidence:* medium.
*Примечание:* «к 1859 г.» — оценка Авигада; сам Кронекер относит перелом к 1856–1857 гг. (Л-49).

**Л-31 · 1860 · прочее.** Куммер прочёл «Gedächtnissrede auf Gustav Peter Lejeune Dirichlet»; Дедекинд цитирует
её (S. 21–22): «Für diejenigen zerlegbaren Formen höherer Grade, deren lineare Factoren keine anderen
Irrationalitäten, als Einheitswurzeln für einen Primzahl-Exponenten, enthalten, hat Dirichlet während seines
Aufenthalts in Italien…» — цитата обрывается в скане.
*Источник:* VZT 1894, S. 623, сноска **) к § 185 (у Куммера — S. 21–22). *kind:* retrospective.
*status:* verified, *confidence:* medium. **Единственное найденное ретроспективное выступление самого Куммера —
и то опосредованно и с обрывом.**

**Л-32 · 1870 · опознание.** Расширяя теорию идеальных делителей Куммера, Кронекер даёт раннюю аксиоматизацию
понятия (конечной абелевой) группы: «The extremely simple principles on which Gauss's method rests… belong to
a more general and more abstract realm of ideas. It seems therefore to be appropriate to free the further
development of the latter from all inessential restrictions».
*Источник:* Kronecker, Monatsbericht 1870 (Werke Bd. 1, S. 274–275), англ. перевод Schlimm по Avigad 2005,
стр. 9. *kind:* secondary. *status:* verified, *confidence:* medium (постраничная ссылка на Monatsbericht
S. 881–889 у Авигада на прочитанной странице не подтверждается).

## 1871-03-01 — Брауншвейг: Vorwort ко 2-му изданию VZT

**Л-33 · 1871-03-01 · опознание.** «Endlich habe ich in dieses Supplement eine allgemeine Theorie der Ideale
aufgenommen, um auf den Hauptgegenstand des ganzen Buches von einem höheren Standpuncte aus ein neues Licht zu
werfen… Die Untersuchungen in diesem von Kummer geschaffenen Gebiete, welche Kronecker vor vierzehn Jahren
angestellt hat, sind bis jetzt nicht veröffentlicht, und ich vermag nach den damaligen brieflichen
Mittheilungen dieses ausgezeichneten Mathematikers nicht zu beurtheilen, in welchen Beziehungen seine
Principien zu den meinigen stehen».
*Источник:* VZT 1871, Vorwort, S. VII–VIII; подписано «Braunschweig, 1. März 1871». *kind:* retrospective
(пограничный случай — см. П-11а). *status:* verified.

**Л-34 · 1871-03-01 · проигрыш.** «Der Aufbau der Theorie in §. 163 befriedigt mich selbst zwar noch nicht
vollständig; allein es ist mir erst nach sehr langem Nachdenken geglückt, ihm diese Form zu geben, während ich
vor etwa zehn Jahren von der Theorie der höheren Congruenzen in Verbindung mit den Principien von Galois zu
einer ganz anderen Begründungsart gelangt war, welche einige Berührungspuncte mit der Theorie der idealen
Zahlen von Selling hat, mir aber jetzt weniger naturgemäss erscheint».
*Источник:* VZT 1871, Vorwort, S. VIII–IX. *kind:* retrospective. *status:* verified.
**Прямое свидетельство отброшенного пути, зафиксированное в момент публикации нового.**

## 1871 — VZT, 2-е издание, Supplement X (первопубликация теории идеалов)

**Л-35 · 1871 · отказ.** Конец § 162 — мотив отказа от куммеровской конструкции: «als nun diese Erscheinung
(bei den aus Einheitswurzeln gebildeten Zahlen) Kummer entgegentrat, so kam er auf den glücklichen Gedanken,
trotzdem eine solche Zahl μ' zu **fingiren** und dieselbe als ideale Zahl einzuführen… Allein die Befürchtung,
dass die unmittelbare Uebertragung der bei den wirklichen Zahlen üblichen Benennungen auf die idealen Zahlen im
Anfang leicht **Misstrauen** gegen die Sicherheit der Beweisführung einflössen könnte, veranlasst uns, die
Untersuchung dadurch in ein **anderes Gewand** einzukleiden, dass wir immer ganze Systeme von wirklichen Zahlen
betrachten».
*Источник:* VZT 1871, S. 451 (пассаж завершает § 162). *kind:* contemporaneous (тело первопубликации).
*status:* verified (локатор уточнён до S. 451; kind исправлен с retrospective).
**Этот мотивировочный пассаж ЕДИНСТВЕНЕН для издания 1871 г. и вычищен из последующих — см. П-7.**

**Л-36 · 1871 · отказ.** § 163 — первое печатное определение идеала как множества: «Wir gründen die Theorie der
in o enthaltenen Zahlen… auf den folgenden neuen Begriff. 1. Ein System a von unendlich vielen in o enthaltenen
Zahlen soll ein Ideal heissen, wenn es den beiden Bedingungen genügt: I. Die Summe und die Differenz je zweier
Zahlen in a sind wieder Zahlen in a. II. Jedes Product aus einer Zahl in a und einer Zahl in o ist wieder eine
Zahl in a».
*Источник:* VZT 1871, S. 452, пункт 1 § 163. *kind:* contemporaneous. *status:* verified (kind исправлен;
S. 452 подтверждена колонтитулом). **Опровергает MacTutor и Wikipedia — см. П-5.**

**Л-37 · 1871–1894 · прочее.** «Dedekind ultimately published four versions of his theory of ideals (1871, 1877,
1879, 1894). The versions of 1871, 1879, and 1894 appeared… in his "supplements"… to the second, third, and
fourth editions… The remaining version was written at the request of Lipschitz, translated into French, and
published in the Bulletin des Sciences Mathématiques et Astronomiques in 1876–1877. It was also published as an
independent monograph in 1877».
*Источник:* Avigad 2005, стр. 7. *kind:* secondary. *status:* verified.

## 1876 — 1880

**Л-38 · 1876-10-06 · опознание.** Письмо Дедекинда Рудольфу Липшицу — методологическая программа: «My efforts
in number theory have been directed towards basing the work not on arbitrary representations or expressions but
on simple foundational concepts and thereby… to achieve in number theory something analogous to what Riemann
achieved in function theory… Almost always they mar the purity of the theory by unnecessarily bringing in forms
of representation which should be results, not tools, of the theory».
*Источник:* Dedekind, Werke Bd. 3, Kap. LXV, S. 468–474; англ. перевод Х. Эдвардса по Avigad 2005, стр. 8
(библиографическая запись — стр. 30). *kind:* contemporaneous (документ времени работы), доступ только через
англ. перевод во вторичном источнике. *status:* verified, *confidence:* medium.

**Л-39 · 1878 · проигрыш.** Дедекинд объясняет, почему НЕ опубликовал более раннюю версию: «I first developed
the new principles… seven years ago, in the second edition of Dirichlet's Lectures on Number Theory… Excited by
Kummer's great discovery, I had previously worked for a number of years on this subject, though I based the
work on a quite different foundation, namely, the theory of higher congruences; but although this research
brought me very close to my goal, I could not decide to publish it because the theory obtained in this way
principally suffers two imperfections. One is that the investigation of a domain of algebraic integers is
initially based on the consideration of a definite number and the corresponding equation, which is treated as a
congruence… The second imperfection… is that sometimes peculiar exceptions arise which require special
treatment. My newer theory, in contrast, is based exclusively on concepts like that of field, integer, or
ideal, that can be defined without any particular representation of numbers».
*Источник:* Dedekind, «Über den Zusammenhang zwischen der Theorie der Ideale und der Theorie der höheren
Kongruenzen» (1878), Werke Bd. 1, S. 202–203; англ. перевод по Avigad 2005, стр. 10–11.
*kind:* retrospective. *status:* verified, *confidence:* medium (оригинал 1878 г. не открывался).
*Дополнение при сверке:* Авигад разворачивает, что́ такое «peculiar exceptions» (Avigad 2005, стр. 11–12):
теория высших сравнений работает, пока есть θ со степенным базисом {1, θ, …, θ^(k−1)} и p не делит дискриминант;
«there are even cases where for a given p no choice of θ will work; Dedekind gives a specific example of a cubic
extension of the rationals in which no choice of θ can be used to represent the ideal divisors of 2».
**Это и есть несходящееся вычисление Дедекинда — но зафиксировано оно в 1878 г., через семь лет после публикации
теории идеалов, а не до неё.**

**Л-40 · 1879 · нужда.** В 3-м издании (Supplement XI) появляется отсутствующий в 1871 г. драматизированный
нарратив об открытии Куммера: «schien es ein durchaus **hoffnungsloses** Unternehmen, die Zusammensetzung und
Theilbarkeit der Zahlen auf einfache Gesetze zurückführen zu wollen. Allein… so ist auch hier diese scheinbar
**unüberwindliche** Schwierigkeit zur Quelle einer wahrhaft grossen und **folgenschweren** Entdeckung geworden;
in der That fand Kummer… dass die alten Euclidischen Gesetze der Theilbarkeit auch in diesen Gebieten ihre volle
Geltung wiedererlangen, sobald dieselben durch die Einführung neuer Zahlen, die er **ideale Zahlen nannte**,
vervollständigt werden».
*Источник:* VZT 1879, S. 451–452 (завершение § 159). *kind:* retrospective. *status:* verified (локатор уточнён:
завершение § 159, а не начало § 160; слово «hoff-nungsloses» разорвано переносом). См. П-6.

**Л-41 · 1880 · опознание.** Золотарёв, открывая мемуар «Sur la théorie des nombres complexes», называет две
обобщающие работы — Селлинга и Дедекинда (в сноске (3): «LEJEUNE-DIRICHLET, Zahlen Theorie, zweite Auflage,
1871») — и заявляет: «si je ne me trompe, jusqu'ici il n'y a pas de théorie des nombres complexes pour le cas
des équations quelconques aussi satisfaisante que la théorie de M. Kummer pour le cas des équations binômes».
*Источник:* JMPA, 3e série, t. 6 (1880), pp. 51–84; введение и сноски (2), (3) на pp. 51–52.
*kind:* contemporaneous. *status:* verified.

**Л-42 · 1880-02-02 · прочее.** Кронекер в докладе «Über die Irreductibilität von Gleichungen» (Берлинская
академия, 2 февраля 1880): «Seitdem ich mich genau vor 35 Jahren bei Gelegenheit einer von Hrn. Kummer in
Breslau gehaltenen Vorlesung über Zahlentheorie auf seine specielle Anregung mit der Vereinfachung des Beweises
der Irreductibilität der Kreistheilungsgleichungen beschäftigt… bin aber erst neuerdings zu einem befriedigenden
Resultate gelangt, und zwar gerade rechtzeitig, um die erste Mittheilung davon meinem Freunde Kummer an seinem
siebzigsten Geburtstagsfeste am 29. v. M. widmen zu können».
*Источник:* Monatsberichte der Königl. Preuss. Akademie, 1880; переизд. Werke Bd. II, помета «[Gelesen…
am 2. Februar 1880.]». *kind:* retrospective. *status:* verified.

**Л-43 · 1880-11-11 · носитель 2.** Vorwort к 3-му изданию: «als eine von meinem Freunde H. Weber in Königsberg
in Gemeinschaft mit mir ausgeführte Untersuchung, welche demnächst erscheinen wird, das Resultat ergeben hat,
dass dieselben Principien sich mit Erfolg auf die Theorie der algebraischen Functionen übertragen lassen»;
далее — отсылки к Селлингу (Zeitschrift für Math. und Physik, Bd. 10, 1865) и Золотарёву (JMPA, 3-я серия, т. 6,
1880), «in welchen die Theorie der Ideale auf diejenige der höheren Congruenzen gegründet wird», и надежда, что
«auch die bezüglichen Untersuchungen von Kronecker… binnen Kurzem veröffentlicht werden».
*Источник:* VZT 1879, Vorwort, S. VIII, подписано «Braunschweig, 11. November 1880». *kind:* retrospective.
*status:* verified. **Первый анонс переноса на второй носитель — за два года до публикации.**

## 1881–1882

**Л-44 · 1881-09-10 · прочее.** Посвящение Кронекера Куммеру, открывающее «Grundzüge» как Festschrift к
пятидесятилетнему докторскому юбилею: «Seit siebenundvierzig Jahren Dein Schüler und beinahe ebenso lange Dein
Freund… die Anfügung einer neuen, vollständigen Ausgabe meiner Doctor-Dissertation, welche Dir am 10. September
1845 von mir gewidmet, aber damals nicht bis zu Ende abgedruckt worden ist… In Wahrheit verdanke ich Dir mein
mathematisches Dasein».
*Источник:* Kronecker, посвящение «Herrn Ernst Eduard Kummer zum 10. September 1881», Grundzüge (Berlin, 1882);
переизд. Werke Bd. II. *kind:* retrospective. *status:* verified.

**Л-45 · 1882 · опознание.** Вступление «Grundzüge»: «Gleichzeitige Beschäftigung mit algebraischen und
zahlentheoretischen Studien hat mich schon früh dazu geleitet, die arithmetische Seite der Algebra besonders ins
Auge zu fassen. So führte mich die Untersuchung der aus Wurzeln Abel'scher Gleichungen gebildeten complexen
Zahlen auf jenes algebraisch-arithmetische Problem, alle Abel'schen Gleichungen für irgend einen
Rationalitäts-Bereich aufzustellen, dessen Lösung ich im Juni 1853 der hiesigen Akademie mitgetheilt habe».
*Источник:* Crelle 92, S. 1 (шапка: «Abdruck einer Festschrift zu Herrn E. E. Kummers Doctor-Jubiläum,
10. September 1881»). *kind:* contemporaneous (содержание о 1853 г. — ретроспективное самоописание).
*status:* verified.

**Л-46 · 1882 · опознание.** Сноска: «Diese Darstellungsweise hat in dem speciellen Falle der algebraischen
Zahlen auch Herr Dedekind angewendet und **vor mir 1871 durch den Druck veröffentlicht** (vgl. die Vorbemerkung
zu meiner Abhandlung im Journ. f. Math. Bd. 91, S. 301). Die Bedeutung gebrochener idealer Zahlen ist schon auf
S. 31 der Kummer'schen Abhandlung „Ueber die allgemeinen Reciprocitätsgesetze" aus dem Jahre 1859 dargelegt».
*Источник:* Crelle 92, S. 2, сноска *). *kind:* contemporaneous. *status:* verified.

**Л-47 · 1882 · проигрыш.** § 1 «Grundzüge»: Кронекер отказывается принять термин «Körper»: «halte ich es für
angemessen, in der Terminologie die Ausdrücke mit entschieden räumlichem Gepräge zu vermeiden… habe ich auch
geglaubt, von der Adoption der Dedekind'schen Bezeichnung „Körper" absehen und meine ältere Bezeichnungsweise im
Wesentlichen beibehalten zu sollen… diese Zusammenfassung selbst durch das Wort „Rationalitäts-Bereich" in
schlichter, ungezwungener Weise ausdrückbar erschien».
*Источник:* Grundzüge, книжное изд. 1882, § 1, ок. S. 3–4. *kind:* contemporaneous. *status:* corrected
(мотивировка: ИСКЛЮЧИТЕЛЬНО избегание пространственных коннотаций, а не «гауссовская систематика», как
глоссировал сборщик 4).

**Л-48 · 1882 · проигрыш.** Методологическое расхождение сформулировано прямо: «In der That stellt Herr Dedekind,
die Abweichung von der Kummerschen Auffassung selbst hervorhebend, den Inbegriff der durch einen idealen Divisor
theilbaren wirklichen Zahlen an die Spitze der Entwickelung, während meine Begriffsbestimmungen von jeher… in
Uebereinstimmung mit der Kummerschen Gedankenrichtung auf die Erhaltung des Divisoren-Begriffes selbst zielten».
*Источник:* Grundzüge, книжное изд. 1882, S. 80–81 (пассаж пересекает границу страниц). *kind:* contemporaneous.
*status:* corrected (источник исправлен с «Werke Bd. II, §22, ок. S. 338» — там по поисковым строкам не находится).

**Л-49 · 1882 · проигрыш.** § 19 «Grundzüge» — ретроспективное описание собственной неудачи: «Ich meinerseits
habe bei meinen Arbeiten über complexe Zahlen in den Jahren 1843 bis 1846 zu einer solchen Erkenntniss nicht
durchzudringen vermocht. Als ich dann später in den Jahren 1856 und 1857… auf meine früheren Untersuchungen…
zurückzukommen, konnte ich mich auf das bereits seit einem Jahrzehnt bekannte Kummer'sche Princip stützen».
*Источник:* Grundzüge, § 19; переизд. Werke Bd. II. *kind:* retrospective. *status:* verified.

**Л-50 · 1882 · проигрыш.** О Золотарёве: «Dieser Versuch ist aber, wie ich glaube, **verfehlt**; und nach den
von Zolotareff im Eingange seiner Arbeit citirten Dedekind'schen Publicationen aus dem Jahre 1871, in welchen mit
voller Klarheit und Schärfe die Nothwendigkeit dargethan ist, jene beschränkte Grundlage der complexen
Zahlentheorie aufzugeben, musste ein Versuch, dieselbe dennoch beizubehalten, von vorn herein… aussichtslos
erscheinen».
*Источник:* Grundzüge, книжное изд. 1882, S. 118. *kind:* contemporaneous. *status:* verified (confidence
повышен с medium до high; номер тома журнала в самом пассаже НЕ назван — сказано «im neusten Bande»).

**Л-51 · 1882 · носитель 2.** Дедекинд и Вебер открывают «Theorie der algebraischen Functionen einer
Veränderlichen» явным переносом: «wiesen die mit bestem Erfolge in der Zahlentheorie angewandten Methoden, die
sich an Kummers Schöpfung der idealen Zahlen anschliessen… auf den richtigen Weg… Auf diese Weise gelangt man zu
dem Begriff des Ideals, ein Name, der aus Kummers zahlentheoretischen Arbeiten stammt, wo die nicht existirenden
Theiler als „ideale Theiler" in die Rechnung eingeführt werden. Obwohl es sich in der vorliegenden Arbeit
keineswegs um „ideale" Functionen handelt, sondern alle Operationen nur an Systemen wirklich existirender
Functionen ausgeführt werden, schien es doch zweckmässig, den Namen „Ideal"… beizubehalten».
*Источник:* Crelle 92, S. 181–182 (Einleitung). *kind:* contemporaneous. *status:* verified.

**Л-52 · 1882 · носитель 2.** Сноска с цепочкой ссылок: «Die idealen Zahlen sind von Kummer zuerst eingeführt
durch die Abhandlung: Zur Theorie der complexen Zahlen (Crelle's Journal, Bd. 35); eine weitere Fortführung und
eine allgemeine Darstellung der Theorie der algebraischen Zahlen findet man in der **zweiten und dritten**
Auflage von Dirichlets Vorlesungen über Zahlentheorie, sowie in der Abhandlung von Dedekind: Sur la théorie des
nombres entiers algébriques (Paris 1877…). Die Kenntniss dieser Schriften wird aber in unserer Arbeit nirgends
vorausgesetzt».
*Источник:* Crelle 92, S. 182, сноска *). *kind:* contemporaneous. *status:* verified.

**Л-53 · 1882 · опознание.** «Aus mündlichen Mittheilungen ist uns jetzt bekannt geworden, dass bereits vor
Jahren Kronecker mit Beziehung auf die Arbeiten von Weierstrass Untersuchungen angestellt hat, die auf derselben
Grundlage, wie die unsrigen, beruhen».
*Источник:* Crelle 92, S. 182. *kind:* contemporaneous. *status:* verified.

**Л-54 · 1882 · носитель 2.** Результат переноса: «Ins Besondere ergiebt sich der Satz, dass jedes Ideal auf eine
einzige Weise in Factoren zerlegbar ist, welche selbst nicht weiter zerlegt werden können und daher Primideale
genannt werden. Diese Primideale entsprechen den linearen Factoren in der Theorie der ganzen rationalen
Functionen. Auf Grund derselben gelangt man zu einer völlig präcisen und allgemeinen Definition des „Punktes der
Riemann'schen Fläche", d. h. eines vollkommen bestimmten Systems von Zahlwerthen, welche man den Functionen des
Körpers widerspruchslos beilegen kann».
*Источник:* Crelle 92, S. 183. *kind:* contemporaneous. *status:* corrected (мелкая правка цитаты: печатный текст
даёт раздельное «Ins Besondere»).

**Л-55 · 1882 · носитель 2.** «He wrote an important paper with Dedekind… in which they examined algebraic
functions from an algebraic rather than analytic point of view… the notion of point on an abstract algebraic
curve is defined for the first time in history, thus taking a decisive step towards the creation of modern
algebraic geometry».
*Источник:* MacTutor, биография Heinrich Weber, раздел о совместной работе. *kind:* secondary.
*status:* verified (страница переоткрыта 2026-09-03), *confidence:* medium (оценочное суждение без ссылок;
фактическое ядро подтверждается Л-54).

## 1887 — 1897

**Л-56 · 1887 · опознание.** «In (1895), he also described an additional, intermediate version which he obtained
in 1887, and which was later obtained, independently, by Hurwitz».
*Источник:* Avigad 2005, стр. 22. *kind:* secondary. *status:* verified (kind исправлен с retrospective:
цитируется формулировка Авигада, не Дедекинда), *confidence:* medium.

**Л-57 · 1890 · носитель 2.** «Such reasoning [неконструктивные, теоретико-множественные рассуждения
дедекиндовского типа] was used, for example, by Hilbert, in proving his Basissatz in 1890».
*Источник:* Avigad 2005, стр. 14. *kind:* secondary. *status:* verified, *confidence:* medium
(первоисточник не открывался).

**Л-58 · 1893-09-30 · опознание.** Vorwort к 4-му изданию: «Nur das letzte Supplement… hat eine vollständige
Umarbeitung erfahren… Durch die Veröffentlichung derselben (1882 in Crelle's Journal, Bd. 92) hat Kronecker
einen Wunsch erfüllt, den ich schon öfter, zuletzt im Juni 1880 bei Gelegenheit der Enthüllung unseres
Braunschweiger Standbildes von Gauss ausgesprochen hatte, wo zugleich verabredet wurde, dass diese Abhandlung
vor der von H. Weber und mir ausgearbeiteten Theorie der algebraischen Functionen… erscheinen sollte. Ihr Inhalt
war auch für mich **vollständig neu**, da ich nach einer alten brieflichen Mittheilung aus dem Jahre 1857
geglaubt hatte, die Theorie Kronecker's auf ganz anderen Wegen suchen zu müssen… Ein sicheres Urtheil über die
Vorzüge und Nachtheile dieser Theorie auszusprechen… halte ich jetzt noch nicht für möglich».
*Источник:* VZT 1894, Vorwort, S. V–VIII, подписано «Bad Harzburg, 30. September 1893». *kind:* retrospective.
*status:* verified.

**Л-59 · 1893-09-30 · проигрыш.** Там же — признание собственной неудачи: «so wird man es für sehr wahrscheinlich
halten, dass auch für die Idealtheorie noch einfachere Grundlagen, als die bisher bekannten, aufgefunden
werden… und ich habe schon vor vielen Jahren versucht, diesen Weg einzuschlagen; hierbei ist es mir zwar nicht
gelungen, eine wesentliche Vereinfachung zu erzielen» (путь — через теорему о наибольшем общем делителе двух
произвольных целых алгебраических чисел; рекомендован вниманию более молодых математиков; отдельно упомянут
собственный «маленький вклад» в Mittheilungen der Deutschen mathematischen Gesellschaft in Prag, 1892).
*Источник:* VZT 1894, Vorwort, S. VII–VIII. *kind:* retrospective. *status:* verified.

**Л-60 · 1894 · опознание.** Сноска к «Körper», отсутствующая в 1871 и 1879 гг.: «Anfangs, in meinen Göttinger
Vorlesungen (1857 bis 1858), hatte ich denselben Begriff mit dem Namen eines rationalen Gebietes belegt, der
aber weniger bequem ist. Der Begriff fällt im Wesentlichen zusammen mit Dem, was Kronecker einen
Rationalitätsbereich genannt hat (Grundzüge… 1882). Vergl. auch die von H. Weber und mir verfasste Theorie der
algebraischen Functionen einer Veränderlichen. (Crelle's Journal, Bd. 92, 1882)».
*Источник:* VZT 1894, Supplement XI, § 160, сноска **), S. 452–453. *kind:* retrospective. *status:* verified.
См. П-8.

**Л-61 · 1894 · опознание.** Вторая такая сноска: «Schon in meinen Göttinger Vorlesungen (1857 — 1858) habe ich
diese Theorie in der Weise vorgetragen, dass sie für Gruppen π von beliebigen Elementen π gilt».
*Источник:* VZT 1894, Supplement XI, § 166, сноска *), S. 484. *kind:* retrospective. *status:* verified
(локатор уточнён с «S. 484–485»). См. П-8.

**Л-62 · 1895 · проигрыш.** «As a result, one will understand that I preferred my definition of an ideal, based on
a characteristic **inner** property, to that that based on an **external** form of representation, which
Mr. Hurwitz uses in his treatise. For the same reasons, I could not be fully satisfied with the proof of
Theorem 3 mentioned above, based on [the Prague Theorem], since, by mixing in functions of variables the purity
of the theory is, in my opinion, tarnished». Там же — признание, что и собственное индуктивное доказательство
не вполне удовлетворяло, так как в нём доминирует «mechanical calculation».
*Источник:* Dedekind, «Über die Begründung der Idealtheorie» (Göttinger Nachrichten, 1895), Werke Bd. 2;
англ. перевод по Avigad 2005, стр. 24–25. *kind:* retrospective. *status:* verified, *confidence:* medium.
*Примечание:* у Авигада напечатано «to that that based» — опечатка источника сохранена.

**Л-63 · 1897 · носитель 2.** «In 1897 the Weierstrass method of power-series development for algebraic functions
led him [Hensel] to the invention of the p-adic numbers… It was in this book [Theorie der algebraischen Zahlen,
1908] that he developed his great idea of p-adic numbers into a systematic theory».
*Источник:* MacTutor, биография Kurt Hensel. *kind:* secondary. *status:* verified (страница переоткрыта
2026-09-03), *confidence:* medium.

## 1905 — 2005

**Л-64 · 1905 · носитель 2.** Ласкер впервые ввёл понятие примарного идеала и доказал теорему о примарном
разложении, но только для кольца многочленов: «the decomposition into maximal primary ideals is given by Lasker
for the polynomial ring with arbitrary complex or integer coefficients, and taken further by Macaulay at
particular points. Both concern themselves with elimination theory».
*Источник:* E. Noether, «Idealtheorie in Ringbereichen» (1921), введение и сноска 3 («E. Lasker, Zur Theorie der
Moduln und Ideale. Math. Ann. 60 (1905), p20»), англ. перевод D. Berlyne, arXiv:1401.2577; независимо —
MacTutor, биография Lasker. *kind:* secondary. *status:* verified (оригинал Ласкера не открывался).

**Л-65 · 1921 · носитель 2.** Нётер открывает «Idealtheorie in Ringbereichen» формулировкой цели переноса:
«This paper aims to convert the decomposition theorems for the integers or the decomposition of ideals in
algebraic number fields into theorems for ideals in arbitrary integral domains (and rings in general)»;
опирается на «Theorem of the Finite Chain» для конечных модулей, атрибутируемую в сноске: «Initially stated for
modules by Dedekind: Zahlentheorie, Suppl. XI, §172».
*Источник:* Math. Annalen 83 (1921), введение; англ. перевод arXiv:1401.2577. *kind:* contemporaneous (документ
работы самой Нётер по переносу). *status:* verified, *confidence:* medium (немецкий оригинал не открывался).

**Л-66 · 1921 · прочее.** Там же — самоограничение автора переноса: «Only the finite ideal basis is made use of
here, so theorems and methods for general rings remain to be addressed, becoming more of a problem through this
paper in terms of equality in size (§11)».
*Источник:* там же, введение. *kind:* contemporaneous. *status:* verified, *confidence:* medium.

**Л-67 · 1975 · прочее · [UNVERIFIED — помечено]** Собрание сочинений Куммера под редакцией Андре Вейля
(2 тома, Springer, 1975) есть в каталоге archive.org (`ernsteduardkumme0002andr`), но полный текст закрыт
режимом контролируемой цифровой выдачи (HTTP 403 при попытке получить OCR), поэтому возможные
историко-редакторские комментарии Вейля прочитать не удалось. Цитаты нет; проверить содержание невозможно.
*kind:* secondary. *status:* **unverified**, *confidence:* low. **Это не факт о кейсе, а протокол
недоступности источника.**

**Л-68 · 2005 · проигрыш.** Непримирённый раскол в оценке цены переноса: «Edwards, who laments mathematics'
departure from the explicitly algorithmic styles of Gauss, Kummer, and Kronecker, judges Dedekind's **first**
version of ideal theory to be his best (Edwards 1980, 1992). In contrast, Emmy Noether, who inherited the mantle
of structuralism from Dedekind through Hilbert, expressed a clear preference for the **last**… there has been a
small but committed minority that agrees with Edwards' contemporary assessment that something important has been
lost in turning away from a more explicit, algorithmic standpoint».
*Источник:* Avigad 2005, стр. 9–10. *kind:* secondary. *status:* verified.

---

## 1.1. Опровергнутое: в ленту НЕ входит

В своде фактов нет ни одной записи со `status: refuted`. Опровергнуты не факты, а УТВЕРЖДЕНИЯ — сборщиков
стадии 1, вторичных источников и самого брифа. Перечисляю отдельно, как требует задание:

| # | Опровергнутое утверждение | Чем опровергнуто |
|---|---|---|
| О-1 | Сборщик 1: «печатного текста Куммера в Comptes Rendus нет», письмо «опубликовано не в CR, а в JMPA» | Письмо напечатано в CR t. 24, pp. 899–900 (заседание 24.05.1847). Причина ложного отрицания установлена: постатейный файл archive.org покрывает только pp. 886–896 |
| О-2 | MacTutor (биография Дедекинда): идеалы введены «in the third and fourth editions… 1879 and 1894»; второе издание не упомянуто | Л-36 (§ 163, S. 452 издания 1871), Л-33, Л-46, Л-41, Л-52, а также Л-39 («seven years ago, in the second edition») — шесть независимых свидетельств |
| О-3 | Wikipedia, «Ideal (ring theory)»: «In 1876, Richard Dedekind… in the third edition of Dirichlet's book» | Те же шесть. Ошибка двойная: и год, и номер издания (3-е вышло в 1879 г.; 1876–77 — отдельная французская публикация) |
| О-4 | Сборщик 1: в мемуаре 1844 г. «никакого признака, что λ = 23 выделен как исключительный случай, нет» | Л-05: таблица λ = 23 аномально коротка и снабжена особой ремаркой. НО: интерпретации Куммер не даёт, и явного утверждения об исключительности λ = 23 по-прежнему не найдено |
| О-5 | Посылка брифа: «мемуар 1844 „De numeris complexis…", Breslau; **письмо Кронекеру**» | Л-14: переписки Куммер→Кронекер здесь не документировано; Куммер переслал ЛИУВИЛЛЮ свой мемуар и ОТДЕЛЬНО диссертацию Кронекера |
| О-6 | Посылка брифа: «письмо Куммера Лиувиллю (Comptes Rendus 24.05.1847?)» как одна дата | Л-13/Л-17: письмо ДАТИРОВАНО 28.04.1847, оглашено и напечатано 24.05.1847 — две разные даты, обе верны |
| О-7 | Краткое описание брифа, слившее место печати и адресата мемуара 1844 г. | Л-20: напечатан в Бреслау, АДРЕСОВАН Кёнигсбергскому университету к его 300-летнему юбилею |
| О-8 | Заявление Ванцеля 15.03.1847, что евклидов алгоритм проходит «pour n quelconque» | Л-12: контрпример Коши 22.03.1847 (произведение = 8 для корней 7-й степени; превосходит единицу для всех простых n ≥ 17). *Это опровержение внутри истории — сам факт Л-10 остаётся в ленте* |
| О-9 | Глосс сборщика 4: Кронекер мотивировал отказ от «Körper» следованием гауссовскому стилю систематики | Л-47: в тексте этого нет; мотивировка — исключительно избегание пространственных коннотаций |
| О-10 | Атрибуция сборщика 2: пассаж о расхождении с Дедекиндом — в Werke Bd. II, § 22, ок. S. 338 | Л-48: по поисковым строкам там не находится; текст локализован в книжном издании 1882 г., S. 80–81 |

*Счёт ленты:* 68 записей на 67 фактов свода + 1 событие без собственного документа (17.05.1847). Факт о письме
Куммера разнесён по двум датам: написание в Бреслау 28.04.1847 — Л-13; оглашение и печать в Париже 24.05.1847 —
Л-17. Статусы: unverified — одна запись (Л-67, помечена); corrected — десять (Л-05, Л-10, Л-13, Л-16, Л-17,
Л-24, Л-28, Л-47, Л-48, Л-54); остальные verified. Записей со status refuted нет.

---

# 2. Противоречия между источниками — помечены, не разрешены

Порядок §4 регламента: «Не сглаживайте противоречия между источниками. Противоречие — данные». Ниже у каждого
пункта указано, разрешается ли он прочитанными источниками. Там, где сверка стадии 1 уже разрешила спор
СБОРЩИКОВ (а не спор источников), это сказано прямо — но само противоречие остаётся записанным.

### П-1 · ДАТА БЕРЛИНСКОГО СООБЩЕНИЯ: март 1845 против марта 1846 · **НЕ РАЗРЕШАЕТСЯ**
Два документа самого Куммера, оба 1847 г., оба сверены дословно, расходятся на год.
- Crelle 35, S. 319, подзаголовок: «(Auszug aus den Berichten der Königl. Akad. der Wiss. zu Berlin vom
  **März 1845**.)» (Л-22; сборщик 5 отдельно сверил визуально по скану высокого разрешения — ошибка OCR исключена).
- Письмо Лиувиллю 28.04.1847: результаты «communiqués à l'Académie de Berlin et imprimés dans les Comptes rendus
  (**mars 1846**)» (Л-13).
**Не сглаживается.** Возможное объяснение (два разных сообщения: 1845 — об идеальных числах, 1846 — о приложении
к теореме Ферма) прочитанными источниками НЕ подтверждается. Разрешающий документ — Monatsberichte Берлинской
академии за оба месяца — не найден (см. §6).
**Следствие для датировки изобретения:** момент, от которого отсчитывается «до изобретения», сам определён
с точностью до года. Для kill-gate это существенно и учтено в §5.

### П-2 · МЕСТО ПУБЛИКАЦИИ ПИСЬМА КУММЕРА · **разрешено на стадии 1** (спор сборщиков, не источников)
Сборщик 1 утверждал, что письма в CR нет; сборщики 3 и 5 — что есть. Правы 3 и 5: CR t. 24, pp. 899–900
(заголовок «SÉANCE DU LUNDI 24 MAI 1847» — строка 48295 полнотекста; письмо — строка 48952). Точные страницы
899–900, а не «898–899» (сборщик 3). Причина ошибки сборщика 1 установлена (усечённый постатейный файл).

### П-3 · ПАГИНАЦИЯ ЗАМЕТКИ ВАНЦЕЛЯ · **разрешено на стадии 1**
Сборщик 1: «430–433»; сборщик 3: «431–434». Оба частично неверны. По печатным колонтитулам: маркер «( 43o )»
непосредственно перед заголовком → заметка начинается на p. 430; цитируемый пассаж — на p. 434. Верно: pp. 430–434.

### П-4 · ОБЪЁМ ВТОРОГО МЕМУАРА КУММЕРА 1847 г. · **разрешено на стадии 1**
Сборщик 1: «S. 327–367, 41 страница»; сборщик 5: «S. 327–352». По IIIF-манифесту структуры тома GDZ
(`PPN243919689_0035`, скачан curl, сохранён как `gdz35_manifest.json`): «Zur Theorie…» = canvas 331–338 =
S. 319–326; «Über die Zerlegung…» = canvas 339–379 = S. 327–367. Прав сборщик 1.

### П-5 · ГДЕ ВПЕРВЫЕ НАПЕЧАТАНЫ ИДЕАЛЫ: вторичные источники против первоисточников · **разрешено в пользу первоисточников**
- MacTutor (биография Дедекинда, переоткрыта 2026-09-03): «It was in the **third and fourth** editions…
  published in 1879 and 1894, that Dedekind wrote supplements in which he introduced the notion of an ideal».
- Wikipedia, «Ideal (ring theory)» (переоткрыта 2026-09-03): «In **1876**… in the **third edition**».
Оба опровергнуты (см. О-2, О-3). **Противоречие оставлено записанным, потому что оно диагностическое: два самых
доступных вторичных источника согласно смещают дату изобретения на 5–8 лет вперёд, и любая реконструкция,
начатая с них, промахивается мимо единственного издания, где записан мотив отказа (Л-35, П-7).**

### П-6 · ЧТО ГОВОРИТ ДЕДЕКИНД О КУММЕРЕ, МЕНЯЕТСЯ ОТ ИЗДАНИЯ К ИЗДАНИЮ · **противоречие внутри одного автора; не сглаживается**
Драматизированный нарратив «казалось совершенно безнадёжным предприятием → источник поистине великого и
многозначительного открытия» (Л-40) ОТСУТСТВУЕТ в издании 1871 г. и ПРИСУТСТВУЕТ в 1879 и 1894 гг. Проверено
частотно по трём сканам: «folgenschwer» 0/1/1, «unüberwindlich» 0/1/1, «ideale Zahlen nannte» 0/1/1.
**Героизация открытия Куммера добавлена Дедекиндом задним числом не ранее 1879 г. — через 32 года после 1847 г.
и через 8 лет после первой публикации собственной теории.**

### П-7 · ЗЕРКАЛЬНОЕ ИСЧЕЗНОВЕНИЕ МОТИВИРОВКИ · **противоречие внутри одного автора; не сглаживается**
Объяснение 1871 г., ПОЧЕМУ Дедекинд заменил куммеровские фикции системами действительных чисел (Л-35),
присутствует ТОЛЬКО в издании 1871 г.: «Misstrauen» 1/0/0, «fingiren» 1/0/0, «glücklichen Gedanken» 1/0/0.
Само определение идеала при этом сохранено и развито.
**Единственная прямая формулировка мотива отказа существует лишь в первом издании теории и потом вычищена.**
Вместе с П-6: из более поздних изданий убран мотив собственного отказа и добавлена героизация чужого открытия.

### П-8 · ПРИТЯЗАНИЯ ДЕДЕКИНДА НА 1857–1858 гг. ПОЯВЛЯЮТСЯ ТОЛЬКО В 1894 г. · **ОТКРЫТО**
Сноски Л-60 и Л-61 отсутствуют в изданиях 1871 и 1879 гг.: «rationales Gebiet» 0/0/1, «Göttinger Vorlesungen»
0/0/2. Именно это издание сам Дедекинд в Vorwort 1893 г. связывает с изучением конкурирующей работы Кронекера
(Л-58). **Источники не позволяют установить, точная ли это память о лекциях 1857–58 гг. (независимого документа
того времени не найдено) или ретроспективное укрепление приоритета в ответ на публикацию Кронекера.** Не разрешаю.

### П-9 · ВЕРСИИ ДЕДЕКИНДА И КРОНЕКЕРА О ВЗАИМНОМ ЗНАНИИ · **НЕ ПРИМИРЯЮТСЯ**
- Дедекинд (Vorwort 1893, Л-58): содержание «Grundzüge» было для него «vollständig neu», ибо по письму 1857 г.
  он полагал, что теорию Кронекера надо искать «auf ganz anderen Wegen»; уверенного суждения о её достоинствах
  он и в 1893 г. вынести не может.
- Кронекер (Grundzüge 1882, Л-46, Л-48): признаёт печатный приоритет Дедекинда 1871 г., но настаивает, что его
  собственный дивизорный подход иной ПО ЦЕЛИ — «auf die Erhaltung des Divisoren-Begriffes selbst» против
  дедекиндовского «Inbegriff der… theilbaren wirklichen Zahlen» — и восходит к его независимым работам, которые
  он сам в § 19 признаёт неудачными вплоть до 1856–1857 гг. (Л-49).
**Кто на кого и когда повлиял, источники не согласовывают.** Письмо Кронекера 1857 г. не найдено — известно
только по одностороннему пересказу Дедекинда.

### П-10 · ИТОГ СПОРА ДЕДЕКИНД–КРОНЕКЕР НЕ КОНСТАТИРОВАН НИ ОДНОЙ СТОРОНОЙ · **ОТКРЫТО**
В собранных источниках — только взаимоисключающие самооценки 1882–1894 гг.: Дедекинд демонстративно
ОТКАЗЫВАЕТСЯ судить о теории Кронекера (Л-58), Кронекер настаивает на верности своего подхода замыслу Куммера
(Л-48). Единственная оценка «кто победил» приходит от вторичного источника (Л-68) и сама расколота: Эдвардс —
за первую, наиболее алгоритмическую версию Дедекинда; Нётер — за последнюю, наиболее абстрактную.

### П-11 · РАЗНОГЛАСИЯ СБОРЩИКОВ ПО ПОЛЮ `kind` (классификация, не факты) · **частично разрешено**
(а) Vorwort 1871 (Л-33, Л-34): сборщик 1 — contemporaneous, сборщик 2 — retrospective. **Пограничный случай,
оставлен помеченным:** по таксономии брифа предисловие — retrospective, и содержание ретроспективно (письма
1857 г., собственный путь ≈1861 г.), но документ СОПРОВОЖДАЕТ первую публикацию теории идеалов. Принято
retrospective с оговоркой. Для kill-gate (§5) это различие решающее.
(б) § 162 и § 163 издания 1871 (Л-35, Л-36): сборщик 5 — retrospective; исправлено на contemporaneous
(тело первопубликации).
(в) Письмо Липшицу 1876 (Л-38): сборщик 3 — secondary, сборщик 4 — contemporaneous. Принято contemporaneous
(тип ДОКУМЕНТА) с понижением confidence до medium (тип ДОСТУПА — англ. перевод во вторичном источнике).
(г) Grundzüge 1882: сборщик 1 — contemporaneous, сборщик 2 — retrospective для одного и того же текста сноски
S. 2. Принято contemporaneous для документа 1882 г.; retrospective — только для пассажей чистого воспоминания
(§ 19 о 1843–1846 гг., посвящение о «47 годах»).

### П-12 · ПОСЫЛКИ САМОГО БРИФА, ОПРОВЕРГНУТЫЕ ПЕРВОИСТОЧНИКАМИ
См. §1.1, пункты О-5, О-6, О-7. Записаны как данные: краткое описание кейса в брифе слило (а) дату написания
письма с датой его оглашения, (б) пересылку диссертации Кронекера с перепиской с Кронекером, (в) место печати
мемуара 1844 г. с его адресатом и поводом.

### П-13 · λ = 23 · **скорректировано, но искомого утверждения нет**
Сборщик 1: признака исключительности λ = 23 в мемуаре 1844 г. нет. Скорректировано: признак есть (Л-05 — три
простых против длинных списков для λ = 13, 17, 19 и особая ремарка), **но интерпретации Куммер не даёт и нигде
не говорит, что λ = 23 — первый случай нарушения единственности.** Одновременно обратное: у Ламе в CR t. 24,
p. 888 (24.05.1847) число 23 стоит в списке простых, для которых условие ВЫПОЛНЕНО (Л-16).
**Явного contemporaneous утверждения об исключительности λ = 23 не найдено ни в одном прочитанном документе.**

---

# 3. «За неделю до»

Требование §4 регламента: «„Озарение" — почти всегда сжатие месяцев. Спрашивайте, что было за неделю до, и в
каком виде задача лежала на столе в тот момент». Требование §8: пустое записывается как пустое.

В кейсе ДВА изобретения, и ответ для них противоположный. Раздел разделён.

## 3.1. Куммер, идеальные числа. Опорная дата — март 1845 либо март 1846 (П-1, не разрешено)

**Документа за неделю до нет.** Ближайший датированный документ времени работы отстоит на месяцы — но он есть,
он печатный, и он содержит именно несходящееся вычисление.

**Что лежало на столе — по документу 1844 г. (JMPA t. 12, pp. 185–212; kind contemporaneous):**

1. **Несходящийся счёт числа множителей.** «Inde sequeretur ut quilibet numerus primus p = mλ + 1 esset
   productum λ − 1 factorum complexorum conjunctorum, quod in universum non pro omnibus valoribus numerorum p et
   λ valere supra demonstravimus» (p. 203, Л-03). Ожидаемое разложение простого p = mλ+1 на λ−1 сопряжённых
   комплексных множителей проходит НЕ для всех p и λ, и это уже доказано выше в том же мемуаре.
2. **Несокращаемость — явление, названное по имени.** «Quod idem numerus primus p pluribus modis diversis in
   factores duos diffinditur, et quod producta certa ex iis factoribus formata per alios factores divisibilia
   fiunt, **neque tamen hi ipsi factores cum illis compensari possunt**, res maximi momenti, indicat hos
   factores non esse primos sed compositos» (pp. 185–186, Л-01). То же простое расщепляется на два множителя
   несколькими разными способами; произведения делятся на другие множители, а сами множители против них не
   сокращаются — «дело величайшей важности», указывающее, что эти множители не простые, а составные.
3. **Открытая задача, сформулированная в лоб и отданная другим.** § IX: «e re est ut inveniatur qui et quales
   sint ii numeri λ et p, pro quibus talis repraesentatio locum habet, atque ut pro iis qui minorem tantum
   numerum factorum primorum habent, horum factorum numerus et forma propria indagetur, quod vero problema
   ulterioribus virorum doctorum perscrutationibus relinquendum est» (p. 203, Л-04). То есть: найти, для каких λ
   и p представление есть, а для остальных — установить ЧИСЛО и СОБСТВЕННУЮ ФОРМУ множителей. Это дословная
   постановка того, что через год-два станет идеальным множителем.
4. **Вычислительная база под рукой.** Разложения на простые множители ВСЕХ простых ниже тысячи вида 5m+1, 7m+1,
   11m+1, 13m+1, 17m+1, 19m+1, 23m+1, посчитанные лично, с методами и таблицами (pp. 203–204, Л-04; таблицы §X,
   pp. 207–208, Л-05).
5. **Место, где счёт ломается заметнее всего.** λ = 23: три простых (599, 491, 829) против длинных списков для
   λ = 13, 17, 19, плюс ремарка «Reliqui numeri primi formae 23m + 1 infra mille undecim factoribus primis
   constant» со списком 47, 139, 277, 461, 967 (Л-05). **Интерпретации Куммер не даёт** (П-13).
6. **Формулировка нужды и прямо названная развилка.** «Maxime dolendum videtur… Eam ipsam ob causam numeri
   complexi, quos hic tractamus, **imperfecti** esse videntur, et dubium inde oriri posset, utrum hi numeri…
   praeferendi, an **alii quaerendi** essent, qui in hac re fundamentali analogiam cum numeris integris realibus
   servarent» (p. 203, Л-03). Развилка названа за три года до решения: либо эти числа несовершенны, либо надо
   искать другие, сохраняющие аналогию.

**Замыкание.** Через три года Куммер сам процитировал эту жалобу дословно по-латыни и объявил её снятой:
«Es erledigt sich somit die Klage, welche ich in dem Breslauer Programm… S. 18 aussprach» (Crelle 35, S. 323,
Л-25). Связь нужды 1844 г. с отказом 1847 г. документирована самим автором, а не реконструирована нами.

**Чего нет.** Тетрадей, черновиков, переписки Куммера 1844–1847 гг. не найдено — они и не разыскивались
(вероятный адрес: Nachlass Kummer, архив BBAW). Ретроспективного самоописания Куммера о собственном открытии
не найдено вовсе (§6). Промежуток между мемуаром 1844 г. и берлинским сообщением (7 либо 19 месяцев, П-1) не
покрыт ни одним документом.

## 3.2. Дедекинд, идеалы. Опорная дата — Vorwort от 1 марта 1871 г.

**Документов времени работы до 1 марта 1871 г. НЕ НАЙДЕНО НИ ОДНОГО.** Это пустой результат, и он записывается
как пустой.

Что есть вместо них — и почему это не заменяет:

| источник | дата | почему не годится как «за неделю до» |
|---|---|---|
| Vorwort 1871, S. VII–IX (Л-33, Л-34) | 1 марта 1871 | Написано В МОМЕНТ публикации, а не до неё; содержание ретроспективно (письма 1857 г., собственный путь «vor etwa zehn Jahren» ≈1861) |
| § 162, § 163 издания 1871 (Л-35, Л-36) | 1871 | Тело первопубликации — это уже изобретение, не «до» |
| Dedekind 1878 (Л-39) | 1878 | Через семь лет ПОСЛЕ. Здесь же — единственное описание несходящегося вычисления: кубическое расширение Q, где ни при каком θ не удаётся представить идеальные делители числа 2 (Avigad 2005, стр. 11–12). Ретроспектива, доступ только через англ. перевод во вторичном источнике |
| Письмо Липшицу 6.10.1876 (Л-38) | 1876 | Документ времени работы — но НАД ВТОРОЙ версией (франц., 1877), через пять лет после первой |
| Dedekind 1857, Crelle 54, S. 1–26 («Abriß einer Theorie der höheren Kongruenzen») | 1857 | Датированный документ времени работы отброшенного пути СУЩЕСТВУЕТ и известен по библиографии Авигада (стр. 30) — **но в этом ресёрче не открывался**; и это начало пути, а не запись его провала |
| Письмо Кронекера Дедекинду 1857 г. | 1857 | Не найдено; известно только по пересказам самого Дедекинда 1871 и 1893 гг. (Л-33, Л-58) |

**Что можно сказать о столе Дедекинда только по документу 1871 г. (и с пометкой «ретроспектива внутри
первопубликации»):** на столе лежала уже готовая, но отвергнутая конструкция — обоснование через теорию высших
сравнений в связи с принципами Галуа, имеющее точки соприкосновения с идеальными числами Селлинга; форма § 163
далась «erst nach sehr langem Nachdenken» и автора «noch nicht vollständig» удовлетворяла (Л-34). Мотив замены
куммеровских фикций системами действительных чисел — не сбой счёта, а опасение внушить недоверие к надёжности
доказательств (Л-35). **Ни одного вычисления, которое не проходило бы, в документах до 1871 г. не названо.**

## 3.3. Единственный случай, где «за неделю до» буквально документирован

Не у изобретателей, а у проигравшего. **15 марта 1847 г.** Ванцель печатно заявляет, что евклидов алгоритм
проходит «pour n quelconque», и что нужное неравенство «se vérifie de plusieurs manières» (Л-10, CR pp. 430–434).
**22 марта 1847 г.**, ровно через семь дней, Коши в том же издании предъявляет счёт: для корней 7-й степени
произведение сопряжённых триномов «sera égal au nombre 8, notablement supérieur à l'unité», и превзойдёт единицу
для всякого простого n ≥ 17; вывод — «la théorie générale des nombres complexes est encore à établir»
(Л-12, CR pp. 469–471).
**Это единственная в кейсе пара «заявление → несходящееся вычисление» с недельным шагом, и обе даты печатные.**

---

# 4. Черновик таблицы брифа

Каждая клетка — с адресом (источник + локатор + status) либо с записью «не найдено, искали там-то».
Сводка сначала, разбор ниже.

| клетка | опорный адрес | status / kind | сила |
|---|---|---|---|
| **нужда** | Куммер 1844, JMPA t. 12, p. 203, «Maxime dolendum videtur…» (Л-03) | verified / contemporaneous | сильная: за три года до решения, автором, в печати |
| **отказ** | Куммер, Crelle 35, S. 319 + S. 323 (Л-23, Л-25); Дедекинд, VZT 1871, S. 451 (Л-35) | verified / contemporaneous | сильная: у обоих авторов, оба раза печатно |
| **модель** | Куммер 1844, § IX–X, pp. 203–208 (Л-04, Л-05); Crelle 35, S. 322 и S. 329 (Л-24, Л-29) | verified+corrected / contemporaneous | сильная у Куммера; **у Дедекинда — не найдено** |
| **опознание** | 20 записей ленты; ядро — Л-01, Л-02, Л-14, Л-19, Л-26, Л-27, Л-33, Л-46, Л-53 | verified | сильнейшая клетка кейса |
| **носитель 2** | Дедекинд–Вебер 1882, Crelle 92, S. 181–183 (Л-51, Л-52, Л-54) | verified / contemporaneous | сильная ВНУТРИ математики; **вне математики — не найдено** |
| **проигрыш** | Ванцель→Коши, март 1847 (Л-10→Л-12); Дедекинд, VZT 1871, S. VIII–IX (Л-34); Кронекер, § 19 (Л-49) | verified | сильная: проигрыши всех трёх сторон, включая датированный недельный |

## 4.1. НУЖДА — «без чего счёт не сходится»

- **Куммер, 1844.** JMPA t. 12, **p. 203** (перед § IX), «Maxime dolendum videtur… non eadem est numerorum
  complexorum, quae si esset, tota haec doctrina… facile absolvi et ad finem perduci posset». *status:* verified,
  *kind:* contemporaneous. Л-03. — Нужда названа как ПОМЕХА СЧЁТУ («вся эта доктрина, страдающая большими
  трудностями, легко была бы доведена до конца»), а не как эстетический дефект.
- **Куммер, 1844, тот же пассаж.** Развилка «imperfecti… an alii quaerendi essent» — там же, p. 203. verified.
- **Лиувилль, 1.03.1847.** CR t. 24, **p. 315**, «N'y a-t-il pas là une lacune à remplir?» *status:* verified,
  contemporaneous. Л-07. — Публичная формулировка той же нужды в другой стране, независимо от Куммера.
- **Коши, 22.03.1847.** CR t. 24, **p. 469**, «exigerait, comme l'a remarqué M. Liouville, que l'on établît
  d'abord…». verified, contemporaneous. Л-11. — К 22 марта формулировка стала общепризнанной.
- **Ламе, 1.03.1847.** CR t. 24, **p. 310** — мотив (теорема Ферма) и происхождение хода от Лиувилля. verified,
  contemporaneous. Л-06.
- **Дедекинд, ретроспективно.** VZT 1879, **S. 451–452**, «hoffnungsloses Unternehmen… folgenschweren
  Entdeckung». verified, **retrospective**. Л-40. — **Использовать с пометкой П-6: этого пассажа нет в издании
  1871 г.; героизация добавлена не ранее 1879 г.**
- **НЕ НАЙДЕНО: формулировка нужды самим Дедекиндом ДО 1871 г.** Искали: Vorwort и Supplement X издания 1871 г.
  целиком (`dedekind1871_djvu.txt`), Avigad 2005 целиком, библиография Авигада (стр. 28–30). Ближайшее —
  ретроспективные Л-39 (1878) и Л-40 (1879).

## 4.2. ОТКАЗ — от какой аксиомы отказались и чем это оправдано

- **Куммер, 28.04.1847.** JMPA t. 12, **p. 136** / CR t. 24, **pp. 899–900**: «elle n'a pas lieu généralement…
  mais qu'on peut la sauver en introduisant un nouveau genre de nombres complexes que j'ai appelé nombre complexe
  idéal». *status:* corrected (место публикации), contemporaneous. Л-13. — **Формула отказа: закон
  (единственность) СПАСАЕТСЯ ценой расширения области объектов.**
- **Куммер, 1847.** Crelle 35, **S. 319**: первое печатное определение термина, «die Factoren aber sind alsdann
  nicht wirkliche, sondern ideale complexe Zahlen». verified, contemporaneous. Л-23.
- **Куммер, 1847.** Crelle 35, **S. 323**: «Es erledigt sich somit die Klage…» + «das innere crystallinische
  Gefüge». verified, contemporaneous. Л-25. — **Единственный документ, где автор сам сшивает нужду 1844 г.
  с отказом 1847 г. Это опорный адрес клетки.**
- **Дедекинд, 1871.** VZT 1871, **S. 451** (конец § 162): «fingiren» / «Misstrauen gegen die Sicherheit der
  Beweisführung» / «in ein anderes Gewand einzukleiden». verified, contemporaneous (kind исправлен). Л-35.
  — **Второй отказ кейса: отказ уже не от аксиомы, а от способа существования объекта (фикция → множество).
  Оправдан НЕ несходящимся счётом, а риском недоверия к доказательству. Помета обязательна: пассаж существует
  только в издании 1871 г. (П-7).**
- **Дедекинд, 1871.** VZT 1871, **S. 452** (§ 163, п. 1): определение идеала двумя условиями замкнутости.
  verified, contemporaneous. Л-36.
- **НЕ НАЙДЕНО: обоснование дедекиндовского отказа через сбой счёта в документе ДО 1871 г.** Искали: там же,
  где §4.1; ближайшее — 1878 г. (Л-39, ретроспектива через англ. перевод).

## 4.3. МОДЕЛЬ — первая реализация, на которой непротиворечивость видна

- **Куммер, 1844, § IX.** JMPA t. 12, **pp. 203–204**: разложения всех простых < 1000 семи видов, посчитанные
  лично. verified, contemporaneous. Л-04. — Эмпирическая база, из которой выросла модель.
- **Куммер, 1844, § X.** JMPA t. 12, **pp. 207–208**: таблицы; λ = 23 — три простых против длинных списков.
  *status:* corrected, *confidence:* medium (OCR таблиц повреждён). Л-05.
- **Куммер, 1847.** Crelle 35, **S. 322**: определение идеального простого множителя ЧЕРЕЗ ДЕЛИМОСТЬ
  произведения — «Wenn f(a) die Eigenschaft hat, dafs das Product f(a)·Ψ(η_r) durch q theilbar ist…».
  *status:* corrected (локатор сужен). Л-24. — **Объект не строится, а задаётся проверяемым предикатом:
  свойство делимости заменяет существование множителя.**
- **Куммер, 1847.** Crelle 35, **S. 329** (§ 2 большого мемуара): уравнения для периодов переистолкованы как
  сравнения по модулю q при q^f ≡ 1 (mod λ). verified, contemporaneous. Л-29. — **Модель вычислительная и
  алгоритмическая; ровно это Дедекинд потом заменит.**
- **Куммер, 1847.** Crelle 35, **S. 327–367** — развёрнутое обоснование (41 страница). corrected (объём). Л-28.
- **НЕ НАЙДЕНО: модель непротиворечивости у Дедекинда — конкретный пример или счёт, на котором видно, что
  новое понятие работает, в документе времени работы.** Искали: § 162–163 издания 1871 г., Vorwort 1871,
  Avigad 2005 целиком. Ближайшее — ретроспективный контрпример 1878 г. (кубическое расширение, делители числа 2;
  Avigad 2005, стр. 11–12, Л-39), и он показывает не работу нового понятия, а провал старого.
- **НЕ ПРОЧИТАНО (адрес известен):** Crelle 35, **S. 330–367** — оставшиеся 38 страниц большого мемуара
  Куммера. Если явное указание на исключительность λ = 23 существует, оно вероятнее всего там.

## 4.4. ОПОЗНАНИЕ — кто и когда узнал в чужой работе своё

Самая плотная клетка кейса: 20 записей. Ядро по типам:
- **Признание предшественника автором.** Куммер о Якоби: JMPA t. 12, **pp. 185–186**, verified, contemporaneous
  (Л-01). Куммер о Дирихле и Кронекере: **pp. 193–194**, verified (Л-02). Куммер о неопубликованном Дирихле:
  Crelle 35, **S. 324**, verified (Л-27) — *факт не найден ни одним сборщиком*. Куммер о диссертации Кронекера:
  Crelle 35, **S. 324**, сноска, verified (Л-26).
- **Признание через посредника.** Куммер → Лиувиллю о Кронекере: JMPA t. 12, **p. 136**, verified (Л-14).
  Лиувилль о приоритете — уклонение: JMPA t. 12, **p. 136**, verified (Л-19). Лиувилль о происхождении мемуара:
  JMPA t. 12, **p. 185**, сноска [*], verified (Л-20).
- **Заявка на приоритет соперника.** Коши о запечатанном мемуаре 19.10.1846: CR t. 24, **pp. 316–317**,
  verified (Л-09). Коши о Куммере: CR t. 24, **p. 887**, verified (Л-15). Сноска Лиувилля: CR t. 24, **p. 899**,
  verified (Л-18) — *факт не найден ни одним сборщиком*.
- **Опознание через поколение.** Дедекинд о неопубликованном Кронекере: VZT 1871, **S. VII–VIII**, verified,
  retrospective (Л-33). Кронекер о печатном приоритете Дедекинда: Crelle 92, **S. 2**, сноска, verified,
  contemporaneous (Л-46). Дедекинд–Вебер об устных сообщениях о Кронекере: Crelle 92, **S. 182**, verified (Л-53).
  Золотарёв о Селлинге и Дедекинде: JMPA 3e s., t. 6, **pp. 51–52**, verified (Л-41). Дедекинд о Гурвице:
  Avigad 2005, **стр. 22**, secondary (Л-56).
- **Опознание задним числом.** VZT 1894, **S. 452–453** и **S. 484**, сноски о геттингенских лекциях 1857–58 гг.,
  verified, retrospective (Л-60, Л-61) — **обязательна помета П-8: появляются только в 1894 г.**
- Не найдено: ни одного случая, где опознание было бы ОТРИЦАТЕЛЬНЫМ (спор о приоритете, обвинение). Все
  найденные — признание чужой работы, часто неопубликованной. Искали: CR t. 24 (grep «Kummer», 12 вхождений),
  Grundzüge целиком, все три Vorwort'а.

## 4.5. НОСИТЕЛЬ 2 — куда линзу перенесли и кто перенёс

- **Дедекинд и Вебер, 1882.** Crelle 92, **S. 181–182**: имя «Ideal» сохранено при переносе на алгебраические
  функции, при этом «keineswegs um „ideale" Functionen handelt». verified, contemporaneous. Л-51.
- **Там же, S. 182, сноска:** цепочка ссылок на источник понятия, «in der zweiten und dritten Auflage».
  verified. Л-52.
- **Там же, S. 183:** единственность разложения на Primideale; «völlig präcisen und allgemeinen Definition des
  „Punktes der Riemann'schen Fläche"». corrected (цитата). Л-54. — **Результат переноса: определение точки
  кривой через простые идеалы.**
- **Анонс переноса за два года:** VZT 1879, Vorwort, **S. VIII**, 11.11.1880. verified, retrospective. Л-43.
- **Дальше по цепочке:** Гильберт, Basissatz 1890 — Avigad 2005, **стр. 14**, secondary, medium (Л-57);
  Гензель, p-адические числа 1897 — MacTutor, secondary, medium (Л-63); Ласкер, кольца многочленов 1905 —
  Нётер 1921, сноска 3, + MacTutor, secondary (Л-64); Нётер, произвольные кольца 1921 — arXiv:1401.2577,
  введение, contemporaneous, medium (Л-65), с самоограничением (Л-66).
- **Оценка вторичного источника:** MacTutor, биография Вебера — «point on an abstract algebraic curve is defined
  for the first time in history». secondary, medium (Л-55). Фактическое ядро подтверждается Л-54.
- **НЕ НАЙДЕНО: носитель вне математики.** Все шесть найденных носителей — математические (теория чисел →
  теория алгебраических функций и геометрия → коммутативная алгебра). По §5/G1 регламента «две подобласти одной
  науки — одна область», то есть **требование двух РАЗНЫХ областей этим кейсом пока НЕ выполнено**. Искали:
  Avigad 2005 целиком, MacTutor (биографии Dedekind, Weber, Hensel, Lasker), перевод Нётер 1921 целиком.
  Это долг стадии 3: либо второй носитель ищется вне математики, либо линза формулируется так, чтобы
  засвидетельствованный перенос (число → функция) читался без словаря обеих областей.

## 4.6. ПРОИГРЫШ — где приложили и не вышло

- **Ванцель, 15.03.1847 → Коши, 22.03.1847.** CR t. 24, **pp. 430–434** (заявление) → **pp. 469–471**
  (контрпример: произведение = 8; все простые n ≥ 17). corrected / verified, оба contemporaneous. Л-10 → Л-12.
  — **Датированный проигрыш с недельным шагом; обе стороны печатные. Лучший материал клетки.**
- **Ламе, JMPA t. 12, p. 176** (Л-21): через два месяца после указания на пробел печатает текст, где разложение
  на простые множители взято как установленное. verified, contemporaneous. — Проигрыш через инерцию.
- **Дедекинд о собственном отброшенном пути.** VZT 1871, Vorwort, **S. VIII–IX**: «vor etwa zehn Jahren…
  ganz anderen Begründungsart… mir aber jetzt weniger naturgemäss erscheint». verified, retrospective. Л-34.
- **Дедекинд, 1878** (Л-39): два изъяна теории высших сравнений; «peculiar exceptions»; кубическое расширение,
  где делители числа 2 не представимы ни при каком θ. retrospective, medium, доступ через Avigad 2005, стр. 10–12.
- **Дедекинд, 1893** (Л-59): попытка упростить основания через НОД двух произвольных целых алгебраических чисел —
  «nicht gelungen, eine wesentliche Vereinfachung zu erzielen». VZT 1894, Vorwort, **S. VII–VIII**. verified,
  retrospective.
- **Дедекинд, 1895** (Л-62): недоволен доказательством через «Пражскую теорему» — «by mixing in functions of
  variables the purity of the theory is… tarnished»; и собственным индуктивным — «dominated by mechanical
  calculation». Avigad 2005, **стр. 24–25**. retrospective, medium.
- **Кронекер о себе, § 19 Grundzüge** (Л-49): «in den Jahren 1843 bis 1846 zu einer solchen Erkenntniss nicht
  durchzudringen vermocht». retrospective, verified. — Признание неудачи конкурентом.
- **Кронекер против Дедекинда:** отказ от «Körper» (Grundzüge, § 1, ок. **S. 3–4**, corrected, Л-47);
  расхождение по цели (**S. 80–81**, corrected, Л-48).
- **Кронекер против Золотарёва:** «Dieser Versuch ist… verfehlt» (Grundzüge, **S. 118**, verified, Л-50).
- **Цена, не сведённая до сих пор:** Avigad 2005, **стр. 9–10** (Л-68): Эдвардс за первую версию, Нётер за
  последнюю; «something important has been lost in turning away from a more explicit, algorithmic standpoint».
  secondary, verified.
- **НЕ НАЙДЕНО: проигрыш идеальных чисел САМОГО Куммера — случай, где он приложил свой аппарат и тот подвёл.**
  Искали: Crelle 35, S. 319–329; JMPA t. 12, pp. 185–212; письмо Лиувиллю. Ближайшее — его собственная оговорка
  в письме (Л-13), что теорема Ферма сведена к двум свойствам простого n и остаётся выяснить, принадлежат ли
  они всем простым: то есть на момент 28.04.1847 общий случай НЕ получен и это сказано автором.

---

# 5. Ответ на kill-gate ставки

Формулировка ставки (`…/b13/stake.md`, стадия 0, 2026-09-03, 17:20 WITA):
> «Если для ≥ 3 из 5 случаев не найдётся датированного документа с несходящимся вычислением ДО изобретения
> (а только ретроспективный рассказ автора), премисса брифа „структура рождается из вычисления, которое не
> проходит" опровергнута для этого набора».
Ожидание ставки по этому кейсу: «Ламе/Коши — единственность разложения в Z[ζ_p]».

## Ответ: **ДА для изобретения Куммера; НЕТ для изобретения Дедекинда.** Кейс засчитывается как «ДА» — с оговоркой

### 5.1. Куммер, идеальные числа — ДА

**Адрес:** E. Kummer, «De numeris complexis, qui radicibus unitatis et numeris integris realibus constant»,
Breslau, **1844**; переиздание целиком: JMPA, 1re série, t. 12 (май 1847), **pp. 185–212**.
`http://www.numdam.org/item/JMPA_1847_1_12__185_0/`; локальная копия
`…/b13/sources/JMPA_1847_1_12__185_0.txt`.
*kind:* **contemporaneous** (печатная программа времени работы). *status:* verified.

**Точные локаторы несходящегося вычисления:**
1. **pp. 185–186** — «neque tamen hi ipsi factores cum illis compensari possunt, res maximi momenti, indicat hos
   factores non esse primos sed compositos» (Л-01, verified). Сокращение не проходит.
2. **p. 203** — «quilibet numerus primus p = mλ + 1 esset productum λ − 1 factorum complexorum conjunctorum,
   quod in universum non pro omnibus valoribus numerorum p et λ valere supra demonstravimus» (Л-03, verified).
   Счёт числа множителей не сходится, и это доказано в том же тексте.
3. **p. 203** — «Maxime dolendum videtur…» (Л-03, verified). Автор называет последствие: без этого свойства
   доктрина не может быть доведена до конца.
4. **pp. 203–204, 207–208** — вычислительная база (все простые < 1000 семи видов) и таблицы, где λ = 23 даёт
   три представимых простых против длинных списков соседей (Л-04 verified, Л-05 corrected/medium).

**Разрыв до изобретения:** не менее **7 месяцев** (если считать от берлинского сообщения марта 1845 г. по
подзаголовку Crelle 35, Л-22) либо **не менее 19 месяцев** (если от марта 1846 г. по письму самого Куммера,
Л-13). Точная величина не определима: см. П-1, противоречие не разрешается прочитанными источниками.

**Замыкание петли документом автора:** Crelle 35, **S. 323** — Куммер сам цитирует жалобу 1844 г. и объявляет её
снятой введением идеальных множителей (Л-25, verified, contemporaneous). Связь «несходящийся счёт → отказ»
установлена автором, а не реконструирована.

### 5.2. Дедекинд, идеалы — НЕТ

**Датированного документа времени работы с несходящимся вычислением до 1 марта 1871 г. не найдено.**
Что найдено вместо и почему не засчитывается — таблица §3.2. Кратко:
- несходящееся вычисление у Дедекинда описано (кубическое расширение Q, идеальные делители числа 2 не
  представимы ни при каком θ), но **в документе 1878 г.**, через семь лет после публикации теории идеалов, и
  доступно только через английский перевод во вторичном источнике: Dedekind 1878, Werke Bd. 1, S. 202–203, по
  Avigad 2005, **стр. 10–12**; *kind:* retrospective, *confidence:* medium (Л-39);
- мотив отказа, записанный в момент публикации (VZT 1871, **S. 451**, Л-35), — **не сбой счёта, а
  «Misstrauen gegen die Sicherheit der Beweisführung»**. Это прямо задевает второй пункт kill-gate ставки:
  «если отказ оправдывался только философией/красотой без восстанавливаемого закона — линза остаётся рассказом».
  У Куммера восстанавливаемый закон назван (единственность разложения, Л-13, Л-25); **у Дедекинда на месте
  восстанавливаемого закона стоит требование к доказательству, а не к вычислению.**

**Не искали (адреса известны, проверка возможна):** Dedekind, «Abriß einer Theorie der höheren Kongruenzen…»,
Crelle 54 (1857), S. 1–26 — документ времени работы отброшенного пути; Nachlass Дедекинда (Гёттинген);
письмо Кронекера 1857 г.; оригинал Dedekind 1878 (Werke Bd. 1) вместо англ. перевода.

### 5.3. Как это засчитывать в общий счёт «≥ 3 из 5»

Кейс в брифе назван по обоим изобретениям («Куммер 1847 → Дедекинд 1871»), и ответ у них разный. Предлагаемое
для стадии 5 правило учёта, чтобы счёт не поплыл:
- **если кейс считается по своей опорной дате (Куммер, 1847) — это «ДА», и премисса брифа для него держится;**
- **если кейс считается по паре — он даёт «ДА» и «НЕТ» и должен войти в счёт как половина, с обязательной
  записью, что вторая половина пуста и почему.**
Дополнительно: ожидание ставки («Ламе/Коши — единственность разложения в Z[ζ_p]») **подтвердилось по существу,
но промахнулось по адресу и по дате**. Публичный сбой у Ламе, Лиувилля, Ванцеля и Коши — это март 1847 г.,
то есть **после** изобретения Куммера (март 1845 либо 1846), а не до него. Документ, который действительно
предшествует изобретению, — не парижский, а бреславльский и на три года более ранний (§5.1).

---

# 6. Осталось непроверенным (адреса для следующего шага)

Записано отдельно, потому что часть «не найдено» в §4 опирается именно на эти пробелы.

1. **Monatsberichte / Berichte Берлинской академии за март 1845 и март 1846 гг.** — единственный документ,
   способный разрешить П-1 и тем самым определить дату изобретения Куммера. Искали: archive.org advancedsearch
   («Monatsberichte Königlich Preussischen Akademie 1846») — 0 результатов. Не проверено: bbaw.de,
   biodiversitylibrary.org, GDZ. **Самый существенный пробел кейса.**
2. **Nachlass Куммера, 1844–1847** (архив BBAW) — тетради и черновики. Не разыскивались вообще.
3. **Ретроспективное самоописание самого Куммера** — не найдено ничего, кроме опосредованной и обрывающейся
   цитаты из Gedächtnissrede 1860 г. (Л-31). **Существенный отрицательный результат: у Дедекинда три
   предисловия и очерк 1895 г., у Кронекера три текста, у Куммера — ноль.**
4. **Полный текст Gedächtnissrede Куммера (1860).** Искали: archive.org по названию и автору/году, Google Books
   API (HTTP 429), Wikisource — не найден.
5. **Оригинал письма Дедекинда Липшицу 6.10.1876** (Werke Bd. 3, Kap. LXV, S. 468–474). Читался англ. перевод.
   Вероятный адрес: W. Scharlau, «Rudolf Lipschitz. Briefwechsel…» (1986), в открытых архивах не оцифровано.
6. **Dedekind, Crelle 54 (1857), S. 1–26** — документ времени работы отброшенного пути. Не открывался.
7. **Crelle 35, S. 330–367** — 38 непрочитанных страниц большого мемуара Куммера; вероятное место явного
   утверждения об исключительности λ = 23 (П-13).
8. **Kronecker, «Vorbemerkung», Crelle 91, S. 301** — более раннее признание приоритета Дедекинда, на которое
   Кронекер сам ссылается в Л-46. Не открывалось.
9. **Оригинал E. Noether, Math. Annalen 83 (1921)** (GDZ `PPN235181684_0083`). Приём с IIIF-манифестом,
   сработавший для Crelle 35, здесь не пробовался.
10. **Оригиналы Ласкера (1905), Zahlbericht Гильберта (1897), Weyl (1940), Molk (Acta Math. 6, 1885).**
    Не открывались или закрыты (Project Euclid — Incapsula; archive.org — HTTP 401/403).
11. **Kummer, Collected Papers, ed. A. Weil (1975)** — HTTP 403, контролируемая цифровая выдача (Л-67).
12. **Реакция Эйзенштейна; английская реакция 1847–1850 гг.; некролог Дедекинда (1916/17).** Не найдены;
    целенаправленный полнотекстовый поиск по именам не проводился.
13. **Прямая переписка Дедекинд ↔ Кронекер** и договорённость июня 1880 г. Известны только по одностороннему
    пересказу Дедекинда (Л-58).
