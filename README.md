1. Introdução:

O objetivo deste projeto é criar um registrador de vendas utilizando Python, SQLite e Flask. A aplicação permite que os usuários registrem, visualizem, editem, removam e filtrem vendas através de uma interface web. Este projeto é ideal para pequenas empresas ou indivíduos que precisam de uma maneira simples e eficiente de gerenciar suas vendas diárias.

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

4.2. Visualizar Vendas:

Exibe todas as vendas registradas em uma tabela na página principal.
Cada linha da tabela representa uma venda com seus respectivos detalhes.

4.3. Remover Venda:

Permite que o usuário remova uma venda específica clicando em um botão "Remover" ao lado da venda na tabela.

4.4. Editar Venda:

Permite que o usuário edite os detalhes de uma venda existente.
O usuário é redirecionado para uma página de edição onde pode atualizar os campos da venda.

4.5. Filtrar Vendas:

Permite que o usuário aplique filtros para visualizar vendas específicas com base no produto e/ou data.
Os filtros são aplicados através de um formulário na página principal.
Exibe apenas as vendas que correspondem aos critérios de filtro.
