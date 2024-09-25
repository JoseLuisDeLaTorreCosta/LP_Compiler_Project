1. Funcionament de la pràctica

L'entrada és un text_area, per tant, si es vol executar un cas, s'han d'introduir les declaracions línia per línia i l'expressió.

La pràctica pot executar la pràctica sense expressió. En aquest cas, sols s'imprimiran en pantalla la taula de tipus.

En el cas que s'introdueixi sols l'expressió, s'imprimirà el primer graf d'inferència, però s'establiran totes les variables
i operadors com genèrics i, per tant, n'hi haurà una col·lisió de tipus.

Cal dir que, encara que està implementada la gramàtica per a tipus genèrics i les funcions, sols està implementada la inferència
bàsica.

2. Documentació

    2.1. Gramàtica

La gramàtica està composta per un conjunt de declaracions i una única expressió.

El conjunt de declaracions poden ser 0 o més declaracions.
Cada declaració està composta per la variable a declarar, dos punts i un tipus.
La variable a declarar pot ser una variable genèrica, un nombre o un operador.
Un tipus poden ser simples o compostos, que són conjunts de simples. Un tipus simple pot ser un tipus individual o una funció,
que és un conjunt d'individuals.

L'expressió pot ser una variable, que tindran la mateixa estructura que les variables declarades, una aplicació, una abstracció,
o una variable parentitzada.

    2.2. Programa

Ara es documentarà el contingut del programa principal (hm.py).

    2.2.1. Arbre algebraic

L'arbre algebraic és utilitzat principalment per a poder dibuixar els grafs d'inferència.
N'hi ha tres tipus d'arbres:
    · Aplication: Representen els nodes d'aplicació de dos variables.
    · Abstraction: Representen els nodes d'abstracció de dos variables.
    · Leaf: Representen les variables individuals.

També n'hi ha els arbres buits que sols serveixen per a inicialitzar els arbres algebraics dins dels visitadors.
Finalment, n'hi ha les consultores: getValue, getType, getEsq, getDret i la modificadora de tipus modifyType.

    2.2.2. write_type

És una classe auxiliar que serveix per a transformar els tipus de variables de llistes (que és el format en el qual estan
els tipus de les variables dins de la taula de símbols) a strings per a poder imprimir els tipus de les variables dins
dels grafs.

    2.2.3. drawTree

És una classe auxiliar que, a partir d'un arbre algebraic, retorna el string que conté quasi tot el codi per a poder
imprimir el graf d'inferència de tipus.

    2.2.4. getNoDeclaredTypes

És una classe que retorna un parell de llistes que representen els tipus genèrics i el tipus inferits d'aquests. Això
serveix per a fer la taula on es podrà veure els tipus inferits de les classes genèriques que han sigut establertes en
el visitador.

    2.2.5. clase TreeVisitor

És la classe encarregada de fer l'anàlisi semàntica, de guardar els tipus declarats i crear tipus genèrics per als nodes
d'abstracció i aplicació.

    2.2.6. generic

És una funció booleana encarregada de veure si el tipus passat per paràmetre és un genèric o no. Això es fa mirant sí
el tipus és minúscula.

    2.2.7. t2_in_t1

És la classe encarregada en veure si els paràmetres t1 i t2 (que són el tipus1 i tipus2) n'hi ha col·lisió de tipus i, si
no n'hi ha, retorna la resta de t2 - t1.

    2.2.8. clase EvalVisitor

És la classe encarregada d'avaluar l'expressió, aplicar-hi inferència i veure els tipus reals dels tipus genèrics creats en la
classe TreeVisitor.

    2.2.9. main

És on es conté el funcionament del programa.
En primer lloc, es declara el container (on es col·locarà la taula de tipus declarats), el text_area on es posarà l'input,
la taula de símbols i el botó de "fer".
Si es polsa el botó, s'analitzaran les expressions, i en cas que no n'hi hagi cap error sintàctic, s'analitza la gramàtica, es
dibuixa el graf de les anotacions de tipus i s'escriu la taula de tipus declarats en el container anteriorment declarat.
Finalment, s'avalua l'expressió i, en cas que no n'hi hagi col·lisió de tipus, es dibuixa el graf d'inferència i la taula on
es pot veure els tipus reals dels tipus anotats.

