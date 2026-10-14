def saudacao(nome, saudacao="ola"):
    """monta uma saudação"""
    return f"{saudacao}, {nome}!"

print(saudacao("João"))
print(saudacao("Maria", "bom dia"))