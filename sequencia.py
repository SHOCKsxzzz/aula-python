total = float(input("total da compra: "))
if total > 500:
    desconto = 10
elif total > 1000:
    desconto = 10
else:
    desconto = 0
    print(f"o desconto: {desconto}%")