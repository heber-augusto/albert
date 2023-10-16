.. _command_check:

============
Comando Check
============

O comando "check" da biblioteca "albert" é usado para verificar os testes de um tipo de trabalho de machine learning previamente criado. Isso é essencial para garantir que o trabalho está funcionando corretamente e que as alterações não introduziram erros.

Uso
---

.. code-block:: shell

    albert check

O comando "check" não requer argumentos adicionais, pois ele opera com base nas configurações e no tipo de trabalho definido durante a criação do projeto.

Exemplo
-------

Para verificar os testes de um trabalho de inferência ou fine-tuning chamado "my_job", simplesmente execute o comando:

.. code-block:: shell

    albert check

Este comando executará testes relevantes ao tipo de trabalho e fornecerá informações sobre o sucesso ou falha dos testes.

.. note::

    Certifique-se de que seu trabalho foi configurado corretamente e que os testes relevantes foram definidos antes de usar o comando "check".

