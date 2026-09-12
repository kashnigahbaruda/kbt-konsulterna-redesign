#!/usr/bin/env python3
"""The topic tree: every level-2 and level-3 page under the three audience hubs.

This is the SEO layer the old site carried at /vuxna/psykologisk-behandling-terapi/*
and friends — 33 pages, one per thing a person actually searches for. The copy is
ported from the client's own pages (crawled into research/crawl-pages.json) and
tightened; no clinical claim here is new.

Node keys
    slug      URL segment
    label     what the sidebar navigator calls it (short)
    h1        page heading
    title     <title>
    desc      meta description
    lede      standfirst under the h1
    body      the article itself, HTML
    people    medarbetare slugs who work with this — the E-E-A-T signal the old
              pages had none of
    also      (label, path-from-root) cross-links rendered as "Läs vidare"
    children  level-3 nodes, if any
"""

# --------------------------------------------------------------------------
# Vuxna → Psykologisk behandling
# --------------------------------------------------------------------------
V_BEHANDLING = [
    dict(
        slug='oro-angest', label='Oro & ångest',
        h1='Oro och ångest',
        title='Behandling vid oro och ångest i Uppsala | KBT-Konsulterna',
        desc='KBT vid ångest, panikångest, social ångest, OCD, hälsoångest och '
             'fobier. Legitimerade psykologer i centrala Uppsala och online.',
        lede='Oro eller ångest känner de flesta ibland. När känslan är mer eller '
             'mindre ständigt närvarande — anspänning, hot, fara — påverkar den '
             'livskvaliteten. Det går att behandla.',
        people=['aksel-reppling', 'angeli-holmstedt', 'thomas-alm'],
        also=[('Nedstämdhet och depression', 'vuxna/behandling/depression/'),
              ('Trauma och PTSD', 'vuxna/behandling/trauma-ptsd/'),
              ('Fobier och flygfobi', 'vuxna/behandling/fobier/')],
        body='''
<p>Många lever med ångestsymtom, känner sig nedstämda och ibland deprimerade, och det
kan bli så tungt att vardagen inte går ihop på det sätt man vill.</p>

<p>Ångest tar sig olika uttryck. Ibland har den ett namn — en diagnos. Andra gånger
handlar det om en oro eller panik som inte passar in i någon definition, men det
lidandet är lika viktigt att ta på allvar. Du behöver inte veta vad ditt problem heter
för att höra av dig.</p>

<p>Kognitiv beteendeterapi är den behandlingsform som har starkast forskningsstöd vid
ångesttillstånd, och den vi arbetar med.</p>

<h2>De vanligaste formerna</h2>

<h3>Generaliserad oro</h3>
<p>Ängslan och grubblande om framtiden, eller ältande av det som varit, som en ständigt
gnagande process. Man är inte närvarande, sover sämre, får spänningar och värk, har
svårt att fokusera. <em>”Tänk om…”</em> är den återkommande tanken.</p>

<h3>Social ångest</h3>
<p>Osäkerhet och rädsla i sociala sammanhang — vanligast inför att tala i grupp, men
också att fika, säga något på ett möte, vara i ett klassrum. Tankarna är självkritiska,
man känner sig granskad, och rädslan för att göra bort sig kan vara stor. Ofta kommer
kroppsliga symtom som svettningar och hjärtklappning som man försöker dölja, och ofta
leder det till att man undviker sammanhang man egentligen skulle vilja vara i.</p>

<h3>Panikångest</h3>
<p>Attacker med starka kroppsliga reaktioner — hjärtklappning, svettningar, darrningar —
tillsammans med en rädsla för att tappa kontrollen, dö eller bli ”galen”. Reaktionerna
kan bli så starka att man bara vill fly till tryggheten, ibland till sjukvården.</p>
<p>Det leder ofta till undvikande av situationer där en attack skulle kunna komma, eller
till strategier för att dämpa ångesten: ta en tablett, ha med sig en trygg person,
bevaka symtomen. Strategierna fungerar i stunden, men problemet finns kvar.</p>

<h3>Tvångssyndrom (OCD)</h3>
<p>Tvångstankar som väcker otrygghet, och tvångshandlingar som ska försäkra att det man
är rädd för inte inträffar. Teman kan vara smitta och baciller, rädsla för att skada
andra, påträngande ”förbjudna” tankar, eller ett mycket starkt behov av ordning och
kontroll. För att dämpa obehaget tvättar man sig kanske överdrivet, ställer
kontrollfrågor till närstående, googlar, kontrollerar eller samlar.</p>
<p>OCD tar sig många uttryck, är plågsamt för den som lever med det, och utvecklas för
en del till ett stort hinder i livet.</p>

<h3>Hälsoångest</h3>
<p>Ett överdrivet fokus på kroppen, drivet av rädsla för att vara eller bli sjuk. Man
kontrollerar pulsen, känner efter knölar, letar hudförändringar, är uppmärksam på
”känningar”. Upptäcker man något som verkar avvikande googlar man, söker läkare eller
frågar andra om råd.</p>

<h3>Fobier</h3>
<p>En stark och orimlig rädsla för något bestämt — ormar, spindlar, sprutor, blod,
höjder, hissar, flygplan. Man gör allt för att undvika det, och uthärdar med stark
ångest när det inte går. Fobier kan vara mycket hindrande: man avstår från
skogspromenaden, undviker vaccin, vågar inte bli gravid på grund av sprutfobi, reser
inte.</p>
<p>Fobier behandlas med exponering och har bland de bästa behandlingsresultaten inom
psykologin. Vi har en särskild <a href="{base}vuxna/behandling/fobier/">sida om fobier
och flygfobi</a>.</p>

<h3>Posttraumatisk stress (PTSD)</h3>
<p>En mycket svår händelse kan ge traumatiska konsekvenser — överspändhet,
lättskrämdhet, negativa tankar om sig själv och andra, och undvikande av aktiviteter,
platser, relationer och till och med känslor och tankar. Läs mer på sidan om
<a href="{base}vuxna/behandling/trauma-ptsd/">trauma och PTSD</a>.</p>
''',
    ),
    dict(
        slug='depression', label='Nedstämdhet & depression',
        h1='Nedstämdhet och depression',
        title='Behandling vid depression och nedstämdhet i Uppsala | KBT-Konsulterna',
        desc='KBT vid depression, långvarig nedstämdhet och utmattningsdepression. '
             'Legitimerade psykologer i Uppsala och online, utan väntetid.',
        lede='Tillfällig nedstämdhet är vanlig, och många depressioner går över av sig '
             'själva. Andra gånger är det viktigt att söka hjälp.',
        people=['thomas-alm', 'aksel-reppling'],
        also=[('Oro och ångest', 'vuxna/behandling/oro-angest/'),
              ('Stress och utmattning', 'vuxna/behandling/stress-utmattning/'),
              ('Låg självkänsla', 'vuxna/behandling/sjalvkansla/')],
        body='''
<p>Det är vanligt att känna sig ledsen och nedstämd, och det brukar gå över efter ett
tag. Om det pågår ett par veckor eller mer, om tröttheten förvärras, om du inte känner
någon glädje inför sådant du annars uppskattar, och om orken att ta tag i vardagen är
borta — då kan det handla om en depression.</p>

<h2>Hur vanligt är det?</h2>
<p>Uppskattningsvis har 5–8 % av befolkningen en pågående depression. Under sin livstid
drabbas omkring 25–30 % av kvinnorna och 15–20 % av männen någon gång.</p>

<h2>Hur ser symtomen ut?</h2>
<p>Att vara deprimerad innebär en stark nedstämdhet, uttalad trötthet, och att glädjen
och lusten till det man tidigare tyckt om är borta. Ofta räcker orken inte till
vardagen, och det mesta känns hopplöst och meningslöst.</p>
<p>Andra vanliga symtom är koncentrationssvårigheter, ångest, irritation, ilska och låg
självkänsla. Många får också kroppsliga besvär: huvudvärk, ont i magen, axlar, nacke och
rygg, minskad eller ökad matlust, minskad sexlust, sömnsvårigheter.</p>

<h2>Det finns flera former</h2>
<p>Svårighetsgraderna varierar, och besvären kan komma vid ett enda tillfälle eller
återkomma. Det finns årstidsbunden nedstämdhet, utmattningsdepression, dystymi (färre
symtom men ihållande under lång tid), och bipolär sjukdom med återkommande svåra
depressioner, ofta varvade med mani. Hos barn och ungdomar ser symtomen delvis
annorlunda ut — se
<a href="{base}barn-och-ungdom/behandling/depression/">nedstämdhet hos barn och unga</a>.</p>

<h2>Hur vi arbetar</h2>
<p>Vi börjar med en gemensam bedömning för att skilja depression från exempelvis
utmattningssyndrom, eftersom behandlingen skiljer sig åt. Därefter arbetar vi vanligen
med beteendeaktivering, kognitiv terapi och återfallsprevention, med mål som utgår från
vad som är viktigt för dig.</p>

<h2>När det blir allvarligt</h2>
<p>En del får självmordstankar, och risken för självmordsförsök ökar. Då behöver du
söka hjälp direkt — kontakta en anhörig, en vän, din vårdcentral eller din psykolog.</p>
<p>Vid akuta besvär: ring <strong>112</strong> vid fara för liv, ring MIND Stödlinje på
<strong>90 101</strong>, eller sök psykakuten där du bor. Se
<a href="{base}akut-hjalp/index.html">akut hjälp</a>.</p>
''',
    ),
    dict(
        slug='stress-utmattning', label='Stress & utmattning',
        h1='Stress och utmattning',
        title='Stress och utmattningssyndrom i Uppsala | KBT-Konsulterna',
        desc='KBT vid långvarig stress, utmattningssyndrom och utmattningsdepression. '
             'Noggrann bedömning först — behandlingen skiljer sig åt.',
        lede='Långvarig stress utan återhämtning kan leda till utmattningssyndrom och '
             'ibland sjukskrivning. Insatserna anpassas efter din situation.',
        people=['thomas-alm', 'angeli-holmstedt'],
        also=[('Nedstämdhet och depression', 'vuxna/behandling/depression/'),
              ('Sömnproblem', 'vuxna/behandling/somn/'),
              ('Rehabilitering för arbetsgivare', 'organisationer/rehabilitering/')],
        body='''
<p>Stress är kroppens reaktion på något som uppfattas som hotfullt eller utmanande. Det
kan handla om att leva under för hög belastning under för lång tid: att vara förälder
och inte få sova, att ha för mycket att göra, arbetslöshet, ekonomiska bekymmer, en
anhörig som är gammal och sjuk, en egen sjukdom. En kombination av sådant gör att
tillfällena till återhämtning krymper.</p>

<h2>Är stress farligt?</h2>
<p>Psykisk belastning är en naturlig del av livet och inte farlig i sig. Men om
omgivningens krav blir för höga och du samtidigt upplever att du inte har kontroll över
dem, kan det leda till trötthet, nedstämdhet och koncentrationssvårigheter.</p>

<h2>Tecken på utmattning</h2>
<p>Utmattningssyndrom kännetecknas av fysiska och psykiska symtom som funnits i minst
två veckor, och brukar innebära brist på energi, minskad ork och uthållighet, samt ett
behov av längre återhämtningstid efter belastning än tidigare.</p>

<h2>Varför bedömningen kommer först</h2>
<p>Utmattningsdepression är en form av utmattningssyndrom, och begreppen används ibland
synonymt. Men det är viktigt att skilja mellan depression, utmattningssyndrom och
utmattningsdepression — framför allt för att behandlingen ser olika ut. Därför gör vi
alltid en noggrann bedömning innan behandlingen börjar.</p>

<h2>Vad behandlingen innehåller</h2>
<p>Vi arbetar med belastning och återhämtning, med gränser och krav — både andras och
dina egna — och med en successiv, hållbar väg tillbaka. Sömnen är ofta en del av
bilden, och behandlas i så fall parallellt.</p>
''',
    ),
    dict(
        slug='somn', label='Sömnproblem',
        h1='Sömnproblem',
        title='KBT vid sömnproblem och insomni i Uppsala | KBT-Konsulterna',
        desc='KBT för insomni har starkt forskningsstöd och är förstahandsvalet vid '
             'långvariga sömnbesvär. Behandling i Uppsala och online.',
        lede='Svårt att somna? Vaknar du mitt i natten, eller utan att känna dig '
             'utvilad? Sömnstörningar är mycket vanliga och skapar stort lidande.',
        people=['thomas-alm', 'aksel-reppling'],
        also=[('Stress och utmattning', 'vuxna/behandling/stress-utmattning/'),
              ('Oro och ångest', 'vuxna/behandling/oro-angest/'),
              ('Sömnproblem hos barn', 'barn-och-ungdom/behandling/somn/')],
        body='''
<p>Sömnen är livsviktig — men vi behöver kanske inte sova så mycket som vi tror.
Sömnbehovet är individuellt, och även för mycket sömn kan skapa problem. Många har
sömnsvårigheter till och från och tycker att sömnen kunde vara bättre. Ibland blir
besvären mer långvariga och påverkar vardagen i hög grad, och då kan det handla om
insomni.</p>

<h2>Vad är insomni?</h2>
<p>Insomni innebär svårigheter att somna, att vakna ofta eller att vakna för tidigt.
Man fungerar sämre under dagen och är missnöjd med sin sömn. Ett kriterium är att
besvären har funnits i minst tre månader.</p>

<h2>Sällan ensamt</h2>
<p>Sömnlöshet förekommer ofta tillsammans med annat — depression, stress och utmattning,
skadligt bruk eller ångest. Därför gör vi en helhetsbedömning: en kartläggning av
sömnen tillsammans med eventuella andra besvär, som grund för en individuell
behandlingsplan.</p>

<h2>Hur lång tid tar det?</h2>
<p>Rena sömnbesvär kan ofta behandlas relativt snabbt. Behandlingstiden blir längre om
det finns fler problem med i bilden.</p>
''',
    ),
    dict(
        slug='trauma-ptsd', label='Trauma & PTSD',
        h1='Trauma och posttraumatisk stress (PTSD)',
        title='Traumabehandling och PTSD i Uppsala | KBT-Konsulterna',
        desc='Evidensbaserad traumabehandling vid PTSD med prolonged exposure. '
             'Specialist i klinisk psykologi, mottagning i centrala Uppsala.',
        lede='En stor del av behandlingen går ut på att — med mycket stöd — närma sig '
             'det svåra som hänt, för att nå en framtid där händelsen inte längre '
             'styr så mycket av ditt liv, dina val och ditt mående.',
        people=['jens-karstrom'],
        also=[('Oro och ångest', 'vuxna/behandling/oro-angest/'),
              ('Sorg', 'vuxna/behandling/sorg/'),
              ('Sömnproblem', 'vuxna/behandling/somn/')],
        body='''
<p>Livet bjuder människor på mycket svåra händelser — krig, misshandel, våldtäkter,
olyckor och mycket annat som leder till traumarelaterad stress. Det ger konsekvenser för
den som drabbas, och det tar sig olika uttryck. En del traumatiska upplevelser leder
till en krisreaktion som skapar stort lidande men som går att behandla och lindra.</p>

<h2>Traumats två delar</h2>
<p>En psykologisk traumareaktion brukar beskrivas som två delar: dels en eller flera
händelser som varit skrämmande, dels en reaktion på händelserna. Människor reagerar
olika, och en rad faktorer spelar in. Reaktionerna kan därför se ut på många sätt — och
orsaka lidande även om händelserna ligger långt tillbaka i tiden.</p>

<h2>Symtom vid PTSD</h2>
<p>Vid posttraumatisk stress kan man ha symtom som överspändhet och lättskrämdhet, och
många negativa tankar om sig själv eller andra — kanske har man svårt att lita på andra,
eller ser världen som en farlig plats. Man kan också börja undvika mycket i livet av
rädsla som bottnar i det som hänt: aktiviteter, platser, relationer, och till och med
egna känslor och tankar.</p>

<h2>Hur vi behandlar</h2>
<p>Vi arbetar med evidensbaserad KBT vid PTSD, bland annat prolonged exposure (PE),
schematerapi och ACT. Behandlingen går i din takt, och exponeringen sker planerat och
med stöd — aldrig oförberett.</p>
''',
    ),
    dict(
        slug='sorg', label='Sorg',
        h1='Sorg',
        title='Stöd och behandling vid sorg i Uppsala | KBT-Konsulterna',
        desc='Samtal, stöd och behandling vid sorg och komplicerad sorg. Vi tar emot '
             'både dig som vill prata av dig och dig som vill ha behandling.',
        lede='Vi tar emot både dig som vill ”prata av dig” med en medmänniska, och dig '
             'som vill ha professionell hjälp att bearbeta dina känslor och hitta vägar '
             'vidare.',
        people=['barry-karlsson'],
        also=[('Nedstämdhet och depression', 'vuxna/behandling/depression/'),
              ('Trauma och PTSD', 'vuxna/behandling/trauma-ptsd/'),
              ('Relationsproblem', 'vuxna/behandling/relationer/')],
        body='''
<p>Sorg är en del av livet. Vi drabbas alla någon gång, och för många händer det många
gånger. Sorgeprocessen leder ofta till svåra känslor, och vanligen förknippar vi sorg
med förlusten av en anhörig eller vän.</p>

<p>Men det finns många andra tillfällen då vi känner förlust, mer eller mindre
långvarigt och djupt: separationer och skilsmässor; att bli sjuk och sörja sitt friska
jag; att få ett sjukt barn och — trots kärleken till det barn man fått — sörja det
friska barn man inte fick. Vi kan sakna yrkeslivet när vi går i pension, eller sörja att
vi aldrig blev föräldrar. Listan kan göras lång.</p>

<h2>Är sorg en diagnos?</h2>
<p>Nej. Att känna sorg är inte psykisk ohälsa. Många gånger räcker det att prata med
familj och vänner för att den outhärdliga känslan ska klinga av och gå mot
bakgrunden.</p>

<p>Ibland behöver man någon utanför den närmaste kretsen att prata med. Andra gånger
fastnar man i sorgeprocessen och kommer inte vidare i sitt liv — och då behövs också
professionell hjälp.</p>

<h2>Forskning på området</h2>
<p>Barry Karlsson, leg. psykolog och specialist i neuropsykologi, forskar om förlust och
komplicerad sorg vid Uppsala universitet.</p>
''',
    ),
    dict(
        slug='sjalvkansla', label='Låg självkänsla',
        h1='Låg självkänsla',
        title='KBT vid låg självkänsla i Uppsala | KBT-Konsulterna',
        desc='Behandling vid låg självkänsla, självkritik och perfektionism. KBT hos '
             'legitimerade psykologer i centrala Uppsala och online.',
        lede='Låg självkänsla kan påverka en människas liv i grunden och bli ett hinder '
             'för det som är väsentligt. Den går att arbeta med.',
        people=['aksel-reppling', 'angeli-holmstedt'],
        also=[('Nedstämdhet och depression', 'vuxna/behandling/depression/'),
              ('Oro och ångest', 'vuxna/behandling/oro-angest/'),
              ('Relationsproblem', 'vuxna/behandling/relationer/')],
        body='''
<p>Med självkänsla menar vi vanligen den övergripande uppfattningen vi har om oss
själva: hur vi bedömer oss, och vilket värde vi sätter på oss. Dessa grundläggande
tankar om dig själv upplevs ofta inte som tankar alls, utan som faktapåståenden — som
sanningen om dig.</p>

<p>Vid stark inre självkritik är upplevelserna av dig själv övervägande negativa, och en
sådan uppfattning kan utgöra kärnan i en känsla av underlägsenhet som påverkar många
delar av livet.</p>

<h2>Hur visar sig låg självkänsla?</h2>
<p>Självtvivel kan visa sig som:</p>
<ul>
  <li>negativa och självkritiska tankar</li>
  <li>svårigheter att hävda sina behov</li>
  <li>oro</li>
  <li>skuldkänslor</li>
  <li>skamkänslor</li>
  <li>frustration</li>
  <li>nedstämdhet och depression</li>
</ul>

<p>Konsekvensen kan bli perfektionism — driven av rädsla för att misslyckas — och ett
behov av kontroll. I relationer till andra kan det visa sig som blygsel,
överkänslighet för kritik och en överdriven önskan att vara till lags.</p>

<p>Ofta innebär en negativ självbild att man missar möjligheter till utveckling, därför
att man inte vågar ta risken att misslyckas.</p>
''',
    ),
    dict(
        slug='relationer', label='Relationsproblem',
        h1='Relationsproblem',
        title='Hjälp vid relationsproblem i Uppsala | KBT-Konsulterna',
        desc='Samtal och KBT vid svårigheter i relationer — till partner, familj, '
             'vänner, kollegor eller till dig själv. Uppsala och online.',
        lede='Vissa upplever att de har för få relationer, andra att det är svårt att '
             'vara i relation med andra. Båda går att arbeta med.',
        people=['aksel-reppling', 'angeli-holmstedt'],
        also=[('Parterapi för er som är två', 'vuxna/parterapi/'),
              ('Låg självkänsla', 'vuxna/behandling/sjalvkansla/'),
              ('Oro och ångest', 'vuxna/behandling/oro-angest/')],
        body='''
<p>Kommunikationssvårigheter är mycket vanliga, och ibland blir problemen så stora att
de blir svåra att hantera. Man kan ha problem med sin partner, sina vänner, kollegor,
anställda, sina barn eller sina föräldrar.</p>

<p>Ibland beror svårigheterna på problem hos den andre — psykisk ohälsa, eller ett
skadligt bruk av alkohol, droger eller spel om pengar. Relationer har en stor plats i
allas våra liv; ibland är de till glädje, andra gånger skapar de stress, oro och
förtvivlan.</p>

<h2>Relationen till sig själv</h2>
<p>Ibland handlar det om relationen till en själv. Det kan ta sig uttryck som självhat
eller självkritik, en önskan att slippa känna starka känslor, missnöje med kropp och
utseende, eller låg självkänsla.</p>

<p>Relationsproblem kan också bottna i arbetsmiljön eller andra svårigheter i
omgivningen snarare än i personerna.</p>

<h2>Är relationsproblem en diagnos?</h2>
<p>Nej — men man kan uppleva problem i relationer inom ramen för många diagnoser, till
exempel:</p>
<ul>
  <li>vid social ångest</li>
  <li>vid depression</li>
  <li>vid adhd eller add</li>
  <li>vid autismspektrumtillstånd</li>
</ul>

<p>Är ni två som vill komma tillsammans arbetar vi med
<a href="{base}vuxna/parterapi/">parterapi</a>. Terapiformen fungerar också vid
konflikter mellan personer som inte lever som par.</p>
''',
    ),
    dict(
        slug='fobier', label='Fobier & flygfobi',
        h1='Fobier och flygfobi',
        title='Behandling av fobier och flygfobi i Uppsala | KBT-Konsulterna',
        desc='Exponeringsbehandling vid specifika fobier och flygrädsla. Metoden har '
             'starkt forskningsstöd och tar ofta kort tid.',
        lede='En stark och orimlig rädsla för något bestämt — och allt man gör för att '
             'undvika det. Exponeringsbehandling har bland de bästa resultaten inom '
             'psykologin.',
        people=['aksel-reppling'],
        also=[('Oro och ångest', 'vuxna/behandling/oro-angest/'),
              ('Trauma och PTSD', 'vuxna/behandling/trauma-ptsd/'),
              ('Oro och ångest hos barn', 'barn-och-ungdom/behandling/oro-angest/')],
        body='''
<p>Det är vanligt att ha en fobi. Ofta handlar det om en stark och orimlig rädsla för
ormar, spindlar, sprutor, blod, höjder, små utrymmen som hissar — eller flygplan. Man
gör allt som går för att undvika det man är rädd för, och uthärdar med stark ångest när
det inte går.</p>

<p>Fobier kan vara mycket hindrande. Man kanske avstår från skogspromenaden av rädsla
för hundar och ormar, undviker vaccin, vågar inte bli gravid på grund av spruträdsla
eller blodfobi, eller reser inte alls på grund av rädslan för det instängda utrymmet i
ett flygplan.</p>

<h2>Flygfobi</h2>
<p>Rädslan för att flyga kan kännas logisk med tanke på hur starkt man tror på en möjlig
katastrof. Vanliga föreställningar är att man ska svimma, bli så rädd att man dör i en
hjärtinfarkt, få panik och tappa kontrollen, eller att planet ska råka ut för en incident
eller störta.</p>

<h2>Analys- och behandlingsfas</h2>
<p>Under analysfasen får du redogöra för din flygrädsla och för vad du tror kommer att
hända under en flygning. Under behandlingsfasen får du, via exponering, möjlighet att på
ett kontrollerat sätt utmana de katastroftankarna under en flygning tillsammans med
terapeuten.</p>

<h2>Evidensen bakom</h2>
<p>Exponeringsbehandling vid fobier har säkrad evidens. Behandlingsupplägget vid
flygfobi bygger på forskningen om andra specifika fobier — blodfobi, klaustrofobi,
injektionsfobi samt orm- och spindelfobi — där exponering genomgående ger goda
resultat.</p>
''',
    ),
    dict(
        slug='npf', label='NPF i vuxen ålder',
        h1='Neuropsykiatriska funktionsnedsättningar (NPF)',
        title='Behandling vid adhd och autism i vuxen ålder | KBT-Konsulterna Uppsala',
        desc='KBT-behandling och anpassat stöd vid adhd, add och autism hos vuxna — '
             'med eller utan färdig diagnos. Uppsala och online.',
        lede='Vi tar särskild hänsyn till både hindren och styrkorna som följer med en '
             'NPF-diagnos. Du behöver inte ha en färdig utredning för att komma.',
        people=['karin-holmstrom', 'elias-westerlund', 'barry-karlsson'],
        also=[('Utredning av adhd', 'vuxna/utredning/adhd/'),
              ('Utredning av autism', 'vuxna/utredning/autism/'),
              ('Omprövning av diagnos', 'vuxna/utredning/omprovning/')],
        body='''
<p>Vi arbetar med KBT-inriktad behandling för personer som har en neuropsykiatrisk
funktionsvariation — adhd, add eller autism.</p>

<p>Det är vanligt att personer med neuropsykiatrisk variation upplever svårigheter att
möta förväntningar och krav från omgivningen, och att det skapar en osäkerhet i relation
till andra som ställer till problem i vardagen.</p>

<p>Det kan också vara extra svårt att reglera och hantera känslor, något som inte sällan
leder till psykisk ohälsa i form av oro och ångest, nedstämdhet och depression eller låg
självkänsla. Ibland leder det även till ett problematiskt användande av alkohol, droger
eller ett överdrivet spelande, med allvarliga konsekvenser.</p>

<h2>Behandling, utredning — eller båda</h2>
<p>Du är välkommen hit både med och utan färdig diagnos. Vill du veta om kriterierna är
uppfyllda erbjuder vi <a href="{base}vuxna/utredning/index.html">neuropsykiatrisk
utredning för vuxna</a>. Vill du ha behandling och anpassat stöd utifrån de svårigheter
du redan känner igen, går det lika bra att börja där.</p>

<h2>Samarbete med specialistläkare</h2>
<p>Vårt nära samarbete med en specialistläkare i psykiatri gör att vi kan erbjuda
ytterligare en vårdnivå för klienter som behöver kombinationsbehandling, där både KBT
och läkemedelsbehandling ingår, samt vid behov sjukskrivning och läkarutlåtande. Se
<a href="{base}vuxna/psykiatri/index.html">psykiatrisk bedömning</a>.</p>
''',
    ),
]

