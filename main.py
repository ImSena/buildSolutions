import customtkinter as ctk
from PIL import Image
import textwrap
import webbrowser

pc_configs = {
    "trabalho": {
        "Opção Básica": {
            "Descrição": "A opção básica é ideal para usuários que precisam de um computador para tarefas de escritório e navegação na web. Com um processador Intel Core i3-10105 e 8GB de memória Corsair Vengeance RGB, este PC oferece desempenho adequado para aplicativos de produtividade e multitarefa leve. Embora não inclua uma placa de vídeo dedicada, o SSD de 512GB proporciona inicializações rápidas do sistema e tempos de carregamento reduzidos para aplicativos.",
            "Processador": ["Intel Core i3-10105, 3.7GHz", 530],
            "Processador": ["Intel Core i3-10105, 3.7GHz", 530],
            "Placa-Mãe": ["Gigabyte H510M H V2 DDR4, LGA1200", 450],
            "Memória": ["Memória Corsair Vengeance RGB RS, 8GB, 3200MHz, DDR4", 150],
            "Placa de vídeo": ["N/A", 0],
            "Armazenamento": ["SSD 512GB KBM! Gaming, SATA III", 160],
            "Resfriamento": ["Air Cooler Rise Mode Gamer G700", 60],
            "Fonte": ["Fonte MSI MAG A650BN, 650W, 80 Plus Bronze", 260],
            "Gabinete": ["Gabinete Gamer Rise Mode X5 Glass", 140],
            "Total": 1750
        },
        "Opção Intermediária": {
            "Descrição": "A opção intermediária é projetada para usuários que exigem um desempenho mais robusto para multitarefas e aplicativos de produtividade. Equipado com um processador Intel Core i5-12400F e 16GB de memória XPG Gammix D35, este PC oferece uma experiência mais fluida ao lidar com várias tarefas simultaneamente. A placa de vídeo RX 6600 CLD 8G ASRock AMD Radeon proporciona um desempenho gráfico sólido para edição de fotos e vídeos leves, bem como jogos casuais.",
            "Processador": ["Processador Intel Core i5-12400F", 750],
            "Placa-Mãe": ["Placa Mãe Asus Prime H610M-E D4 DDR4", 580],
            "Memória": ["2X Memória XPG Gammix D35, 8GB, 3200MHz, DDR4", 300],
            "Placa de vídeo": ["Placa de Vídeo RX 6600 CLD 8G ASRock AMD Radeon", 1300],
            "Armazenamento": ["SSD 512 GB XPG SX6000 Lite", 320],
            "Resfriamento": ["Water Cooler Rise Mode RGB, 120mm, AMD/Intel, Preto - RM-WCB-01-RGB", 135],
            "Fonte": ["Fonte MSI MAG A650BN, 650W, 80 Plus Bronze", 260],
            "Gabinete": ["Gabinete Gamer Rise Mode Wave Black", 230],
            "Total": 3875
        },
        "Opção Avançada": {
            "Descrição": "A opção avançada é ideal para profissionais que exigem o máximo desempenho para cargas de trabalho intensivas. Com um processador Intel Core i7-12700F e 32GB de memória XPG Gammix D35, este PC oferece poder de processamento excepcional para renderização de vídeo, modelagem 3D e outras tarefas exigentes. A placa de vídeo RTX 4060 Ti Click OC Galax NVIDIA GeForce proporciona gráficos impressionantes para jogos AAA e criação de conteúdo.",
            "Processador": ["Processador Intel Core i7-12700F", 1650],
            "Placa-Mãe": ["Placa Mãe Gigabyte B760M Gaming X (rev. 1.0)", 900],
            "Memória": ["Memória XPG Gammix D35, 16GB, 3200MHz, DDR4", 450],
            "Placa de vídeo": ["Placa de Vídeo RTX 4060 Ti Click OC Galax NVIDIA GeForce", 2200],
            "Armazenamento": ["SSD 1 TB Kingston", 390],
            "Resfriamento": ["Water Cooler Rise Mode Frost, RGB, 360mm, AMD/Intel, Branco - RM-WCF-04-RGB", 300],
            "Fonte": ["Fonte XPG Core Reactor, 850W, 80 Plus Gold", 700],
            "Gabinete": ["Gabinete Gamer Rise Mode Galaxy Glass", 390],
            "Total": 6980
        }
    },
    "jogo": {
        "Opção Básica": {
            "Descrição": "A opção avançada é ideal para profissionais que exigem o máximo desempenho para cargas de trabalho intensivas. Com um processador Intel Core i7-12700F e 32GB de memória XPG Gammix D35, este PC oferece poder de processamento excepcional para renderização de vídeo, modelagem 3D e outras tarefas exigentes. A placa de vídeo RTX 4060 Ti Click OC Galax NVIDIA GeForce proporciona gráficos impressionantes para jogos AAA e criação de conteúdo.",
            "Processador": ["Processador AMD Ryzen 5 4500", 450],
            "Placa-Mãe": ["Placa Mãe ASRock B450M-HDV R4.0 DDR4", 360],
            "Memória": ["Memória XPG Gammix D35, 2x 8GB, 3200MHz, DDR4", 300],
            "Placa de vídeo": ["Placa de Vídeo Galax NVIDIA GeForce GTX 1650 EX Plus (1-Click OC)", 800],
            "Armazenamento": ["SSD Lexar NVME 512GB", 250],
            "Resfriamento": ["Air Cooler Rise Mode Gamer G800, RGB, AMD/Intel, 180mm, Preto - RM-AC-O8-RGB", 70],
            "Fonte": ["Fonte MSI MAG A650BN, 650W, 80 Plus Bronze", 260],
            "Gabinete": ["Gabinete Gamer Rise Mode Glass 06X", 180],
            "Total": 2670
        },
        "Opção Intermediária": {
            "Descrição": "A opção intermediária é voltada para jogadores que buscam uma experiência de jogo mais imersiva e gráficos de alta qualidade. Com um processador AMD Ryzen 7 5700X e uma placa de vídeo RTX 4060 Ti OC Edition Asus NVIDIA GeForce, este PC oferece desempenho excepcional em resoluções de 1080p e 1440p. O SSD de 1 TB Kingston proporciona amplo espaço de armazenamento para jogos, enquanto os 16GB de memória XPG Gammix D35 garantem uma resposta rápida e suave durante o jogo.",
            "Processador": ["Processador AMD Ryzen 7 5700X", 1000],
            "Placa-Mãe": ["Placa Mãe Gigabyte B550M Aorus Elite DDR4", 850],
            "Memória": ["Memória XPG Gammix D35, 2x 8GB, 3200MHz, DDR4", 300],
            "Placa de vídeo": ["Placa de Vídeo RTX 4060 Ti OC Edition Asus NVIDIA GeForce", 2500],
            "Armazenamento": ["SSD 1 TB Kingston", 390],
            "Resfriamento": ["Water Cooler Rise Mode, ARGB, 240mm, AMD/Intel, Preto - RM-WCB-04-ARGB", 200],
            "Fonte": ["Fonte MSI MAG A650BN, 650W, 80 Plus Bronze", 260],
            "Gabinete": ["Gabinete Gamer Hyrax HGB720", 450],
            "Total": 5650
        },
        "Opção Avançada": {
            "Descrição": "A opção avançada é destinada a jogadores entusiastas e criadores de conteúdo que exigem o melhor desempenho e gráficos de alta qualidade. Com um processador AMD Ryzen 9 7900 e uma placa de vídeo RTX 4070 1-Click OC 3X Black PCI-E Galax NVIDIA GeForce, este PC oferece desempenho excepcional em jogos AAA, streaming e edição de vídeo. O SSD de 1 TB Kingston Fury Renegade proporciona armazenamento rápido e amplo espaço para jogos e arquivos multimídia, enquanto o sistema de resfriamento Water Cooler MSI Mag Coreliquid M360 garante temperaturas baixas mesmo em cargas de trabalho intensas.",
            "Processador": ["Processador AMD Ryzen 9 7900", 2300],
            "Placa-Mãe": ["Placa Mãe Asus TUF Gaming B650M-Plus DDR5", 1200],
            "Memória": ["Memória Corsair Vengeance RGB, 32GB (2x16GB), 6200MHz, DDR5", 1000],
            "Placa de vídeo": ["Placa de Vídeo RTX 4070 1-Click OC 3X Black PCI-E Galax NVIDIA GeForce", 3800],
            "Armazenamento": ["SSD 1 TB Kingston Fury Renegade", 700],
            "Resfriamento": ["Water Cooler MSI Mag Coreliquid M360, ARGB, 360mm, Intel e AMD, Preto", 650],
            "Fonte": ["Fonte XPG Core Reactor, 850W, 80 Plus Gold", 700],
            "Gabinete": ["Gabinete Gamer Rise Mode Galaxy Glass", 550],
            "Total": 10900
        }
    }
}

