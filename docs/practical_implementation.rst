Eerste praktische implementatie
===============================

De applicatie
-----------------

Als praktische implementatie voor de Boven-Maas wordt een interactieve applicatie voorgesteld waarbij 
een gebruiker, via keuzes, de waarde van een aantal drukfactoren kan wijzigen en instantaan het effect op soorten kan visualiseren. Het idee is de ecologische relaties 
tussen soorten en omgevingsvariabelen in een GraphQL DDL (data definitie laag, ofwel het geheel van tabellen en de relaties tussen tabellen) worden ondergebracht. 
De drukfactoren bestaan uit ruimtelijke gegevens die uit baseline applicaties opgehaald kunnen worden voor de Boven-Maas.

Een mockup van de applicatie is als animatie opgenomen, zie daarvoor 

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://github.com/openearth/iEAT/assets/6429095/e516bc4e-9d6a-40b4-955d-16b0b66e3b07" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>


Data gebruik
-----------------
Als voorbeeld van een drukfactor is de stroomsnelheid gebruikt. De gegevens, zijn afkomstig van een scenario berekening met RWS BaseLine voor project
Basis Rivier Bodemligging. 
Afhankelijk van de gebruikte drukfactoren en scenario's worden diverse datasets voorzien. 

Data architectuur
-----------------
Als architectuur voor de data wordt voorgesteld gebruik te maken van data services volgens de OGC standaarden. Het voordeel is dat gemakkelijk nieuwe dataset beschikbaar gemaakt
kunnen worden vanuit modellen. Het gebruik van OGC standaarden brengt flexibiliteit met zich mee. Als de data geschikt is kunnen deze datalagen ook van andere instanties dan directive
die van Deltares gebruikt worden. Het biedt vele andere mogelijkheden voor flexibel gebruik. Door FAIR volledige toe te passen is het zelfs mogelijk om dele van de applicatie zodanig
in te richten dat de scenario's opgehaald worden uit de metadata van de lagen. OGC services zijn hier een bewuste keuze, die zorgen voor beschikbaarheid, interactie en uitgebreide mogelijkheden 
wat betreft visualisatie van data.

Wat betreft de operationalisatie van een netwerk van ecologische relaties wordt een geografische database gebruikt. In Libaries en database wordt hier verder op ingegaan, inclusief
de gebruikte packages.

Een prototype
-----------------
Er is een prototype beschikbaar van een Python Shiny applicatie die het mogelijk maakt om de cursor te verschuiven over de uitkomsten die als OGC WFS worden
aangeboden. De waarde van de cursor wordt uit de data opgehaald. Vervolgens wordt een opzoektabel geraadpleegd waarin per soort een range van stroomsnelheden is opgenomen. Als 
de stroomsnelheid binnen de range valt, dan kan een soort daar voorkomen (als hypotethisch geval).
Hieronder een impressie van dat prototype.

.. image:: images/ieat_prototype.png

Dit is overigens niet verder gebracht. Het idee om een dashboard achtige applicatie te maken waarbij diverse typen visualisaties worden toegepast vereist een minder strikte omgeving dan een
dashboard ontwikkelomgeving. In het algemeen is het aantal beperkingen wat groter dan in een omgeving gebaseerd op web technologie. Bovendien is een webomgeving ook beter overdraagbaar (geen issue eigenlijk), 
terwijl een python dashboard allerlei voorwaarden stelt aan de omgeving waarin het gebruikt wordt. 

Het maken van dit prototype heeft echter een belangrijke bijdrage geleverd aan de manier waarop ecologische netwerk gegevens gekoppeld kunnen worden aan fysische gegevens (drukfactoren). 
Door de flexibiliteit van data die via gestandaardiseerde protocollen beschikbaar zijn (lees de OGC Services zoals door de Rijksoverheid worden gepromotoot en door Geonovum en PDOK worden geïmplementeerd) is het
mogelijk gemakkelijk te kunnen wisselen van databron (het is immers een link waarbij het leesdeel data de data inlees alleen wijzigt van adres, niet van functionaliteit).

Voorstel
-----------------
De animatie van de mockup hierboven laat een op web technologie gebaseerd product zien. Het voorstel is dat er een basisopzet is met een aantal vast elementen:
- kaartcomponent (met de gebruikelijke opties, inzoomen, navigeren en een zoekmogelijkheid om op toponiemen te kunnen zoeken)
- keuze opties (uiteraard staan deze nog niet vast)
- een visualisatie componenten die geactualiseerd wordt middels de waarden van de laag uit het scenario

De exacte layout van zowel de look and feel als gebruikte data dient in een aantal sessies tot stand te komen, alsmede de 'knoppen' waaraan gedraaid kan worden om het effect op
ecologische netwerken te kunnen bepalen. Er is al wel een goed idee wat betreft de te gebruiken software en andere middelen. Dat wordt in het hoofdstuk Libraries en database verder
uitgewerkt. 

Libraries en database
-----------------
Als database wordt een geografische database gebruikt. De voorkeur gaat daarbij uit naar PostgreSQL/PostGIS. Deze open source database geeft alle mogelijkheden
om een GraphQL DDL op te nemen en heeft tevens ruimtelijke functionaliteit beschikbaar.
Naast Python worden de volgende packages gebruikt:

- graphql-python-api
- ariadne 
- flask 
- flask-sqlalchemy 
- flask-cors
- psycopg2-binary