# --------------------------------------------------------------------------
# Vuxna → Utredning & bedömning
# --------------------------------------------------------------------------
UTREDNING_STEPS_VUXEN = '''
<h2>Så går utredningen till</h2>
<ol class="steps steps--plain">
  <li><h3>Inledande bedömningssamtal</h3><p>Vi går igenom din bakgrund och din
  nuvarande situation, och bedömer om en fortsatt utredning är motiverad. Samtalet är
  också till för att du ska få träffa din psykolog, ställa frågor och känna efter om
  samarbetet känns tryggt.</p></li>
  <li><h3>Kartläggning och testning</h3><p>Psykologiska tester och intervjuer som
  undersöker psykisk hälsa och ohälsa, kognitiva funktioner och symtombild, med
  standardiserade instrument.</p></li>
  <li><h3>Livshistoria (anamnes)</h3><p>En djupgående intervju om din utveckling från
  barndom till vuxen ålder. När det är möjligt, och i samråd med dig, intervjuar vi
  också en närstående.</p></li>
  <li><h3>Sammanställning och återgivning</h3><p>Vi går igenom resultatet och
  bedömningen tillsammans. Du får med dig ett skriftligt utlåtande och konkreta
  rekommendationer för stöd eller behandling framåt.</p></li>
</ol>
<p>En utredning hos oss består vanligtvis av 6–7 besök.</p>
'''

