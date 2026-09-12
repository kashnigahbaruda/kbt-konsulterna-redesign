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

<h2>Varför depression håller i sig</h2>
<p>Depression har en inbyggd logik som gör den svår att ta sig ur. När orken tryter drar
man ner på det som kräver något — träffa folk, träna, ta itu med det som skjutits upp.
Det är fullt rimligt i stunden, och samtidigt försvinner då också det som gav energi,
sammanhang och en känsla av att duga. Måendet sjunker ytterligare, orken blir mindre, och
man drar ner mer. Det är den nedåtgående spiralen behandlingen riktar sig mot.</p>

<h2>Så arbetar vi</h2>
<p>Vi börjar med en gemensam bedömning för att skilja depression från exempelvis
utmattningssyndrom, eftersom behandlingen skiljer sig åt. Därefter arbetar vi vanligen
med:</p>
<ul>
  <li><strong>Beteendeaktivering.</strong> Att stegvis och planerat föra tillbaka
  aktiviteter som ger mening eller tillfredsställelse — utifrån schema snarare än utifrån
  lust, eftersom lusten vid depression kommer efter aktiviteten, inte före den. Det är
  den enskilt mest studerade och verksamma delen.</li>
  <li><strong>Att arbeta med tankarna.</strong> Att känna igen grubblandet och de
  självkritiska slutsatserna, och att hitta ett annat sätt att förhålla sig till dem.</li>
  <li><strong>Sömn och rutiner</strong>, som nästan alltid behöver adresseras
  parallellt.</li>
  <li><strong>Återfallsprevention.</strong> Att i slutet av behandlingen kartlägga dina
  tidiga varningstecken och göra en konkret plan, eftersom depression för många är
  återkommande.</li>
</ul>

<h2>Läkemedel och KBT</h2>
<p>KBT och antidepressiva läkemedel är båda verksamma vid depression, och för många
fungerar de bra tillsammans. Vi samarbetar med en specialistläkare i psykiatri när
läkemedelsbedömning är aktuell — se
<a href="{base}vuxna/psykiatri/index.html">psykiatrisk bedömning</a>. Har du redan
medicinering hos din vårdcentral går det utmärkt att gå i behandling hos oss parallellt.</p>

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

<p>Det som ofta oroar mest är kognitionen: att inte hitta ord, tappa tråden, läsa samma
stycke tre gånger, glömma sådant man aldrig brukade glömma. Många tolkar det som att
något är allvarligt fel med hjärnan. Det är en väntad del av bilden vid utmattning, och
den delen brukar förbättras — men långsammare än man hoppas.</p>

<h2>Varför bedömningen kommer först</h2>
<p>Utmattningsdepression är en form av utmattningssyndrom, och begreppen används ibland
synonymt. Men det är viktigt att skilja mellan depression, utmattningssyndrom och
utmattningsdepression — framför allt för att behandlingen ser olika ut. Därför gör vi
alltid en noggrann bedömning innan behandlingen börjar.</p>

<p>Skillnaden är inte akademisk. Vid depression är beteendeaktivering — att stegvis göra
mer — en central del av behandlingen. Vid utmattning i ett tidigt skede kan samma
tillvägagångssätt förvärra tillståndet om det görs för fort. Ordningen och takten är en
del av behandlingen.</p>

<h2>Vad behandlingen innehåller</h2>
<ul>
  <li><strong>Kartläggning av belastning och återhämtning.</strong> Inte bara arbetet —
  också allt det andra som ska rymmas i ett dygn.</li>
  <li><strong>Återhämtning som planeras.</strong> Vila som ligger i schemat, inte vila
  som blir över.</li>
  <li><strong>Sömnen</strong>, som nästan alltid är påverkad och ofta behandlas
  parallellt. Se <a href="{base}vuxna/behandling/somn/">sömnproblem</a>.</li>
  <li><strong>Krav och gränser.</strong> Andras krav — och de egna, som ofta är
  hårdare.</li>
  <li><strong>Värderingar.</strong> Vad belastningen ska vara till för, och vad som kan
  få ta mindre plats.</li>
  <li><strong>Stegvis återgång.</strong> Att bygga upp aktivitet och arbetstid i en takt
  som håller, i samverkan med arbetsgivare och företagshälsovård när det är aktuellt.</li>
</ul>

<h2>Sjukskrivning</h2>
<p>Vissa behöver vara sjukskrivna en period, andra klarar sig med anpassningar och
fortsätter arbeta. Båda vägarna kan vara rätt. Vi utfärdar inte sjukintyg som psykologer,
men samarbetar med en specialistläkare i psykiatri när läkarbedömning, intyg eller
läkemedel behövs — se <a href="{base}vuxna/psykiatri/index.html">psykiatrisk
bedömning</a>.</p>

<p>Är det din arbetsgivare som vill ordna insatsen, se
<a href="{base}organisationer/rehabilitering/">rehabilitering</a>.</p>

<h2>Hur lång tid tar det?</h2>
<p>Utmattning läker långsamt, och de flesta underskattar hur långsamt. Samtidigt går det
oftast att märka en riktning redan tidigt — i sömn, i tålamod, i hur lång stunden är
innan man är slut. Vi stämmer av regelbundet att behandlingen går åt rätt håll och att
takten är rimlig.</p>
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

<p>Det som gör insomni svår att ta sig ur på egen hand är att de lösningar som ligger
närmast till hands ofta förvärrar problemet. Man går och lägger sig tidigare för att
försöka få igen förlorad sömn, ligger kvar på morgonen, sover middag, drar ner på det som
är ansträngande. Var och en av de sakerna är begriplig — och tillsammans försvagar de
kopplingen mellan sängen och sömnen.</p>

<h2>Sällan ensamt</h2>
<p>Sömnlöshet förekommer ofta tillsammans med annat — depression, stress och utmattning,
skadligt bruk eller ångest. Därför gör vi en helhetsbedömning: en kartläggning av
sömnen tillsammans med eventuella andra besvär, som grund för en individuell
behandlingsplan.</p>

<h2>Varför KBT och inte sömntabletter?</h2>
<p>KBT vid insomni — ofta förkortat KBT-i — rekommenderas i dag som förstahandsval vid
långvariga sömnbesvär, före sömnläkemedel. Skälet är att effekten håller i sig efter att
behandlingen avslutats, medan sömnmedel verkar så länge man tar dem och för många blir
svåra att sluta med.</p>

<p>Det betyder inte att läkemedel är fel. Om du använder sömnmedel i dag går det bra att
göra behandlingen ändå. En eventuell nedtrappning planeras alltid tillsammans med den
läkare som skrivit ut dem — aldrig på egen hand och aldrig som ett krav från oss.</p>

<h2>Vad behandlingen innehåller</h2>
<ul>
  <li><strong>Sömndagbok.</strong> Vi börjar med att kartlägga hur du faktiskt sover under
  ett par veckor. Bilden blir nästan alltid en annan än den man bär med sig.</li>
  <li><strong>Sömnrestriktion.</strong> Att under en period korta ner tiden i sängen så att
  den motsvarar den sömn du får. Det låter bakvänt och är krävande de första veckorna, men
  det är den enskilt mest verksamma delen. Metoden passar inte alla, och vi bedömer alltid
  lämpligheten först.</li>
  <li><strong>Stimuluskontroll.</strong> Att återupprätta kopplingen mellan säng och sömn —
  sängen används för att sova i, inte för att ligga vaken och oroa sig i.</li>
  <li><strong>Att hantera tankarna.</strong> Oro för sömnen håller i sig sömnlösheten. Vi
  arbetar med grubblandet och med katastroftankarna om hur i morgon ska gå.</li>
  <li><strong>Sömnvanor och dygnsrytm.</strong> Ljus, motion, koffein, alkohol och
  regelbundenhet — men som ett komplement, inte som behandlingen i sig.</li>
</ul>

<h2>Hur lång tid tar det?</h2>
<p>Rena sömnbesvär kan ofta behandlas relativt snabbt; ett vanligt upplägg är en handfull
samtal. Behandlingstiden blir längre om det finns fler problem med i bilden — vid samtidig
depression eller utmattning arbetar vi vanligen med sömnen parallellt med det andra.</p>

<h2>Vanliga frågor</h2>

<h3>Fungerar behandlingen via video?</h3>
<p>Ja. Sömnbehandling lämpar sig väl för videosamtal, eftersom arbetet till stor del bygger
på dagboken och på det du provar hemma mellan samtalen.</p>

<h3>Måste jag sluta med mina sömntabletter först?</h3>
<p>Nej. Många börjar behandlingen med pågående medicinering, och en eventuell nedtrappning
kommer senare och alltid i samråd med förskrivande läkare.</p>

<h3>Blir jag tröttare innan jag blir bättre?</h3>
<p>Under de första veckorna av sömnrestriktion brukar dagtröttheten öka innan sömnen börjar
bli djupare och mer sammanhållen. Det är väntat, du får veta det i förväg, och vi planerar
när i ditt liv det passar att göra den delen.</p>
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

<p>Många beskriver också påträngande minnen som kommer utan förvarning, mardrömmar, och
en känsla av att återuppleva händelsen snarare än att minnas den. Sömnen är nästan alltid
påverkad. Det är vanligt att skämmas över sina reaktioner och att tolka dem som svaghet.
De är i stället väntade följder av något som hjärnan inte hunnit bearbeta.</p>

<h2>Varför besvären håller i sig</h2>
<p>Undvikande är det som mest effektivt håller kvar posttraumatisk stress. Att hålla sig
borta från platser, samtal, tankar och känslor som påminner ger lättnad i stunden, och
gör samtidigt att minnet aldrig får chansen att bearbetas och läggas till rätta bland
andra minnen. Det är därför behandlingen går i motsatt riktning mot det som känns
naturligt — och därför den fungerar.</p>

<h2>Hur vi behandlar</h2>
<p>Vi arbetar med evidensbaserad KBT vid PTSD, bland annat prolonged exposure (PE),
schematerapi och ACT. Behandlingen går i din takt, och exponeringen sker planerat och
med stöd — aldrig oförberett.</p>

