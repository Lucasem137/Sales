1. Introdução:

O objetivo deste projeto é criar um registrador de vendas utilizando Python, SQLite e Flask. A aplicação permite que os usuários registrem, visualizem, editem, removam e filtrem vendas através de uma interface web. Este projeto é ideal para pequenas empresas ou indivíduos que precisam de uma maneira simples e eficiente de gerenciar suas vendas diárias.

![Captura de tela 2025-04-07 151245](https://github.com/user-attachments/assets/5ff3951d-7f54-48b9-a3b5-028e1d57c893)

2. Descrição das Tabelas e Campos:

A aplicação utiliza uma única tabela no banco de dados SQLite chamada vendas. A estrutura da tabela é a seguinte:

id: INTEGER PRIMARY KEY - Identificador único para cada venda.
produto: TEXT - Nome do produto vendido.
quantidade: INTEGER - Quantidade do produto vendido.
preço: REAL - Preço do produto vendido.
data: TEXT - Data da venda.

3. Lista das Bibliotecas Utilizadas:

Flask: Um micro framework para Python que facilita a criação de aplicações web.
sqlite3: Utilizada para criar e manipular o banco de dados de vendas.

4. Descrição das Funcionalidades Implementadas:

4.1. Adicionar Venda:

Permite que o usuário adicione uma nova venda preenchendo um formulário com os campos: produto, quantidade, preço e data.

![Captura de tela 2025-04-07 151023](https://github.com/user-attachments/assets/f4dce02d-7c5c-4fef-82b2-1f583527767a)

4.2. Visualizar Vendas:

Exibe todas as vendas registradas em uma tabela na página principal.
Cada linha da tabela representa uma venda com seus respectivos detalhes.

![Captura de tela 2025-04-07 150932](https://github.com/user-attachments/assets/6379aa69-a944-4c15-aa30-45de83921944)

4.3. Remover Venda:

Permite que o usuário remova uma venda específica clicando em um botão "Remover" ao lado da venda na tabela.

![Captura de tela 2025-04-07 151110](https://github.com/user-attachments/assets/31fe4517-9769-4671-ada2-ca0b55aca288)

4.4. Editar Venda:

Permite que o usuário edite os detalhes de uma venda existente.
O usuário é redirecionado para uma página de edição onde pode atualizar os campos da venda.

![Captura de tela 2025-04-07 151126](https://github.com/user-attachments/assets/16ec95e3-10e7-41e3-9632-dedc0bc88218)

4.5. Filtrar Vendas:

Permite que o usuário aplique filtros para visualizar vendas específicas com base no produto e/ou data.
Os filtros são aplicados através de um formulário na página principal.
Exibe apenas as vendas que correspondem aos critérios de filtro.

![Captura de tela 2025-04-07 151149](https://github.com/user-attachments/assets/a3f6ff33-7e54-42ee-a8b7-be0c5beeaaf2)