PRIS_UTREDNING = '''
<h3>Vad kostar en privat utredning?</h3>
<p>Kostnaden varierar beroende på omfattning och individuella behov. Vi ger alltid
tydlig information om pris och upplägg innan utredningen påbörjas, så att du vet vad som
ingår.</p>
<p>Bedömningssamtalet är kostnadsfritt om vi bestämmer oss för att genomföra en
utredning, eftersom det då ingår i den. Om vi kommer överens om att inte inleda någon
utredning faktureras bedömningssamtalet som ett enskilt besök om 1 500 kr.</p>
'''

V_UTREDNING = [
    dict(
        slug='adhd', label='Utredning av adhd',
        h1='ADHD-utredning för vuxna i Uppsala',
        title='Privat ADHD-utredning för vuxna i Uppsala | KBT-Konsulterna',
        desc='Privat ADHD-utredning för vuxna hos legitimerade psykologer i Uppsala. '
             'Kort väntetid, skriftligt utlåtande och samarbete med specialistläkare.',
        lede='Många vuxna lever med odiagnostiserad adhd utan att förstå varför '
             'tillvaron känns mer krävande än den borde.',
        people=['karin-holmstrom', 'elias-westerlund', 'barry-karlsson'],
        also=[('Utredning av autism', 'vuxna/utredning/autism/'),
              ('Omprövning av diagnos', 'vuxna/utredning/omprovning/'),
              ('Behandling vid NPF', 'vuxna/behandling/npf/')],
        body='''
<p>Upplever du svårigheter med koncentration, uppmärksamhet eller rastlöshet i vardagen?
Det kan vara påfrestande och påverka arbetsliv, vardag och relationer. En kartläggning
kan skapa förutsättningar för rätt stöd och eventuell medicinsk behandling — och ge ökad
självkännedom.</p>

<p>Vid behov samarbetar vi med specialistläkare i psykiatri, så att du på ett tryggt sätt
kan få stöd kring eventuell medicinering i samband med en diagnos.</p>

<h2>Varför göra en privat utredning?</h2>
<p>En privat utredning innebär att du snabbare kommer igång och därmed snabbare kan
påbörja en behandling. Vi möter många i Uppsala som söker en utredning med hög klinisk
kvalitet men vill undvika de långa väntetider som ofta finns i den offentliga vården.</p>
''' + UTREDNING_STEPS_VUXEN + '''
<h2>Vanliga frågor</h2>

<h3>Vilka är de vanligaste adhd-symtomen hos vuxna?</h3>
<p>Adhd hos vuxna visar sig på olika sätt, men vanliga symtom är svårigheter med
koncentration och uppmärksamhet, att komma igång med eller avsluta uppgifter, bristande
struktur och tidsplanering, samt en känsla av inre rastlöshet. Många beskriver också att
de lätt blir distraherade, glömmer saker, eller upplever att vardagen kräver mer energi
än för andra. Symtomen kan påverka arbete, studier, relationer och självkänsla — men med
rätt stöd finns goda möjligheter till förändring.</p>

<h3>Skiljer sig adhd hos kvinnor från de traditionella symtomen?</h3>
<p>Adhd har historiskt beskrivits utifrån hur symtomen visar sig hos pojkar, där
hyperaktivitet och utåtagerande beteende varit framträdande. Hos kvinnor ser vi oftare
en mer inåtvänd problematik — koncentrationssvårigheter, exekutiva svårigheter, inre
stress och stark självkritik. Eftersom symtomen generellt inte är lika tydliga för
omgivningen, och eftersom många har kompenserat för sina svårigheter, upptäcks
diagnosen ofta senare i livet.</p>

<h3>Kan jag utredas om jag samtidigt har ångest, depression eller utmattning?</h3>
<p>Ja. Det är mycket vanligt bland dem som söker utredning hos oss. Under utredningen
gör vi en differentialdiagnostisk bedömning av om symtomen beror på en underliggande
NPF-diagnos, på psykisk ohälsa, eller på samsjuklighet — för att du ska få rätt
behandling framåt.</p>
''' + PRIS_UTREDNING,
    ),
    dict(
        slug='autism', label='Utredning av autism',
        h1='Autismutredning för vuxna i Uppsala',
        title='Privat autismutredning för vuxna i Uppsala | KBT-Konsulterna',
        desc='Privat utredning av autismspektrumtillstånd (AST) hos vuxna. '
             'Legitimerade psykologer i Uppsala, kort väntetid, skriftligt utlåtande.',
        lede='Många vuxna med odiagnostiserad autism har lagt enorm energi på att '
             '”passa in”. En utredning kan vara en bekräftelse på att utmaningarna '
             'har varit — och är — verkliga.',
        people=['karin-holmstrom', 'barry-karlsson', 'elias-westerlund'],
        also=[('Utredning av adhd', 'vuxna/utredning/adhd/'),
              ('Omprövning av diagnos', 'vuxna/utredning/omprovning/'),
              ('Behandling vid NPF', 'vuxna/behandling/npf/')],
        body='''
<p>En autismdiagnos i vuxen ålder kan ge ökad självförståelse och acceptans, och skapa
förutsättningar för rätt stöd och anpassningar. Vi utreder autismspektrumtillstånd hos
vuxna och har tillgång till specialistläkare som bidrar till diagnostiken.</p>

<h2>Känner du igen dig?</h2>
<p>Autism är en neuropsykiatrisk funktionsnedsättning som kan innebära att det är
svårt:</p>
<ul>
  <li>att förstå vad andra menar</li>
  <li>att kommunicera med andra och bli förstådd på rätt sätt</li>
  <li>när vissa intressen blir mycket intensiva</li>
  <li>när det nya och ovana är stressande, samtidigt som behovet av förutsägbarhet och
  rutiner är starkt</li>
  <li>med sinnesintryck som ljud, dofter, beröring och smaker, när de upplevs som extra
  starka och påträngande</li>
</ul>
<p>Det kan ge svårigheter i sociala sammanhang, i relationer och i arbetslivet.</p>
''' + UTREDNING_STEPS_VUXEN + '''
<h2>Vanliga frågor</h2>

<h3>Vad innebär det att autism är ett spektrum?</h3>
<p>Att autism är ett spektrum innebär att diagnosen — medicinskt autismspektrumtillstånd,
AST — tar sig mycket olika uttryck från person till person. Det finns ingen ”typisk”
profil; varje individ har en unik kombination av styrkor och utmaningar. Begreppet
beskriver variationen inom social kommunikation, flexibilitet i tänkandet och
bearbetning av sinnesintryck. Vissa vuxna med autism behöver omfattande stöd i vardagen,
andra lever helt självständigt men upplever stor mental trötthet eller stresskänslighet
i vissa miljöer.</p>

<h3>Vad är högfungerande autism?</h3>
<p>Högfungerande autism (HFA) är en icke-officiell term som ibland används om personer
som uppfyller kriterierna för en autismdiagnos men inte har en intellektuell
funktionsnedsättning.</p>

<h3>Vilka är de vanligaste tecknen hos vuxna?</h3>
<p>Vanliga tecken är svårigheter att tolka socialt samspel och kroppsspråk, ett behov av
fasta rutiner och förutsägbarhet, samt känslighet för sinnesintryck som ljud, ljus eller
beröring. Många upplever också en intensiv förmåga att fokusera på specifika intressen,
men känner stor mental trötthet efter social interaktion. En utredning hjälper till att
skilja dessa drag från exempelvis social ångest eller depression.</p>
''' + PRIS_UTREDNING,
    ),
    dict(
        slug='omprovning', label='Omprövning av diagnos',
        h1='Omprövning av diagnos: adhd och autism',
        title='Omprövning av adhd- och autismdiagnos i Uppsala | KBT-Konsulterna',
        desc='Omprövning av tidigare ställd neuropsykiatrisk diagnos för vuxna över 18 '
             'år — inför polisutbildning, militärtjänstgöring eller av egna skäl.',
        lede='Behöver du få en tidigare ställd diagnos omprövad? Som en del av '
             'utredningsarbetet med vuxna över 18 år erbjuder vi omprövning av tidigare '
             'ställda neuropsykiatriska diagnoser.',
        people=['elias-westerlund'],
        also=[('Utredning av adhd', 'vuxna/utredning/adhd/'),
              ('Utredning av autism', 'vuxna/utredning/autism/'),
              ('Behandling vid NPF', 'vuxna/behandling/npf/')],
        body='''
<p>Under senare år har behovet vuxit av att kunna följa upp neuropsykiatriska diagnoser
över tid. Vi ser ett växande antal vuxna som inte längre känner igen sig i en tidigare
ställd diagnos, inte längre upplever samma funktionsnedsättning, eller som önskar en
omprövning på grund av karriärdrömmar inom yrken med strikta antagningskrav. Då kan det
vara viktigt att utreda om diagnosen fortfarande är aktuell, och i vilken grad den
påverkar funktionsnivån i dag.</p>

<h2>Ett historiskt rättsfall</h2>
<p>Under 2021 slog Diskrimineringsombudsmannen fast att Försvarsmakten samt Plikt- och
prövningsverket gjort sig skyldiga till diskriminering när de automatiskt uteslöt sökande
med autism- eller adhd-diagnos. Myndigheterna måste därmed pröva lämpligheten även för
personer med neuropsykiatrisk funktionsnedsättning.</p>

<p>För att kunna bedömas som lämplig krävs dock en utredning som undersöker om personen i
dag uppfyller kriterierna för diagnosen, och i så fall vilken nedsatt funktion det rör
sig om. I dessa fall är en omprövning därför viktig — framför allt för att säkerställa
att du kan utföra det framtida arbetet på ett säkert sätt.</p>

<h2>Hur går en omprövning till?</h2>
<p>Vi inleder alltid med ett bedömningssamtal för att tillsammans säkerställa att
omprövningen är motiverad. För hela utredningen beräknas ungefär fyra besök på
mottagningen.</p>

<p>Oavsett orsak får du efter utredningen med dig ett utlåtande som beskriver din
nuvarande funktion och om diagnosen fortfarande är aktuell. Önskar du omprövning i syfte
att söka till polisutbildning eller militärtjänstgöring är det viktigt att du meddelar
det — det ställer specifika krav på hur omprövningen ska gå till och på den efterföljande
dokumentationen.</p>

<p>Precis som vid all utredning kan vi tillsammans upptäcka att du behöver stöd eller
hjälp för annan psykisk ohälsa. Då hjälper vi dig vidare med fördjupad utredning eller
behandling hos oss, eller hos en annan vårdgivare.</p>
''',
    ),
]