<p>Ett vanligt upplägg innehåller:</p>
<ul>
  <li><strong>Psykoedukation.</strong> Att förstå vad som händer i kroppen och varför
  reaktionerna ser ut som de gör. För många är det i sig en lättnad.</li>
  <li><strong>Andnings- och nedvarvningsteknik</strong>, som något att ha med sig.</li>
  <li><strong>Exponering in vivo.</strong> Att stegvis återta platser och situationer som
  undvikits men som i dag är ofarliga, enligt en plan ni gör tillsammans.</li>
  <li><strong>Imaginativ exponering.</strong> Att gå igenom minnet i trygg miljö, med
  psykologen närvarande, tillräckligt många gånger för att det ska förlora sin laddning
  och bli ett minne bland andra.</li>
  <li><strong>Bearbetning av slutsatserna.</strong> Det trauman ofta lämnar efter sig är
  inte bara rädsla utan övertygelser — att det var mitt fel, att jag borde ha gjort
  annorlunda, att ingen går att lita på. De arbetar vi med särskilt.</li>
</ul>

<h2>Vanliga frågor</h2>

<h3>Måste jag berätta allt?</h3>
<p>Du bestämmer takten, och ingenting sker oförberett. Samtidigt är kärnan i behandlingen
att stegvis närma sig det som undviks, och det arbetet börjar vi inte förrän du känner
dig trygg med både metoden och med psykologen.</p>

<h3>Kan jag må sämre av behandlingen?</h3>
<p>Det är vanligt att må något sämre under en period när exponeringen börjar, innan det
vänder. Du får veta det i förväg, vi följer det noga, och vi lägger upp arbetet så att du
har återhämtning omkring det.</p>

<h3>Hur många samtal handlar det om?</h3>
<p>Traumabehandling vid en avgränsad händelse rör sig ofta om ett begränsat antal samtal.
Har du varit utsatt under lång tid, eller under uppväxten, tar det längre tid och inleds
vanligen med ett stabiliserande arbete först.</p>

<h3>Tar ni emot remisser?</h3>
<p>Jens Karström, leg. psykolog, leg. psykoterapeut och specialist i klinisk psykologi,
arbetar särskilt med trauma och tar emot remisser från Regionen.</p>
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

<h2>Sorg tar sig fler uttryck än ledsenhet</h2>
<p>Många blir förvånade över hur mycket annat än sorgsenhet som ryms i en sorg. Det är
vanligt med ilska — mot vården, mot omgivningen, mot den som dött. Med skuld över det
man sade eller inte hann säga. Med lättnad, om det föregåtts av lång sjukdom, och med
skam över den lättnaden. Kroppen är ofta med: trötthet, orolig mage, att man inte kan
sova eller inte kan göra annat än sova. Koncentrationen och minnet sviktar.</p>

<p>Sorg går sällan i prydliga faser, och den kommer ofta i vågor som utlöses av små
saker långt efter att omgivningen slutat fråga. Inget av det betyder att något gått
fel.</p>

<h2>När sorgen fastnar</h2>
<p>För de flesta blir sorgen med tiden möjlig att bära, utan att den för den skull
försvinner. För en del gör den inte det. Tecken på att sorgeprocessen kört fast kan vara
att längtan efter den som dött är lika intensiv efter lång tid, att man undviker allt som
påminner, eller tvärtom inte kan göra något annat än att söka sig till påminnelserna —
att livet i praktiken har stannat.</p>

<p>Då finns hjälp att få. Behandlingen handlar inte om att sluta sörja eller att gå
vidare, utan om att kunna leva med förlusten: att våga närma sig det som undviks, att
hitta tillbaka till sammanhang och aktiviteter som betyder något, och att ge sorgen en
plats i livet i stället för hela utrymmet.</p>

<h2>Hos oss</h2>
<p>Vi tar emot både dig som vill prata av dig med en medmänniska och dig som vill ha
behandling. Det första samtalet syftar bland annat till att skilja de två sakerna åt —
ibland är det stöd under en period som behövs, inte terapi.</p>

<p>Barry Karlsson, leg. psykolog och specialist i neuropsykologi, forskar om förlust och
komplicerad sorg vid Uppsala universitet.</p>

<p>Sorg och depression överlappar, men är inte samma sak och behandlas delvis olika. Om
du känner igen dig mer i beskrivningen av
<a href="{base}vuxna/behandling/depression/">nedstämdhet och depression</a> kan den sidan
passa bättre. Har förlusten skett plötsligt eller under skrämmande omständigheter kan
<a href="{base}vuxna/behandling/trauma-ptsd/">trauma och PTSD</a> vara mer relevant.</p>
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

<h2>Självkänsla och självförtroende är inte samma sak</h2>
<p>Självförtroende handlar om vad du tror att du klarar av — det kan vara högt inom något
område och lågt inom ett annat. Självkänsla handlar om vad du är värd oavsett vad du
presterar. Det är fullt möjligt att vara skicklig, uppskattad och framgångsrik och ändå
bära på en grundkänsla av att inte duga. Många som söker hjälp hos oss beskriver just
det, och blir förvånade över att det går att skilja på de två sakerna.</p>

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

<h2>Varför det håller i sig</h2>
<p>En negativ självbild är svår att motbevisa, eftersom den påverkar vad man gör. Tror du
att du är ointressant håller du dig i bakgrunden, och då får du sällan erfarenheter som
säger något annat. Presterar du för att slippa känna dig otillräcklig, och det går bra,
är det lätt att tänka att det berodde på ansträngningen snarare än på dig. På så vis blir
varje utfall en bekräftelse. Det är det mönstret behandlingen riktar sig mot — inte
tanken i sig.</p>

<h2>Så arbetar vi</h2>
<ul>
  <li><strong>Kartläggning.</strong> Vilka situationer väcker självkritiken, vad gör du då,
  och vad blir konsekvensen på kort och lång sikt?</li>
  <li><strong>Beteendeexperiment.</strong> Att pröva att göra tvärtom — säga vad du tycker,
  lämna in något som inte är perfekt, be om hjälp — och se vad som faktiskt händer. Det är
  erfarenheten, inte argumentet, som förändrar en grundläggande uppfattning.</li>
  <li><strong>Att arbeta med självkritiken.</strong> Att känna igen den inre rösten och möta
  den med något annat än att antingen tro på den eller bråka med den.</li>
  <li><strong>Att sluta undvika.</strong> Perfektionism och undvikande är två sidor av
  samma sak, och båda behöver minska för att bilden av dig själv ska kunna ändras.</li>
  <li><strong>Värderingar.</strong> Vad vill du använda ditt liv till, om du slutar
  använda det till att bevisa något?</li>
</ul>

<h2>Hur lång tid tar det?</h2>
<p>Självkänsla förändras långsammare än exempelvis en fobi, eftersom det handlar om
antaganden som byggts upp under lång tid. Samtidigt märks ofta en skillnad i hur du
handlar långt innan känslan hunnit ikapp — och det är den ordningen som gäller: först
gör man annorlunda, sedan känns det annorlunda.</p>

<p>Låg självkänsla förekommer ofta tillsammans med
<a href="{base}vuxna/behandling/depression/">nedstämdhet</a>,
<a href="{base}vuxna/behandling/oro-angest/">social ångest</a> eller
<a href="{base}vuxna/behandling/stress-utmattning/">utmattning</a>. Vi börjar alltid med
en gemensam bedömning av vad som är mest angeläget att arbeta med först.</p>
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

<h2>Mönster som går igen</h2>
<p>Många som söker för relationsproblem känner igen sig i att samma sak upprepas, med
olika människor. Några vanliga mönster:</p>
<ul>
  <li><strong>Att ge efter.</strong> Att säga ja när du menar nej, tills irritationen
  samlas och kommer ut på fel sätt eller mot fel person.</li>
  <li><strong>Att dra sig undan.</strong> Att hantera konflikt genom att tystna eller gå
  därifrån, vilket dämpar obehaget i stunden och gör att inget löses.</li>
  <li><strong>Att kräva och kontrollera.</strong> Att försöka få trygghet genom att söka
  bekräftelse eller genom att styra, vilket ofta ger kortvarig lättnad och långsiktigt
  avstånd.</li>
  <li><strong>Att välja bort.</strong> Att avsluta relationer vid första besvikelsen,
  innan det blir för nära.</li>
</ul>
<p>Mönstren är sällan dumma val. De har oftast fungerat någon gång, i något sammanhang.
Frågan behandlingen ställer är om de fungerar nu.</p>

<h2>Är relationsproblem en diagnos?</h2>
<p>Nej — men man kan uppleva problem i relationer inom ramen för många diagnoser, till
exempel:</p>
<ul>
  <li>vid social ångest</li>
  <li>vid depression</li>
  <li>vid adhd eller add</li>
  <li>vid autismspektrumtillstånd</li>
</ul>

<h2>Så arbetar vi</h2>
<p>Vi börjar med att kartlägga konkreta situationer: vad hände, vad tänkte och kände du,
vad gjorde du, och hur blev det sedan? Utifrån det arbetar vi med färdigheter som går att
öva — att säga vad du vill ha utan att anklaga, att stå kvar i en konflikt utan att
eskalera eller fly, att sätta en gräns och stå för den, och att stå ut med det obehag som
uppstår när du gör något annat än vanligt.</p>

<p>Vi arbetar också med vad du vill med dina relationer. Det är en annan fråga än vad som
skaver i dem, och den är ofta lättare att hålla fast vid när det blir svårt.</p>

<h2>Enskilt eller tillsammans?</h2>
<p>Den här sidan handlar om samtal där du kommer ensam — och det går utmärkt att arbeta
med en relation även om den andra personen inte är med. Är ni två som vill komma
tillsammans arbetar vi med <a href="{base}vuxna/parterapi/">parterapi</a>. Den
terapiformen fungerar också vid konflikter mellan personer som inte lever som par, till
exempel föräldrar som separerat eller kollegor som inte kan komma överens.</p>

<p>Handlar svårigheterna framför allt om relationen till dig själv är
<a href="{base}vuxna/behandling/sjalvkansla/">låg självkänsla</a> ofta en mer träffsäker
ingång.</p>
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

<h2>Varför undvikandet håller rädslan vid liv</h2>
<p>Varje gång du undviker det du är rädd för sjunker obehaget omedelbart. Den lättnaden
är en belöning, och den lär hjärnan att undvikandet var det som räddade dig. Slutsatsen
blir att faran var verklig — och nästa gång blir steget ännu svårare att ta. Det är den
mekaniken behandlingen bryter, och den är densamma oavsett vad fobin gäller.</p>

