# Tarea Dev Junior - Ruuf

## 🎯 Objetivo

El objetivo de este ejercicio es poder entender tus habilidades como programador/a, la forma en que planteas un problema, cómo los resuelves y finalmente cómo comunicas tu forma de razonar y resultados.

## 🛠️ Problema

El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones "a" y "b" (paneles solares) que caben dentro de un rectángulo de dimensiones "x" e "y" (techo).

## 🚀 Cómo Empezar

### Opción 1: Solución en TypeScript
```bash
cd typescript
npm install
npm start
```

### Opción 2: Solución en Python
```bash
cd python
python3 main.py
```

## ✅ Casos de Prueba

Tu solución debe pasar los siguientes casos de prueba:
- Paneles 1x2 y techo 2x4 ⇒ Caben 4
- Paneles 1x2 y techo 3x5 ⇒ Caben 7
- Paneles 2x2 y techo 1x10 ⇒ Caben 0

---

## 📝 Tu Solución

Primero, se valida que ninguna de las dimensiones con las que se está trabajando sea 0, para así evitar futuras divisiones por 0 que rompan el código. 

Luego, se toman las dimensiones validadas y se evalúan 4 configuraciones distintas, calculando en cada una cuántos paneles completos caben en la orientación principal y,  adicionalmente, si se pueden aprovechar las franjas que sobran poniendo paneles rotados. Finalmente se comparan todas estas configuraciones y se devuelve la de mayor valor, asegurando la mejor utilización posible del espacio del techo. 

Se utilizan 4 configuraciones porque combinan ambas orientaciones posibles del panel (horizontal y vertical) con los dos ejes del techo (ancho y alto), lo que permite cubrir todos los casos relevantes.
---

## 💰 Bonus (Opcional)

Si completaste alguno de los ejercicios bonus, explica tu solución aquí:

### Bonus Implementado
*[Indica cuál bonus implementaste: Opción 1 (techo triangular) o Opción 2 (rectángulos superpuestos)]*




### Explicación del Bonus
*[Explica cómo adaptaste tu algoritmo para resolver el bonus]*




---

## 🤔 Supuestos y Decisiones

*[Si tuviste que tomar algún supuesto o decisión de diseño, explícalo aquí]*