# Funções acesso externo
def abrir_url():
    url = 'https://github.com/ImSena/buildSolutions/blob/master/assets/ebook.pdf'
    webbrowser.open(url)

def comprar_pecas():
    url = 'https://www.kabum.com.br'
    webbrowser.open(url)

# Funções de navegação e exibição
def mostrar_frame(frame):
    for f in frames:
        f.pack_forget()
    frame.pack(fill="both", expand=True)

def abrir_orcamento():
    mostrar_frame(frame_orcamento)

def abrir_faixa_orcamento(objetivo):
    global objetivo_selecionado
    objetivo_selecionado = objetivo
    atualizar_texto_faixa_orcamento()
    mostrar_frame(frame_faixa_orcamento)

def atualizar_texto_faixa_orcamento():
    if objetivo_selecionado == "trabalho":
        faixa1.configure(text="Mais de 1500 e menos de 3k", command=lambda: exibir_opcoes("2k-3k"))
        faixa2.configure(text="Mais de 3k e menos de 5k", command=lambda: exibir_opcoes("3k-5k"))
        faixa3.configure(text="Mais de 5k", command=lambda: exibir_opcoes("5k+"))
        faixa3.pack(pady=10)
    elif objetivo_selecionado == "jogo":
        faixa1.configure(text="Mais de 2k e menos de 4k", command=lambda: exibir_opcoes("2k-4k"))
        faixa2.configure(text="Mais de 4k e menos de 6k", command=lambda: exibir_opcoes("4k-6k"))
        faixa3.configure(text="Mais de 6k", command=lambda: exibir_opcoes("6k+"))
        faixa3.pack()
    elif objetivo_selecionado == "estudo":
        faixa1.configure(text="Mais de 1k e menos de 2k", command=lambda: exibir_opcoes("1k-2k"))
        faixa2.configure(text="Mais de 2k e menos de 4k", command=lambda: exibir_opcoes("2k-4k"))
        faixa3.pack_forget()