<h2>Exponering i praktiken</h2>
<p>Ni börjar med att tillsammans göra en trappa, från det som väcker lite obehag till det
som känns omöjligt. Sedan arbetar ni er uppåt, ett steg i taget, och stannar kvar i varje
steg tillräckligt länge för att obehaget ska hinna sjunka av sig självt medan du är kvar
i situationen. Det är den erfarenheten — att ångesten går ner utan att du flyr — som
förändrar saken.</p>

<p>Du bestämmer takten, och inget sker överraskande. Psykologen är med, och vid flera
specifika fobier går en stor del av behandlingen ut på att göra sakerna tillsammans i
verkligheten snarare än att prata om dem.</p>

<h2>Blod-, spruts- och skadefobi</h2>
<p>Blod- och sprutfobi skiljer sig från andra fobier: många svimmar eller är rädda för
att svimma, eftersom blodtrycket sjunker i stället för att stiga. Där kompletteras
exponeringen med <em>applied tension</em> — en teknik där du spänner stora muskelgrupper
för att hålla uppe blodtrycket, så att du kan genomföra exponeringen utan att svimma.
Det är en av anledningarna till att det är värt att söka hjälp i stället för att träna på
egen hand.</p>

<h2>Flygfobi</h2>
<p>Rädslan för att flyga kan kännas logisk med tanke på hur starkt man tror på en möjlig
katastrof. Vanliga föreställningar är att man ska svimma, bli så rädd att man dör i en
hjärtinfarkt, få panik och tappa kontrollen, eller att planet ska råka ut för en incident
eller störta.</p>

<p>Under analysfasen får du redogöra för din flygrädsla och för vad du tror kommer att
hända under en flygning. Under behandlingsfasen får du, via exponering, möjlighet att på
ett kontrollerat sätt utmana de katastroftankarna under en flygning tillsammans med
terapeuten.</p>

<p>För en del handlar flygrädslan egentligen om det instängda utrymmet, för andra om
höjden, om att tappa kontrollen eller om att få en panikattack inför andra. Vad rädslan
faktiskt gäller påverkar hur behandlingen läggs upp, och det är en av de första sakerna
vi tar reda på.</p>

<h2>Evidensen bakom</h2>
<p>Exponeringsbehandling vid fobier har säkrad evidens och hör till de mest verksamma
behandlingar som finns inom psykologin. Behandlingsupplägget vid flygfobi bygger på
forskningen om andra specifika fobier — blodfobi, klaustrofobi, injektionsfobi samt orm-
och spindelfobi — där exponering genomgående ger goda resultat.</p>

<h2>Hur lång tid tar det?</h2>
<p>Avgränsade specifika fobier är bland de tillstånd som går snabbast att behandla, och
det rör sig ofta om ett fåtal samtal. Finns flera fobier samtidigt, eller
<a href="{base}vuxna/behandling/oro-angest/">panikångest eller social ångest</a> i botten,
tar det längre tid — och då är det oftast det bredare ångesttillståndet vi arbetar
med.</p>
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

<h2>Det som kommer ovanpå</h2>
<p>Mycket av det som är tyngst att bära vid en NPF-diagnos i vuxen ålder är inte
funktionsnedsättningen i sig, utan det som lagt sig ovanpå den under åren: en
grundläggande känsla av att vara sämre, av att ha misslyckats med sådant som andra
verkar klara utan ansträngning, och en trötthet efter att länge ha kompenserat i det
tysta. Den delen går att behandla, oavsett hur svårigheterna i grunden ser ut.</p>

<h2>Vad behandlingen kan innehålla</h2>
<ul>
  <li><strong>Struktur och strategier.</strong> Konkreta sätt att komma igång, hålla
  ordning, planera tid och avsluta det som påbörjats — anpassade efter hur just du
  fungerar, inte efter hur ett schema borde se ut.</li>
  <li><strong>Känsloreglering.</strong> Att känna igen och hantera starka känslor innan
  de tar över, och att återhämta sig snabbare när de gjort det.</li>
  <li><strong>Självkänsla.</strong> Att arbeta med den inre kritiken efter år av
  tillsägelser och jämförelser.</li>
  <li><strong>Sömn och dygnsrytm.</strong> Sömnsvårigheter är mycket vanliga vid adhd och
  autism och förvärrar nästan allt annat.</li>
  <li><strong>Överbelastning och återhämtning.</strong> Särskilt vid autism — att
  planera in vila från intryck och sociala krav innan utmattningen är ett faktum.</li>
  <li><strong>Ångest och nedstämdhet</strong>, som ofta finns med i bilden och behandlas
  parallellt.</li>
</ul>

<h2>Terapin anpassas</h2>
<p>KBT fungerar väl vid NPF, men behöver ofta läggas upp annorlunda: tydligare ramar,
konkreta exempel i stället för resonemang, skriftliga sammanfattningar att ta med sig,
kortare eller färre moment per samtal, och hemuppgifter som är utformade för att faktiskt
bli gjorda. Det är vårt jobb att anpassa formen — inte ditt att passa in i den.</p>

<h2>Med eller utan diagnos</h2>
<p>Du är välkommen hit både med och utan färdig utredning. Vill du veta om kriterierna är
uppfyllda erbjuder vi <a href="{base}vuxna/utredning/index.html">neuropsykiatrisk
utredning för vuxna</a>. Vill du ha behandling och anpassat stöd utifrån de svårigheter
du redan känner igen, går det lika bra att börja där — en diagnos är inget krav för att
få hjälp med det som är svårt.</p>

<p>Har du en diagnos som inte längre känns rätt finns också
<a href="{base}vuxna/utredning/omprovning/">omprövning av diagnos</a>.</p>

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

<h2>Vilka söker omprövning?</h2>
<ul>
  <li>Du som fick en diagnos som barn och inte känner igen dig i den som vuxen.</li>
  <li>Du som söker till polisutbildning, militärtjänstgöring, flygutbildning eller ett
  annat yrke med särskilda hälsokrav.</li>
  <li>Du som utreddes under en period då du samtidigt hade en depression, en utmattning
  eller ett skadligt bruk, och undrar om bilden blev rättvisande.</li>
  <li>Du som behöver ett aktuellt underlag om din nuvarande funktionsnivå — för
  arbetsgivare, för studier eller för fortsatt vård.</li>
</ul>

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

<p>Omprövningen bygger på samma metodik som en förstagångsutredning — klinisk intervju,
standardiserade bedömningsinstrument och en genomgång av din utveckling och livshistoria
— men med tonvikt på nuläget: vilka svårigheter finns kvar, vilka har förändrats, och
vilken funktionsnivå har du i dag. Underlag från den tidigare utredningen är värdefullt
om du kan få tag på det, men inget krav.</p>

<h2>Vad utlåtandet säger</h2>
<p>Oavsett orsak får du efter utredningen med dig ett utlåtande som beskriver din
nuvarande funktion och om diagnosen fortfarande är aktuell. Önskar du omprövning i syfte
att söka till polisutbildning eller militärtjänstgöring är det viktigt att du meddelar
det — det ställer specifika krav på hur omprövningen ska gå till och på den efterföljande
dokumentationen.</p>

<h2>Bra att veta innan du bokar</h2>
<p>En omprövning är en förutsättningslös undersökning, inte ett uppdrag att komma fram
till ett bestämt svar. Utfallet kan bli att diagnosen kvarstår, att den inte längre är
uppfylld, eller att bilden har förändrats på ett sätt som behöver beskrivas i nyanser.
Vi kan inte veta i förväg vilket det blir, och vi lovar aldrig ett resultat.</p>

<p>En omprövning raderar inte heller din journalhistorik. Den beskriver hur din funktion
ser ut i dag, vilket är det myndigheter och arbetsgivare efterfrågar när de ska göra en
individuell lämplighetsprövning.</p>

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

<h2>Hur ångest ser ut i olika åldrar</h2>
<p>Yngre barn beskriver sällan att de är oroliga. I stället kommer det ut som ont i
magen eller huvudet, som svårigheter att somna, som klängighet, eller som ilska och
utbrott när de ska göra något de vill slippa. Skolbarn börjar kunna sätta ord på oron men
skäms ofta för den. Tonåringar kan beskriva den väl, och döljer den samtidigt effektivt
genom att helt enkelt avstå från saker och kalla det ointresse.</p>

<h2>Undvikande och trygghetsbeteenden</h2>
<p>Det som gör ångest svårare över tid är sällan rädslan i sig, utan allt man gör för att
slippa känna den: låta bli att gå på kalaset, be mamma svara i telefonen, kontrollera en
extra gång, sitta längst bak. Varje sådant undvikande ger lättnad direkt — och lär barnet
att det var undvikandet som gjorde det möjligt att klara sig. Nästa gång blir därför
svårare.</p>

<p>Som förälder dras man nästan alltid in i det, av kärlek och för att få lugn i stunden.
En viktig del av behandlingen handlar om att stegvis lämna över de trygghetsbeteendena,
utan att barnet känner sig lämnat.</p>

<h2>När skolan blir svår att gå till</h2>
<p>Ångest är en av de vanligaste orsakerna till att ett barn får allt svårare att komma
iväg till skolan. Frånvaron ger omedelbar lättnad och blir snabbt svårare att bryta ju
längre den pågått. Här är tidiga insatser särskilt viktiga, och samarbete med skolan
nästan alltid en del av arbetet.</p>

<h2>Så behandlar vi</h2>
<ul>
  <li><strong>Kartläggning.</strong> Vad är barnet rädd för, vad gör hen för att slippa,
  och vad gör ni som föräldrar?</li>
  <li><strong>Förståelse.</strong> Barnet och ni får lära er hur ångest fungerar — ofta
  med bilder och exempel — så att den blir begriplig i stället för läskig.</li>
  <li><strong>Stegvis exponering.</strong> En trappa av små, överenskomna utmaningar som
  barnet klarar och lyckas med, uppbyggd tillsammans med barnet självt.</li>
  <li><strong>Föräldrastöd.</strong> Hur ni uppmuntrar utan att pressa, och hur ni
  stegvis slutar hjälpa till med undvikandet.</li>
  <li><strong>Samarbete med skolan</strong> när det behövs, efter ert samtycke.</li>
