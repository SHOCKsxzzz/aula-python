#Cantina da Dona Marta 
cardapio = {
    1: {"produto": "Coxinha", "preco": 6.50},
    2: {"produto": "Pão de queijo", "preco": 4.00},
    3: {"produto": "Suco natural", "preco": 5.00},
    4: {"produto": "Refrigerante lata", "preco": 6.00},
    5: {"produto": "Bolo do dia", "preco": 4.50}
}

total_pedidos_dia = 0
faturamento_dia = 0.0

nome_cantina = "Cantina da Dona Marta"
print(f"=== {nome_cantina} ===")

while True:
    print("\n--- Novo Atendimento (digite 'SAIR' no nome para fechar o caixa) ---")
    nome_cliente = input("Nome do cliente: ").strip()
    if nome_cliente.upper() == "SAIR":
        break
        
    print(f"Olá, {nome_cliente}! Veja o cardápio:")
    
    for codigo, item in cardapio.items():
        print(f"{codigo} - {item['produto']}: R$ {item['preco']:.2f}")
    
    subtotal_pedido = 0.0
    
    while True:
        try:
            codigo = int(input("\nCódigo do produto (0 para finalizar): "))
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue

        if codigo == 0:
            break
            
        if codigo not in cardapio:
            print("Código inexistente! Digite um código de 1 a 5 ou 0 para finalizar.")
            continue
            
        try:
            quantidade = int(input("Quantidade: "))
        except ValueError:
            print("Por favor, digite um número inteiro válido para a quantidade.")
            continue

        if quantidade < 1:
            print("Quantidade inválida! A quantidade deve ser no mínimo 1.")
            continue
            
        produto_nome = cardapio[codigo]["produto"]
        preco_unitario = cardapio[codigo]["preco"]
        valor_item = preco_unitario * quantidade
        
        subtotal_pedido += valor_item
        print(f"Adicionado: {quantidade} x {produto_nome} R$ {valor_item:.2f}")

    if subtotal_pedido == 0:
        print("Nenhum item foi adicionado ao pedido.")
        continue
    desconto_percentual = 0
    
    if subtotal_pedido >= 30.00:
        desconto_percentual += 10
        
    tem_gremio = input("Possui carteirinha do grêmio? (S/N): ").strip().upper()
    if tem_gremio == 'S':
        desconto_percentual += 5
        
    valor_desconto = subtotal_pedido * (desconto_percentual / 100)
    total_final = subtotal_pedido - valor_desconto

    print(f"\nSubtotal: R$ {subtotal_pedido:.2f}")
    if desconto_percentual > 0:
        print(f"Desconto aplicado ({desconto_percentual}%): -R$ {valor_desconto:.2f}")
    print(f"Total a pagar: R$ {total_final:.2f}")


    valor_pago = 0.0
    while valor_pago < total_final:
        try:
            valor_pago = float(input("Valor pago: R$ "))
            if valor_pago < total_final:
                falta = total_final - valor_pago
                print(f"Valor insuficiente! Faltam R$ {falta:.2f}")
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

    troco = valor_pago - total_final
    print(f"Troco: R$ {troco:.2f}")
    
    total_pedidos_dia += 1
    faturamento_dia += total_final

print("\n=== Fechamento do Caixa ===")
print(f"Total de pedidos realizados: {total_pedidos_dia}")
print(f"Faturamento total do dia: R$ {faturamento_dia:.2f}")
print("Caixa encerrado com sucesso!")