# --------------------------------------------------------------------------
# Barn & ungdom → Psykologisk behandling
# --------------------------------------------------------------------------
VARDNADSHAVARE = ('<p class="callout">All behandling av barn och ungdomar genomförs i '
                  'nära samarbete med vårdnadshavare.</p>')

B_BEHANDLING = [
    dict(
        slug='oro-angest', label='Oro, ängslan & ångest',
        h1='Oro, ängslan och ångest hos barn och ungdomar',
        title='KBT vid oro och ångest hos barn och unga i Uppsala | KBT-Konsulterna',
        desc='Bedömning och KBT-behandling vid oro, ängslan och ångest hos barn och '
             'ungdomar i alla åldrar. Psykologmottagning i centrala Uppsala.',
        lede='Det är vanligt att barn och ungdomar känner nervositet och rädsla. Ofta '
             'är det övergående — men ibland är oron stark och hindrande i vardagen.',
        people=['karin-holmstrom', 'aksel-reppling'],
        also=[('Tvångstankar och tvångshandlingar (OCD)', 'barn-och-ungdom/behandling/ocd/'),
              ('Nedstämdhet och depression', 'barn-och-ungdom/behandling/depression/'),
              ('Stöd till föräldrar och anhöriga', 'barn-och-ungdom/stod/foraldrar/')],
        body='''
<p>Våra psykologer bedömer och behandlar oro, ängslan och ångest hos barn och ungdomar
i alla åldrar.</p>

<p>Det är inte ovanligt att barn och ungdomar visar stark rädsla för specifika
företeelser — insekter, att känna sig instängd, eller rädsla för att kräkas
(<strong>specifik fobi</strong>).</p>

<p>Det är också vanligt att barn och ungdomar känner intensiv panik och rädsla i sociala
situationer (<strong>social oro</strong>). Och för yngre barn är känslomässiga
svårigheter vid att lämna föräldrar eller andra trygga personer inte ovanligt
(<strong>separationsoro</strong>).</p>

<p>När rädslan börjar styra vad barnet gör och inte gör — vilka platser som undviks,
vilka aktiviteter som väljs bort, om skolan blir svår att gå till — är det en god idé
att söka hjälp.</p>
''' + VARDNADSHAVARE,
    ),
    dict(
        slug='depression', label='Nedstämdhet & depression',
        h1='Nedstämdhet och depression hos barn och ungdomar',
        title='Depression hos barn och unga i Uppsala | KBT-Konsulterna',
        desc='Bedömning och KBT-behandling vid nedstämdhet och depression hos barn och '
             'ungdomar i alla åldrar. Legitimerade psykologer i Uppsala.',
        lede='Det finns ingen skarp gräns mellan att vara nedstämd och att vara '
             'deprimerad, men depression innebär mer uttalade svårigheter.',
        people=['karin-holmstrom', 'aksel-reppling'],
        also=[('Oro, ängslan och ångest', 'barn-och-ungdom/behandling/oro-angest/'),
              ('Sömnproblem', 'barn-och-ungdom/behandling/somn/'),
              ('Stöd till föräldrar och anhöriga', 'barn-och-ungdom/stod/foraldrar/')],
        body='''
<p>Våra psykologer har lång erfarenhet av att bedöma och behandla nedstämdhet och
depression hos barn och ungdomar i alla åldrar.</p>

<p>Nedstämdhet och depression hos barn och ungdomar visar sig genom svårigheter att
känna glädje och lust inför sådant som tidigare har varit roligt. Det är vanligt med
energilöshet, irritation, låg självkänsla, sömnstörningar, koncentrationssvårigheter och
en känsla av hopplöshet.</p>

<p>Hos barn och unga kan symtomen se annorlunda ut än hos vuxna — irritation och ilska är
ofta mer framträdande än den nedstämdhet man förväntar sig. Det gör att en depression
ibland misstas för trots eller för en jobbig period.</p>

<p>Om du som förälder är orolig för att ditt barn har tankar på att inte vilja leva:
fråga rakt ut, och sök hjälp direkt. Se <a href="{base}akut-hjalp/index.html">akut
hjälp</a>.</p>
''' + VARDNADSHAVARE,
    ),
    dict(
        slug='ocd', label='Tvångstankar (OCD)',
        h1='Tvångstankar och tvångshandlingar (OCD) hos barn och ungdomar',
        title='KBT vid OCD hos barn och unga i Uppsala | KBT-Konsulterna',
        desc='Bedömning och KBT-behandling vid tvångstankar och tvångshandlingar (OCD) '
             'hos barn och ungdomar i alla åldrar, i Uppsala.',
        lede='KBT är en effektiv behandlingsmetod vid tvångssyndrom, och våra psykologer '
             'bedömer och behandlar tvångstankar och tvångsbeteenden hos barn och '
             'ungdomar i alla åldrar.',
        people=['angeli-holmstedt', 'karin-holmstrom'],
        also=[('Oro, ängslan och ångest', 'barn-och-ungdom/behandling/oro-angest/'),
              ('Beteenden som utmanar', 'barn-och-ungdom/behandling/beteende/'),
              ('Oro och ångest hos vuxna', 'vuxna/behandling/oro-angest/')],
        body='''
<p>Tvångssyndrom kallas också OCD, en förkortning för <em>Obsessive-Compulsive
Disorder</em>.</p>

<p>Det är vanligt att barn har tvångsliknande tankar ibland. Många känner igen en period
i barndomen då det betydde otur att kliva på brunnslock, eller då vissa siffror skulle
undvikas av samma skäl. Ofta är det övergående.</p>

<p>Men ibland utvecklas den här typen av tankar och beteenden på ett sätt som blir
hindrande i barnets eller ungdomens vardag. Vanliga teman för tvångstankar är oro för
smuts, baciller och föroreningar; oro för att orsaka skador och olyckor; eller tankar om
balans och om att saker måste vara ”på ett visst sätt”.</p>

<p>När tankarna och beteendena utgör ett hinder i vardagen kan behandling vara nödvändig
för att komma till rätta med problemen.</p>
''' + VARDNADSHAVARE,
    ),
    dict(
        slug='somn', label='Sömnproblem',
        h1='Sömnproblem hos barn och ungdomar',
        title='Behandling vid sömnproblem hos barn och unga | KBT-Konsulterna Uppsala',
        desc='Bedömning och behandling av sömnsvårigheter hos barn och ungdomar i alla '
             'åldrar. Psykologmottagning i centrala Uppsala.',
        lede='Sömnen är viktig för barn och ungdomar, och långvarig sömnbrist märks i '
             'allt annat: känsloreglering, koncentration, inlärning.',
        people=['karin-holmstrom'],
        also=[('Oro, ängslan och ångest', 'barn-och-ungdom/behandling/oro-angest/'),
              ('Nedstämdhet och depression', 'barn-och-ungdom/behandling/depression/'),
              ('Sömnproblem hos vuxna', 'vuxna/behandling/somn/')],
        body='''
<p>Det är vanligt att barn och ungdomar i perioder sover sämre än vanligt, eller har
svårt att komma till ro och somna. Det är ofta övergående och går att hantera med stöd
av föräldrar eller andra viktiga vuxna.</p>

<p>Vid långvarig sömnbrist kan det däremot leda till svårigheter att reglera känslor,
till rastlöshet, ökad impulsivitet, sämre minne, och till svårigheter med koncentration
och inlärning. Sömnbrist förstärker också det mesta annat: oro blir mer oroligt,
irritation mer irriterad.</p>

<p>När besvären blir mer uttalade och inte går över kan psykologisk behandling för
sömnsvårigheter vara en god idé.</p>
''' + VARDNADSHAVARE,
    ),
    dict(
        slug='beteende', label='Beteenden som utmanar',
        h1='Beteenden som utmanar',
        title='Hjälp vid utåtagerande beteende hos barn | KBT-Konsulterna Uppsala',
        desc='Bedömning och behandling av utmanande och utåtagerande beteende hos barn '
             'och ungdomar i alla åldrar, i nära samarbete med vårdnadshavare.',
        lede='Har ditt barn affektutbrott som blir svåra att hantera? Våra psykologer '
             'bedömer och behandlar utmanande beteende hos barn och ungdomar i alla '
             'åldrar.',
        people=['karin-holmstrom', 'aksel-reppling'],
        also=[('Stöd till föräldrar och anhöriga', 'barn-och-ungdom/stod/foraldrar/'),
              ('Utredning av adhd', 'barn-och-ungdom/utredning/adhd/'),
              ('Oro, ängslan och ångest', 'barn-och-ungdom/behandling/oro-angest/')],
        body='''
<p>Att visa känsloutbrott är en naturlig del i barns utveckling, på samma sätt som
perioder av mer protester och minskad följsamhet. Vissa barn får lättare än andra
affektutbrott, är mer envisa, impulsiva och utagerande. Svårigheterna brukar minska
eller försvinna när barnet blir äldre.</p>

<p>Men om känsloutbrotten fortsätter, och barnet inte verkar få det lättare att hantera
motgångar samtidigt som sättet att agera blir svårt att möta — då kan det vara en god idé
att söka psykologisk behandling.</p>

<p>Arbetet handlar lika mycket om de vuxna runt barnet som om barnet självt: vad som
utlöser utbrotten, vad som händer efteråt, och vilka strategier som faktiskt fungerar i
just er familj. Ibland finns en neuropsykiatrisk förklaring i botten, och då kan en
<a href="{base}barn-och-ungdom/utredning/index.html">utredning</a> vara nästa steg.</p>
''' + VARDNADSHAVARE,
    ),
]

# --------------------------------------------------------------------------
# Barn & ungdom → Utredning & bedömning
# --------------------------------------------------------------------------
UTREDNING_STEPS_BARN = '''
<h2>Så går utredningen till</h2>
<ol class="steps steps--plain">
  <li><h3>Inledande bedömning</h3><p>Vi träffas tillsammans med barnet eller ungdomen
  och vårdnadshavare för att gå igenom bakgrund och nuvarande situation, och bedöma om
  en fortsatt utredning är motiverad. Tillfället är också till för att ni ska få träffa
  er psykolog, ställa frågor och känna efter om samarbetet känns tryggt.</p></li>
  <li><h3>Djupgående intervjuer</h3><p>En intervju med barnet och vårdnadshavare om
  viktiga livshändelser. Efter samtycke från vårdnadshavare inhämtar vi också
  information från barnets lärare och skola.</p></li>
  <li><h3>Kartläggning och testning</h3><p>Individuellt anpassad efter barnets behov,
  men alltid med en bedömning av psykisk hälsa och ohälsa, av styrkor och svårigheter,
  och en systematisk genomgång av symtomen med standardiserade instrument.</p></li>
  <li><h3>Sammanställning och återgivning</h3><p>Vi går igenom resultatet tillsammans.
  Ni får med er ett skriftligt utlåtande och rekommendationer för stöd och anpassningar
  framåt. Vi har tillgång till specialistläkare som bidrar till diagnostiken.</p></li>
</ol>
<p>En utredning hos oss består för det mesta av 5–7 besök, och vi lägger stor vikt vid
att den ska ske i barnets takt.</p>
'''

