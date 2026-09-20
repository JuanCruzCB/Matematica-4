<h1 align="center">Resumen segundo parcial<h1>

# [Estructuras Algebraicas](https://www.youtube.com/playlist?list=PLDJU8kNAPOn_On9WQEYzA08dxxVyKSNzu)

## Definición

Una estructura algebraica es un conjunto no vacío A con una operación ∗ y se denota **(A, ∗)**.

## Tipos de operaciones

-   **Operación binaria**: Toma dos elementos del conjunto y da un resultado que puede o no estar dentro de ese mismo conjunto.

-   **Operación bien definida**: Garantiza que el resultado es único y no depende de cómo se representen los elementos.

-   **Operación cerrada**: El resultado de operar dos elementos del conjunto **pertenece al mismo conjunto**.

## Propiedades de las operaciones binarias

-   **Conmutatividad**: Para todo a, b de A, a ∗ b = b ∗ a
-   **Asociatividad**: Para todo a, b y c de A, a ∗ (b ∗ c) = (a ∗ b) ∗ c
    -   Si para una operación asociativa ∗ en A existe un elemento neutro e y un elemento a de A tiene inverso a<sup>-1</sup> entonces este es único.
    -   Si para una operación asociativa ∗ en A existe un elemento neutro e y todo elemento tiene su inverso, entonces vale en A la llamada propiedad cancelativa: a ∗ b = a ∗ c ⇒ b = c (de modo similar, b ∗ a = c ∗ a ⇒ b = c).
-   **Elemento neutro**: (A, ∗) tiene elemento neutro si existe, para todo a en A un elemento e tal que a ∗ e = e ∗ a = a
-   **Elemento inverso**: Si (A, ∗) tiene elemento neutro e, un elemento a de A tiene inverso si existe a<sup>-1</sup> tal que a ∗ a<sup>-1</sup> = a<sup>-1</sup> ∗ a = e
    -   Si para una operación ∗ en A existe un elemento neutro, este es **único**.

## Tipos de estructuras algebraicas

Sea (A, ∗) una estructura algebraica.

### Grupoide

La operación ∗ es binaria.

### Semigrupo

La operación ∗ es asociativa.
Si además es conmutativa tenemos un semigrupo conmutativo.

### Monoide

La operación ∗ es asociativa y existe elemento neutro e para ∗.
Si además es conmutativa tenemos un monoide conmutativo.

### Grupo

La operación ∗ es asociativa, existe elemento neutro e para ∗, y cada elemento a de A tiene inverso.
Si además es conmutativa tenemos un grupo conmutativo.

-   El elemento neutro e es único.
-   Todo elemento tiene un único inverso.
-   Valen las propiedades cancelativas.
-   Cualquiera sea a ∈ G, (a<sup>-1</sup>)<sup>-1</sup> = a.
-   Cualesquiera sean a, b ∈ G, (ab)<sup>-1</sup> = b<sup>-1</sup> a<sup>-1</sup>.

#### Teorema 1

Si (G<sub>1</sub>, ∗<sub>1</sub>), (G<sub>2</sub>, ∗<sub>2</sub>), (G<sub>n</sub>, ∗<sub>n</sub>) son grupos, entonces G = G<sub>1</sub> X G<sub>2</sub> X ... X G<sub>n</sub> es un grupo con operación ∗ definida por:

(a<sub>1</sub>, ..., a<sub>n</sub>) ∗ (b<sub>1</sub>, ..., b<sub>n</sub>) = (a<sub>1</sub> ∗<sub>1</sub> b<sub>1</sub>, a<sub>n</sub> ∗<sub>n</sub> b<sub>n</sub>)

#### Grupo cíclico

Un grupo (G, ∗) es cíclico si existe g ∈ G tal que ∀ a ∈ G, a = g<sup>k</sup>, con k entero. En este caso, g es generador de G y se denota G = < g >

