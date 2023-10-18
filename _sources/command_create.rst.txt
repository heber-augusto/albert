.. _command_create:

==============
Comando Create
==============

O comando "create" da biblioteca "albert" é usado para criar um novo tipo de trabalho (job type) que pode ser de dois tipos: "inference" ou "finetuning". O tipo de trabalho a ser criado é especificado como argumento.

Este comando é útil para iniciar um novo projeto de machine learning, seja para tarefas de inferência de modelos pré-treinados ou para ajuste fino (fine-tuning).

Uso
---

.. code-block:: shell

    albert create <jobtype> <folder_name> [<destination_folder>]

- `<jobtype>`: Especifique o tipo de trabalho, que pode ser "inference" ou "finetuning".
- `<folder_name>`: Forneça um nome de pasta para identificar o trabalho.
- `[<destination_folder>]` (opcional): Especifique a pasta de destino onde o trabalho será criado. Se não fornecido, a pasta atual será usada.

Exemplo
-------

Para criar um novo trabalho de inferência com o nome "my_inference_job", você pode executar o seguinte comando:

.. code-block:: shell

    albert create inference my_inference_job

Isso criará a estrutura de pastas necessária para o trabalho de inferência.

.. note::

    Certifique-se de ter configurado um arquivo de configuração apropriado para seu trabalho antes de usar o comando "create". Este comando é o primeiro passo na criação de um novo projeto.

