# Generación de Imágenes a partir de Frases de Libros

Este proyecto genera imágenes basadas en frases de libros utilizando dos modelos de inteligencia artificial: **Stable Diffusion XL** y **FLUX.1-dev**. El flujo completo incluye la generación de prompts a partir de frases usando LLaMA 3, la generación de imágenes, la superposición de texto en las imágenes (con indicación del modelo generador) y la creación de GIFs comparativos.

## Modelos Utilizados

### Stable Diffusion XL (SDXL)

* **Proveedor**: Hugging Face Inference API
* **Modelo**: `stabilityai/stable-diffusion-xl-base-1.0`

### FLUX.1-dev

* **Proveedor**: Hugging Face Inference API via Replicate
* **Modelo**: `black-forest-labs/FLUX.1-dev`

---

## Preguntas por Modelo

### 1. ¿Cuáles fueron los parámetros seleccionados por cada modelo para ajustar y cómo afectaron la generación de la imagen?

* **Stable Diffusion XL**: Se utilizó resolución por defecto del modelo (1024x1024) y prompts generados con temperatura 0.7. Afectó positivamente la coherencia en escenas amplias y naturales.
* **FLUX.1-dev**: Se mantuvieron los valores por defecto del modelo en Replicate. El estilo es más artístico y atmosférico, pero con menos control sobre detalles específicos.

### 2. ¿Cuál es la arquitectura subyacente del modelo que estás utilizando?

* **Stable Diffusion XL**: Utiliza una arquitectura basada en *Latent Diffusion Models* con codificadores de texto CLIP y una UNet mejorada.
* **FLUX.1-dev**: Basado en *transformers difusivos* altamente entrenados para estilo cinemático, aprovechando una arquitectura no públicamente detallada, pero orientada a generación estilizada.

### 3. ¿Qué datos de entrenamiento se utilizaron para entrenar este modelo y cómo afecta esto a la diversidad de las imágenes generadas?

* **SDXL**: Entrenado con datasets LAION-5B, lo que le permite generar imágenes variadas y coherentes con una gran diversidad visual.
* **FLUX.1-dev**: Entrenado con datasets curados enfocados en cine, arte y atmoferas; esto favorece composiciones estilizadas pero limita la variedad contextual.

### 4. ¿Cuáles son las limitaciones de los modelos que estás usando en términos de resolución, coherencia visual y generación realista de detalles?

* **SDXL**: Puede producir resultados altamente coherentes, pero en prompts complejos puede fallar en detalles finos. Tiene buena resolución nativa.
* **FLUX.1-dev**: Muy estético pero menos preciso en detalles realistas. Puede generar rostros o objetos inconsistentes.

### 5. ¿Cómo maneja el modelo la variabilidad en la generación de imágenes? ¿Utiliza redes neuronales convolucionales (CNNs), transformers u otra técnica para capturar patrones visuales?

* **SDXL**: Usa una combinación de CNNs (UNet) y codificadores de texto (CLIP) con difusión latente.
* **FLUX.1-dev**: Utiliza arquitectura basada en transformers y atención para capturar patrones estéticos y semánticos.

### 6. ¿Qué diferencias clave has encontrado entre los modelos de generación de imágenes que has probado en términos de calidad de salida, velocidad de generación y precisión visual?

* **SDXL**: Salida coherente, algo más lenta, pero muy confiable.
* **FLUX.1-dev**: Más rápido en generación, pero más centrado en estilo que en precisión semántica.

### 7. ¿Cómo afectan las configuraciones de parámetros (como la resolución, el tamaño de la imagen y el número de iteraciones) a la calidad final de la imagen generada por cada modelo?

* La resolución influye directamente en los detalles finos: SDXL genera mejor en 1024x1024. El número de pasos de difusión (no ajustado manualmente aquí) también es clave. Ambos modelos mejoran cuando los prompts son bien definidos.

---

## Frases del Libro y Prompts Generados

A continuación se listan las frases utilizadas, junto con el prompt y anti-prompt generado por LLaMA 3 para cada una:

### Frase 1:

* **Oración**: "Los libros son los espejos del alma."
* **Prompt**: "Una mujer sentada en una biblioteca oscura con una lámpara de lectura en la mano, rodeada de libros antiguos y tapices. La iluminación proviene de la lámpara, creando sombras en el rostro y las manos de la mujer. La vista se enfoca en su expresión serena y en el título de un libro abierto, que es: 'Los libros son los espejos del alma'. La escena es tranquila y poética."
* **Anti-Prompt**: "personajes jóvenes, armas, violento, urbano, día claro"

### Frase 2:

* **Oración**: "Me encontré en un mar en el que las olas de la alegría y la tristeza chocaban entre sí."
* **Prompt**: "Un personaje en una playa solitaria con oleaje suave, pero con un rostro que refleja la lucha entre la alegría y la tristeza. La luz del sol se refleja en las olas, creando un contraste de emociones en el entorno sereno."
* **Anti-Prompt**: "ciudades, personas corriendo, sonrisas contagiosas, fiestas, luz intensa, paisajes desérticos, agua cristalina, personas jugando, clima soleado, arcoíris, personajes felices y despreocupados."

### Frase 3:

* **Oración**: "Los hermanos sean unidos porque esa es la ley primera; tengan unión verdadera en cualquier tiempo que sea, porque si entre ellos pelean los devoran los de afuera."
* **Prompt**: "Dos hermanos unidos, con sus brazos alrededor, sonrientes, en un campo abierto con una leyenda antigua en el fondo, ilustración inspirada en la Biblia o el Antiguo Testamento, con colores cálidos y una atmósfera de fraternalidad, estilo artista renacentista."
* **Anti-Prompt**: "violencia, pelea, conflicto, hermanos separados, ambiente oscuro, colores fríos, estilo de arte moderno o abstracto, no incluir a personas de afuera, evitar imágenes de desastres o caos"

### Frase 4:

* **Oración**: "Cristobal Colón prendió una fogata, Llegaron los indios y prendió la mata."
* **Prompt**: ""Una pintura de estilo épico de Cristóbal Colón prendiendo una fogata en una playa tropical, mientras que un grupo de indígenas llegan al lugar con una mata en las manos, en un entorno primitivo y boscoso, con detalles de la ropa y el barco de Colón en la distancia."
* **Anti-Prompt**: "ciudad moderna, automóviles, edificios altos, personas normales, objetos tecnológicos, iluminación brillante"


---


## Resultado Final

Se generó un archivo GIF combinando todas las imágenes generadas (con y sin texto) por ambos modelos para cada frase, lo que permite una comparación visual efectiva entre estilos y resultados. Cada imagen generada con texto incluye también el nombre del modelo que la produjo, lo cual facilita la evaluación directa de diferencias estilísticas entre FLUX y Stable Diffusion.