FAQ_UTREDNING_BARN = '''
<h2>Vanliga frågor</h2>

<h3>Hur vet jag om mitt barn behöver en utredning?</h3>
<p>Om barnets svårigheter håller i sig över tid och påverkar skolan, kompisrelationerna
eller måendet hemma kan det vara klokt att göra en bedömning. Hör gärna av er för en
inledande konsultation om ni är osäkra.</p>

<h3>Krävs remiss från skola eller vårdcentral?</h3>
<p>Nej. Som privat mottagning kan ni söka er till oss direkt utan remiss. Vi samarbetar
gärna med barnets skola eller andra vårdgivare om ni önskar det.</p>

<h3>Vad kostar en privat utredning?</h3>
<p>Kostnaden varierar beroende på vilken typ av utredning som genomförs. Vi ger alltid
tydlig information om pris och upplägg innan utredningen påbörjas. Bedömningssamtalet är
kostnadsfritt om vi bestämmer oss för att genomföra en utredning, eftersom det då ingår
i den.</p>

<h3>Hur lång är väntetiden?</h3>
<p>En tidig utredning ger snabbare tillgång till rätt stöd, vilket förbättrar barnets
självkänsla, skolsituation och relationer — och förebygger sekundära svårigheter som
psykisk ohälsa. Vår ambition är därför att kunna erbjuda en första tid för bedömning
inom kort tid, så att ni slipper den stress som en lång väntan innebär för familjen.</p>
'''

B_UTREDNING = [
    dict(
        slug='adhd', label='Utredning av adhd',
        h1='ADHD-utredning för barn och ungdomar i Uppsala',
        title='Privat ADHD-utredning för barn i Uppsala | KBT-Konsulterna',
        desc='Privat ADHD-utredning för barn och ungdomar hos legitimerade psykologer '
             'i Uppsala. Ingen remiss krävs, skriftligt utlåtande, kort väntetid.',
        lede='Adhd tar sig olika uttryck hos barn, och symtomen ser inte likadana ut '
             'för alla. En utredning är första steget mot ökad förståelse.',
        people=['karin-holmstrom', 'barry-karlsson'],
        also=[('Utredning av autism', 'barn-och-ungdom/utredning/autism/'),
              ('Utredning av intellektuell funktion', 'barn-och-ungdom/utredning/intellektuell-funktion/'),
              ('Beteenden som utmanar', 'barn-och-ungdom/behandling/beteende/')],
        body='''
<p>Har ditt barn svårt att sitta still, svårt att komma igång med läxor, eller hamnar
ofta i konflikter med familj och vänner? Eller är det tvärtom — att barnet verkar lugnt
men är dagdrömmande, glömskt och har svårt att fokusera?</p>

<h2>Tecken att vara uppmärksam på</h2>
<p>Föräldrar och lärare reagerar ofta på olika saker beroende på hur profilen ser ut.
Vanliga tecken är:</p>
<ul>
  <li>svårigheter med uppmärksamhet och att slutföra uppgifter</li>
  <li>motorisk rastlöshet, eller en känsla av att ständigt vara ”på språng”</li>
  <li>svårt att vänta på sin tur, och en tendens att avbryta andra</li>
  <li>glömska i vardagen och svårt att hålla ordning på sina saker</li>
</ul>
<p>En professionell bedömning är viktig för att skilja dessa symtom från vanlig
utveckling eller från andra bakomliggande orsaker.</p>

<h2>Skillnader mellan pojkar och flickor</h2>
<p>En vanlig fråga är varför adhd ibland upptäcks senare hos vissa barn, särskilt hos
flickor. Historiskt har adhd förknippats med utåtriktad hyperaktivitet, vilket ofta är
mer framträdande hos pojkar.</p>
<p>Många flickor — och en del pojkar — har i stället en mer inåtvänd problematik, adhd av
ouppmärksam form. Hyperaktiviteten syns inte på utsidan; barnet kan verka lugnt men
kämpar med en enorm inre stress, koncentrationssvårigheter och trötthet. Eftersom dessa
barn ofta kompenserar för sina svårigheter (”masking”) riskerar symtomen att missas utan
en grundlig neuropsykiatrisk utredning.</p>
''' + UTREDNING_STEPS_BARN + FAQ_UTREDNING_BARN,
    ),
    dict(
        slug='autism', label='Utredning av autism',
        h1='Autismutredning för barn och ungdomar i Uppsala',
        title='Privat autismutredning för barn i Uppsala | KBT-Konsulterna',
        desc='Privat utredning av autismspektrumtillstånd (AST) hos barn och ungdomar '
             'i Uppsala. Ingen remiss krävs, skriftligt utlåtande, kort väntetid.',
        lede='En utredning handlar inte om att hitta fel. Den handlar om att skapa '
             'förståelse för barnets sätt att bearbeta information och möta omvärlden.',
        people=['karin-holmstrom', 'barry-karlsson'],
        also=[('Utredning av adhd', 'barn-och-ungdom/utredning/adhd/'),
              ('Utredning av intellektuell funktion', 'barn-och-ungdom/utredning/intellektuell-funktion/'),
              ('Oro, ängslan och ångest', 'barn-och-ungdom/behandling/oro-angest/')],
        body='''
<p>Upplever du att ditt barn har ett annorlunda sätt att kommunicera, leka eller
interagera med andra? Som förälder kan det väcka många frågor när barnet inte riktigt
följer de förväntade utvecklingsstegen.</p>

<h2>Tidiga tecken</h2>
<p>Symtomen visar sig ofta tidigt, men kan vara subtila och variera stort mellan barn.
Vanliga tecken som föranleder en utredning är:</p>
<ul>
  <li>svårigheter med ögonkontakt och socialt samspel</li>
  <li>sen språkutveckling, eller ett annorlunda sätt att använda språket, till exempel
  ekotal</li>
  <li>ett starkt behov av rutiner, och svårigheter vid oväntade förändringar</li>
  <li>överkänslighet för sinnesintryck som ljud, ljus eller konsistenser på mat</li>
</ul>
<p>Ser du tidiga tecken är en utredning viktig — det finns forskningsstöd för att tidiga
insatser har bäst effekt.</p>

<h2>Att förstå autismspektrumet</h2>
<p>Tidigare delades autism upp i diagnoser som Aspergers syndrom och atypisk autism. I
dag talar man om autismspektrumtillstånd (AST) som en helhet.</p>
<p>Spektrumet är inte en rak linje från ”lite” till ”mycket” autism, utan ett spektrum av
unika kombinationer av styrkor och utmaningar. Ett barn kan ha hög intellektuell förmåga
och ett välutvecklat språk men stora sociala svårigheter; ett annat kan ha en
intellektuell funktionsnedsättning och begränsat tal. Diagnosen baseras på vilken grad av
stöd barnet behöver. Vårt mål är att kartlägga just ditt barns profil.</p>
''' + UTREDNING_STEPS_BARN + FAQ_UTREDNING_BARN,
    ),
    dict(
        slug='intellektuell-funktion', label='Intellektuell funktion',
        h1='Utredning av intellektuell funktion hos barn',
        title='Utredning av intellektuell funktion hos barn | KBT-Konsulterna',
        desc='Begåvningsutredning av barn och ungdomar i Uppsala — vid misstanke om '
             'intellektuell funktionsnedsättning och vid misstanke om särskild begåvning.',
        lede='Ibland beror skolsvårigheter på att barnets kognitiva förutsättningar inte '
             'matchar de krav som ställs. Vi utreder både vid misstanke om '
             'funktionsnedsättning och vid misstanke om särskild begåvning.',
        people=['barry-karlsson', 'karin-holmstrom'],
        also=[('Utredning av adhd', 'barn-och-ungdom/utredning/adhd/'),
              ('Utredning av autism', 'barn-och-ungdom/utredning/autism/'),
              ('Stöd för skolpersonal', 'barn-och-ungdom/stod/skola/')],
        body='''
<p>Märker ni att ert barn kämpar hårt i skolan men trots stora ansträngningar har svårt
att nå målen eller förstå instruktioner?</p>

<p>Alla barn är olika och har sin egen utvecklingsresa — en enskild försening betyder
inte automatiskt en intellektuell funktionsnedsättning. Liknande tecken kan bero på andra
faktorer, som autism eller adhd. Därför är en professionell bedömning viktig: en diagnos
är avgörande för att barnet ska få rätt stöd och rätt förutsättningar.</p>

<h2>Rätt stöd i skolan</h2>
<p>Att leva med en oupptäckt intellektuell funktionsnedsättning kan leda till stor stress,
en upplevd känsla av misslyckande och låg självkänsla. Genom att fastställa vilka
förutsättningar som finns kan kravnivåer justeras och rätt resurser ges. Målet är att
barnet ska möta utmaningar som är anpassade efter sin förmåga, och att förståelsen ökar —
både hos omgivningen och hos barnet självt.</p>
''' + UTREDNING_STEPS_BARN + '''
<h2>Vanliga frågor</h2>

<h3>Vad innebär intellektuell funktionsförmåga?</h3>
<p>Förmågan till teoretiskt tänkande: att resonera, planera, tänka ut olika lösningar på
problem och kombinera fakta. Utvecklingen av dessa förmågor pågår under hela
uppväxten.</p>

<h3>Vad menas med särskild begåvning?</h3>
<p>En betydligt högre intellektuell funktionsnivå än vad som förväntas i en viss ålder —
en ovanligt hög förmåga till inlärning, reflektion och tankemässig bearbetning, ofta med
extra stora färdigheter inom något speciellt område. Utmärkande är att särskilt begåvade
barn utvecklas olika snabbt inom olika domäner: intellektuellt, känslomässigt och
socialt. De reagerar ofta starkare på sin omgivning än andra barn.</p>
<p>Enligt Skolverket behöver särskilt begåvade elever lärande och diskussion på sin nivå,
och därmed större intellektuella utmaningar än sina klasskamrater. Det finns en risk att
de missförstås och inte blir tillräckligt utmanade. Att utreda hög begåvning kan därför
vara gynnsamt för att öka förståelsen för barnet.</p>

<h3>Vilket stöd har barn med intellektuell funktionsnedsättning rätt till?</h3>
<p>Stödet ser olika ut beroende på behov, men kan handla om pedagogiska anpassningar,
extra resurser i skolan och ibland samhällsinsatser. En diagnos gör det ofta lättare att
få tillgång till rätt stöd. Det viktigaste är att barnet inte ska behöva kämpa utan
förståelse eller rätt hjälp.</p>

<h3>Krävs remiss från skola eller vårdcentral?</h3>
<p>Nej. Som privat mottagning kan ni söka er till oss direkt utan remiss.</p>
''',
    ),
]

