Conceptuele opzet
=================

(pm. IN januari 2024 geupdate met informatie uit de review state of art)

Wat is nodig qua kennis?
------------------------

**Voor elke soort: habitat, voedsel, voortplanting**

Om alles in samenhang te analyseren zijn de volgende kennisaspecten nodig:

Kunnen soorten voorkomen?
    - Relaties tussen abiotiek en soorten voor bepalen fysiek habitat
    - Relaties tussen soorten wanneer een soort het habitat is of creëert voor de ander

Hebben soorten te eten?
    - Voedsel relaties tussen soorten
    - Abiotiek als (drager van) voedsel

Kunnen soorten zich voortplanten?
    - Zijn de fysieke omstandigheden aanwezig voor voortplanting? (incl. dispersie)
    - Zijn faciliterende soorten aanwezig?

Duidelijk is dat er onderlinge afhankelijkheden zijn tussen deze 3 aspecten. Bijvoorbeeld:
    - Als een soort niet kan voorkomen (geen habitat) dan is het niet beschikbaar in het voedselweb voor andere soorten.
    - Als een soort wel kan voorkomen, maar veel van zijn voedsel is niet aanwezig, dan is de kans kleiner dat de soort voorkomt
    - Als een soort wel kan voorkomen en er is voedsel, maar kan zich niet voortplanten, dan is er geen duurzame populatie (en is die afhankelijk van bovenstroomse aanwas)

**Het ruimtelijke aspect**

Het inbrengen van de ruimtelijke setting is een logische stap. Dit kan op meerdere manieren aangepakt worden. 

Compartiment aanpak
    Bovenstaande relaties tussen soorten kunnen geplaatst worden in éen ruimtelijk compartiment, waarin wordt verondersteld dat systeemtoestanden
    (hydrologie, morfologie en chemie) en soorten unform verdeeld zijn. PCLAKE is zo'n model waarin het meer (lake) gemodelleerd is in een ruimtelijke eenheid
    (het meer) en daarin een aantal subcompartimenten, zie https://www.sciencedirect.com/science/article/pii/S0304380019300201. Hierin zijn ook trofische
    relaties gemodelleerd.
    
    Een ander voorbeeld, waarin een rivier in gehomogeniseerde compartimenten is ingedeeld, is bijvoorbeeld het 1-d hydraulische model SOBEK.
    In SOBEK zijn de rivier en aanliggende uiterwaarden opgeknipt in compartimenten dwars op de as van de rivier. Binnen het compartiment zijn de 
    beschrijvende variabelen uniform, denk aan de hydraulische weerstand in de uiterwaarden en de bodemschuifspanning.

    Wanneer in deze opzet soort-soort interacties worden meegenomen, afstanden bestaan niet in een compartiment, dan moet verondersteld worden dat binnen een compartiment de afstand tussen
    soorten geen beperkende factor is.

(add figuren)
(voeg toe welke vragen we kunnen beantwoorden)

Hogere resolutie ruimtelijke aanpak
    De aanpak die voor abiotiek-soort relaties in rivieren meestal wordt gebruikt is die van een raster gebaseerde aanpak. De abiotiek, bijvoorbeeld
    stroomsnelheid of temperatuur, wordt in een fijn ruimtelijk grid berekend. Vervolgens wordt voor elke gridcel (onafhankelijk) de habitatgeschiktheid
    uitgerekend.

    Wanneer in deze opzet soort-soort relaties meeneemt, en de gridcellen zijn klein, dan wordt de ruimtelijke homerange van soorten een factor om
    rekening mee te houden. Een vis kan over verschillende cellen heen naar zijn voedsel zwemmen.

(add figuren)
(welke vragen kunnen we hiermee beantwoorden)

**Hoe kunnen we dit vormgeven voortbouwend op bestaande instrumenten**

Stel we nemen de hogere ruimtelijke resolutie aanpak, en we gebruiken bijvoorbeeld het rekengrid van hydraulische modellen, dan:

1. Gebruik de soort - abiotiek relaties uit KRW-Verkenner: produceer ruimtelijke habitat geschiktheidskaarten
2. Bouw een database op van soort - soort relaties voor de 3 genoemde aspecten (voedsel, habitat, voortplanting)
3. Kies voor fauna soorten een ruimtelijke homerange --> paper uit de groep Hendriks met schattingen voor soorten
4. Voeg deze kennisregels toe: reken opnieuw (itererend over de soorten) de habitatgeschiktheid uit met de op abiotiek gestoelde 
   kaarten en de habitatkaarten als invoer.
5. Itereer over de soorten totdat uitkomsten niet of nauwelijks veranderen.

Grofweg op deze wijze kunnen de puur op abitisch habitat kaarten als startpunt nemen, en hierop verder bouwen.

(GG: verder uitschrijven en figuren als voorbeeld nemen)

**Welke bouwstenen zijn beschikbaar**

Abiotiek - biotiek
    - deze relaties zijn beschikbaar in de HABITAT kennisregels voor waterplanten, macrofauna en vissen (link)
    - de hydromorfologische relaties kunnen worden gemodelleerd in de ruimte

Voorbeeld figuren: modellen

(GG: verder uitschrijven: welke soort-soort interactie data is beschikbaar)
