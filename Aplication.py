from tkinter import *
from tkinter import messagebox

from JanelaResultados import Resultado

# main aonde deve ser rodado a aplicação

root = Tk()


class App(Resultado):
    def __init__(self):
        super().__init__()
        self.frame_conteudo = None
        self.frame_titulo = None
        self.frame_externo = None
        self.borda_frame = 'lightblue'
        self.cor_fundo = "antiquewhite"
        self.root = root
        self.tela()
        self.frame_mais_externo()
        self.frame_titulo_CDB()
        self.frame_conteudo_interno()
        self.labels()
        self.spin_box()
        self.widgets_radio_button()
        self.button_calcular()
        self.root.mainloop()

    def tela(self):
        self.root.minsize(width=425, height=650)
        self.root.title("Calculadora CDB")

    def frame_mais_externo(self):
        self.frame_externo = Frame(self.root, bg="#cac5bb", relief="solid", bd=1)
        self.frame_externo.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.frame_externo.bind("<Button-1>", self.focar_frame)

    def frame_titulo_CDB(self):
        self.frame_titulo = Frame(self.frame_externo, bg="#ff6347",
                                  highlightbackground=self.borda_frame,
                                  highlightthickness=5)
        self.frame_titulo.place(relx=0.10, rely=0.03, relwidth=0.8, relheight=0.095)
        self.frame_titulo.bind("<Button-1>", self.focar_frame)

    def frame_conteudo_interno(self):
        self.frame_conteudo = Frame(self.frame_externo, bg=self.cor_fundo,
                                    highlightbackground=self.borda_frame,
                                    highlightthickness=4,
                                    highlightcolor="#86c7db")
        self.frame_conteudo.place(relx=0.04, rely=0.135, relwidth=0.9, relheight=0.7)
        self.frame_conteudo.bind("<Button-1>", self.focar_frame)

    def focar_frame(self, event):
        self.frame_conteudo.focus_set()

    def labels(self):
        """Textos da interface"""
        # variaveis de config
        cor_fundo_atri = self.cor_fundo
        tamanho_letras = ("Verdana", 11)
        borda = 0.02

        self.lbl_titulo = Label(self.frame_titulo,
                                text="CDBs, LCIs e LCAs indexadas por\n"
                                     "Certificados de Depósito Interbancários",
                                bg="#ff6347", font=("Arial", 12, "bold"), justify="left")
        self.lbl_titulo.place(relx=0.05, rely=0.05)

        # label das entradas Capital
        self.lb_capital = Label(self.frame_conteudo, text="Capital:               $",
                                bg=cor_fundo_atri, font=tamanho_letras)
        self.lb_capital.place(relx=0.02, rely=0.03)

        # label das entradas Taxa Selic
        self.lb_taxa_selic = Label(self.frame_conteudo, text="Taxa Selic:", bg=cor_fundo_atri,
                                   font=tamanho_letras)
        self.lb_taxa_selic.place(relx=borda, rely=0.12)

        # label das entradas Taxa CDI
        self.lb_taxa_cdi = Label(self.frame_conteudo, text="Taxa CDI:", bg=cor_fundo_atri,
                                 font=tamanho_letras)
        self.lb_taxa_cdi.place(relx=borda, rely=0.24)

        # label das entradas Rentabilidade
        self.lb_rentabilidade = Label(self.frame_conteudo, text="Rentabilidade:", bg=cor_fundo_atri,
                                      font=tamanho_letras)
        self.lb_rentabilidade.place(relx=borda, rely=0.36)

        # label das entradas Meses
        self.lb_meses = Label(self.frame_conteudo, text="Meses:", bg=cor_fundo_atri,
                              font=tamanho_letras)
        self.lb_meses.place(relx=borda, rely=0.48)

    def _verificar(self, event=None):

        try:
            # foi colocado na lista para vericar se as entradas ao final irão ser iguais a 0

            lista = [
                bool(float(self.sb_capi.get())),
                bool(float(self.sb_taxa_selic.get())),
                bool(float(self.sb_taxa_cdi.get())),
                bool(float(self.sb_taxa_rent.get())),
                bool(float(self.sb_mes.get()))]

            if False not in lista:
                self.janela_resultado()
            else:
                messagebox.showerror(title="ERROR", message="Valor inválido, verifique se informou"
                                                            " apenas números e verique tambem"
                                                            " se são maiores que 0")
        except ValueError:
            messagebox.showerror(title="ERROR", message="Valor inválido, verifique se informou"
                                                        " apenas números e maiores que 0"
                                                        " verique também se são maiores que 0")
        except ZeroDivisionError:
            messagebox.showerror(title="ERROR", message="divisão por zero, informe um número"
                                                        " maior que zero")

    def spin_box(self):
        """ Caixa de entrada dos valores """
        pos_x = 0.42
        fontes = ("Verdana", 11)
        valor_default_cap = IntVar(value=1000)
        self.sb_capi = Spinbox(self.frame_conteudo, from_=1, to=100000000,
                               increment=0.01, textvariable=valor_default_cap)

        self.sb_capi.place(relx=pos_x, rely=0.03, height=24, width=160)

        # entrada de texto da taxa selic e texto a seguir
        valor_default_selic = StringVar(value="13.25")
        self.sb_taxa_selic = Spinbox(self.frame_conteudo, from_=1, to=100000000, increment=0.01,
                                     textvariable=valor_default_selic, validate="key")

        self.sb_taxa_selic.place(relx=pos_x, rely=0.12, height=24, width=85)
        Label(self.frame_conteudo, text="% ano", font=fontes, bg=self.cor_fundo).place(relx=0.65, rely=0.12)

        # entrada de texto da taxa CDI
        valor_default_cdi = StringVar(value="13.15")
        self.sb_taxa_cdi = Spinbox(self.frame_conteudo, from_=1, to=100000000, increment=0.05,
                                   textvariable=valor_default_cdi, validate="key")

        self.sb_taxa_cdi.place(relx=pos_x, rely=0.24, height=24, width=85)
        Label(self.frame_conteudo, text="% ano", font=fontes, bg=self.cor_fundo).place(relx=0.65, rely=0.24)

        # entrada de texto da rentabilidade
        valor_default_rent = StringVar(value="100")
        self.sb_taxa_rent = Spinbox(self.frame_conteudo, from_=0, to=100000000, increment=0.5,
                                    textvariable=valor_default_rent, validate="key")

        self.sb_taxa_rent.place(relx=pos_x, rely=0.36, height=24, width=75)
        Label(self.frame_conteudo, text="% CDI", font=fontes, bg=self.cor_fundo).place(relx=0.62, rely=0.36)

        # entrada de texto dos meses
        valor_default_mes = StringVar(value="1")
        self.sb_mes = Spinbox(self.frame_conteudo, from_=0, to=100000000, validate="key",
                              textvariable=valor_default_mes)

        self.sb_mes.place(relx=pos_x, rely=0.48, height=24, width=70)

        self.sb_mes.bind("<Button-1>", self.seleci_ir_rb)
        self.sb_mes.bind("<FocusOut>", self.seleci_ir_rb)

    def seleci_ir_rb(self, event):
        """Metodo responsável para fazer a seleção automática dos radios botões"""
        if self.sb_mes.get() != "":
            mes = int(self.sb_mes.get())
        else:
            mes = 1

        aumentar_Mes = str(event)[1:12]

        if aumentar_Mes.__eq__("ButtonPress"):
            mes += 1

        if 0 <= mes <= 6:
            self.ra_5.select()

        elif 7 <= mes <= 12:
            self.ra_4.select()

        elif 13 <= mes <= 24:
            self.ra_3.select()

        elif mes >= 25:
            self.ra_2.select()

    def widgets_radio_button(self):
        # label das entradas Alíquota IR
        fonte = ("Verdana", 11)
        self.lb_aliquota = Label(self.frame_conteudo, text="Aliquota IR:", bg=self.cor_fundo,
                                 font=fonte)
        self.lb_aliquota.place(relx=0.02, rely=0.57)

        self.valor = StringVar()

        self.ra_1 = Radiobutton(self.frame_conteudo, font=fonte, bg=self.cor_fundo, text="0.0 (LCA ou LCI)",
                                variable=self.valor, value=0.0)

        self.ra_2 = Radiobutton(self.frame_conteudo, font=fonte, bg=self.cor_fundo, text="15.0 (acima de 721 dias)",
                                variable=self.valor, value=15.0)

        self.ra_3 = Radiobutton(self.frame_conteudo, font=fonte, bg=self.cor_fundo,
                                text="17.5 (de 361 até 720 dias)",
                                variable=self.valor, value=17.5)

        self.ra_4 = Radiobutton(self.frame_conteudo, font=fonte, bg=self.cor_fundo,
                                text="20.0 (de 181 até 360 dias)",
                                variable=self.valor, value=20.0)

        self.ra_5 = Radiobutton(self.frame_conteudo, font=fonte, bg=self.cor_fundo, text="22.5 (até 180 dias)",
                                variable=self.valor, value=22.5)

        self.ra_1.place(relx=0.07, rely=0.65)
        self.ra_2.place(relx=0.07, rely=0.72)
        self.ra_3.place(relx=0.07, rely=0.79)
        self.ra_4.place(relx=0.07, rely=0.86)
        self.ra_5.place(relx=0.07, rely=0.93)

        # selecionando o padrao

        self.ra_5.select()

    def button_calcular(self):
        self.btn_calcular = Button(self.root, text="Calcular", bg="#f8fad7",
                                   fg="red", width=10, height=1, font=("Verdana", 10),
                                   relief="solid", border=1, command=self._verificar)
        self.btn_calcular.place(relx=0.40, rely=0.845)

        Label(text="(arraste-me para reposicionar a janela)",
              font=("Verdana", 10), bg="#cac5bb").place(relx=0.2, rely=0.93)


App()
