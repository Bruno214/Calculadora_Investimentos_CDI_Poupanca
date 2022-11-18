# # Juros compostos .
#
# É a adição de juros ao capital principal de um empréstimo ou depósito ,
# ou em outras palavras , juros sobre juros .
#
# É o resultado do reinvestimento dos juros , ao invés de pagá -lo ,
# de tal forma que a taxa no próximo período é calculada
# sobre o principal , mais os juros recebidos previamente .
#
# A função de acumulação mostra como uma unidade monetária
# cresce após o período de tempo .
#
# @param r taxa de juros nominal .
# @param t período de tempo total no qual os juros são aplicados
# ( expressa nas mesmas unidades de tempo de r , usualmente anos ).
# @param n frequência de composição ( pagamento dos juros ) , por exemplo ,
# mensal , trimestral ou anual .
# @return juros obtidos no período : (1 + r/n)nt − 1
#

import math
from typing import Any


class Funcs:

    def jc(self, r: float, t: int, n: int = 1) -> float:
        return (1 + r / float(n)) ** (n * t) - 1

    # # Converte uma taxa diária para uma taxa anual .
    # Em matemática financeira , consideramos 252 dias por ano .
    #
    # @param d taxa de juros diária .
    # @param wd número de dias úteis por ano .
    # @return taxa de juros anual dada a taxa diária ,
    # na forma de um percentual .
    def day2year(self, d: float, wd: int = 252) -> float:
        return 100 * self.jc(d, wd)

    # # Converte uma taxa de juros anual para uma taxa mensal .
    #
    # @param a taxa de juros anual .
    # @return taxa de juros mensal dada a taxa anual ,
    # na forma de um percentual .
    def year2month(self, a: float) -> float:
        return 100 * self.jc(a, 1 / 12.0)

    # # Calcula log1+r 2 ( logaritmo de 2 na base 1 + r).
    # Pode ser aproximado por 72/(100 ∗ r).
    #
    # É usada para calcular o tempo necess á rio
    # para dobrar o principal quando sujeito uma taxa de juros dada .
    #
    # @param r taxa de juros nominal .
    # @return tempo para dobrar o principal .
    def doublePrincipal(self, r: float) -> float:
        return math.log(2, 1 + r)

    # Converte uma taxa de juros mensal para uma taxa diária
    #
    # @param a taxa de juros mensal.
    # @return taxa de juros diária dada a taxa mensal,
    # na forma de um percentual.
    def year2day(self, a: float) -> float:
        return 100 * self.jc(a, 1 / 252.0)

    # Metodo que calcula a rentabilidade em função do cdi
    #
    # @param t rentabilidade do rendimento
    # @param a taxa de 100% cdi ao ano
    # @return rentabilidade anual em cima do cdi
    def rentabilidade(self, t: float, a: float) -> float:
        return (t * a) / 100

    # metodo que calcula a rentabilidade com Impostos
    # @param t é a rentabilidade
    # @param a é a taxa do cdi
    # @param i é o alíquota do imposto de renda
    # @return rentabilidade com impostos e a porcentagem do cdi
    def rentabilida_com_impostos(self, t: float, a: float, i: float) -> 'list[float]':
        return [t * (1 - (i / 100)), t * a * (1 - (i / 100))]

    # metodo para aplicar o imposto de renda ao liquido bruto da aplicação
    # @param montante é o liquido bruto do rendimento
    # @param c é o capital investido
    # @param i é a aliquota do imposto de renda
    # @return o rendimento bruto descontando o imposto de renda
    def aplicarImpostoRenda(self, montante: float, c: float, i: float) -> float:
        return montante - ((montante - c) * i / 100)

    # metodo responsavel por calcular o montante liquido da aplicação
    # @param c é o capital investido
    # @param m é o periodo dado em meses
    # @param t é rendimento desda aplicação
    # @param i é o alíquota do imposto de renda
    # @return o montante líquido dessa aplicação no periodo informado
    def montanteLiquidoAplicacao(self, c: float, m: int, t: float, i: float, a: float) -> float:
        montante = self.liquidoBruto(c, m, t, a)
        return self.aplicarImpostoRenda(montante, c, i)

    # Metodo que calcula o liquido bruto da aplicação
    # @param c é o capital investido
    # @param m é a quantidade de meses
    # @param t é o rendimento em %
    # @param a é a taxa do cdi #ATENÇÂO ++++++++++++++++==========
    # @return liquido Bruto da aplicação
    def liquidoBruto(self, c: float, m: int, t: float, a: float) -> float:
        rentabilidadeAplicacao = self.rentabilidade(t, a)
        liquiBruto = c * (1 + self.year2month(rentabilidadeAplicacao) / 100) ** m
        return liquiBruto

    # faz a cheacagem da taxa de juros da poupança em,
    # comparação a selic.
    # @param s é a taxa de juros da selic ao ano
    # @return lista com 2 valores o primeiro é a taxa ao ano,
    # e a segunda a taxa ao mes
    def checkRendPoupanca(self, s: float) -> 'list[float]':
        if s * 100 < 8.5:
            return [(s * 100) * 0.70, self.year2month(s)]
        else:
            return [6.17, 0.5]

    # calcula o rendimento da poupança
    # @param c é o capital investido
    # @param p é a taxa de juros anual da poupança
    # @param m é a quantidade de meses
    # @return o rendimento da poupança no período de tempo informado
    def rendimentoPoupanca(self, c: float, p: float, m: int) -> float:
        # convertendo o rendimento de anos para meses
        p = self.year2month(p / 100)
        return c * (1 + (p / 100)) ** m

    # calcula a taxa do cdi ao mes e ao dia
    # @param a é a taxa do cdi ao ano
    # @return a taxa do cdi ao mes e ao dia
    def cdiAoMesDia(self, a: float) -> tuple[float, float]:
        cdiAoMes = self.year2month(a)
        cdiAoDia = self.year2day(a)
        return cdiAoMes, cdiAoDia

    # metodo que é usado para calcular o rendimento no periodo,
    # e a diferença da aplicação e da poupança no mesmo periodo
    # @param c capital
    # @param montAplica é o montante liquido da aplicação
    # @param montPoupan é o montante liquido da poupança
    # @return rendimento no periodo(meses)em % e ,
    # e a diferença de rendimento em reais
    def porcenDifencaEmMeses(self, c: float, montAplica: float, montPoupan: float) -> tuple[float, float]:
        rendMeses = ((montAplica - c) / 100) * 1000 / 100
        diferencaMMeses = ((montAplica - montPoupan) / 100) * c / 100
        return rendMeses, diferencaMMeses

    # Metodo que utiliza de outro metodo para saber em quanto tempo
    # vou dobra o capital investido
    # @param taxaJuros porcentegem de rendimento ao ano
    # @return retorna o tempo total em anos e meses
    def dobraCapital(self, taxaJuros: float) -> tuple[float, float]:
        aoAno = self.doublePrincipal(taxaJuros / 100)
        aoMes = aoAno * 12
        return aoAno, aoMes

    def help(self):
        print("Usage ./ cdi . py -c [ capital ] -a [ CDI anual ] -s [ Selic ]" +
              " -i [ alíquota IR ] -t [ taxa CDI ] -m [ ""meses ] -h [ help ]")

    # # Calcula o montante final , imposto , rendimento e
    # rentabilidade equivalente .
    #
    # @param c capital
    # @param cdi taxa cdi anual
    # @param p taxa poupança anual = 0.70 * selic
    # @param t rentabilidade da aplicação em função do CDI
    # @param i alíquota do imposto de renda
    # @param m meses
    # @return
    # - montante da aplicação ,
    # - montante poupança ,
    # - imposto de renda retido ,
    # - rendimento em m meses (%) ,
    # - rendimento em m meses ,
    # - rendimento líquido em 1 m ês ,
    # - rentabilidade para igualar poupança (%) CDI
    #

    def CDB(self, c: float, cdi: float, p: float, t: float,
            i: float, m: int = 1) -> tuple[float, Any, Any, float, float, float]:

        montante_aplicacao = self.montanteLiquidoAplicacao(c, m, t, i, cdi)
        montante_poupanca = self.rendimentoPoupanca(c, p, m)

        liq_Bruto = self.liquidoBruto(c, m, t, cdi)
        imposto = liq_Bruto - self.aplicarImpostoRenda(liq_Bruto, c, i)
        rendi_Meses, difer_Meses_Apl_Pou = self.porcenDifencaEmMeses(c, montante_aplicacao, montante_poupanca)

        igualar_Poup_Cdi = p / (cdi * (1 - (i / 100)))

        return igualar_Poup_Cdi, rendi_Meses, difer_Meses_Apl_Pou, imposto, montante_aplicacao, montante_poupanca
