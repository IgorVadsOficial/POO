"""
Atividade Prática – Classes Abstratas e Polimorfismo com Contas Bancárias
Autor: Professor Demetrios A. M. Coutinho – IFRN

Objetivo:
- Praticar conceitos de herança, polimorfismo e classes abstratas em Python.
- Utilizar o módulo abc para restringir a instância de classes base abstratas.
- Aplicar sobrescrita de métodos (override) e uso correto de super().

Hierarquia das classes:

            Conta (classe abstrata)
              ↑       ↑         ↑
     ContaCorrente  ContaPoupanca  ContaInvestimento

CONTRATO (método obrigatório):
- Toda subclasse de Conta DEVE implementar o método:

    @abc.abstractmethod
    def atualiza(self, taxa):
        pass

Caso contrário, um erro será gerado ao tentar instanciar.

-----------------------------------
1. A classe Conta deve:
-----------------------------------
- Ser abstrata (herdar de abc.ABC).
- Ter os atributos: número, titular, saldo (default=0), limite (default=1000).
- Ter o método abstrato: atualiza(self, taxa).
- Ter o método deposita(self, valor): soma o valor ao saldo.
- Ter o método __str__() que imprime todos os dados da conta + tipo da conta.

-----------------------------------
2. A classe ContaCorrente deve:
-----------------------------------
- Herda de Conta.
- Implementar atualiza(self, taxa): saldo *= (1 + taxa * 2).
- Redefinir deposita(self, valor): desconta taxa de 0.10.
- Ter um atributo tipo = "Conta Corrente".

-----------------------------------
3. A classe ContaPoupanca deve:
-----------------------------------
- Herda de Conta.
- Implementar atualiza(self, taxa): saldo *= (1 + taxa * 3).
- Ter um atributo tipo = "Conta Poupança".

-----------------------------------
4. A classe ContaInvestimento deve:
-----------------------------------
- Herda de Conta.
- Implementar atualiza(self, taxa): saldo *= (1 + taxa * 5).
- Ter um atributo tipo = "Conta Investimento".

-----------------------------------
5. Classe auxiliar: AtualizadorDeContas
-----------------------------------
A classe `AtualizadorDeContas` serve para **percorrer diversas contas** e **atualizar seus saldos com base em uma taxa padrão**, chamada de **selic**. Além disso, ela mantém o **saldo total acumulado** de todas as contas que foram atualizadas até o momento.

Atributos:
- `self._selic`: a taxa percentual de atualização, fornecida no momento da criação.
- `self._saldo_total`: acumulador que armazena o total atualizado de todas as contas processadas (inicializado como zero).

Métodos:
- `roda(self, conta)`:
    - Imprime o saldo **anterior** da conta.
    - Aplica `conta.atualiza(self._selic)`, que modifica o saldo da conta.
    - Soma o saldo **atualizado** ao atributo `self._saldo_total`.
    - Imprime o novo saldo da conta.


-----------------------------------
Exemplo de uso:
-----------------------------------
if __name__ == '__main__':
    cc = ContaCorrente('123-4', 'João', 1000.0)
    cp = ContaPoupanca('123-5', 'Maria', 2000.0)
    ci = ContaInvestimento('123-6', 'Carlos', 3000.0)

    cc.deposita(500.0)
    cp.deposita(1000.0)
    ci.deposita(1500.0)

    adc = AtualizadorDeContas(0.01)

    adc.roda(cc)
    adc.roda(cp)
    adc.roda(ci)

    print(f"Saldo total acumulado: {adc.saldo_total}")

-----------------------------------
Restrições:
-----------------------------------
- A classe Conta não pode ser instanciada.
- Subclasses que não implementarem atualiza() gerarão erro.
- Não usar isinstance() ou type(); siga o estilo Duck Typing.

-----------------------------------
Desafio:
-----------------------------------
- Crie uma classe Banco que armazena contas, com métodos:
    - adiciona()
    - pegaConta()
    - totalContas()
- Aplique AtualizadorDeContas em todas as contas via loop.

Bom trabalho!
"""