</ul>

<h2>Vad ni kan göra som föräldrar</h2>
<p>Ta oron på allvar utan att bekräfta faran, och beröm modet snarare än resultatet — att
ha försökt är det som räknas. Undvik att lova att det obehagliga inte ska hända, och undvik
samtidigt att tvinga fram stora steg. Små steg som barnet varit med och bestämt fungerar
bättre än stora som bestämts över huvudet på hen.</p>

<h2>Hur lång tid tar det?</h2>
<p>Ångestbehandling för barn är ofta relativt kortvarig, särskilt vid avgränsade rädslor.
Är oron bred, har pågått länge eller finns tillsammans med
<a href="{base}barn-och-ungdom/behandling/depression/">nedstämdhet</a> eller
<a href="{base}barn-och-ungdom/behandling/ocd/">tvång</a> tar det längre tid.</p>
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

<h2>Det ser inte alltid ut som ledsenhet</h2>
<p>Hos barn och unga är irritation och ilska ofta mer framträdande än den nedstämdhet man
förväntar sig. Det gör att en depression ibland misstas för trots, lathet eller en jobbig
period. Andra vanliga tecken är att barnet drar sig undan från kompisar, tappar intresset
för fritidsaktiviteter, sover mycket mer eller mycket sämre än vanligt, får ont i magen
eller huvudet, eller att skolresultaten sjunker utan tydlig förklaring.</p>

<p>Hos yngre barn är kroppsliga besvär och klängighet vanligare. Hos tonåringar syns
oftare social tillbakadragenhet, sömn som vänts på dygnet, och en stark självkritik.</p>

<h2>Nedstämd eller deprimerad?</h2>
<p>Det finns ingen skarp gräns, men några saker talar för att det är mer än en svacka:
att det pågått ett par veckor eller mer, att det syns i flera delar av livet samtidigt —
skola, kompisar, hemma — och att barnet inte piggnar till ens av sådant som brukar
fungera. Då är det värt att göra en bedömning.</p>

<h2>Så arbetar vi</h2>
<ul>
  <li><strong>Bedömning.</strong> Vi kartlägger måendet, sömnen, skolan och relationerna,
  och tar reda på om det finns annat med i bilden — oro, tvång, eller en obemärkt
  inlärnings- eller koncentrationssvårighet som gjort skolan orimligt tung.</li>
  <li><strong>Beteendeaktivering.</strong> Att stegvis och planerat få tillbaka
  aktiviteter som ger energi och sammanhang. Vid depression kommer lusten efter
  aktiviteten, inte före — det är en av de viktigaste sakerna både barnet och ni får med
  er.</li>
  <li><strong>Sömn och dygnsrytm</strong>, som nästan alltid behöver adresseras
  parallellt.</li>
  <li><strong>Tankar och självkritik.</strong> Att känna igen de hårda slutsatserna om
  sig själv och att öva på ett annat sätt att möta dem.</li>
  <li><strong>Föräldrastöd.</strong> Hur ni stöttar utan att ta över, och hur ni orkar
  själva.</li>
  <li><strong>Skolan</strong>, efter ert samtycke, när kraven behöver anpassas under en
  period.</li>
</ul>

<h2>Vad ni kan göra som föräldrar</h2>
<p>Håll fast vid det lilla och vardagliga: mat, sömn, att komma ut, att någon finns kvar
i rummet. Sänk kraven tillfälligt utan att ta bort dem helt. Undvik att argumentera mot
de negativa tankarna — det leder sällan någon vart — och satsa hellre på att göra saker
tillsammans. Och ta hand om er själva; att leva nära ett barn som mår dåligt är
tungt.</p>

<h2>Om du är orolig för självmordstankar</h2>
<p>Fråga rakt ut. Att fråga ökar inte risken, och de flesta unga blir lättade över att
någon vågar. Får du ett ja, lämna inte barnet ensamt och sök hjälp direkt.</p>

<p>Vid fara för liv: ring <strong>112</strong>. Ni kan också ringa
<strong>1177</strong> för råd, eller söka barn- och ungdomspsykiatrisk akutmottagning där
ni bor. Se <a href="{base}akut-hjalp/index.html">akut hjälp</a>. Vi är en mottagning med
bokade tider och kan inte ta emot akut.</p>
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

<h2>Hur OCD visar sig hos barn</h2>
<p>Tvångshandlingarna är inte alltid synliga. Vid sidan av tvättande, kontrollerande och
ordnande finns mentala ritualer — att räkna, att upprepa ord tyst för sig själv, att i
huvudet gå igenom en händelse om och om igen för att försäkra sig om att inget hemskt
hänt. Ett vanligt tecken är också att barnet ställer samma fråga gång på gång och behöver
höra samma svar, eller att rutiner tar orimligt lång tid: läggningen drar ut, morgonen
går inte ihop, läxan skrivs om flera gånger.</p>

<p>Många barn skäms djupt över innehållet i sina tvångstankar och berättar därför inte
om dem. Att tankarna känns obehagliga och främmande är just det som kännetecknar dem —
de säger ingenting om barnet.</p>

<h2>När familjen dras in</h2>
<p>Nästan alla familjer hamnar med tiden i att hjälpa till med tvånget: svara på frågan
en gång till, tvätta extra, gå in i rummet i en viss ordning, vänta medan ritualen
genomförs. Det är begripligt — det ger lugn, och konflikten uteblir. Men det gör också
att tvånget får rätt, och det växer.</p>

<p>En central del av behandlingen är därför att ni som föräldrar, stegvis och planerat,
slutar delta i ritualerna. Det görs tillsammans med barnet och i en takt ni kommer
överens om — inte över en natt.</p>

<h2>Behandlingen: exponering med responsprevention</h2>
<p>KBT vid OCD bygger på exponering med responsprevention, ERP. Barnet närmar sig
stegvis det som väcker obehag — utan att utföra tvångshandlingen. Genom att stanna kvar i
obehaget får barnet erfarenheten att det klingar av av sig självt, och att det befarade
inte inträffar. Det är den erfarenheten, inte resonemanget, som får tvånget att släppa.</p>

<p>Vi gör det konkret och åldersanpassat: barnet får ofta göra tvånget till en egen
figur att bekämpa, ni bygger trappan tillsammans, och varje steg är något barnet varit
med och valt. ERP är en av de bäst dokumenterade behandlingarna som finns för barn.</p>

<h2>Hur lång tid tar det?</h2>
<p>Ett vanligt upplägg rör sig om ett antal samtal över några månader, med hemuppgifter
mellan gångerna — det är där det viktigaste arbetet sker. Många märker skillnad
förhållandevis tidigt, men behandlingen fortsätter tills tvånget släppt sitt grepp om
vardagen och ni har en plan för hur ni gör om det skulle komma tillbaka.</p>

<p>OCD förekommer ofta tillsammans med
<a href="{base}barn-och-ungdom/behandling/oro-angest/">annan oro och ångest</a>. Vi gör
alltid en bedömning av helheten först.</p>
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

<h2>Hur mycket sömn behövs?</h2>
<p>Sömnbehovet minskar med åldern och varierar mellan individer. Grovt räknat behöver
förskolebarn omkring 10–13 timmar, skolbarn ungefär 9–11 timmar och tonåringar omkring
8–10 timmar. Siffrorna är riktmärken, inte krav — ett barn som är piggt, fungerar i
skolan och är på gott humör sover sannolikt tillräckligt, även om timmarna är något
färre.</p>

<h2>Vanliga orsaker</h2>
<ul>
  <li><strong>Oro och ångest.</strong> Kvällen är ofta den stund på dygnet då tankarna
  får plats. Många barn med insomningssvårigheter är i själva verket oroliga barn.</li>
  <li><strong>Inlärda vanor.</strong> Att somna med en förälder i rummet, med tv eller i
  soffan gör det svårt att somna om vid nattliga uppvaknanden — som alla har, flera
  gånger per natt.</li>
  <li><strong>Oregelbundenhet.</strong> Mycket olika tider i veckan och på helgen ger en
  dygnsrytm som aldrig hinner sätta sig.</li>
  <li><strong>Skärmar och sena kvällar</strong>, framför allt det som är engagerande
  precis innan läggning.</li>
  <li><strong>NPF.</strong> Sömnsvårigheter är mycket vanliga vid adhd och autism.</li>
</ul>

<h2>Tonåringar och dygnsrytm</h2>
<p>I puberteten förskjuts dygnsrytmen biologiskt — det blir naturligt att somna och vakna
senare. Kombinerat med tidiga skolstarter ger det en kronisk sömnskuld som tas igen på
helgerna, vilket i sin tur förskjuter rytmen ytterligare. Att en tonåring inte kan somna
klockan tio är alltså ofta inte trots, utan biologi. Det går att arbeta med, men det
kräver en annan ansats än med yngre barn.</p>

<h2>Så arbetar vi</h2>
<p>Vi börjar med en kartläggning, ofta med sömndagbok under ett par veckor, och tar reda
på om sömnen är problemet eller ett symtom på något annat. Därefter arbetar vi med
regelbundna tider, med rutinerna kring läggning, med att barnet stegvis lär sig somna på
egen hand, och — när oron är drivkraften — med oron i sig.</p>

<p>Precis som all behandling av barn sker arbetet i nära samarbete med er som
vårdnadshavare, eftersom det är hemma på kvällarna som förändringen ska genomföras.</p>

<h2>Vad ni kan göra</h2>
<p>Håll ungefär samma tider även på helgerna. Låt den sista halvtimmen före läggning vara
förutsägbar och lugn, och lägg den utanför sängen om möjligt. Låt barnet somna på den
plats där det ska vakna. Och undvik att göra sömnen till en stridsfråga — ju mer
prestation, desto svårare blir det att somna.</p>

<p>Om oron är det som håller barnet vaket, se
<a href="{base}barn-och-ungdom/behandling/oro-angest/">oro, ängslan och ångest</a>. För
vuxna med långvariga besvär, se <a href="{base}vuxna/behandling/somn/">sömnproblem hos
vuxna</a>.</p>
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

<h2>Vad som ligger bakom</h2>
<p>Utmanande beteende är nästan alltid ett uttryck för att kraven i situationen är större
än barnets förmåga just då. Bakom kan ligga svårigheter att vänta, att byta aktivitet,
att hantera besvikelse, att förstå vad som förväntas, eller att sätta ord på det som
känns. Ofta finns också trötthet, hunger eller för många intryck med i bilden.</p>

