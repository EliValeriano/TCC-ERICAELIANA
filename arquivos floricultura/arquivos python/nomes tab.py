import sqlite3

nome_banco = "Floricultura.db"
con = sqlite3.connect(nome_banco)
cur = con.cursor()


produtos_Floricultura= [
(None, 'Arranjos Líricos e Rosas Vermelhas', 139.00),
(None, 'Delicado Mix De Flores Silvestres', 108.90),
(None,'Linda Begônia Vermelha Plantada', 129.90),
(None, 'Lírios Plantados', 119.90),
(None, 'Flores do Campo', 168.10),
(None, 'Buquê Partitura Flores do Campo', 49.90),
(None, 'Kit Decoração Buquê Astromélias Com Folhagens + Vaso Rosa', 167.15),
(None, '10 Alstroemérias de Canto - Creme', 100.00),
(None, 'Arranjo de Flores do Campo em Tons Suaves', 109.90),
(None, 'Boque de Rosas 5 unidades', 50.00),
]

cur.executemany("INSERT INTO Floricultura VALUES (?, ?, ?"), Floricultura)

con.commit()
con.close()