# --------------------------------------------------------------------------
# Barn & ungdom → Stöd till vuxna runt barnet
# --------------------------------------------------------------------------
B_STOD = [
    dict(
        slug='foraldrar', label='Föräldrar & anhöriga',
        h1='Stöd till föräldrar och anhöriga',
        title='Föräldrastöd och anhörigstöd i Uppsala | KBT-Konsulterna',
        desc='Rådgivande samtal till föräldrar och anhöriga till barn och ungdomar i '
             'alla åldrar. Psykologmottagning i centrala Uppsala och online.',
        lede='Att vara förälder eller nära anhörig till ett barn är ibland utmanande och '
             'svårt. Det uppstår ständigt nya situationer och frågor.',
        people=['aksel-reppling', 'angeli-holmstedt'],
        also=[('Beteenden som utmanar', 'barn-och-ungdom/behandling/beteende/'),
              ('Stöd för skolpersonal', 'barn-och-ungdom/stod/skola/'),
              ('Anhörig vid beroende', 'vuxna/beroende/')],
        body='''
<p>Vi har mångårig erfarenhet av att ge stöd till föräldrar och anhöriga till barn och
ungdomar i alla åldrar.</p>

<p>Det kan vara svårt att veta hur man ska ge bästa möjliga stöd till barnet eller
ungdomen. Då kan det vara till god hjälp att träffa en utomstående, professionell person
för att diskutera det som oroar eller bekymrar.</p>

<p>Stödet kan handla om konkreta strategier i vardagen, om hur man förhåller sig till ett
barn som mår dåligt, om hur syskon påverkas, eller om ditt eget mående — att vara
förälder till ett barn som har det svårt tär, och det är inte själviskt att ta hand om
sig själv också.</p>

<p>Du behöver inte ha ett barn i behandling hos oss för att boka ett samtal.</p>
''',
    ),
    dict(
        slug='skola', label='Skola & elevhälsa',
        h1='Stöd för skolpersonal',
        title='Skolpsykolog och stöd för skolpersonal | KBT-Konsulterna',
        desc='Skolpsykologisk kompetens för skolor: hälsofrämjande och förebyggande '
             'arbete, åtgärdande insatser för enskilda elever, personalhandledning.',
        lede='Behöver er skola skolpsykologisk kompetens? Vi har mångårig erfarenhet av '
             'skolpsykologiskt konsultarbete.',
        people=['karin-holmstrom', 'barry-karlsson'],
        also=[('Utredning av intellektuell funktion', 'barn-och-ungdom/utredning/intellektuell-funktion/'),
              ('Stöd till socialtjänst', 'barn-och-ungdom/stod/socialtjanst/'),
              ('Handledning och coaching', 'organisationer/handledning/')],
        body='''
<p>I skolan möter personalen barn och ungdomar med olika förutsättningar för skolarbete.
Vissa elever kommer till skolan med goda förutsättningar, medan andra av olika
anledningar kämpar med sämre. Skolans personal har som uppgift att erbjuda utbildning och
en gynnsam skolmiljö till alla — vilket ofta innebär stora utmaningar.</p>

<h2>Vad vi erbjuder</h2>
<ul>
  <li>hälsofrämjande och förebyggande arbete</li>
  <li>åtgärdande arbete för enskilda elever</li>
  <li>personalhandledning, enskilt och i grupp</li>
  <li>skolpsykologiskt utredningsarbete</li>
</ul>

<p>Vi är väl förtrogna med både personalhandledning och skolpsykologiskt
utredningsarbete, och kan utgöra en stabil stöttepelare för er i dessa frågor.</p>

<p>För upphandling, ramavtal och större uppdrag, se
<a href="{base}organisationer/index.html">För organisationer</a>.</p>
''',
    ),
    dict(
        slug='hvb-familjehem', label='HVB & familjehem',
        h1='Stöd till HVB-hem och familjehem',
        title='Handledning för HVB-hem och familjehem | KBT-Konsulterna Uppsala',
        desc='Handledning till familjehemsföräldrar och personal vid behandlingshem och '
             'HVB-hem. Mångårig erfarenhet av placerade barn och ungdomar.',
        lede='Att stötta och vägleda barn och ungdomar som placerats i HVB-hem och '
             'familjehem är en viktig, krävande och svår uppgift.',
        people=['barry-karlsson', 'thomas-alm'],
        also=[('Stöd till socialtjänst', 'barn-och-ungdom/stod/socialtjanst/'),
              ('Stöd för skolpersonal', 'barn-och-ungdom/stod/skola/'),
              ('Handledning och coaching', 'organisationer/handledning/')],
        body='''
<p>Familjehemsföräldrar och personal vid HVB-hem ställs ofta i situationer som kräver stor
kunskap och väl genomtänkta strategier — och som samtidigt väcker starka egna
reaktioner.</p>

<p>Vi har mångårig erfarenhet av att handleda familjehemsföräldrar och personal vid
behandlingshem och HVB-hem. Handledningen kan handla om ett enskilt placerat barn, om
bemötande och förhållningssätt i gruppen, eller om att ge personalen ett rum att bearbeta
det som är tungt i uppdraget.</p>

<p>Vi arbetar både på plats hos er och via videosamtal, i hela landet.</p>
''',
    ),
    dict(
        slug='socialtjanst', label='Socialtjänst',
        h1='Stöd till socialtjänsten',
        title='Handledning för socialtjänsten | KBT-Konsulterna Uppsala',
        desc='Handledning till socialtjänsten om barns och ungdomars utveckling och '
             'behov, psykisk hälsa och ohälsa samt neuropsykiatriska funktionsnedsättningar.',
        lede='Socialtjänsten finns nära barn och ungdomar i svåra situationer, och '
             'behöver därför en bred kunskap om olika förutsättningar.',
        people=['thomas-alm', 'barry-karlsson'],
        also=[('Stöd till HVB och familjehem', 'barn-och-ungdom/stod/hvb-familjehem/'),
              ('Stöd för skolpersonal', 'barn-och-ungdom/stod/skola/'),
              ('Skadligt bruk på arbetsplatsen', 'organisationer/skadligt-bruk/')],
        body='''
<p>De som arbetar med barn och ungdom inom socialtjänsten behöver ha bred kunskap om
mycket: utveckling och behov, psykisk hälsa och ohälsa, och neuropsykiatriska
funktionsnedsättningar.</p>

<p>Vi erbjuder handledning inom samtliga dessa områden — ärendehandledning,
metodhandledning och processhandledning, enskilt eller i grupp. Flera av oss har lång
egen erfarenhet av arbete i och mot socialtjänst, beroendevård och Statens
institutionsstyrelse.</p>

<p>Vi har också lång erfarenhet av frågor om skadligt bruk och beroende hos föräldrar,
och av hur det påverkar barnen i en familj. Se
<a href="{base}vuxna/beroende/index.html">skadligt bruk och beroende</a>.</p>
''',
    ),
]

# --------------------------------------------------------------------------
# För organisationer — five level-2 pages, no children
# --------------------------------------------------------------------------
ORG = [
    dict(
        slug='handledning', label='Handledning & coaching',
        h1='Handledning och coaching',
        title='Handledning och coaching för verksamheter | KBT-Konsulterna Uppsala',
        desc='Ärende-, metod- och utbildningshandledning samt coaching för primärvård, '
             'psykiatri, socialtjänst, skola, behandlingshem och beroendekliniker.',
        lede='I många yrken behövs stöd för att kunna fortsätta utvecklas, och för att '
             'orka hantera svåra situationer.',
        people=['angeli-holmstedt', 'thomas-alm', 'jens-karstrom'],
        also=[('Föreläsningar och utbildning', 'organisationer/utbildning/'),
              ('Rehabilitering', 'organisationer/rehabilitering/'),
              ('Stöd för skolpersonal', 'barn-och-ungdom/stod/skola/')],
        body='''
<p>Det kan handla om komplicerade och ovanliga problem, eller om personliga reaktioner
som påverkar arbetet. Handledning hjälper individer och grupper att utveckla sin
kompetens, att hantera ett stressfyllt arbete, och att klara av utmanande situationer.</p>

<h2>Vilka handleder vi?</h2>
<p>Handledningen kan vara inriktad på att stödja personal i att ge den vård, behandling
eller det stöd som deras klienter och patienter behöver. Vi har lång erfarenhet av att
handleda anställda inom bland annat:</p>
<ul>
  <li>primärvård</li>
  <li>psykiatrisk verksamhet</li>
  <li>socialtjänst</li>
  <li>skolor och specialskolor</li>
  <li>behandlingshem</li>
  <li>beroendekliniker</li>
</ul>

<h2>Utbildningshandledning</h2>
<p>Vi har under många år handlett blivande psykologer, psykoterapeuter och andra
yrkesgrupper — enskilt eller i grupp — inom ramen för utbildningar i KBT. Av tradition
finns ett gap mellan forskning och klinisk praktik, och handledningen syftar till att
överbrygga det. Handledaren har både uppgiften att bidra till utvecklingen av den
terapeutiska kompetensen och till inskolningen i yrket.</p>

<h2>Coaching</h2>
<p>Coaching handlar om att få stöd och vägledning i att utvecklas och nå mål, både
individuellt och i grupp. I psykologens och psykoterapeutens utbildningar ingår teorier
och metoder som är användbara för det.</p>
<p>Vi har bred erfarenhet av att ge stöd och vägledning baserad på beteendeanalys,
formulerande av värderingar och mål, beteendeförändringar, samt analys och utveckling av
hjälpsammare tankemönster och förhållningssätt till tankar som kan upplevas hindrande.
Även känslohantering ingår.</p>
''',
    ),
    dict(
        slug='utbildning', label='Föreläsningar & utbildning',
        h1='Föreläsningar, kurser och utbildningar',
        title='Utbildningar i KBT, MI och mindfulness | KBT-Konsulterna',
        desc='Skräddarsydda föreläsningar, workshops och längre utbildningar i KBT, '
             'motiverande samtal (MI) och mindfulness för företag och offentlig verksamhet.',
        lede='Allt från kortare workshops och seminarier till orienteringsutbildningar '
             'på 4–5 dagar och längre grundläggande psykoterapiutbildningar.',
        people=['angeli-holmstedt', 'thomas-alm', 'barry-karlsson'],
        also=[('Handledning och coaching', 'organisationer/handledning/'),
              ('Kontakt för uppdrag', 'organisationer/kontakt/'),
              ('Vad är KBT?', 'om-oss/index.html#kbt')],
        body='''
<p>Vi har lång erfarenhet av att utbilda i kognitiv beteendeterapi (KBT), motiverande
samtal (MI) och mindfulness.</p>

<p>Utbudet sträcker sig från kortare workshops och seminarier, via orienteringsutbildningar
på 4–5 dagar, till längre grundläggande psykoterapiutbildningar — det som tidigare kallades
”Steg 1”.</p>

<p>Vi är också verksamma som lärare och handledare på psykolog- och
psykoterapeututbildningar knutna till Uppsala universitet.</p>

<h2>Skräddarsydda uppdrag</h2>
<p>Vi erbjuder utbildning och föredrag för företag och offentlig verksamhet om exempelvis
stress, skadligt bruk och beroende, ledarskap och kommunikation, samtalsmetodik,
motiverande samtal, mindfulness och många andra teman.</p>

<p>Hör av er för information om uppdragsutbildningar, workshops, föreläsningsserier,
föredrag och övrig fortbildning.</p>
''',
    ),
    dict(
        slug='rehabilitering', label='Rehabilitering',
        h1='Rehabilitering och arbetsrelaterad psykisk ohälsa',
        title='Rehabilitering vid stress och utmattning | KBT-Konsulterna',
        desc='Kartläggning, bedömning och behandling vid arbetsrelaterad stress, '
             'utmattning och sjukskrivning med grund i psykisk ohälsa.',
        lede='En frisk arbetsplats och ett hållbart arbetsliv är mål vi tror att alla '
             'arbetsgivare har. Många viktiga insatser görs — men ibland räcker de inte '
             'ända fram.',
        people=['thomas-alm', 'angeli-holmstedt'],
        also=[('Skadligt bruk på arbetsplatsen', 'organisationer/skadligt-bruk/'),
              ('Handledning och coaching', 'organisationer/handledning/'),
              ('Stress och utmattning', 'vuxna/behandling/stress-utmattning/')],
        body='''
<h2>Stress och utmattning</h2>
<p>Medarbetare såväl som chefer kan uppleva höga krav — från sig själva att göra ett gott
jobb, och från arbetsuppgifter som är krävande och ibland känns övermäktiga. Man kan
känna tidspress, att aldrig bli klar, att sakna stöd och uppmuntran, eller — i arbete med
andra människor — att lidandet och behoven överstiger de resurser man har för att
hjälpa.</p>

<p>I dagens arbetsliv krävs ofta också en ständig digital närvaro, och möjligheten till
återhämtning har krympt. Livet består inte heller enbart av arbete: vi ska också finnas
för partner, barn, familj, sjuka föräldrar, vänner och allt annat som hör till.</p>

<h2>Sjukskrivning med grund i psykisk ohälsa</h2>
<p>Arbetsrelaterad stress kan leda till en mängd kroppsliga och psykiska besvär, och i
värsta fall till långvarig frånvaro och sjukskrivning — stressrelaterade symtom,
utmattning, oro, ångest, sömnproblem eller skadligt bruk. En stor del av dagens
sjukskrivningar beror på psykisk ohälsa, som kan vara relaterad till både privata och
arbetsrelaterade problem.</p>

<h2>Skadligt bruk</h2>
<p>Vi är specialister på att upptäcka, utreda och behandla problem med skadligt bruk av
alkohol, läkemedel och droger, samt problematiskt spelande om pengar. Se
<a href="{base}organisationer/skadligt-bruk/">skadligt bruk på arbetsplatsen</a>.</p>

<h2>Vad vi kan erbjuda</h2>
<p>Vid psykisk ohälsa erbjuder vi kartläggning, bedömning och behandling, och minskar på
så sätt de negativa konsekvenserna för både arbetstagaren och arbetsgivaren.</p>

<p>Vid problem med alkohol, droger, läkemedel och spel hjälper vi till att identifiera
problemen och stödjer chefer i att samtala med medarbetare om dem. Vi erbjuder också
fördjupade utredningar och bedömningar, och ger vid behov kvalificerade behandlingar med
evidensbaserade metoder.</p>

<p>Vidare handleder och utbildar vi de nätverk som drabbas — anhöriga, vänner,
arbetskamrater och chefer.</p>
''',
    ),
    dict(
        slug='skadligt-bruk', label='Skadligt bruk på arbetsplatsen',
        h1='Skadligt bruk på arbetsplatsen',
        title='Alkohol, droger och spel på arbetsplatsen | KBT-Konsulterna Uppsala',
        desc='Stöd till arbetsgivare vid skadligt bruk av alkohol, läkemedel, droger och '
             'spel om pengar: policyarbete, samtalsstöd för chefer, utredning och behandling.',
        lede='Vi hjälper till att identifiera problemen och stödjer chefer i att samtala '
             'med medarbetare om dem.',
        people=['thomas-alm', 'angeli-holmstedt'],
        also=[('Rehabilitering', 'organisationer/rehabilitering/'),
              ('Skadligt bruk och beroende för privatpersoner', 'vuxna/beroende/'),
              ('Handledning och coaching', 'organisationer/handledning/')],
        body='''
<p>När spelande, alkohol eller läkemedel tappat sin ursprungliga funktion — glädjen,
förgyllandet av en god middag, lindringen av smärta — och i stället börjar skapa problem
och negativa konsekvenser, blir det problematiskt för individen själv, på arbetet, bland
vänner, i familjen och för barnen.</p>

<h2>Vad vi erbjuder arbetsgivare</h2>
<ul>
  <li>stöd till chefer inför och under det svåra samtalet med en medarbetare</li>
  <li>fördjupade utredningar och bedömningar kring skadligt bruk, beroende och
  överdrivet spelande om pengar</li>
  <li>kvalificerad behandling med evidensbaserade metoder som följer Socialstyrelsens
  rekommendationer</li>
  <li>handledning och utbildning till de nätverk som påverkas — anhöriga, vänner,
  arbetskamrater och chefer</li>
</ul>

<h2>Vår kompetens</h2>
<ul>
  <li>återfallsprevention</li>
  <li>motiverande samtal (MI)</li>
  <li>KBT-behandling vid alkohol, droger och spel om pengar</li>
  <li>mindfulnessbaserad återfallsprevention (MBRP)</li>
  <li>12-stegsbehandling / Minnesotamodellen, för olika typer av beroenden och för
  anhöriga</li>
</ul>

<p>Den fullständiga beskrivningen av hur vi arbetar kliniskt — riskbruk, skadligt bruk,
beroende och spelberoende — finns på sidan
<a href="{base}vuxna/beroende/index.html">skadligt bruk och beroende</a>.</p>
''',
    ),
    dict(
        slug='kontakt', label='Kontakt för uppdrag',
        h1='Kontakt för uppdrag',
        title='Kontakt för uppdrag, handledning och utbildning | KBT-Konsulterna',
        desc='Här kan företag och offentliga verksamheter kontakta oss för frågor om '
             'uppdrag, handledning, utbildning och samarbeten.',
        lede='Här kan företag och offentliga verksamheter höra av sig om uppdrag, '
             'handledning, utbildning och samarbeten.',
        people=[],
        also=[('Handledning och coaching', 'organisationer/handledning/'),
              ('Föreläsningar och utbildning', 'organisationer/utbildning/'),
              ('Alla medarbetare', 'medarbetare/index.html')],
        body='''
<h2>Vilka är vi?</h2>
<p>På KBT-Konsulterna arbetar en erfaren och kvalificerad grupp av legitimerade psykologer
och legitimerade psykoterapeuter. KBT-Konsulterna är ett paraplyföretag som vi äger
gemensamt, och inom ramen för det arbetar vi också i våra individuella aktiebolag —
något som är vanligt i branschen.</p>

<h2>Vilka har vi hjälpt?</h2>
<p>Vi har arbetat inom, varit konsulter för, gett utbildningar till och handlett många
olika verksamheter:</p>
<ul>
  <li>BUP</li>
  <li>primärvården</li>
  <li>psykiatrin</li>
  <li>behandlingshem och HVB</li>
  <li>universitet</li>
  <li>socialtjänst</li>
  <li>Statens institutionsstyrelse (SiS)</li>
  <li>skolor samt resurs- och specialskolor</li>
  <li>företagshälsovård</li>
</ul>

<h2>Var håller vi hus?</h2>
<p>Vår bas är i centrala Uppsala, där mottagningen ligger i Gårdshuset vid Slottskällan
på gångavstånd från Centralstationen. Där tar vi emot kunder och klienter — men vi
arbetar också online och hos arbetsgivare runt om i landet.</p>

<h2>Nå oss</h2>
<p>E-post: <a href="mailto:kontakt@kbt-konsulterna.se">kontakt@kbt-konsulterna.se</a><br>
Telefon: <a href="tel:+4618104044">018 – 10 40 44</a></p>
<p>Du kan också använda <a href="{base}kontakt/index.html">kontaktformuläret</a>. Vi
återkommer så snart vi har möjlighet.</p>
''',
    ),
]

