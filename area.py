def area_retangulo(base, altura):
    """Calcula a área de um retângulo"""
    return base * altura

def main():
    b = float(input("base:"))
    h = float(input("altura:"))
    a = area_retangulo(b, h)
    print(f"area = {a:.2f}")

main()
