<h1 align="center">Resumen primer parcial<h1>

# Números

## Enteros (ℤ)

### Definición

Un entero es un elemento del conjunto formado por la unión de estos 3 conjuntos:

1. Los naturales (+1, +2, +3, ... +N)
2. Los enteros negativos (-1, -2, -3, ... -N)
3. El cero, que no es ni positivo ni negativo.

ℤ = {-N, ..., -1, 0, 1, ..., N}

### Orden

Los números enteros están ordenados:

1. **a, -b → -b < a**
2. **a, b → El menor es el de menor valor absoluto**
3. **-a, -b → El menor es el de mayor valor absoluto**
4. **Negativos < 0 < Positivos**

### Propiedades de la suma

1. **Cerrada: a + b, con a ∈ ℤ y b ∈ ℤ da como resultado c ∈ ℤ.**
2. **Asociativa: (a + b) + c = a + (b + c)**
3. **Conmutativa: a + b = b + a**
4. **El elemento neutro es el 0: a + 0 = a**
5. **Ley de Monotonía: Si a ≤ b → (a + c) ≤ (b + c)**
6. **Resta: a + (-b) = a - b**

### Propiedades de la multiplicación

1. **Cerrada: a × b, con a ∈ ℤ y b ∈ ℤ da como resultado c ∈ ℤ.**
2. **Asociativa: (a × b) × c = a × (b × c)**
3. **Conmutativa: a × b = b × a**
4. **El elemento neutro es el 1: a × 1 = a**
5. **Ley de Monotonía: Si a ≤ b → (a × c) ≤ (b × c) si c es positivo y (a × c) ≥ (b × c) si c es negativo.**
6. **Distributiva: a × (b + c) = a × b + a × c**

### Divisibilidad

La división está parcialmente definida porque ∀a ∈ ℤ, $\frac{a}{0}$ no está definido. Además es una operación no cerrada porque $\frac{a}{b}$ no siempre da como resultado un entero.

#### División exacta

Sea a, b ∈ ℤ con b ≠ 0.

b divide a $a$ y se escribe b | a, **si existe un c ∈ ℤ tal que a se puede escribir como:**

**$a = b×c $**

En ese caso se dice que:

1. **b es divisor de a**
2. **a es divisible por b**
3. **a es múltiplo de b**

##### Propiedades:

1. a | a
2. 1 | a
3. a | 0
4. a | b → a | -b, -a | b, -a | -b
5. a | b → a | (b × c)
6. a | b, b | c → a | c (transitiva)
7. a | b, a | c → a | b + c

#### División inexacta

Sea a, b ∈ ℤ con b ≠ 0.

Si no existe c que cumpla $a = b×c $, se trata de aproximar de la mejor forma a $a$ por un múltiplo de b. La diferencia entre a y ese número es el resto.

$$a = (b × c) + r$$ $$0 ≤ r < |b|$$

### Enteros primos

Sea p ∈ ℤ, p ≠ 1, p es **primo** si sus únicos divisores son p, -p, 1 y -1.

Por ejemplo: 2, 3, 5, 7, ...

-   Hay infinitos números primos.
-   Si a es un entero no primo, entonces existe un primo p tal que p | a.

#### Teorema fundamental de la aritmética

Todo número entero distinto de 0, 1 y -1 es producto finito de números primos y esa factorización es única excepto el orden.

### Máximo Común Divisor (MCD)

Sea a, b ∈ ℤ, a ≠ 0, b ≠ 0, existe d > 0 tal que:

1. d | a y d | b
2. Si existe D tal que D | a y D | b → D | d.

d es MCD(a,b).

-   Si MCD(a,b) = 1 → a y b son **coprimos**.
-   Si p es primo, entonces MCD(a, p) para cualquier a ∈ ℤ será p o son coprimos.

#### Algoritmo para calcular el MCD

MCD(70,50)

1. 70 / 50 = 20, resto 1.
2. 50 / 20 = **10**, resto 2.
3. 20 / 10 = 2, resto 0.

El MCD es 10.

#### Identidad de Bezout