<p>Det är sällan fråga om att barnet inte vill. Att utgå från att barnet gör så gott det
kan med de förmågor det har förändrar både vad man letar efter och vad man provar.</p>

<h2>Mönstret som byggs upp</h2>
<p>Utbrott har konsekvenser som gör att de upprepas. Om utbrottet gör att kravet
försvinner har det fungerat. Om det som fungerar för att få uppmärksamhet är att bråka,
medan det som fungerar dåligt är att göra rätt, blir slutsatsen begriplig. Samtidigt
hamnar familjen lätt i ett mönster där nästan all uppmärksamhet handlar om det som går
fel. Det är den balansen behandlingen arbetar med.</p>

<h2>Så arbetar vi</h2>
<ul>
  <li><strong>Beteendeanalys.</strong> Vad händer före, under och efter utbrotten? Ofta
  framträder ett tydligt mönster som går att förändra.</li>
  <li><strong>Föräldrastöd.</strong> Konkreta verktyg att öva på hemma — det är den mest
  verksamma insatsen vid utmanande beteende hos yngre barn.</li>
  <li><strong>Förutsägbarhet.</strong> Att förbereda övergångar och göra dagen begriplig,
  eftersom det mesta som utlöser utbrott är sådant som kommer oväntat.</li>
  <li><strong>Att förstärka det som fungerar.</strong> Att systematiskt lägga märke till
  och bekräfta det barnet gör bra, i stället för att enbart hantera det som går fel.</li>
  <li><strong>Lågaffektivt bemötande.</strong> Hur ni möter ett barn i affekt utan att
  trappa upp, och hur ni tar samtalet efteråt i stället för mitt i.</li>
  <li><strong>Färdighetsträning med barnet</strong>, anpassad efter ålder — att känna igen
  ilskan tidigare och att hitta något annat att göra med den.</li>
</ul>

<h2>Vad ni kan göra</h2>
<p>Förbered övergångar i förväg. Ge ett val i stället för en order när det går. Undvik att
förhandla eller resonera mitt i ett utbrott — då är förmågan att tänka tillfälligt
borta. Och satsa på att öka andelen stunder som är positiva; det gör mer för samarbetet
än fler konsekvenser gör.</p>

<h2>När det kan finnas något mer bakom</h2>
<p>Ihållande svårigheter med impulskontroll, med att vänta eller med att klara
förändringar kan ibland ha en neuropsykiatrisk förklaring. Om bilden pekar åt det hållet
kan en <a href="{base}barn-och-ungdom/utredning/index.html">utredning</a> vara nästa steg
— men behandling och föräldrastöd kan påbörjas oavsett, och kräver ingen diagnos.</p>
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

<h2>Vad samtalen kan handla om</h2>
<ul>
  <li>Konkreta situationer som återkommer — morgnar, läggning, läxor, skärmar,
  konflikter mellan syskon.</li>
  <li>Hur ni förhåller er till ett barn som är oroligt, nedstämt eller argt.</li>
  <li>Hur ni pratar med barnet om något svårt: en separation, en sjukdom, ett dödsfall.</li>
  <li>Att ni som föräldrar gör olika och drar åt olika håll.</li>
  <li>Om det ni ser är skäl att söka hjälp, och i så fall var.</li>
  <li>Ert eget mående. Att leva nära ett barn som har det svårt tär, och det är inte
  själviskt att ta hand om sig själv också.</li>
</ul>

<h2>Föräldrastöd är ofta behandlingen</h2>
<p>Vid yngre barn och vid utmanande beteende är arbete med föräldrarna inte ett komplement
till behandlingen — det är den mest verksamma delen av den. Det är hemma, i vardagen, som
mönstren finns och som förändringen ska ske, och ni är de som är där. Ofta räcker ett
begränsat antal samtal med er för att en situation ska vända, utan att barnet behöver gå
i egen behandling.</p>

<h2>Ni behöver inte ha ett barn i behandling hos oss</h2>
<p>Många hör av sig för att de är oroliga och vill resonera med någon, utan att barnet är
patient någonstans. Det går utmärkt. Ni behöver ingen remiss, och ett samtal kan lika
gärna landa i att det ni redan gör är rätt.</p>

<h2>Att vara anhörig</h2>
<p>Vi tar också emot anhöriga i vidare mening — mor- och farföräldrar, bonusföräldrar,
vuxna syskon. Är du anhörig till någon med skadligt bruk eller beroende finns särskild
erfarenhet av det hos oss; se <a href="{base}vuxna/beroende/index.html">skadligt bruk och
beroende</a>.</p>

<h2>Praktiskt</h2>
<p>Samtalen sker på mottagningen i centrala Uppsala eller via video. Ni kan komma en och
en eller tillsammans — vid gemensam vårdnad är det ofta värdefullt att båda är med, men
det är inget krav för att boka. Aksel Reppling och Angeli Holmstedt arbetar särskilt med
föräldra- och anhörigstöd.</p>
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
  <li><strong>Hälsofrämjande och förebyggande arbete</strong> — att bygga en skolmiljö
  som fungerar för fler elever, innan enskilda ärenden uppstår.</li>
  <li><strong>Åtgärdande arbete för enskilda elever</strong> — konsultation i ett
  specifikt ärende, som underlag för era beslut om anpassningar och stöd.</li>
  <li><strong>Personalhandledning</strong>, enskilt eller i grupp — för arbetslag,
  elevhälsoteam eller resurspersonal.</li>
  <li><strong>Skolpsykologiskt utredningsarbete</strong> — inklusive bedömning av
  intellektuell funktionsnivå, som ofta är avgörande för att förstå varför en elev inte
  når målen trots ansträngning.</li>
  <li><strong>Fortbildning</strong> för personalgrupper om exempelvis neuropsykiatriska
  funktionsnedsättningar, utmanande beteende, skolfrånvaro eller bemötande.</li>
</ul>

<p>Vi är väl förtrogna med både personalhandledning och skolpsykologiskt
utredningsarbete, och kan utgöra en stabil stöttepelare för er i dessa frågor.</p>

<h2>Vanliga frågeställningar</h2>
<p><strong>Skolfrånvaro.</strong> Frånvaro som börjat krypa uppåt är svårare att vända ju
längre den pågår. Bakom ligger ofta oro, social rädsla eller en skolsituation där kraven
inte motsvarar elevens förutsättningar. Vi hjälper er kartlägga vad som upprätthåller
frånvaron och lägga en plan för stegvis återgång.</p>

<p><strong>NPF i klassrummet.</strong> Hur anpassningar utformas så att de faktiskt
används, hur lektionsstruktur och övergångar kan se ut, och hur personalen möter en elev
i affekt utan att situationen trappas upp.</p>

<p><strong>Elever som inte når målen.</strong> När insatserna prövats utan effekt behövs
ibland en bedömning av vilka kognitiva förutsättningar som finns, för att kravnivån ska
kunna läggas rätt. Se
<a href="{base}barn-och-ungdom/utredning/intellektuell-funktion/">utredning av
intellektuell funktion</a>.</p>

<p><strong>Personalens egna reaktioner.</strong> Att arbeta nära elever som har det svårt
väcker känslor, och utan ett rum för det blir slitaget stort. Handledning är också
personalvård.</p>

<h2>Upplägg</h2>
<p>Uppdragen ser olika ut: en enstaka konsultation, handledning en gång i månaden under
ett läsår, en utbildningsdag, eller återkommande skolpsykologiskt arbete på konsultbasis.
Vi börjar alltid med ett samtal om vad ni behöver, och gör därefter en tydlig
överenskommelse om omfattning, frekvens och ramar.</p>

<p>Vi arbetar hos er, hos oss i centrala Uppsala eller via video, i hela landet. Priser
lämnas på förfrågan; moms tillkommer. För större uppdrag, ramavtal och upphandling, se
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
behandlingshem och HVB-hem.</p>

<h2>Vad handledningen kan innehålla</h2>
<ul>
  <li><strong>Enskilda ärenden.</strong> Att tillsammans förstå ett placerat barns
  beteende och lägga upp ett gemensamt förhållningssätt.</li>
  <li><strong>Bemötande och struktur.</strong> Hur verksamheten möter utmanande beteende
  utan att trappa upp, och hur förutsägbarhet byggs in i vardagen.</li>
  <li><strong>Trauma och anknytning.</strong> Många placerade barn bär på svåra
  erfarenheter, och beteenden som ser ut som trots eller manipulation är ofta begripliga
  överlevnadsstrategier. Det perspektivet förändrar vad som fungerar.</li>
  <li><strong>Gränssättning.</strong> Hur regler och konsekvenser kan utformas så att de
  fungerar och inte blir en kamp.</li>
  <li><strong>Neuropsykiatri.</strong> Vad en adhd- eller autismdiagnos betyder i
  praktiken för hur vardagen behöver läggas upp.</li>
  <li><strong>Personalens egna reaktioner.</strong> Frustration, uppgivenhet, konflikter
  i arbetsgruppen och den utmattning som kommer av att engagera sig länge i barn som har
  det svårt. Ett rum för det är en förutsättning för att orka stanna kvar i uppdraget.</li>
</ul>

<h2>Form och omfattning</h2>
<p>Handledningen kan ges till en hel personalgrupp, till ett arbetslag eller enskilt till
familjehemsföräldrar. Vanligast är återkommande tillfällen över en längre period —
exempelvis varannan eller var fjärde vecka — eftersom värdet till stor del ligger i
kontinuiteten. Vi tar också enskilda konsultationsuppdrag i ett avgränsat ärende.</p>

<p>Vi arbetar både på plats hos er och via videosamtal, i hela landet. Inför ett uppdrag
gör vi alltid en överenskommelse om syfte, ramar, frekvens och sekretess.</p>

<h2>Konsultation och utbildning</h2>
<p>Utöver löpande handledning erbjuder vi konsultation i enskilda ärenden och fortbildning
för personalgrupper — om utmanande beteende, om NPF, om trauma eller om bemötande. Se
<a href="{base}organisationer/utbildning/">föreläsningar och utbildning</a>.</p>

