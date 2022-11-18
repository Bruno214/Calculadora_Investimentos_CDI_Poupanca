from tkinter import *
from Functions import Funcs


class Resultado(Funcs):
    def __init__(self):
        self.root_resultado = None
        self.cor_bg_frame = "lightgray"

    def janela_resultado(self):
        self.root_resultado = Toplevel()
        self.root_resultado.title("Calculos")
        self.root_resultado.geometry("900x600")
        self.frameJanela2()

    def frameJanela2(self):
        self.resul_f1 = Frame(self.root_resultado, bg=self.cor_bg_frame, highlightbackground='green',
                              highlightthickness=15)
        self.resul_f1.place(relx=0.02, rely=0.05, relwidth=0.55, relheight=0.45)
        self.result_frame1()

        self.resul_f2 = Frame(self.root_resultado, highlightbackground='blue', highlightthickness=15, bg=self.cor_bg_frame)
        self.resul_f2.place(relx=0.60, rely=0.05, relwidth=0.37, relheight=0.45)
        self.result_frame2()

        self.resul_f3 = Frame(self.root_resultado, highlightbackground='red', highlightthickness=15, bg=self.cor_bg_frame)
        self.resul_f3.place(relx=0.02, rely=0.55, relwidth=0.55, relheight=0.40)
        self.result_frame3()

    def result_frame1(self):
        self.capital = float(self.sb_capi.get())
        capital = f"Capital: ${self.capital:.2f}"
        Label(self.resul_f1, text=capital, bg=self.cor_bg_frame,
              font=("Verdana", 10, "bold")).place(relx=0.02, rely=0.03)

        taxa_selic = str(self.sb_taxa_selic.get())
        Label(self.resul_f1, text="Taxa Selic: $" + taxa_selic + " % ao ano",
              font=("Verdana", 10, "bold"), bg=self.cor_bg_frame).place(relx=0.02, rely=0.12)

        # CDI ao ano ao mes ao dia
        self.taxa_cdi = float(self.sb_taxa_cdi.get()) / 100
        cdi_ao_mes, cdi_ao_dia = self.cdiAoMesDia(self.taxa_cdi)
        CDI = f"CDI: {self.taxa_cdi * 100}% ao ano = {cdi_ao_mes:.4f}% ao mês = {cdi_ao_dia:.6f}% ao dia"
        Label(self.resul_f1, text=CDI, font=("Verdana", 10, "bold"), bg=self.cor_bg_frame).place(relx=0.02, rely=0.22)

        # Taxa poupança ao ano e ao mês
        self.poupancaAoAno, poupancaAoMes = self.checkRendPoupanca(float(taxa_selic))
        taxa_poupanca = f"Taxa Poupança: {self.poupancaAoAno}% ao ano = {poupancaAoMes:.4f}% ao dia"
        Label(self.resul_f1, text=taxa_poupanca,
              font=("Verdana", 10, "bold"), bg=self.cor_bg_frame).place(relx=0.02, rely=0.32)

        # IR imposto de renda
        self.IR = float(self.valor.get())
        IRstr = f"IR: {self.valor.get()}%"
        Label(self.resul_f1, text=IRstr,
              font=("Verdana", 10, "bold"), bg=self.cor_bg_frame).place(relx=0.02, rely=0.42)

        # Rentabilidade
        self.rent = float(self.sb_taxa_rent.get())
        rentabilidade = f"Rentabilidade: {self.rent:.1f}% CDI = {float(self.rentabilidade(self.rent, self.taxa_cdi)) * 100}% ao ano"
        Label(self.resul_f1, text=rentabilidade,
              font=("Verdana", 10, "bold"), bg=self.cor_bg_frame).place(relx=0.02, rely=0.52)

        # Rentabilidade com Impostos
        rent_impo_cdi = self.rentabilida_com_impostos(self.rent, self.taxa_cdi, self.IR)
        formatado_ren_impostos = f"Com impostos: {rent_impo_cdi[0]:.2f}% CDI = {rent_impo_cdi[1]:.2f}% ao"
        Label(self.resul_f1, text=formatado_ren_impostos,
              font=("Verdana", 10, "bold"), bg=self.cor_bg_frame).place(relx=0.02, rely=0.62)

        # Meses
        self.mes = int(self.sb_mes.get())
        form_meses = f"Meses: {self.mes}"
        Label(self.resul_f1, text=form_meses,
              font=("Verdana", 10, "bold"), bg=self.cor_bg_frame).place(relx=0.02, rely=0.72)

    def result_frame2(self):
        self.igualarPoupCdi, rendiEmMMeses, self.difeEMMmeses, imposto, montante_aplicacao, montante_poupanca = self.CDB(
            self.capital, self.taxa_cdi, self.poupancaAoAno, self.rent, self.IR, self.mes)

        # montante da aplicação
        mont_apli = f"Montante Aplicação = ${montante_aplicacao:.2f}"
        Label(self.resul_f2, text=mont_apli,
              font=("Verdana", 10, "bold"), bg=self.cor_bg_frame).place(relx=0.02, rely=0.03)

        # Montante poupança

        mont_pou = f"Montante Poupança = ${montante_poupanca:.2f}"
        Label(self.resul_f2, text=mont_pou,
              font=("Verdana", 10, "bold"), bg=self.cor_bg_frame).place(relx=0.02, rely=0.15)

        # Aplicao diferença com a poupança
        apl_poup = f"Apl - Poup ({self.mes} meses) = ${montante_aplicacao - montante_poupanca:.2f}"

        Label(self.resul_f2, text=apl_poup,
              font=("Verdana", 10, "bold"), bg=self.cor_bg_frame).place(relx=0.02, rely=0.27)

        # imposto
        imposto = f"Imposto = ${imposto:.4f}"
        Label(self.resul_f2, text=imposto,
              font=("Verdana", 10, "bold"), bg=self.cor_bg_frame).place(relx=0.02, rely=0.39)

        # Rendimento na quantidade de Meses
        rend_mes = f"Rendimento em {self.mes} meses = {rendiEmMMeses:.4f}%"
        Label(self.resul_f2, text=rend_mes,
              font=("Verdana", 10, "bold"), bg=self.cor_bg_frame).place(relx=0.02, rely=0.51)

    def result_frame3(self):
        # diferença em meses
        dif_mes = f"Ap1 - Poup ({self.mes} meses) = {self.difeEMMmeses:.4f}%"
        Label(self.resul_f3, text=dif_mes,
              font=("Verdana", 10, "bold"), bg=self.cor_bg_frame).place(relx=0.02, rely=0.03)

        # igular com a poupança
        igua_poup = f"Apl = Poup = {self.igualarPoupCdi:.2f}% CDI"
        Label(self.resul_f3, text=igua_poup,
              font=("Verdana", 10, "bold"), bg=self.cor_bg_frame).place(relx=0.02, rely=0.15)

        # rentabilidade em anos
        renta_anual_apl = self.rentabilida_com_impostos(self.rent, self.taxa_cdi, self.IR)[1]

        # tempo para dobrar poupança
        dobrar_poup = f"Tempo 2 x Poupança = {self.dobraCapital(self.poupancaAoAno)[0]:.2f} anos = {self.dobraCapital(self.poupancaAoAno)[1]:.2f} meses"
        Label(self.resul_f3, text=dobrar_poup,
              font=("Verdana", 10, "bold"), bg=self.cor_bg_frame).place(relx=0.02, rely=0.27)

        # tempo para dobrar aplicação
        dobrar_apl = f"Tempo 2 x Aplicação = {self.dobraCapital(renta_anual_apl)[0]:.2f} anos = {self.dobraCapital(renta_anual_apl)[1]:.2f} meses"
        Label(self.resul_f3, text=dobrar_apl,
              font=("Verdana", 10, "bold"), bg=self.cor_bg_frame).place(relx=0.02, rely=0.39)