def exibir_opcoes(faixa):
    global faixa_selecionada
    faixa_selecionada = faixa
    options = []
    if objetivo_selecionado == "trabalho":
        if faixa_selecionada == "2k-3k":
            options = ["Opção Básica"]
        elif faixa_selecionada == "3k-5k":
            options = ["Opção Básica", "Opção Intermediária"]
        elif faixa_selecionada == "5k+":
            options = ["Opção Básica", "Opção Intermediária", "Opção Avançada"]
    elif objetivo_selecionado == "jogo":
        if faixa_selecionada == "2k-4k":
            options = ["Opção Básica"]
        elif faixa_selecionada == "4k-6k":
            options = ["Opção Básica", "Opção Intermediária"]
        elif faixa_selecionada == "6k+":
            options = ["Opção Básica", "Opção Intermediária", "Opção Avançada"]
    elif objetivo_selecionado == "estudo":
        if faixa_selecionada == "1k-2k":
            options = ["Opção Básica"]
        elif faixa_selecionada == "2k-4k":
            options = ["Opção Básica", "Opção Intermediária"]

    for widget in frame_opcoes.winfo_children():
        widget.destroy()

    ctk.CTkLabel(frame_opcoes, text=f"Opções de PC para {objetivo_selecionado} na faixa {faixa_selecionada}:", font=("Arial", 20)).pack(pady=20)
    for option in options:
        ctk.CTkButton(frame_opcoes, text=option, command=lambda opt=option: exibir_detalhes(opt), width=430, height=85, font=("Arial", 20)).pack(pady=10)

    ctk.CTkButton(frame_opcoes, text="Voltar", command=lambda: mostrar_frame(frame_faixa_orcamento), height=40, width=100).place(x=30, y=480)

    mostrar_frame(frame_opcoes)

