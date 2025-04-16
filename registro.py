def registro(nome, idade, telefone, email):

    if " " in nome and "48" in telefone and "@" in email:
        return {
            "nome":nome,
            "telefone":telefone,
            "email": email,
            "idade": idade
        }
    else:
        return "Dados inválidos"