<p>Vi handleder även socialtjänsten som placerar barnen; se
<a href="{base}barn-och-ungdom/stod/socialtjanst/">stöd till socialtjänsten</a>. Priser
lämnas på förfrågan, moms tillkommer.</p>

<h2>Familjehem har andra behov än personalgrupper</h2>
<p>Familjehemsföräldrar arbetar inte i skift och går inte hem efter passet — uppdraget
pågår dygnet runt, i det egna hemmet, och påverkar hela familjen inklusive egna barn.
Handledningen ser därför annorlunda ut: den behöver rymma både strategierna kring det
placerade barnet och det som händer med familjen som helhet, och den behöver vara en
plats där det går att säga att man inte orkar utan att det uppfattas som att uppdraget
ifrågasätts.</p>

<h2>Skolgången</h2>
<p>Placerade barn har som grupp betydligt sämre skolresultat än andra barn, och skolan är
samtidigt en av de starkaste skyddsfaktorer som finns. Vi arbetar gärna med den delen —
kontakten med skolan, vilka anpassningar som behövs, och hur läxor och krav hanteras
hemma utan att det blir en daglig strid.</p>
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

<h2>Tre former</h2>
<ul>
  <li><strong>Ärendehandledning.</strong> Att tillsammans gå igenom enskilda ärenden och
  få psykologisk kompetens som underlag för era egna bedömningar och beslut.</li>
  <li><strong>Metodhandledning.</strong> Stöd i att använda en metod som avsett — vi
  utbildar och handleder bland annat i motiverande samtal (MI) och i KBT-baserade
  arbetssätt.</li>
  <li><strong>Processhandledning.</strong> Arbetsgruppens eget arbete: samarbete,
  förhållningssätt, och de reaktioner som väcks av att arbeta med människor i utsatta
  situationer.</li>
</ul>

<h2>Vanliga teman</h2>
<p>Barns utveckling och behov i olika åldrar. Psykisk ohälsa hos barn, unga och
föräldrar. Neuropsykiatriska funktionsnedsättningar och vad de innebär i praktiken.
Skadligt bruk och beroende hos föräldrar, och hur det påverkar barnen i en familj — ett
område där vi har särskilt lång erfarenhet, se
<a href="{base}vuxna/beroende/index.html">skadligt bruk och beroende</a>. Bemötande av
klienter i kris eller affekt. Och sekundär traumatisering och medkänsloutmattning hos
personalen — ett slitage som är väl dokumenterat i människovårdande yrken och som sällan
får tillräckligt utrymme.</p>

<h2>Konsultation, bedömning och utbildning</h2>
<p>Vi tar också uppdrag som avgränsad konsultation i ett enskilt ärende, och som
fortbildning för en hel enhet. Behöver ni en psykologisk eller neuropsykiatrisk utredning
som underlag finns den möjligheten också — se
<a href="{base}barn-och-ungdom/utredning/index.html">utredning och bedömning</a>.</p>

<p>Vi handleder även de verksamheter ni placerar i; se
<a href="{base}barn-och-ungdom/stod/hvb-familjehem/">stöd till HVB-hem och
familjehem</a>.</p>

<h2>Upplägg</h2>
<p>Handledning ges vanligen återkommande över en längre period, hos er, hos oss eller via
video. Vi inleder med ett samtal om behov och gör därefter en överenskommelse om syfte,
omfattning, frekvens och ramar. Priser lämnas på förfrågan; moms tillkommer.</p>

<h2>Utredning som underlag för era beslut</h2>
<p>Ibland är det inte handledning som saknas utan ett faktaunderlag. Vi gör psykologiska
och neuropsykiatriska utredningar av barn och ungdomar, samt bedömningar av intellektuell
funktionsnivå — vilket kan vara avgörande för att förstå varför en ungdom inte tar till
sig en insats, eller varför en placering inte fungerat. Se
<a href="{base}barn-och-ungdom/utredning/index.html">utredning och bedömning</a>.</p>

<h2>Samverkan kring en placering</h2>
<p>Vi handleder ofta flera parter kring samma barn: er som placerar, och verksamheten där
barnet bor. Det ger en gemensam förståelse och minskar risken att barnet möts av olika
förhållningssätt på olika håll. När vi arbetar med flera parter regleras alltid i förväg
vad som får delas mellan dem och vad som stannar i respektive handledning.</p>
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

<h2>Olika slags handledning</h2>
<ul>
  <li><strong>Ärendehandledning</strong> — enskilda ärenden, som stöd för medarbetarnas
  egna bedömningar.</li>
  <li><strong>Metodhandledning</strong> — att använda en metod som avsett, exempelvis KBT
  eller motiverande samtal.</li>
  <li><strong>Processhandledning</strong> — arbetsgruppens samarbete, förhållningssätt och
  de reaktioner arbetet väcker.</li>
  <li><strong>Utbildningshandledning</strong> — inom ramen för formella utbildningar, se
  nedan.</li>
  <li><strong>Chefshandledning och coaching</strong> — enskilt stöd i en roll där man
  ofta står ensam med besluten.</li>
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

<h2>Så går det till</h2>
<p>Vi inleder med ett samtal om vad ni behöver och vad ni vill att handledningen ska leda
till. Därefter gör vi en överenskommelse som reglerar syfte, deltagare, frekvens,
omfattning, sekretess och hur uppdraget följs upp — en tydlig ram är en förutsättning för
att handledningen ska bli något annat än ett trevligt samtal.</p>

<p>Grupphandledning sker vanligen med en grupp om några få till ett tiotal deltagare, ofta
varannan till var fjärde vecka över en längre period. Kontinuiteten är en stor del av
värdet.</p>

<h2>Praktiskt</h2>
<p>Vi arbetar hos er, hos oss i centrala Uppsala eller via video, i hela landet. Tre av
oss är utbildade handledare. Priser lämnas på förfrågan; moms tillkommer. Hör av er via
<a href="{base}organisationer/kontakt/">kontakt för uppdrag</a>.</p>
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

<h2>Format</h2>
<ul>
  <li><strong>Föredrag och föreläsningar</strong> — från en timme och uppåt, för en
  arbetsplatsträff, en konferens eller en hel personaldag.</li>
  <li><strong>Workshops och seminarier</strong> — kortare och med praktiska inslag, där
  deltagarna får öva och inte bara lyssna.</li>
  <li><strong>Orienteringsutbildningar</strong> på 4–5 dagar, för en yrkesgrupp som ska
  börja arbeta utifrån ett gemensamt förhållningssätt.</li>
  <li><strong>Föreläsningsserier</strong> över en termin eller ett år.</li>
  <li><strong>Grundläggande psykoterapiutbildning</strong> i KBT.</li>
</ul>

<h2>Ämnen vi undervisar i</h2>
<p>Kognitiv beteendeterapi och beteendeanalys. Motiverande samtal och samtalsmetodik.
Mindfulness och mindfulnessbaserade program. Stress, utmattning och återhämtning.
Skadligt bruk, beroende och spel om pengar. Neuropsykiatriska funktionsnedsättningar.
Oro, ångest, nedstämdhet och trauma. Ledarskap, kommunikation och bemötande.</p>

<h2>Skräddarsydda uppdrag</h2>
<p>Vi erbjuder utbildning och föredrag för företag och offentlig verksamhet om exempelvis
stress, skadligt bruk och beroende, ledarskap och kommunikation, samtalsmetodik,
motiverande samtal, mindfulness och många andra teman.</p>

<p>De flesta uppdrag anpassas efter verksamheten. Vi börjar med ett samtal om vilka
deltagarna är, vad de redan kan, och vad som ska vara annorlunda efteråt — det sista är
den viktigaste frågan, och den som avgör hur dagen läggs upp. En utbildning som ska
förändra hur människor faktiskt arbetar behöver mer övning och mindre föreläsning än man
ofta tänker sig.</p>

<h2>Uppföljning</h2>
<p>Kunskap från en utbildningsdag försvinner snabbt om ingenting följer på den. Vi
rekommenderar därför ofta att en utbildningsinsats kombineras med
<a href="{base}organisationer/handledning/">handledning</a> under en period efteråt, så
att det som lärts in får stöd att bli praktik.</p>

<h2>Praktiskt</h2>
<p>Vi håller utbildningar hos er, hos oss i centrala Uppsala eller via video, i hela
landet. Angeli Holmstedt är medlem i MINT, det internationella nätverket av
MI-utbildare. Priser lämnas på förfrågan; moms tillkommer.</p>

<p>Hör av er för information om uppdragsutbildningar, workshops, föreläsningsserier,
föredrag och övrig fortbildning — se
<a href="{base}organisationer/kontakt/">kontakt för uppdrag</a>.</p>

<h2>Vanliga frågor</h2>

<h3>Hur stor grupp kan ni ta?</h3>
<p>En föreläsning kan hållas för en stor grupp. En utbildning som ska förändra hur
deltagarna arbetar behöver mindre grupper, eftersom den bygger på övning och
återkoppling. Vi säger gärna vad vi tror är rimligt utifrån vad ni vill uppnå.</p>

<h3>Kan utbildningen hållas på distans?</h3>
<p>Ja, både föreläsningar och längre utbildningar fungerar via video. Moment som bygger på
rollspel och praktisk övning blir dock oftast bättre på plats.</p>

<h3>Får deltagarna intyg?</h3>
<p>Ja, vi utfärdar intyg på genomgången utbildning med omfattning och innehåll angivet.</p>

<h3>Hur lång framförhållning behövs?</h3>
<p>Det varierar med årstid och uppdragets storlek. Hör av er så tidigt ni kan, särskilt
för längre utbildningar och för datum under vår och höst.</p>
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

<h2>Så kan ett uppdrag se ut</h2>
<ol class="steps steps--plain">
  <li><h3>Kontakt och ramar</h3><p>Vi går igenom situationen med er som arbetsgivare,
  och kommer överens om uppdragets omfattning, ramar och vad ni får återkoppling om.</p></li>
  <li><h3>Bedömningssamtal</h3><p>Medarbetaren träffar en av våra psykologer för en
  kartläggning av besvär, belastning och återhämtning — och för att bedöma om vår insats
  är rätt, eller om något annat behövs.</p></li>
  <li><h3>Behandling</h3><p>KBT anpassad efter vad bedömningen visade. Vid behov
  samarbetar vi med en specialistläkare i psykiatri.</p></li>
  <li><h3>Återgång i steg</h3><p>Upptrappning av arbetstid och uppgifter i en takt som
  håller, i samverkan med er och med företagshälsovården.</p></li>
