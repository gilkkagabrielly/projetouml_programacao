
class Usuario:
    def __init__(self, nome, idade):
        # Valores iniciais seguros
        self.__nome = "Usuário"
        self.__idade = 12

        # Validação dos dados
        self.set_nome(nome)
        self.set_idade(idade)

    # Getter do nome
    def get_nome(self):
        return self.__nome

    # Setter do nome
    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) >= 3:
            self.__nome = nome.strip()
        else:
            print("Erro: o nome deve ter pelo menos 3 caracteres.")

    # Getter da idade
    def get_idade(self):
        return self.__idade

    # Setter da idade
    def set_idade(self, idade):
        if isinstance(idade, int) and not isinstance(idade, bool) and idade >= 12:
            self.__idade = idade
        else:
            print("Erro: a idade deve ser um número inteiro maior ou igual a 12.")


# ==============================================================================
# TESTE DE VALIDAÇÃO DO PROJETO FINAL
# ==============================================================================
if __name__ == "__main__":
    print("=== TESTANDO A CLASSE BASE DO PROJETO FINAL ===")

    # 1. Teste de instanciação com dados válidos
    usuario_valido = Usuario("Gilkka", 17)
    print(
        f"Usuário criado: {usuario_valido.get_nome()} - "
        f"{usuario_valido.get_idade()} anos"
    )

    # 2. Teste de instanciação com dados inválidos
    print("\n--- Teste 1: Tentativa de criar com idade negativa ---")
    usuario_invalido = Usuario("Maria", -5)
    print(
        f"Resultado mantido com segurança: "
        f"{usuario_invalido.get_idade()} anos"
    )

    # 3. Teste de alteração via Setter com dado inválido
    print("\n--- Teste 2: Tentativa de alterar o nome para um texto muito curto ---")
    usuario_valido.set_nome("AB")
    print(f"Nome do usuário protegido: {usuario_valido.get_nome()}")