Dados a, b ∈ ℤ y d el MCD entre ellos, existen enteros m y n tal que:

**d = m × a + n × b**

### Mínimo Común Múltiplo (MCM)

Sea a, b ∈ ℤ, existe m tal que:

1. $a | m$ y $b | m$
2. Si existe M tal que a | M y b | M → m | M.

m es MCM(a,b).

### Números pares e impares

Un número par se define como 2k, con k ∈ ℤ.
Un número impar se define como 2k + 1, con k ∈ ℤ.

### Conversión a otras bases

Para convertir un número en base 10 a base X, se usa el siguiente algoritmo:

1. Se divide el número por X, se anota el resto y el cociente.
2. Se divide el cociente anterior por X.
3. Se repite 1 y 2 hasta que el resto sea 0.
4. Cuando el resto es 0, se unen los restos del último al primero.

## Racionales (ℚ)

### Definición

Un racional es un número que puede expresarse como $\frac{a}{b}$.

**ℤ ⊂ ℚ**: Los enteros son un subconjunto de los racionales ya que $\frac{a}{1} = a, a ∈ ℤ$.

### Propiedades generales

1. $\frac{a}{b} = \frac{c}{d}$ si solo si $a×d = b×c$
2. $\frac{a}{b} < \frac{c}{d}$ si solo si $a×d < b×c$

### Propiedades de la suma

-   Es cerrada, asociativa y conmutativa.
-   $\frac{a}{b} + \frac{c}{d} = \frac{a×d}{b×d} + \frac{b×c}{b×d} = \frac{a×d + b×c}{b×d}$

### Propiedades de la resta

-   Es cerrada, asociativa y conmutativa.
-

### Propiedades de la multiplicación

-   Es cerrada, asociativa y conmutativa.
-

### Propiedades de la división

-   Es cerrada, asociativa y conmutativa.
-

## Irracionales (ℙ)

### Definición

Un irracional es un número que no puede ser expresado como cociente de dos enteros.

Propiedades:

1. Racional + irracional = irracional.
2. Un racional ≠ 0 multiplicado por un irracional = irracional.
3. Un racional ≠ 0 dividido por un irracional = irracional.
4. El inverso de un irracional es un irracional.
5. La suma y multiplicación de irracionales no son operaciones cerradas.

## Complejos (ℂ)

### Definición

Un número complejo es un número que tiene parte real y parte imaginaria.

Forma binómica:

$z = a + ib$ con a, b ∈ ℝ

-   La unidad imaginaria i se define como $i^2 = -1$.
-   Si la parte real, (Re(z) = a) es igual a 0, z es un imaginario puro.
-   Si la parte imaginaria, (Im(z) = b) es igual a 0, z es un real.
-   Existen muchas formas de definirlos:
-   z1 = z2 si solo si Re(z1) = Re(z2) y Im(z1) = Im(z2).

### Operaciones

#### Conjugado

El conjugado de un número complejo es:

$z = a + bi$
$\bar{z} = z^{*} = a - bi$

El conjugado se suele usar para hallar las partes Real e Imaginaria de un número complejo que tiene a $i$ tanto en el numerador como en el denominador. Para esto se multiplica a ese número complejo por su conjugado dividido por ese mismo conjugado.

#### Módulo

El módulo de un número complejo representa la distancia al origen (0,0), si representamos a nuestro complejo z en el plano, con (a,b) a real, b complejo.

$|z| = \sqrt{a^2 + b^2}$

donde a = Re(z), b = Im(z)

#### Suma

-   Es cerrada, asociativa y conmutativa.
-   $z_1 + z_2 = (a_1 + a_2) + i(b_1 + b_2)$
-   Elemento neutro: $0 + i0 = 0$

#### Resta

-   Opuesto(z) = -z = -a - ib
-   $z_1 - z_2 = (a_1 + ib_1) + (-a_2 - ib_2)$

#### Producto

-   $ z_1 × z_2 = (a_1×a_2 - b_1×b_2)+i(a_1×b_2 - a_2×b_1)$

#### Inverso