</ol>

<h2>Sekretess och roller</h2>
<p>Det här är ofta den viktigaste punkten att reda ut i förväg. Även när ni som
arbetsgivare betalar för insatsen omfattas medarbetarens uppgifter av tystnadsplikt. Ni
får veta att kontakt är etablerad, att den fortgår, och — med medarbetarens samtycke —
det som rör arbetsförmåga, anpassningar och planering. Innehållet i samtalen är inte er
information.</p>

<p>Den tydligheten är inte en begränsning utan en förutsättning: en medarbetare som inte
litar på ramarna berättar inte det som behövs för att insatsen ska göra nytta.</p>

<h2>Praktiskt</h2>
<p>Vi arbetar på mottagningen i centrala Uppsala, hos er och via video i hela landet.
Priser lämnas på förfrågan; moms tillkommer när arbetsgivare, försäkringsbolag eller
socialtjänst betalar. Hör av er via
<a href="{base}organisationer/kontakt/">kontakt för uppdrag</a>.</p>
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

<h2>Tecken på en arbetsplats</h2>
<p>Det som märks först är sällan berusning. Oftare är det upprepad korttidsfrånvaro,
särskilt måndagar och dagen efter helger; sena ankomster; att prestationen svajar utan
förklaring; att humöret svänger; att personen drar sig undan gemensamma sammanhang eller
tvärtom blir påfallande beroende av dem; och att kollegor börjar täcka upp. Det sista är
ett tidigt och ofta förbisett tecken — problemet blir synligt i arbetsgruppens beteende
innan det blir synligt hos individen.</p>

<h2>Vad vi erbjuder arbetsgivare</h2>
<ul>
  <li>stöd till chefer inför och under det svåra samtalet med en medarbetare</li>
  <li>fördjupade utredningar och bedömningar kring skadligt bruk, beroende och
  överdrivet spelande om pengar</li>
  <li>kvalificerad behandling med evidensbaserade metoder som följer Socialstyrelsens
  rekommendationer</li>
  <li>handledning och utbildning till de nätverk som påverkas — anhöriga, vänner,
  arbetskamrater och chefer</li>
  <li>stöd i att ta fram eller se över en alkohol- och drogpolicy, så att rutinerna är
  bestämda innan de behövs</li>
</ul>

<h2>Chefssamtalet</h2>
<p>Många chefer väntar för länge, av rädsla för att ha fel eller för att göra situationen
värre. Ett samtal behöver inte innehålla någon anklagelse och inte någon diagnos. Det
räcker att beskriva det man faktiskt har sett — frånvaron, förändringen, det som inte
stämmer — och att erbjuda hjälp. Vi förbereder gärna chefen inför ett sådant samtal, och
finns med som stöd efteråt.</p>

<h2>Vår kompetens</h2>
<ul>
  <li>återfallsprevention</li>
  <li>motiverande samtal (MI)</li>
  <li>KBT-behandling vid alkohol, droger och spel om pengar</li>
  <li>mindfulnessbaserad återfallsprevention (MBRP)</li>
  <li>12-stegsbehandling / Minnesotamodellen, för olika typer av beroenden och för
  anhöriga</li>
</ul>

<h2>Sekretess och roller</h2>
<p>Även när arbetsgivaren betalar omfattas medarbetarens uppgifter av tystnadsplikt. Ni
får veta att kontakt finns och pågår, och — med medarbetarens samtycke — det som rör
arbetsförmåga och planering. Innehållet i samtalen är inte arbetsgivarens information. Vi
går igenom vad som gäller med båda parter innan en insats påbörjas.</p>

<h2>Anhöriga och kollegor</h2>
<p>Skadligt bruk drabbar fler än den som dricker eller spelar. Vi arbetar också med
anhöriga, och med arbetsgrupper som påverkats.</p>

<p>Den fullständiga beskrivningen av hur vi arbetar kliniskt — riskbruk, skadligt bruk,
beroende och spelberoende — finns på sidan
<a href="{base}vuxna/beroende/index.html">skadligt bruk och beroende</a>. Priser lämnas
på förfrågan; moms tillkommer.</p>
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

<h2>Så brukar ett uppdrag börja</h2>
<p>Med ett samtal, utan kostnad, där ni beskriver situationen och vi säger vad vi tror
behövs — eller att någon annan är bättre lämpad. Därefter lämnar vi ett förslag på
upplägg och pris, och när ni sagt ja gör vi en skriftlig överenskommelse om syfte,
omfattning, frekvens, ramar och sekretess.</p>

<p>Det hjälper oss om ni redan i första kontakten kan säga något om vilka deltagarna är,
vad ni har provat tidigare, ungefär vilken omfattning ni tänker er, och vad som ska vara
annorlunda när uppdraget är slut.</p>

<h2>Var håller vi hus?</h2>
<p>Vår bas är i centrala Uppsala, där mottagningen ligger i Gårdshuset vid Slottskällan
på gångavstånd från Centralstationen. Där tar vi emot kunder och klienter — men vi
arbetar också online och hos arbetsgivare runt om i landet.</p>

<h2>Priser och fakturering</h2>
<p>Priser för handledning, utbildning, konsultation och utredning lämnas på förfrågan,
eftersom de beror på uppdragets omfattning och form. Moms tillkommer när arbetsgivare,
försäkringsbolag eller socialtjänst betalar. Vi fakturerar efter överenskommelse.</p>

<h2>Nå oss</h2>
<p>E-post: <a href="mailto:kontakt@kbt-konsulterna.se">kontakt@kbt-konsulterna.se</a><br>
Telefon: <a href="tel:+4618104044">018 – 10 40 44</a></p>
<p>Du kan också använda <a href="{base}kontakt/index.html">kontaktformuläret</a>. Vi
återkommer så snart vi har möjlighet.</p>

<h2>Sekretess när ni är uppdragsgivare</h2>
<p>Rör uppdraget en enskild medarbetare omfattas dennes uppgifter av tystnadsplikt även
när ni betalar. Ni får veta att en kontakt finns och pågår, och — med medarbetarens
samtycke — det som rör arbetsförmåga och planering. Vad som gäller går vi igenom med båda
parter innan insatsen påbörjas, eftersom tydliga ramar är en förutsättning för att
insatsen ska göra nytta.</p>
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

<h2>Hur ett samtal går till</h2>
<p>Ett samtal är 45 minuter. De första en till tre gångerna handlar om att tillsammans
ta reda på vad du behöver hjälp med — och om du känner dig bekväm med oss. Därefter
formulerar vi mål och kommer överens om metod och ungefär hur många samtal det troligen
handlar om.</p>

<p>Mellan samtalen brukar du ha något med dig att pröva eller observera i vardagen. Det
är inte läxor för deras egen skull: det är där förändringen sker, medan samtalet är
platsen där ni planerar och utvärderar den. Vi stämmer av regelbundet att behandlingen
går i rätt riktning och att tiden används väl.</p>

<h2>Hur många samtal behövs?</h2>
<p>Det varierar kraftigt. En avgränsad fobi kan vara avklarad på några gånger, medan
utmattning, trauma eller långvarig nedstämdhet tar längre tid. Du binder dig aldrig till
ett antal, och du bestämmer själv när du vill avsluta.</p>

<h2>På mottagningen eller online</h2>
<p>Vi tar emot i Gårdshuset vid Slottskällan i centrala Uppsala, tio minuters promenad
från Centralstationen, och erbjuder videosamtal i hela Sverige. De flesta
behandlingsformer fungerar lika väl på video.</p>

<p>Du behöver ingen remiss, och du behöver inte veta vad problemet heter för att höra av
dig.</p>
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

<h2>När är parterapi rätt?</h2>
<p>Vanliga skäl att söka är återkommande konflikter om samma sak, en känsla av att ha
blivit sambos i stället för partners, otrohet eller annat svek, ojämn fördelning av
ansvaret hemma, olika syn på närhet och sex, eller att en av er funderar på att gå.</p>

<p>Ni behöver inte vara överens om att ni vill fortsätta relationen för att börja. Ni
behöver däremot båda vara beredda att komma och att titta på er egen del — parterapi
fungerar dåligt som en plats dit den ena tar med den andra för att få denne
tillrättavisad.</p>

<h2>Vilken metod använder vi?</h2>
<p>Vi arbetar utifrån IBCT — Integrative Behavioral Couple Therapy — en evidensbaserad
form av KBT som syftar till att integrera förändringsarbete med acceptansstrategier.</p>

<p>Varför fortsätter vi att agera och kommunicera på vissa sätt, även när det utifrån sett
inte är särskilt hjälpsamt? Varför bråkar vi om och om igen om samma saker? Utifrån de
frågorna arbetar man med metoder för beteendeförändring — men lägger samtidigt till
acceptans och förståelse för sin partner. Acceptansen är en förutsättning för att
förändringarna ska bli bestående, och för att den känslomässiga närheten ska kunna
byggas upp igen.</p>

<p>En bärande tanke i IBCT är att en del skillnader mellan två personer inte går att
förhandla bort. Det som går att förändra är vad ni gör med dem — om de fortsätter vara
det ni bråkar om, eller blir något ni förstår hos varandra.</p>

<h2>Hur går det till?</h2>
<p>Vid den första kontakten börjar vi vanligen med ett gemensamt samtal där ni tillsammans
beskriver den situation ni befinner er i. Det följs oftast av två individuella möten, för
bakgrund, problembeskrivning och målformulering. Därefter ses vi gemensamt igen för en
sammanfattning från psykologen, som beskriver hur den fortsatta behandlingen kan läggas
upp utifrån de mål ni formulerat.</p>

<p>En målsättning kan vara att stärka relationen — men den kan lika gärna vara att göra
ett bra avslut. Att separera ordnat, särskilt när det finns barn med i bilden, är ett
fullt legitimt mål för en parterapi.</p>