# --------------------------------------------------------------------------
# The tree. Level-2 nodes with children render as section hubs; without
# children they render as ordinary articles.
# --------------------------------------------------------------------------
TREE = [
    dict(
        slug='vuxna', label='Vuxna', img='vuxna',
        children=[
            dict(
                slug='behandling', label='Psykologisk behandling',
                h1='Psykologisk behandling och terapi för vuxna',
                title='Psykologisk behandling och KBT för vuxna i Uppsala | KBT-Konsulterna',
                desc='KBT vid ångest, depression, stress, sömnproblem, trauma, sorg och '
                     'låg självkänsla. Legitimerade psykologer i Uppsala och online.',
                lede='Våra psykologer och psykoterapeuter har lång erfarenhet av att '
                     'behandla psykisk ohälsa i de flesta former. Du behöver inte ha en '
                     'diagnos, och du behöver inte veta vad problemet heter.',
                people=['angeli-holmstedt', 'thomas-alm', 'jens-karstrom', 'aksel-reppling'],
                body='''
<p>Psykisk ohälsa är något de flesta upplever någon gång i livet, och för en del pågår
det under lång tid och skapar stort lidande. Det som kännetecknar psykisk ohälsa är att
den påverkar välbefinnandet och försämrar livskvaliteten. Ibland handlar det om
tillfälliga besvär av oro, nedstämdhet eller sömnsvårigheter — andra gånger om en eller
flera diagnoser och svårare problem med ångest, depression, utmattning eller
alkohol.</p>

<p>Ibland upplever man ingen psykisk ohälsa alls, men vill ha en samtalspartner eller
stöd och vägledning kring sig själv, sina relationer eller andra utmaningar i livet. Du
är lika välkommen då.</p>

<h2>Varför KBT?</h2>
<p>Vi är specialister i kognitiv beteendeterapi, och våra legitimerade psykologer och
psykoterapeuter har lång erfarenhet av evidensbaserad behandling.</p>

<p>För oss är det viktigt att ge den behandling som utifrån dagens kunskap har största
möjliga effekt — inte den vi själva råkar gilla. Därför arbetar vi med KBT: den
innehåller många olika metoder och vilar på flera teoretiska modeller.</p>

<p>Det viktigaste med KBT är att den är evidensbaserad. Behandlingarna är framtagna och
prövade vetenskapligt, och vi vet därför i vilken grad de fungerar, hur de fungerar och
för vilka de fungerar. För många problemområden har KBT den största möjligheten att bota
och lindra psykologiskt lidande.</p>

<h2>Så arbetar vi</h2>
<p>Vi börjar med en gemensam bedömning och formulerar därefter en plan utifrån dina mål
och värderingar. För det mesta arbetar vi ”här och nu”, men om din tidigare historia
påverkar hur du mår i dag finns även den med i samtalen.</p>
''',
                children=V_BEHANDLING,
            ),
            dict(
                slug='parterapi', label='Parterapi',
                h1='Parterapi i Uppsala',
                title='Parterapi i Uppsala med IBCT | KBT-Konsulterna',
                desc='Evidensbaserad parterapi med IBCT för alla typer av par, oavsett '
                     'sexuell läggning och oavsett om ni lever tillsammans eller inte.',
                lede='Vi erbjuder evidensbaserad parterapi för alla typer av par, oavsett '
                     'sexuell läggning och oavsett om ni lever tillsammans eller inte.',
                people=['aksel-reppling'],
                also=[('Relationsproblem', 'vuxna/behandling/relationer/'),
                      ('Priser för parterapi', 'priser/index.html'),
                      ('Låg självkänsla', 'vuxna/behandling/sjalvkansla/')],
                body='''
<p>Terapiformen kan också användas vid konflikter mellan personer som inte lever som par
och som inte kan komma överens.</p>

<p>Ibland känner man att man fastnat i dåliga mönster, med tjat och tjafs om småsaker.
Kanske har intresset för varandra tunnats ut, och närheten som fanns från början saknas.
Kriser i livet, otrohet, ett livspussel med för lite tid tillsammans, oro för ekonomin,
alkoholproblem hos partnern, sexuella problem — det finns många påfrestningar som gör
kommunikationen allt sämre. Då kan man behöva hjälp utifrån.</p>

<h2>Vilken metod använder vi?</h2>
<p>Vi arbetar utifrån IBCT — Integrative Behavioral Couple Therapy — en evidensbaserad
form av KBT som syftar till att integrera förändringsarbete med acceptansstrategier.</p>

<p>Varför fortsätter vi att agera och kommunicera på vissa sätt, även när det utifrån sett
inte är särskilt hjälpsamt? Varför bråkar vi om och om igen om samma saker? Utifrån de
frågorna arbetar man med metoder för beteendeförändring — men lägger samtidigt till
acceptans och förståelse för sin partner. Acceptansen är en förutsättning för att
förändringarna ska bli bestående, och för att den känslomässiga närheten ska kunna
byggas upp igen.</p>

<h2>Hur går det till?</h2>
<p>Vid den första kontakten börjar vi vanligen med ett gemensamt samtal där ni tillsammans
beskriver den situation ni befinner er i. Det följs oftast av två individuella möten, för
bakgrund, problembeskrivning och målformulering. Därefter ses vi gemensamt igen för en
sammanfattning från psykologen, som beskriver hur den fortsatta behandlingen kan läggas
upp utifrån de mål ni formulerat.</p>

<p>En målsättning kan vara att stärka relationen — men den kan lika gärna vara att göra
ett bra avslut.</p>

<h2>Tider och pris</h2>
<p>Parterapi bokas i 60-minuterspass, eller som 2 × 45 minuter. Ofta behövs minst 60
minuter per besök. Se <a href="{base}priser/index.html">priser</a>.</p>
''',
            ),
            dict(
                slug='beroende', label='Skadligt bruk & beroende',
                h1='Skadligt bruk och beroende',
                title='Behandling vid alkohol, läkemedel, droger och spel | KBT-Konsulterna',
                desc='Bedömning och behandling vid riskbruk, skadligt bruk och beroende — '
                     'alkohol, läkemedel, droger och spel om pengar. Även stöd till anhöriga.',
                lede='Vi gör bedömningar och behandlingar med evidensbaserade metoder som '
                     'följer Socialstyrelsens rekommendationer. Du är välkommen även som '
                     'anhörig.',
                people=['thomas-alm', 'angeli-holmstedt'],
                also=[('Skadligt bruk på arbetsplatsen', 'organisationer/skadligt-bruk/'),
                      ('Stress och utmattning', 'vuxna/behandling/stress-utmattning/'),
                      ('Behandling vid NPF', 'vuxna/behandling/npf/')],
                body='''
<p>När spelande, alkohol eller läkemedel tappat sin ursprungliga funktion — glädjen,
förgyllandet av en god middag, lindringen av smärta — och mer och mer börjar skapa
problem och negativa konsekvenser, börjar det bli problematiskt. För dig själv, på
arbetet, i familjen, för barnen.</p>

<p>Vi har lång erfarenhet av att arbeta med personer som utvecklat problem med alkohol,
droger, läkemedel och spel. Vi tar emot dig som själv söker bedömning och behandling för
problem med alkohol och spel om pengar. I vissa fall tar vi också emot personer med
drogproblem eller läkemedelsberoende.</p>

<h2>Vår kompetens</h2>
<ul>
  <li>återfallsprevention</li>
  <li>motiverande samtal (MI)</li>
  <li>KBT-behandling vid alkohol, droger och spel om pengar</li>
  <li>mindfulnessbaserad återfallsprevention (MBRP)</li>
  <li>12-stegsbehandling / Minnesotamodellen, för olika typer av beroenden och för
  anhöriga</li>
</ul>

<h2>Alkohol</h2>
<p>För många är alkohol en del av livet som förgyller vardagen vid speciella tillfällen
och inte ställer till några problem. För andra kan alkohol innebära något helt annat: en
påverkan på uppväxten om en förälder haft alkoholproblem, en partner som dricker för
mycket, självmedicinering vid psykisk ohälsa, eller att man dricker för att våga
umgås.</p>

<h3>Frågor värda att ställa sig</h3>
<ul>
  <li>Har du blivit orolig eller fundersam över din alkoholkonsumtion?</li>
  <li>Funderar du på om du behöver en ”vit period”?</li>
  <li>Har du känt skuld över ditt drickande?</li>
  <li>Har personer i din omgivning reagerat?</li>
  <li>Har du — eller andra — lagt märke till att humöret förändrats, eller att
  prestationen sjunkit?</li>
  <li>Har relationerna till anhöriga, vänner eller arbetskamrater blivit ansträngda?</li>
  <li>Har konsumtionen gradvis ökat?</li>
</ul>

<h3>Riskbruk</h3>
<p>Med riskbruk menas en alkoholkonsumtion som på sikt kan leda till skador och problem.
Socialstyrelsen ändrade sina rekommendationer 2023: gränsen går vid 10 standardglas per
vecka, för såväl män som kvinnor. Som riskbruk räknas också intensivkonsumtion — 4
standardglas eller mer vid samma tillfälle, en gång i månaden eller oftare.</p>
<p>Ett standardglas motsvarar ungefär 33 cl starköl, 12–15 cl vin eller knappt 4 cl
sprit. Viktigt att veta är att det för en enskild person kan vara riskfyllt att dricka
mindre mängder än så.</p>

<h3>Skadligt bruk</h3>
<p>Med skadligt bruk menas att dricka så mycket att det kan leda till fysisk eller psykisk
ohälsa och till sociala problem — i familjen, på arbetet, i studierna. Att köra bil
påverkad, att komma för sent till eller stanna hemma från arbetet, att hamna i konflikter
med vänner och familj: det är exempel på varningstecken.</p>

<h3>Beroende</h3>
<p>När ett beroende har utvecklats har alkoholen gett sådana skador att den i allt högre
grad styr personens liv, och det är mycket svårt att med egen vilja minska eller sluta.
Tecken kan vara tankar som ofta kretsar kring alkohol, en längtan efter att dricka igen,
abstinenssymtom, toleransökning eller kontrollförlust.</p>

<h2>Spelberoende (hasardspelsyndrom)</h2>
<p>Att spela om pengar har blivit en allt vanligare del av kulturen, och vi möts dagligen
av reklam för olika spel. För de flesta håller sig spelandet inom rimliga gränser, men
drygt fyra procent av befolkningen mellan 16 och 84 år har någon form av spelproblem.</p>

<p>Ett utvecklat spelberoende liknar andra beroenden och påverkar både personen själv och
omgivningen. Tecken kan vara att man spelar för allt större summor, blir irriterad och
rastlös när man försöker sluta, är upptagen av speltankar, försöker spela tillbaka
förlorade pengar, spelar när man mår dåligt, eller ljuger för omgivningen om hur mycket
man spelar och förlorar.</p>

<h3>Hur behandlar vi spelproblem?</h3>
<ul>
  <li>med KBT och motiverande samtal</li>
  <li>med ett mindfulnessbaserat program</li>
  <li>på mottagningen i Uppsala eller via videosamtal</li>
  <li>med ett forskningsbaserat onlineprogram i kombination med samtal hos oss</li>
</ul>

<h2>En kartläggning som grund</h2>
<p>Tillsammans med oss kan du göra en grundläggande kartläggning av din konsumtion eller
ditt spelande: hur det uppstått, utvecklats och vidmakthållits, och vilka konsekvenser
det fått i ditt liv. Kartläggningen syftar också till att föreslå en behandling som
passar dig, om en sådan behövs. Vi behandlar såväl riskbruk som beroende.</p>

<h2>Anhöriga och vänner</h2>
<p>Att vara anhörig eller vän till någon som har problem med alkohol, droger, spel eller
psykisk ohälsa är för de flesta en stor stress. Många försöker i det längsta att hjälpa
på alla sätt de förmår, men når sällan ett varaktigt resultat, och känner sig förtvivlade
och maktlösa.</p>

<p>Många anhöriga far också illa av att se sin vän, partner, förälder eller sitt barn vara
destruktiv, må dåligt eller skada sig själv. Ibland är det så illa att man själv som
anhörig — och i värsta fall barnen i familjen — utsätts för psykisk eller fysisk
misshandel, övergrepp eller skadas på andra sätt. Många anhöriga får egna symtom: oro,
ångest, stressymtom, sömnproblem eller depression.</p>

<p>Vi har lång erfarenhet av att stödja och behandla anhöriga, genom råd och stöd, hjälp
med egen psykisk ohälsa, eller med andra behov som finns. Vi ger också råd, stöd och
handledning till arbetsgivare, socialtjänst och behandlingshem.</p>
''',
            ),
            dict(
                slug='utredning', label='Utredning & bedömning',
                h1='Neuropsykiatrisk utredning för vuxna i Uppsala',
                title='ADHD- och autismutredning för vuxna i Uppsala | KBT-Konsulterna',
                desc='Specialiserade neuropsykiatriska utredningar (NPF) för vuxna vid '
                     'misstanke om adhd eller autism — utan långa väntetider.',
                lede='Att genomgå en utredning är ofta ett viktigt steg mot en förklaring '
                     'till sina svårigheter — men också ett sätt att identifiera sina '
                     'styrkor.',
                people=['karin-holmstrom', 'elias-westerlund', 'barry-karlsson'],
                body='''
<p>Vi erbjuder specialiserade neuropsykiatriska utredningar för vuxna vid misstanke om
adhd eller autism, utan de långa väntetider som ofta finns i den offentliga vården.</p>

<p>Vårt mål är att ge dig ökad självkännedom och de verktyg du behöver för att skapa en
fungerande tillvaro — oavsett om det handlar om arbetsliv, studier eller livet i övrigt.
Våra legitimerade psykologer bedömer om symtomen uppfyller kriterierna för adhd, autism
(autismspektrumtillstånd) eller annan neuropsykiatrisk funktionsnedsättning.</p>

<h2>Varför en privat utredning?</h2>
<p>Många som vänder sig till oss söker en utredning utan de långa väntetiderna inom den
offentliga vården och psykiatrin. Vi erbjuder privata utredningar med hög klinisk kvalitet
i en trygg miljö centralt i Uppsala, och arbetar utifrån evidensbaserade metoder — med ett
bemötande präglat av respekt och av förståelse för att symtomen kan se olika ut hos olika
personer.</p>

<h2>Vanliga frågor</h2>

<h3>Kan jag utredas om jag samtidigt har ångest, depression eller utmattning?</h3>
<p>Ja, det går utmärkt. Det är mycket vanligt att vuxna som söker utredning hos oss
också kämpar med ångest, depression eller utmattning. Under utredningen gör vi en
differentialdiagnostisk bedömning av om symtomen beror på en underliggande NPF-diagnos,
på psykisk ohälsa eller på samsjuklighet — för att du ska få rätt behandling framåt.</p>

<h3>Hur vet jag om jag borde utredas som vuxen?</h3>
<p>Det kan vara värt att överväga om du under lång tid har känt att vardagen kräver
oproportionerligt mycket energi. Kanske har du alltid känt att du behöver anstränga dig
mer än andra för att få livet att fungera. Om du upplever inre stress, oförklarlig
trötthet, eller blir överväldigad av intryck och sociala krav så att livskvaliteten
påverkas, kan det finnas en neuropsykiatrisk förklaring värd att undersöka.</p>

<h3>Vad händer om utredningen visar att jag inte har adhd eller autism?</h3>
<p>En utredning är inte bara till för att ge en diagnos, utan för att förstå varför
vardagen inte fungerar som du önskar. Om kriterierna inte uppfylls hjälper vi dig att
tolka resultatet, och att se om det i stället handlar om exempelvis din kognitiva profil,
stress, depression eller andra faktorer. Målet är alltid att du efter en utredning ska ha
en tydligare karta över dina styrkor och utmaningar.</p>
''',
                children=V_UTREDNING,
            ),
            dict(
                slug='psykiatri', label='Psykiatrisk bedömning',
                h1='Psykiatrisk bedömning och behandling',
                title='Psykiatrisk bedömning och behandling i Uppsala | KBT-Konsulterna',
                desc='Kontakt med legitimerad specialistläkare i psykiatri för utredning, '
                     'bedömning och behandling — på mottagningen eller online.',
                lede='Vi erbjuder kontakt med psykiater — legitimerad specialistläkare i '
                     'psykiatri — för utredning, bedömning och behandling, vid både '
                     'fysiska besök och onlinebesök.',
                people=[],
                also=[('Behandling vid NPF', 'vuxna/behandling/npf/'),
                      ('Utredning och bedömning', 'vuxna/utredning/index.html'),
                      ('Psykologisk behandling', 'vuxna/behandling/index.html')],
                body='''
<p>Vi har ett nära samarbete med vår psykiater, och i vissa situationer har våra klienter
kontakt både med psykologen eller psykoterapeuten och med psykiatern.</p>

<h2>Vad psykiatern erbjuder</h2>
<ul>
  <li>bedömning och utredning av besvär</li>
  <li>diagnossättning och förslag på evidensbaserad, lämplig behandling</li>
  <li>rådgivning om medicinering med psykofarmaka</li>
  <li>behandling med psykofarmaka vid behov</li>
  <li>rådgivning om hur man går vidare, och om det finns andra behandlingsalternativ</li>
  <li>bedömning av redan insatt behandling, och förslag på alternativ vid biverkningar
  eller utebliven effekt</li>
  <li>anhörigsamtal</li>
  <li>utbildningar och föreläsningar</li>
</ul>

<p>Kombinationen av KBT och läkemedelsbehandling kan också innefatta sjukskrivning och
läkarutlåtande vid behov.</p>

<p>För att komma i kontakt med vår psykiater, hör av dig via
<a href="mailto:kontakt@kbt-konsulterna.se">e-post</a>.</p>
''',
            ),
        ],
    ),
    dict(
        slug='barn-och-ungdom', label='Barn & ungdom', img='barn',
        children=[
            dict(
                slug='behandling', label='Psykologisk behandling',
                h1='Psykologisk behandling för barn och ungdomar',
                title='KBT för barn och ungdomar i Uppsala | KBT-Konsulterna',
                desc='Psykologisk bedömning och evidensbaserad KBT-behandling för barn '
                     'och ungdomar i alla åldrar, i nära samarbete med vårdnadshavare.',
                lede='Vi erbjuder psykologisk bedömning och evidensbaserad KBT-behandling '
                     'för barn och ungdomar i alla åldrar.',
                people=['karin-holmstrom', 'aksel-reppling'],
                body='''
<p>Att ett barn eller en ungdom mår psykiskt dåligt kan visa sig på många olika sätt:
nedstämdhet, oro, ilska och irritation, svårigheter att sova, och olika kroppsliga
besvär.</p>

<p>De flesta besvär kan tas om hand i barnets närhet, tillsammans med föräldrar och andra
viktiga vuxna. Men ibland behövs professionell hjälp — och då är tröskeln hit låg. Du
behöver ingen remiss, och ni behöver inte veta på förhand vad problemet heter.</p>
''' + VARDNADSHAVARE,
                children=B_BEHANDLING,
            ),
            dict(
                slug='utredning', label='Utredning & bedömning',
                h1='Neuropsykiatrisk utredning för barn i Uppsala',
                title='ADHD-, autism- och IF-utredning för barn i Uppsala | KBT-Konsulterna',
                desc='Specialiserade neuropsykiatriska utredningar för barn och ungdomar '
                     'i Uppsala. Ingen remiss krävs, kort väntetid, skriftligt utlåtande.',
                lede='Som förälder kan det vara tungt att se sitt barn möta motgångar utan '
                     'att riktigt veta hur man bäst kan hjälpa till.',
                people=['karin-holmstrom', 'barry-karlsson'],
                body='''
<p>Upplever du att ditt barn kämpar mer än sina jämnåriga i skolan, hemma eller i sociala
sammanhang?</p>

<p>Vi erbjuder specialiserade neuropsykiatriska utredningar för barn och ungdomar, där
barnets behov och familjens situation står i centrum. En utredning är ofta nyckeln till
att förstå bakomliggande orsaker till utmaningar med koncentration, socialt samspel eller
inlärning. Genom att kartlägga barnets styrkor och svårigheter skapar vi förutsättningar
för rätt stöd i skolan, en mer harmonisk vardag hemma, och en stärkt självkänsla hos
barnet.</p>

<h2>Ingen remiss behövs</h2>
<p>Som privat mottagning kan ni söka er till oss direkt. Vi samarbetar gärna med barnets
skola eller andra vårdgivare om ni önskar det.</p>
''',
                children=B_UTREDNING,
            ),
            dict(
                slug='stod', label='Stöd till vuxna runt barnet',
                h1='Råd, stöd och handledning',
                title='Stöd till föräldrar, skola, HVB och socialtjänst | KBT-Konsulterna',
                desc='Rådgivande och handledande samtal till vårdnadshavare och till dem '
                     'som i sitt arbete möter barn och ungdomar.',
                lede='Att ta hand om och vägleda barn och ungdomar är ofta utmanande, och '
                     'ibland behöver den som har uppgiften en diskussionspartner.',
                people=['karin-holmstrom', 'aksel-reppling', 'barry-karlsson'],
                body='''
<p>Vi erbjuder rådgivande och handledande samtal både till vårdnadshavare och till
personer som i sitt arbete möter barn och ungdomar — i skolan, inom socialtjänsten, på
behandlingshem och i familjehem.</p>

<p>Ofta är det de vuxna runt barnet som har mest att vinna på stöd: det är där
strategierna finns, och det är där uthålligheten behöver komma ifrån.</p>
''',
                children=B_STOD,
            ),
        ],
    ),
    dict(
        slug='organisationer', label='För organisationer', img='org',
        children=ORG,
    ),
]