def exibir_detalhes(opcao):
    for widget in frame_detalhes.winfo_children():
        widget.destroy()

    if objetivo_selecionado == 'estudo':
        detalhes = pc_configs['trabalho'][opcao]
    else:
        detalhes = pc_configs[objetivo_selecionado][opcao]

    # Frame rolável para os detalhes das configurações
    scrollable_frame = ctk.CTkScrollableFrame(frame_detalhes, width=600, height=200)
    scrollable_frame.place(x=20, y=20)
    scrollable_descricao = ctk.CTkScrollableFrame(frame_detalhes, width=600, height=200)
    scrollable_descricao.place(x= 20, y=240)

    ctk.CTkLabel(scrollable_frame, text=f"Detalhes da Opção {opcao}:", font=("Arial", 20)).pack(pady=20)
    ctk.CTkLabel(scrollable_descricao, text=f"O que você poderia fazer: ", font=("Arial", 20)).pack(pady=20)

    for componente, detalhe in detalhes.items():
        if componente != "Descrição":
            if isinstance(detalhe, list):
                componente_quebrada = "\n".join(textwrap.wrap(detalhe[0], width=60))

                ctk.CTkLabel(scrollable_frame, text=f"{componente}: {componente_quebrada} (Preço: R${detalhe[1]})", font=("Arial", 13), justify="left").pack(pady=5)
            else:
                ctk.CTkLabel(scrollable_frame, text=f"{componente}: {detalhe} (Preço Total)", font=("Arial", 20)).pack(pady=5)
        else:
            descricao = detalhe
            descricao_quebrada = "\n".join(textwrap.wrap(descricao, width=80))
            ctk.CTkLabel(scrollable_descricao, text=f"{componente}: {descricao_quebrada}", justify="left",font=("Arial", 13)).pack(pady=5)
            

    # Adição da imagem ao lado direito
    pc = 0
    if opcao == 'Opção Básica':
        pc = 0
    elif opcao == 'Opção Intermediária':
        pc = 1
    elif opcao == 'Opção Avançada':
        pc = 2

    caminhoImg = f'assets/img/{objetivo_selecionado}/{pc}.png'
    imagem = ctk.CTkImage(light_image=Image.open(caminhoImg), dark_image=Image.open(caminhoImg), size=(300, 300))
    label_imagem = ctk.CTkLabel(frame_detalhes, text='', image=imagem)
    label_imagem.place(x= 670, y=50)

    # Botão "Comprar Peças"
    ctk.CTkButton(frame_detalhes, text="Comprar Peças", height=40, width=150, command=comprar_pecas).place(x=670, y=400)

    # Botão "Voltar"
    ctk.CTkButton(frame_detalhes, text="Voltar", command=lambda: mostrar_frame(frame_opcoes), height=40, width=100).place(x=30, y=480)

    mostrar_frame(frame_detalhes)