<h2>Vad ni arbetar med</h2>
<ul>
  <li><strong>Konfliktmönstret.</strong> Inte vem som har rätt, utan hur bråket brukar gå
  — vem som trappar upp, vem som drar sig undan, och vad som utlöser det.</li>
  <li><strong>Att prata så att den andra kan höra.</strong> Att säga vad du behöver i
  stället för vad den andra gör fel.</li>
  <li><strong>Närhet.</strong> Vänskapen och det positiva, som ofta hunnit bli det man
  slutar prioritera först.</li>
  <li><strong>Acceptans.</strong> Att förstå varför den andra reagerar som den gör, även
  när du inte håller med.</li>
</ul>

<h2>Tider och pris</h2>
<p>Parterapi bokas i 60-minuterspass, eller som 2 × 45 minuter — ofta behövs minst 60
minuter per besök för att båda ska hinna komma till tals. Aksel Reppling tar emot par.
Se <a href="{base}priser/index.html">priser</a>.</p>

<p>Söker du hjälp med relationer men kommer ensam, se
<a href="{base}vuxna/behandling/relationer/">relationsproblem</a>.</p>
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

<h2>När kan det vara aktuellt?</h2>
<ul>
  <li>När psykologisk behandling behöver kompletteras med läkemedel — eller när du vill
  veta om den möjligheten finns.</li>
  <li>När en diagnos behöver fastställas av läkare, till exempel i samband med en
  <a href="{base}vuxna/utredning/index.html">neuropsykiatrisk utredning</a>.</li>
  <li>När en pågående medicinering inte ger effekt, ger biverkningar, eller behöver ses
  över.</li>
  <li>När sjukskrivning eller ett läkarutlåtande behövs. Psykologer utfärdar inte
  sjukintyg.</li>
  <li>När bilden är oklar och en psykiatrisk bedömning behövs som grund för att välja
  rätt väg framåt.</li>
</ul>

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

<h2>Hur det går till</h2>
<p>Besöken sker på mottagningen i centrala Uppsala eller som videosamtal. Bedömningen
börjar med ett samtal om dina besvär, din historia och din nuvarande situation, och
utmynnar i ett förslag på hur en behandling kan se ut. Går du redan i behandling hos
någon av oss kan psykologen och psykiatern — med ditt samtycke — samråda, så att de två
insatserna drar åt samma håll i stället för var för sig.</p>

<h2>Kombinationsbehandling</h2>
<p>För flera tillstånd är KBT och läkemedel var för sig verksamma, och för en del
fungerar de bäst tillsammans. Kombinationen kan också innefatta sjukskrivning och
läkarutlåtande när det behövs. Vad som passar dig avgörs av vad du söker för, vad du
tidigare provat och vad du själv vill — läkemedel är aldrig ett villkor för att gå i
behandling hos oss.</p>

<h2>Bra att veta</h2>
<p>Vi är en mottagning med bokade tider och kan inte ta emot akut. Behöver du hjälp
omedelbart, se <a href="{base}akut-hjalp/index.html">akut hjälp</a>. Vi bedriver inte
heller beroendevård med läkemedelsassisterad behandling eller avgiftning; vid sådana
behov hänvisar vi vidare. Se <a href="{base}vuxna/beroende/index.html">skadligt bruk och
beroende</a> för vad vi gör på det området.</p>

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

<h2>När är det dags att söka hjälp?</h2>
<p>Det finns ingen skarp gräns, men några hållpunkter: när besvären håller i sig över tid
snarare än går över, när de påverkar skolan, kompisrelationerna eller vardagen hemma, när
barnet drar sig undan från sådant det tidigare tyckte om, eller när ni som föräldrar
märker att det ni brukar göra inte längre räcker.</p>

<p>Ni behöver inte vänta tills det är allvarligt. Det är ofta lättare att vända en
utveckling tidigt, och ett bedömningssamtal kan lika gärna landa i att det inte behövs
någon behandling.</p>

<h2>Hur vi arbetar med barn</h2>
<p>Behandlingen anpassas efter ålder och mognad. Med yngre barn arbetar vi konkret och
lekfullt, med bilder och material snarare än långa resonemang, och en stor del av arbetet
sker via föräldrarna. Med tonåringar ser samtalen mer ut som med vuxna, och ungdomen får
större utrymme att själv formulera vad hen vill ha hjälp med.</p>

<p>Gemensamt är att KBT för barn och unga är konkret och inriktat på vad som ska bli
annorlunda i vardagen — inte bara på att prata om hur det känns.</p>

<h2>Föräldrarnas roll</h2>
<p>All behandling av barn och ungdomar genomförs i nära samarbete med vårdnadshavare.
Ni är inte åskådare: ni är ofta den viktigaste delen av behandlingen, eftersom det är
hemma, i vardagen, som det som övas ska fungera. Ju yngre barnet är, desto större andel
av arbetet sker genom er.</p>

<p>Vid gemensam vårdnad behöver båda vårdnadshavarna vanligtvis samtycka till
behandlingen. Hör av er om ni är osäkra på vad som gäller i er situation.</p>

<h2>Skolan</h2>
<p>Skolan är en stor del av ett barns liv, och mycket av det som är svårt visar sig där.
Om ni vill, och efter ert samtycke, samarbetar vi gärna med skolan — det kan handla om
att inhämta information, delta i ett möte eller ge råd om anpassningar.</p>

<h2>Praktiskt</h2>
<p>Vi tar emot på mottagningen i centrala Uppsala, och erbjuder videosamtal när det
passar bättre. Ingen remiss behövs. Om det under bedömningen visar sig att barnet behöver
en annan vårdnivå än den vi kan erbjuda, säger vi det och hjälper er vidare.</p>
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

<h2>När är en utredning aktuell?</h2>
<p>Om svårigheterna håller i sig över tid, visar sig i mer än ett sammanhang — både hemma
och i skolan — och påverkar barnets inlärning, kompisrelationer eller mående. Enstaka
perioder av svårigheter hör till uppväxten; det är varaktigheten och bredden som gör en
utredning motiverad.</p>

<p>Ofta är det skolan som först väcker frågan, men ni kan söka er hit direkt utan att
någon annan gjort det. Är ni osäkra går det bra att boka ett bedömningssamtal för att
resonera om saken.</p>

<h2>Vad en utredning ger — och inte ger</h2>
<p>En utredning ger en beskrivning av hur ert barn fungerar: vilka förmågor som är
starka, vilka som är svaga, och vad det betyder i praktiken. Den ger ett skriftligt
utlåtande med konkreta rekommendationer, och den ger ofta en lättnad — både för er och för
barnet, som kan ha gått länge med en känsla av att vara sämre utan att förstå varför.</p>

<p>Den ger däremot ingen garanti om ett visst resultat. Utfallet kan bli att kriterierna
för en diagnos är uppfyllda, att de inte är det, eller att svårigheterna har en annan
förklaring — stress, oro, sömnbrist, en inlärningssvårighet eller något i barnets
situation. Även då är kartan över styrkor och svårigheter användbar, och vi går igenom
vad den betyder för er.</p>

<p>En diagnos utlöser inte automatiskt insatser. Skolans stöd ska ges utifrån elevens
behov, inte utifrån diagnos — men utlåtandet blir ofta det underlag som gör behovet
tydligt och konkret.</p>

<h2>Ingen remiss behövs</h2>
<p>Som privat mottagning kan ni söka er till oss direkt. Vi samarbetar gärna med barnets
skola eller andra vårdgivare om ni önskar det.</p>

<h2>Efter utredningen</h2>
<p>Återgivningen är inte slutet. Vi går igenom vad resultatet innebär i vardagen, vilka
anpassningar som är rimliga att be skolan om, och vad ni kan göra hemma. Behöver barnet
behandling eller ni föräldrastöd finns båda hos oss — se
<a href="{base}barn-och-ungdom/behandling/index.html">psykologisk behandling</a> och
<a href="{base}barn-och-ungdom/stod/foraldrar/">stöd till föräldrar</a>. Vi har också
tillgång till specialistläkare som bidrar till diagnostiken och som kan hjälpa till vid
önskemål om medicinsk behandling.</p>
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

<h2>Tre former av stöd</h2>
<ul>
  <li><strong>Rådgivning</strong> — ett eller några samtal om en konkret fråga. Vad gör vi
  åt morgnarna? Hur pratar vi med henne om det här? Ska vi söka hjälp?</li>
  <li><strong>Handledning</strong> — återkommande samtal med en yrkesgrupp, enskilt eller i
  grupp, om det egna arbetet: bemötande, förhållningssätt och de egna reaktionerna på
  det som är svårt.</li>
  <li><strong>Konsultation</strong> — en avgränsad insats i ett enskilt ärende, där ni
  behöver psykologisk kompetens som underlag för era egna beslut.</li>
</ul>

<h2>Vilka vi arbetar med</h2>
<p>Föräldrar och andra anhöriga, skolpersonal och elevhälsoteam, personal vid HVB-hem och
behandlingshem, familjehemsföräldrar, och medarbetare inom socialtjänsten. Flera av oss
har lång egen erfarenhet från BUP, skola, behandlingshem och specialskolor.</p>

<h2>Så går det till</h2>
<p>Vi börjar med ett samtal om vad ni behöver, hur ofta och i vilken form. Därefter gör vi
en överenskommelse om upplägg, omfattning och ramar. Handledning sker vanligen
återkommande över en längre period; rådgivning kan vara ett enda samtal.</p>

<p>Vi arbetar på mottagningen i centrala Uppsala, hos er, och via videosamtal i hela
landet. För uppdrag från arbetsgivare, se även
<a href="{base}organisationer/index.html">För organisationer</a>.</p>

<p>Priser för handledning och konsultation lämnas på förfrågan. Moms tillkommer när
arbetsgivare, försäkringsbolag eller socialtjänst betalar.</p>

<h2>Rådgivning eller behandling?</h2>
<p>En vanlig fråga är om det är barnet som ska gå i behandling eller ni som vuxna som
behöver stöd. Ofta är svaret det senare, särskilt när barnet är yngre — det är hemma och i
skolan som vardagen finns, och det är de vuxna som är där. Ett bedömningssamtal reder
vanligen ut vilket som är mest verkningsfullt att börja med, och de två utesluter inte
varandra.</p>

<p>Behöver barnet egen behandling finns den hos oss, se
<a href="{base}barn-och-ungdom/behandling/index.html">psykologisk behandling</a>. Behövs
en kartläggning av barnets förutsättningar, se
<a href="{base}barn-och-ungdom/utredning/index.html">utredning och bedömning</a>.</p>
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
