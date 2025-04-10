import os
import xml.etree.ElementTree as ET

# Caminho onde estão os arquivos XML das notas
caminho_das_notas = 'notas_fiscais/'

for arquivo in os.listdir(caminho_das_notas):
    if arquivo.endswith('.xml'):
        caminho_completo = os.path.join(caminho_das_notas, arquivo)
        tree = ET.parse(caminho_completo)
        root = tree.getroot()
        
        # Namespace da NF-e
        ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

        # Pega o valor total declarado da nota
        valor_total = float(root.find('.//nfe:vNF', ns).text)

        # Soma os valores dos produtos
        produtos = root.findall('.//nfe:det', ns)
        soma_produtos = 0.0
        for produto in produtos:
            valor_produto = float(produto.find('.//nfe:vProd', ns).text)
            soma_produtos += valor_produto

        # Verifica diferença
        if abs(soma_produtos - valor_total) > 0.01:
            print(f"⚠️ Inconsistência na nota {arquivo}")
            print(f"➡️ Total declarado: R${valor_total:.2f} | Soma dos produtos: R${soma_produtos:.2f}")
            print()

