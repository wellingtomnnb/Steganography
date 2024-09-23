# Steganography
API de ocultação de informações baseando-se em esteganografia.

Esse recurso apresenta duas funções principais: **transliteração** e **inserção de caracteres invisíveis**, que podem ser aplicadas em diferentes cenários, como:

* **Ofuscação de texto:** O código transforma letras latinas em equivalentes visuais de outros alfabetos (como cirílico e grego), dificultando a leitura por sistemas automáticos ou buscas de texto simples. Isso é útil para contornar filtros de conteúdo ou algoritmos que detectam determinadas palavras.

* **Proteção contra cópia ou detecção automática:** Inserir caracteres invisíveis (`\u200B`, `\u200C`, `\u200D`) entre as letras faz com que o texto pareça o mesmo para o olho humano, mas seja diferente internamente. Isso pode ser usado para evitar que o texto seja facilmente copiado e reutilizado, ou para burlar verificações automáticas de similaridade.

* **Contornar algoritmos de detecção de spam ou conteúdo sensível:** A combinação de caracteres visuais de outros alfabetos com caracteres invisíveis pode ser usada para impedir que o texto seja detectado por sistemas de moderação automatizada.

* **Criação de armadilhas digitais:** Inserir caracteres invisíveis em textos pode servir para rastrear quem copia ou compartilha o conteúdo, já que o texto alterado contém uma "marca" oculta que é difícil de remover.