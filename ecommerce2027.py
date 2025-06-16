import sqlite3

conexao = sqlite3.connect("db/loja.db")
cursor = conexao.cursor()

categorias = [
    ("Vendas", "receita"),
    ("Frete", "receita"),
    ("Compra de estoque", "despesa"),
    ("Publicidade", "despesa"),
    ("Serviços", "despesa")
]

cursor.executemany("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", categorias)

transacoes = [
    ("2025-04-01", "Venda via site", 1500.00, 1),
    ("2025-04-02", "Frete cliente SP", 30.00, 2),
    ("2025-04-03", "Compra de tênis", -800.00, 3),
    ("2025-04-04", "Google Ads", -200.00, 4),
    ("2025-04-05", "Consultoria", -150.00, 5),
    ("2025-04-06", "Venda via Instagram", 750.00, 1)
]

cursor.executemany("INSERT INTO transacoes (data, descricao, valor, categoria_id) VALUES (?, ?, ?, ?)", transacoes)
conexao.commit()
conexao.close()
print("✅ Dados inseridos com sucesso!")