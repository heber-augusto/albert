.. albert documentation master file, created by
   sphinx-quickstart on Thu Oct 14 20:14:36 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=======================
Documentação do Albert
=======================

Bem-vindo à documentação do Albert, uma biblioteca para facilitar o teste, execução e implantação de modelos de Aprendizado de Máquina Generativo.

.. note::

    Versão testada atualmente com Python 3.10.

.. note::

    Sistema operacional testado: Ubuntu 22.04.

.. note::

    Repositório da biblioteca no GitHub: `https://github.com/heber-augusto/albert <https://github.com/heber-augusto/albert>`_.

Instalação
----------

Para instalar a biblioteca Albert, você pode utilizar o comando pip. Execute o seguinte comando no seu ambiente Python:

.. code-block:: shell

    pip install git+https://github.com/heber-augusto/albert.git

Introdução
----------

O Albert é uma biblioteca projetada para simplificar o ciclo de vida de projetos de Aprendizado de Máquina Generativo, como modelos de linguagem ou modelos de geração de texto. Ele fornece comandos de linha que facilitam a criação, execução e implantação desses modelos.

Com o Albert, você pode:

- **Criar** novos tipos de trabalhos de machine learning, seja para tarefas de inferência de modelos pré-treinados ou para ajuste fino (fine-tuning).

- **Executar** esses trabalhos em ambientes apropriados.

- **Implantar** modelos de machine learning em produção para uso em aplicações reais.

- **Verificar** os testes associados ao seu projeto para garantir que tudo funcione conforme o esperado.

O Albert é uma ferramenta poderosa que ajuda a acelerar o desenvolvimento de projetos de Aprendizado de Máquina Generativo, tornando o processo mais eficiente e produtivo.

.. note::

    Certifique-se de explorar a documentação detalhada sobre os comandos disponíveis e como utilizá-los para melhorar seu fluxo de trabalho de machine learning.

.. toctree::
   :maxdepth: 2
   :caption: Conteúdo da Documentação

   command_create
   command_run
   command_deploy
   command_check

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