#### Teorema 2

Todo grupo cíclico es conmutativo.

#### Orden

Sea G un grupo y a ∈ G, diremos que a es de **orden finito** si existe un k natural tal que a<sup>k</sup> = e. En ese caso el orden de a es = mink : a<sup>k</sup> = e.

#### Teorema 3

Si G es un grupo cíclico de orden m, entonces G = {e, a, a<sup>2</sup>, ..., a<sup>m−1</sup>}

#### Subgrupo

Dado un grupo (G, ∗) y dado H ⊂ G, si (H, ∗) es un grupo, entonces H es subgrupo de G.

Como H ⊂ G, hereda varias propiedades de G que es un grupo. Entonces,para chequear que H es subgrupo, solo se necesita chequear:

1. e ∈ H. El mismo elemento neutro de ∗ en G debe estar en H.
2. a, b ∈ H → a ∗ b ∈ H. Cerradura de la operación ∗.
3. a ∈ H → a<sup>-1</sup> ∈ H. Cada elemento de H tiene inverso.

#### Teorema 4

Si (G, ∗), es un grupo cíclico y (H, ∗) es un subgrupo de (G, ∗), entonces (H, ∗) es cíclico.

### Anillo

...

---

# [Aritmética Modular](https://www.youtube.com/playlist?list=PLDJU8kNAPOn-w-aMjTHEM4J2qqohqZY0p)

## Introducción

La aritmética modular es una forma de representar números para que su valor nunca exceda un cierto límite, llamado módulo. Entonces, cuando el valor alcanza el módulo, se vuelve a cero y comienza a contar nuevamente. Por ejemplo, 18 en módulo 12 sería 6: 11 0 1 2 3 4 5 6.

## Clases de congruencia módulo m

La clase de congruencia módulo m de x será el conjunto

\(\overline{x}\) = {y ∈ Z : y ≡<sub>m</sub> x}

Intuitivamente, son todos los números que al dividirlos por el módulo, m, **dejan resto x**.

Dos números son congruentes módulo m si y solo si están en la misma clase de equivalencia.

### Teorema 1

Sea m ∈ N, ℤ<sub>m</sub> = ℤ<sub>m</sub> = Z/ ≡m , el conjunto cociente, tiene m clases de equivalencias.

## Operaciones en ℤ<sub>m</sub>

### Suma

\(\overline{x}\) + \(\overline{y}\) = \(\overline{x + y}\)

Es asociativa, conmutativa, tiene neutro, y todo elemento tiene opuesto.

### Producto

\(\overline{x}\) · \(\overline{y}\) = \(\overline{x · y}\)

Es asociativa, conmutativa, tiene neutro, y el producto se distribuye en la suma.

### Ejemplo

ℤ<sub>5</sub> = {\(\overline{0}\), \(\overline{1}\), \(\overline{2}\), \(\overline{3}\), \(\overline{4}\)}

\(\overline{2}\) + \(\overline{2}\) = \(\overline{4}\)
\(\overline{2}\) + \(\overline{3}\) = \(\overline{0}\)

\(\overline{2}\) · \(\overline{3}\) = \(\overline{1}\)
\(\overline{2}\) · \(\overline{0}\) = \(\overline{0}\)

...

ℤ<sub>6</sub> = {\(\overline{0}\), \(\overline{1}\), \(\overline{2}\), \(\overline{3}\), \(\overline{4}\), \(\overline{5}\)}

Simplificando clases de equivalencia:

\(\overline{10}\) = \(\overline{4}\) (porque 10 dividido 6 da 1 con resto **4**.)
\(\overline{15}\) = \(\overline{3}\) (porque 15 dividido 6 da 2 con resto **3**.)
\(\overline{20}\) = \(\overline{2}\) (porque 20 dividido 6 da 3 con resto **2**.)
\(\overline{25}\) = \(\overline{1}\) (porque 25 dividido 6 da 4 con resto **1**.)

