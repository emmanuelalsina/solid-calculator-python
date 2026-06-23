# SOLID Calculator — Python

Este proyecto es un ejercicio práctico diseñado para demostrar y reforzar la aplicación de los principios **SOLID** en el desarrollo de software, específicamente utilizando **Python**. 

El objetivo principal es transformar una calculadora tradicional (que suele violar principios de diseño) en un sistema altamente escalable, desacoplado y fácil de mantener.

---

## 🛠️ Principios SOLID Aplicados

### 1. Principio de Responsabilidad Única (SRP)
> *"Una clase debe tener una sola razón para cambiar."*

En arquitecturas tradicionales, una sola clase se encarga de recibir los datos, validar la operación, realizar el cálculo y mostrar el resultado. Aquí, cada clase hace **una sola cosa bien**:
* Las operaciones (`Suma`, `Resta`, etc.) solo conocen su propia lógica matemática.
* La clase contenedora (`Calculator`) solo se encarga de coordinar y ejecutar, delegando el trabajo pesado.

### 2. Principio de Abierto/Cerrado (OCP)
> *"El software debe estar abierto para su extensión, pero cerrado para su modificación."*

Si quisiéramos agregar una nueva operación (como *Multiplicación* o *Potencia*), **no necesitamos modificar el código de la clase `Calculator`**. 

**La analogía del restaurante:** Imagina que la calculadora es un restaurante. El dueño (la clase `Calculator`) contrató a un chef experto en comida mexicana (`Suma`) y a otro en comida italiana (`Resta`). Si mañana el dueño quiere vender comida japonesa, no tiene que obligar a los chefs actuales a aprender una nueva receta (modificar código existente). Simplemente contrata a un chef experto en sushi (`Multiplicación`) que cumpla con el contrato de la cocina. El restaurante crece sin alterar lo que ya funcionaba.

---

## 🧠 Conceptos Clave de Python Reforzados

### 🔄 El uso de `self` (Goku y Vegeta)
Para entender cómo las clases mantienen su propio estado en la Programación Orientada a Objetos, usamos la analogía de las armaduras Saiyajin:
* La clase `Operacion` es el molde de la armadura.
* Cuando creamos a `goku = Operacion(5, 3)`, la palabra `self` se convierte internamente en `goku`. Así, sus niveles de poder se guardan en `goku.num1` y `goku.num2`.
* Si creamos a `vegeta = Operacion(10, 8)`, su `self` hace referencia exclusiva a `vegeta`. 

Graas a `self`, los datos de Goku y Vegeta jamás se mezclan, aunque usen el mismo molde de código.

---

##  Estructura del Código

El proyecto utiliza un diccionario de despacho dinámico para evitar los bloques infinitos de `if/elif` y permitir la extensión limpia del sistema:

* **Abstracción:** Definición de la estructura base de las operaciones.
* **Polimorfismo:** Cada clase hija implementa su propio método de ejecución bajo el mismo nombre.
* **Inyección de Dependencias:** El despachador mapea el string del usuario con la clase correspondiente.

---
Prototipo de aprendizaje desarrollado por [Emmanuel Alsina](https://github.com/emmanuelalsina).
