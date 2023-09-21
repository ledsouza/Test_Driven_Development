from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000' # Given-Contexto
        esperado = 23
        
        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() #When-ação
        
        assert resultado == esperado # Then-desfecho
        
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' # Given
        esperado = 'Carvalho'
        
        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # When
        
        assert resultado == esperado # Then-desfecho
        
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 10000 # Given
        entrada_nome = 'Paulo Bragança'
        esperado = 9000
        
        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # When
        resultado = funcionario_teste.salario
        
        assert resultado == esperado # Then