## Elementos invertibles

Dado \(\overline{a}\) ∈ ℤ<sub>m</sub>, decimos que \(\overline{a}\) es invertible (o divisor de la unidad), si: existe \(\overline{c}\) ∈ ℤ<sub>m</sub> tal que \(\overline{a}\) · \(\overline{c}\) = \(\overline{1}\).

### Teorema 2

Sea \(\overline{a}\) ∈ ℤ<sub>m</sub>, \(\overline{a}\) es invertible si y sólo si (a, m) = 1.

### Teorema 3

Si m ∈ ℤ es primo, ℤ<sub>m</sub> es un cuerpo.

### Teorema 4

Dado a ∈ ℤ<sub>m</sub>, a es invertible si y sólo si a NO es divisor de 0

### Teorema 5

"Pequeño teorema de Fermat"...

## Función de Euler

La función ϕ, llamada función de Euler, es tal que a cada número natural m le asocia el número ϕ(m) de elementos invertibles de ℤ<sub>m</sub>.

### Teorema 6

El teorema de Euler dice:

Sean a y m enteros tales que (a, m) = 1 → \(\overline{a}\)<sup>ϕ(m)</sup> ≡<sub>m</sub> \(\overline{1}\).

---

# Morfismos

## Definición

Dados dos grupos (G<sub>1</sub>, ∗) y (G<sub>2</sub>, ⊗), la función f : G<sub>1</sub> → G<sub>2</sub> es un morfismo si y sólo si “respeta” las operaciones, en la siguiente forma:

f(a ∗ b) = f(a) ⊗ f(b) para todo a, b ∈ G<sub>1</sub>

Es decir, cuando se opera en G<sub>1</sub>, las correspondientes imágenes resultan operadas en G<sub>2</sub>.

## Tipos de morfismos

Un morfismo **inyectivo es un monomorfismo**.
Un morfismo **sobreyectivo es un epimorfismo**.
Un morfismo **biyectivo (tanto inyectivo como sobreyectivo) es un isomorfismo**.

## Correspondencias entre elementos neutros e inversos

Sean los grupos (G<sub>1</sub>, ∗) y (G<sub>2</sub>, ⊗) y la función f : G<sub>1</sub> → G<sub>2</sub> un morfismo entre ellos, entonces f(e1) = e2 (siendo e1 y e2 los neutros respectivos a cada grupo).

Además para cualquier a ∈ G<sub>1</sub>, f(a<sup>−1</sup>) = (f(a))<sup>−1</sup>.

## Nucleo de un morfismo

Se denomina núcleo del morfismo f al conjunto:

Nu(f) = {a ∈ G<sub>1</sub> : f(a) = e2}

Es decir, el subconjunto del dominio formado por todos los elementos cuya imagen es el neutro del codominio.

**Nu(f) es subgrupo de G<sub>1</sub>.**

## Imágen de un morfismo

Se denomina imágen del morfismo f al conjunto:

Im(f) = {b ∈ G<sub>2</sub> : ∃a ∈ G<sub>1</sub>, f(a) = b}

**Im(f) es subgrupo de G<sub>2</sub>.**

---

# [Espacios Vectoriales - Transformaciones Lineales](https://www.youtube.com/playlist?list=PLDJU8kNAPOn9J1wHGodDsERZq3mNv285n)

## Espacios Vectoriales

### Definición

Un espacio vectorial sobre los reales o los complejos es una estructura algebraica (V, +, ·) creada a partir de un conjunto no vacío V, una operación interna +, definida entre los elementos de V, y una operación externa · definida entre V y los reales o los complejos.

### Axiomas

Para demostrar que un conjunto es un espacio vectorial se prueban **10 cosas**, 2 de cerradura, 4 sobre la suma, 4 sobre el producto:

1.  **\+ cerrada.**
2.  **∙ cerrada.**
3.  **\+ conmutativa.**
4.  **\+ asociativa.**
5.  **Existe neutro para \+.**
6.  **Existe opuesto para \+.**
7.  **∙ asociativa.**
8.  **∙ distributiva en la suma de escalares.**
9.  **∙ distributiva en la suma de vectores.**
10. **Existe neutro para ∙.**

#### Teorema 1

Si V es espacio vectorial:

1. **Para todo escalar c se cumple c ∙ 0 = 0**
2. **Para todo vector v de V, se cumple 0 ∙ v = 0**
3. **Si c ∙ v = 0 entonces c = 0 o v = 0 o ambos son 0.**
4. **Para todo vector v de V vale que 1 ∙ v = v**

### Subespacios Vectoriales

Sea V un espacio vectorial y sea S ⊂ V.
S es subespacio de V si se cumplen 3 condiciones:

1. **S ≠ ∅.**
2. **∀s<sub>1</sub>, s<sub>2</sub> ∈ S → s<sub>1</sub> + s<sub>2</sub> ∈ S.**
3. **Sea k ∈ ℝ, ∀s ∈ S → k ∙ s ∈ S.**

### Combinación lineal de vectores

Dado un conjunto de vectores S = {v<sub>1</sub>, v<sub>2</sub>, ..., v<sub>r</sub>} de V, se llama combinación lineal de los vectores de S, a los vectores v de la forma:

**v = c<sub>1</sub> ∙ v<sub>1</sub> + c<sub>2</sub> ∙ v<sub>2</sub> + ... + c<sub>r</sub> ∙ v<sub>r</sub>**

donde los coeficientes c<sub>1</sub>, c<sub>2</sub>, ..., c<sub>r</sub> son escalares reales.

#### Teorema 2

Si S = {v<sub>1</sub>, v<sub>2</sub>, ..., v<sub>r</sub>} son vectores del espacio vectorial V, entonces el conjunto de todas las combinaciones lineales de estos vectores:

**gen(S) = ⟨v1, v2, ..., vr⟩**

es un subespacio de V y se lo denomina al espacio generado por S.

### Conjunto generador

Se dice que el conjunto S = {v<sub>1</sub>, v<sub>2</sub>, ..., v<sub>r</sub>} es un conjunto generador del espacio vectorial V si y sólo si todo vector de V puede escribirse como combinación lineal de
v<sub>1</sub>, v<sub>2</sub>, ..., v<sub>r</sub>.

**O lo que es igual, V = gen(S).**

### Independencia lineal

Los vectores v<sub>1</sub>, v<sub>2</sub>, ..., v<sub>r</sub> de V se dicen linealmente dependientes si existen escalares c<sub>1</sub>, c<sub>2</sub>, ..., c<sub>r</sub> no todos nulos tales que:

**c<sub>1</sub>∙v<sub>1</sub> + c<sub>2</sub>∙v<sub>2</sub> + ... + c<sub>r</sub>∙v<sub>r</sub> = 0**

Equivalentemente, v<sub>1</sub>, v<sub>2</sub>, ..., v<sub>r</sub> de V se dicen linealmente independientes si la combinación c<sub>1</sub>∙v<sub>1</sub> + c<sub>2</sub>∙v<sub>2</sub> + ... + c<sub>r</sub>∙v<sub>r</sub> = 0 implica que **todos los c<sub>i</sub> son nulos**.

Una combinación lineal de un conjunto S de vectores linealmente independientes es **única**. Esto es, existe una **única manera de expresar un vector particular como combinación lineal de los vectores de S linealmente independientes**.

Si el conjunto de vectores no es linealmente independiente se podrá **escribir cualquier vector de varias formas** (por ejemplo sumando la combinación nula a una expresión particular del vector).

### Base de V

Un conjunto de vectores v<sub>1</sub>, v<sub>2</sub>, ..., v<sub>r</sub> forma una base de V si y sólo si:

1. v<sub>1</sub>, v<sub>2</sub>, ..., v<sub>r</sub> son linealmente independientes.
2. v<sub>1</sub>, v<sub>2</sub>, ..., v<sub>r</sub> generan V.

Si una base de un espacio vectorial V tiene n vectores, se dice que V tiene **dimensión n**.

El subespacio {0} tiene dimensión 0.

**REVISAR**:

_Un conjunto es base de R<sub>n</sub> si posee n vectores y además esos vectores son linealmente independientes._

#### Teorema 3

Si B = {v<sub>1</sub>, v<sub>2</sub>, ..., v<sub>n</sub>} es una base de V, todo conjunto M = {u<sub>1</sub>, u<sub>2</sub>, ..., u<sub>m</sub>} de m > n vectores de V es linealmente dependiente.

Si B = {v<sub>1</sub>, v<sub>2</sub>, ..., v<sub>n</sub>} y B′ = {u<sub>1</sub>, u<sub>2</sub>, ..., u<sub>m</sub>} son dos bases de un espacio vectorial V, entonces m = n.

Es decir, todas las bases de V tienen la misma cantidad de elementos.

#### Teorema 4

Si V tiene dimensión n > 0, entonces:

1. Cualquier conjunto de n vectores linealmente independientes de V genera todo V y por ende forma una base de V.
2. Todo conjunto de n vectores que generan V son linealmente independientes, osea forman una base de V.

Es decir:

-   Un conjunto **genera** R<sub>n</sub> si posee cantidad de vectores >= n y además se puede formar cualquier vector en R<sub>n</sub> usando sumas y multiplicaciones de los vectores del conjunto.
    -   Si cantidad de vectores exactamente n, estos deben ser independientes.
    -   Si cantidad de vectores > n, no importa si son o no dependientes, siempre y cuando las combinaciones cubran todo R<sub>n</sub>.

## Transformaciones Lineales

### Definición

Sean V y W dos espacios vectoriales.

Una transformación lineal es una aplicación de V en W, denotada como L : V → W, si cumple:

1. **∀v<sub>1</sub>, v<sub>2</sub> ∈ V, L(v<sub>1</sub> + v<sub>2</sub>) = L(v<sub>1</sub>) + L(v<sub>2</sub>)**
2. **∀k ∈ K y ∀v ∈ V, L(k.v) = k.L(v)**

### Propiedades

Dada una transformación lineal L : V → W, se cumplen las siguientes propiedades:

1. **L(0<sub>v</sub>) = 0<sub>w</sub>**
2. **∀v ∈ V, L(−v) = −L(v)**
3. **Si v<sub>1</sub>, v<sub>2</sub>, ..., v<sub>n</sub> ∈ V → L(α<sub>1</sub>v<sub>1</sub> + ... + α<sub>n</sub>v<sub>n</sub>) = α<sub>1</sub>L(v<sub>1</sub>) + ... + α<sub>n</sub>L(v<sub>n</sub>).**

### Núcleo

El Núcleo de una transformación lineal L es el conjunto de vectores v ∈ V que son transformados o “enviados” al vector nulo 0<sub>w</sub> de W. Es decir:

**Nu(L) = {v ∈ V : L(v) = 0<sub>w</sub>}**

Nu(L) es un subespacio de V.

### Imagen

La Imagen de la transformación lineal L es el conjunto de vectores w ∈ W que son imagen por L de elementos v ∈ V y se denota:

**Im(L) = {w ∈ W : ∃v ∈ V tal que w = L(v)}**

Im(L) es un subespacio de W.

### Teorema "2.9"

Si L : V → W es una transformación lineal entre los espacios vectoriales V y W de dimensión finita, entonces:

**dim( Nu(L) ) + dim( Im(L) ) = dim(V)**

### Representación matricial

...

![](https://i.imgur.com/lRPWEy8.jpeg)