def sair():
    app.quit()

# Configuração da janela principal
app = ctk.CTk()
app.title("Build Solutions")
app.geometry("1000x550")
app.resizable(width=False, height=False);
app.iconbitmap('assets/icon.ico')

# Variáveis globais
objetivo_selecionado = ""
faixa_selecionada = ""

# Frames para diferentes telas
frame_inicial = ctk.CTkFrame(app)
frame_orcamento = ctk.CTkFrame(app)
frame_faixa_orcamento = ctk.CTkFrame(app)
frame_opcoes = ctk.CTkFrame(app)
frame_detalhes = ctk.CTkFrame(app)
frames = [frame_inicial, frame_orcamento, frame_faixa_orcamento, frame_opcoes, frame_detalhes]

# Frame inicial
botao_orcamento = ctk.CTkButton(frame_inicial, text="Orçamento", command=abrir_orcamento, height=85, width=430, font=("Arial", 20))
botao_tutorial = ctk.CTkButton(frame_inicial, text="Tutorial", height=85, width=430, command=abrir_url, font=("Arial", 20))
botao_sair = ctk.CTkButton(frame_inicial, text="Sair", command=sair, height=85, width=430, font=("Arial", 20))

botao_orcamento.place(x=30, y=150)
botao_tutorial.place(x=30, y=250)
botao_sair.place(x=30, y=350)
    #imagem
my_image = ctk.CTkImage(light_image=Image.open('assets/img/logo.png'), dark_image=Image.open('assets/img/logo.png'), size=(325, 325))
label_img = ctk.CTkLabel(frame_inicial, text='', image=my_image);
label_img.pack(pady=10);
label_img.place(x= 600, y=130)

# Frame de foco
ctk.CTkLabel(frame_orcamento, text="Escolha o objetivo do PC:", font=("Arial", 20)).place(relx=0.5, rely=0.1, anchor="center")

ctk.CTkButton(frame_orcamento, text="Trabalho", command=lambda: abrir_faixa_orcamento("trabalho"), height=85, width=200, font=("Arial", 20)).place(x=100, y=250)
ctk.CTkButton(frame_orcamento, text="Jogo", command=lambda: abrir_faixa_orcamento("jogo"), height=85, width=200, font=("Arial", 20)).place(x=400, y=250)
ctk.CTkButton(frame_orcamento, text="Estudo", command=lambda: abrir_faixa_orcamento("estudo"), height=85, width=200, font=("Arial", 20)).place(x=700, y=250)

ctk.CTkButton(frame_orcamento, text="Voltar", command=lambda: mostrar_frame(frame_inicial), height=40, width=100, font=("Arial", 20)).place(x=30, y=480)

# Frame de faixa de orçamento
ctk.CTkLabel(frame_faixa_orcamento, text="Selecione a faixa de orçamento:", font=("Arial", 20)).pack(pady=20)

faixa1 = ctk.CTkButton(frame_faixa_orcamento, text="", height=85, width=430, font=("Arial", 20))
faixa1.pack(pady=10)
faixa2 = ctk.CTkButton(frame_faixa_orcamento, text="", height=85, width=430, font=("Arial", 20))
faixa2.pack(pady=10)
faixa3 = ctk.CTkButton(frame_faixa_orcamento, text="", height=85, width=430, font=("Arial", 20))
faixa3.pack(pady=10)

ctk.CTkButton(frame_faixa_orcamento, text="Voltar", command=lambda: mostrar_frame(frame_orcamento), height=40, width=100).place(x=30, y=480)

# Frame de opções
ctk.CTkLabel(frame_opcoes, text="Opções disponíveis:", font=("Arial", 20)).pack(pady=20)

# Frame de detalhes
ctk.CTkLabel(frame_detalhes, text="Detalhes da opção selecionada:", font=("Arial", 20)).pack(pady=20)

# Exibe o frame inicial
mostrar_frame(frame_inicial)

app.mainloop()