-   $z^{-1} = \frac{a-ib}{(a+ib)(a-ib)}$

#### Cociente

-   $\frac{z_1}{z_2} = \frac{(a_1×a_2 + b_1×b_2)+i(-a_1×b_2 + a_2×b_1)}{a_2^2 + b_2^2}$

#### Potencias

-   $i^0 = 1$
-   $i^1 = i = \sqrt{-1}$
-   $i^2 = -1$
-   $i^3 = -i$
-   $i^4 = 1$
-   $i^r = i^{4q + r}$

-   Por ejemplo:

$i^{65} = i^{4×16 + 1} = i^1 = i$
$i^{220} = i^{4×55 + 0} = i^0 = 1$
$i^{2003} = i^{4×500 + 3} = i^3 = -i$

### Pasar un número complejo en forma binómica a la forma exponencial

Dado un complejo $z$, su forma exponencial es:

$|z|e^{i×\theta}$

-   Para hallar el argumento tita, es útil graficar el complejo y ver qué ángulo tiene(línea desde el punto hasta el origen).
-   π = 180°
-   Cuadrantes:

    ![Cuadrantes](https://www.varsitytutors.com/assets/vt-hotmath-legacy/hotmath_help/topics/cartesian-plane/example-2.gif)

-   Por ejemplo:

$z = -6 -2i$
$a = -6$
$b = -2$

Dibujar el complejo:

![](https://i.imgur.com/HAG7hG8.png)

Ver en qué cuadrante se encuentra:

1. Si está en el cuadrante 1, tita será $arctg(\frac{b}{a})$.
2. Si está en el cuadrante 2 o 3, tita será $arctg(\frac{b}{a}) + π$
3. Si está en el cuadrante 4, tita será $arctg(\frac{b}{a}) + 2π$

$\theta = arctg(\frac{4}{3}) = 53°$
$π = 180°$
$180° → π$
$53° → x$

Aproximadamente $\frac{1}{3}\pi$

Como se encuentra en el cuadrante 3, le sumamos π:

$\frac{1}{3}\pi + \pi = \frac{4}{3}\pi$

### Hallar raíces enésimas de un complejo

1. Se halla la forma exponencial de z.
2. Se define: $|w| = \sqrt[n](|z|)$
3. Se define: $φ_k = \frac{\frac{3}{4}\pi + 2k\pi}{n}; 0\le k \le n-1$
4. Se calcula $φ_0$ $φ_1$ $φ_2$ ... $φ_{n-1}$.

---

# Relaciones

## Definición

Una relación es un **subconjunto del producto cartesiano** entre A y B (relación binaria), o entre A, B, C, ..., N (relación n-aria).

Hay 2 notaciones principales:

-   xRy: x está relacionado con y por R.
-   (x,y) ∈ R.

## Dominio e Imagen

Sea R una relación de A en B:

$Dom(R) = \{x ∈ A: (x,y) ∈ R\}$

$Im(R) = \{y ∈ B: (x,y) ∈ R\}$

Por ejemplo:

A = {1, 2, 3}

R = {(1,2), (3,3)}

Dom(R) = {1, 3}
Im(R) = {2, 3}

## Relación inversa

La relación inversa es la que inverte el orden de los elementos dentro de todas las tuplas dentro de la relación.

$R = \{ (x,y) : (x,y) ∈ AXB\}$
$R^{-1} = \{ (y,x) : (x,y) ∈ R\}$

Ejemplo:

-   $R = \{(1,3), (5,6)\}$
-   $R^{-1} =\{(3,1), (6,5)\}$

## Relación complemento

La relación complemento de $R$, $(\overline{R})$ es el opuesto de R, es decir, todos los pares que **no están en R** pero que si **están en el producto cartesiano** del conjunto de donde salió la relación.

Ejemplo:

$A = \{1, 2\}$
$R = \{(1,1),(1,2)\}$
$\overline{R} = \{(2,1),(2,2)\}$

## Matriz de relación

Consiste en una matriz donde se pone 1 si a está relacionado con b por R (aRb), y 0 en caso contrario.

Ejemplo:

$A = \{1, 2, 3\}$
$R = \{(1,2),(1,3),(3,3)\}$

|     | 1   | 2   | 3   |
| --- | --- | --- | --- |
| 1   | 0   | 0   | 0   |
| 2   | 1   | 0   | 0   |
| 3   | 1   | 0   | 1   |

Es decir, la cantidad de unos es igual a la cantidad de tuplas de R.

## Digrafo de relación

Consiste en escribir los elementos del conjunto como nodos, y flechas que representan las relaciones entre ellos.

## Diagrama de Hasse

Consiste en un diagrama que representa a las relaciones de forma más concisa que el digrafo de relación. Pasos para construirlo:

1. Se crea el digrafo de relación.
2. Se borran todas las flechas de elementos hacia sí mismos.
3. Se borran las relaciones transitivas.
4. Se reordena el resultado del paso anterior, poniendo los elementos más grandes arriba y más chicos abajo. Se obtuvo el Diagrama de Hasse.

## Reflexividad, simetría, antisimetría, transitividad

Dada una relación $R$ sobre un conjunto $A$:

### Reflexividad

$R$ es reflexiva si para todo elemento $a ∈ A$ se cumple que $aRa$, o dicho de otra forma, que $(a,a) ∈ R$.

De forma intuitiva, significa que cada elemento de A está **relacionado consigo mismo**.

-   Ejemplo que cumple ✅:

$A = \{1,2,3\} $
$R = \{(1,1),(2,2),(3,3)\}$

-   Ejemplo que no cumple ❌:

$A = \{1,2,3\} $
$R = \{(1,1),(2,2)\}$

**No cumple porque 3 no está relacionado consigo mismo.**

### Simetría

$R$ es simétrica si para todo par de elementos $(a,b) ∈ A$ se cumple que si $aRb → bRa$, o dicho de otra forma, que $(a,b) ∈ R$ **implica** $(b,a) ∈ R$

De forma intuitiva, significa que si un elemento $a$ está relacionado con un elemento $b$, entonces $b$ también está relacionado con $a$.

-   Ejemplo que cumple ✅:

$A = \{1,2,3\} $
$R = \{(1,2),(2,1),(2,3),(3,2)\}$

-   Ejemplo que no cumple ❌:

$A = \{1,2,3\} $
$R = \{(1,2),(2,1),(2,3)\}$

**No cumple porque 2 está relacionado con 3 pero 3 no está relacionado con 2.**

### Antisimetría

$R$ es antisimétrica si para todo par de elementos $(a,b) ∈ A$ se cumple que si $aRb$ y $bRa$ → $a = b$, o dicho de otra forma, que $(a,b) ∈ R$ ^ $(b,a) ∈ R$ **implica** $a = b$

De forma intuitiva, significa que si un elemento $a$ está relacionado con un elemento $b$, y $b$ también está relacionado con $a$, entonces $a$ es **igual** a $b$.

-   Ejemplo que cumple ✅:

$A = \{1,2,3\} $
$R = \{(1,1),(2,2),(3,1)\}$

-   Ejemplo que no cumple ❌:

$A = \{1,2,3\} $
$R = \{(1,2),(2,1)\}$

**No cumple porque 1 está relacionado con 2 y 2 está relacionado con 1, pero 1 ≠ 2.**

### Transitividad

$R$ es transitiva si para toda terna de elementos $(a,b,c) ∈ A$ se cumple que si $aRb$ y $bRc$ → $aRc$, o dicho de otra forma, que $(a,b) ∈ R$ ^ $(b,c) ∈ R$ **implica** $(a,c) ∈ R$

De forma intuitiva, significa que si un elemento $a$ está relacionado con un elemento $b$, y $b$ está relacionado con $c$, entonces $a$ también está relacionado con $c$.

-   Ejemplo que cumple ✅:

$A = \{1,2,3\} $
$R = \{(1,2),(2,3),(1,3)\}$

-   Ejemplo que no cumple ❌:

$A = \{1,2,3\} $
$R = \{(1,2),(2,3),(1,1)\}$

**No cumple porque 1 está relacionado con 2 y 2 está relacionado con 3, pero 1 no está relacionado con 3.**

### Resumen

|             | Reflexividad | Simetría                | Antisimetría                    | Transitividad                    |
| ----------- | ------------ | ----------------------- | ------------------------------- | -------------------------------- |
| Definición  | ∀a ∈ A, aRa  | ∀a, b ∈ A, si aRb → bRa | ∀a, b ∈ A, si aRb ^ bRa → a = b | ∀a, b, c ∈ A, si aRb ^ bRc → aRc |
| Condiciones |              | P → Q                   | P ^ O → Q                       | P ^ O → Q                        |

Es decir, si la condición P o O son falsas, ya está, no tengo que chequear nada más, la condición será verdadera.

Lo único que hay que chequear es que cuando P y O son verdaderas, que Q también sea verdadera. Si en ese caso Q es falso, no se cumple la propiedad.

## Relaciones de Orden y Preorden

Una relación $R$ se considera de Preorden si es **reflexiva y transitiva**.

Una relación $R$ se considera de Orden si es **reflexiva, transitiva y antisimétrica.**

Una relación de orden puede ser de orden parcial o total:

-   Si es parcial, algunos elementos no pueden compararse entre sí.
-   Si es total, todos los elementos se pueden comparar entre sí.

En particular, se define que a y b son comparables si se verifica aRb o bRa, si no se dan ninguna de las dos entonces no son comparables. Con tener un solo caso donde dos elementos no puedan compararse es suficiente para decir que tenemos un orden parcial y no total.

## Relaciones de equivalencia

Una relación $R$ se considera de equivalencia si es **reflexiva, simétrica y transitiva.**

Se denota con $\equiv$.

### Clases de equivalencia

Las clases de equivalencia de una relación de equivalencia son conjuntos, para cada elemento de $A$, que tienen como elementos a todos los otros elementos con quienes están relacionados en la R.E.

Puede haber clases de equivalencia repetidas, en cuyo caso se toma solo una.

La unión de todas las clases de equivalencia da como resultado a la partición que induce la relación $R$ sobre $A$.

Cualquier elemento de la clase de equivalencia se llama representante de la clase.

### Partición

Es un conjunto que representa una "división" de un conjunto $A$. Para que una partición sea válida debe cumplir 3 condiciones:

1. Ningun elemento es vacío $(\emptyset)$.
2. Las intersecciones entre todos los elementos del conjunto dan vacío $(\emptyset)$ (no puede haber elementos repetidos).
3. La unión $(\cup)$ entre todos los elementos del conjunto da como resultado el conjunto original $A$.

### Conjunto cociente

Es el conjunto formado por todas las clases de equivalencia de elementos del conjunto A respecto a la relación R.

Se denota A/R.

Si R es una relación de equivalencia en A, entonces el conjunto cociente A/R es partición de A.

## Relaciones de congruencia

### Definición

Se trata de una relación de equivalencia que cumple lo siguiente:

Dados $a, b, m$ se dice que $a$ es congruente con $b$ módulo $m$ (y se escribe a $\equiv_m b$) si solo si $m | a - b$, es decir que existe $k ∈ ℤ$ tal que **$a - b = k×m$**

Por ejemplo:

$4 ≡ 10 (3)$

Porque:

1. $3 | 4 − 10$
2. $3 | -6$
3. $-6 = k×m$
4. $-6 = 3×(-2)$

Existe m = -2 tal que se cumple.

### Teoremas y proposiciones

Dos enteros a, b pertenecen a la misma clase de equivalencia si solo si son congruentes módulo m.

Todo entero es congruente módulo m con su resto en la división por m.

Dos enteros son congruentes módulo m si solo si los respectivos restos en su división por m son iguales.

### Cómo encontrar x tal que a $\equiv_x modb$

1. Se divide $a$ por $b$
2. $x = $ el resto de la división.

Luego, se dice que $a$ pertenece a la clase de equivalencia $x$.
