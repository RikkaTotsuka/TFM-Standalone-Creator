import os
import urllib.request
import tkinter as tk
from tkinter import messagebox
import webbrowser  # Importando o módulo webbrowser


def make_entry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption, bg='black', fg='white').pack(side=tk.TOP, padx=10, pady=(5, 0))  # Fundo preto e texto branco
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry


def enter(event):
    create()


def open_github():
    webbrowser.open("https://github.com/RikkaTotsuka")


def create():
    """ Collect 1's for every failure and quit program in case of failure_max failures """
    print(mice_name.get(), mice_swfL.get())
    mice = mice_name.get()
    url = mice_swfL.get()
    root.destroy()

    if (mice, url):
        window = tk.Tk()
        window.wm_withdraw()

        # Ajuste para abrir a nova janela com tamanho 1x1 até que a operação comece
        window.geometry('1x1+' + str(int(window.winfo_screenwidth() / 2)) + '+' + str(int(window.winfo_screenheight() / 2)))

        messagebox.showinfo(title='Standalone Generator', message='Baixando a swf do ' + str(mice) + ', aguarde.')
        tfmAIR = None

        try:
            pbFile = urllib.request.urlopen(url)
            tfmAIR = pbFile.read()
            pbFile.close()
        except:
            tfmAIR = None

        if tfmAIR is None:
            messagebox.showinfo(title='Standalone Generator', message='Falha no download, o link deve estar errado.')
            data = os.system("Emulador.py")

        if tfmAIR is not None:
            messagebox.showinfo(title='Standalone Generator', message='Download concluído.')
            application = '<?xml version="1.0" encoding="utf-8" standalone="no"?>' + \
                          '<application xmlns="http://ns.adobe.com/air/application/3.4">' + \
                          '<id>' + str(mice) + '</id>' + \
                          '<filename>' + str(mice) + '</filename>' + \
                          '<name>Transformice</name>' + \
                          '<versionNumber>1.0.0</versionNumber>' + \
                          '<description>Fromage !</description>' + \
                          '<copyright>Copyright Atelier 801</copyright>' + \
                          '<initialWindow>' + \
                          '<content>TransformiceAIR.swf</content>' + \
                          '<title>' + str(mice) + '</title>' + \
                          '<autoOrients>false</autoOrients>' + \
                          '<fullScreen>false</fullScreen>' + \
                          '<visible>true</visible>' + \
                          '</initialWindow></application>'
            pbFile = open("./files/tfmstand.exe", "rb")
            appexe = pbFile.read()
            pbFile.close()

            pbFile = open("./files/signatures.xml", "rb")
            signatures = pbFile.read()
            pbFile.close()

            os.mkdir(mice)
            os.mkdir(mice + "/META-INF")
            os.mkdir(mice + "/META-INF/AIR")
            with open(str(mice) + "/" + str(mice) + ".exe", "wb") as code:
                code.write(appexe)
            with open(mice + "/TransformiceAIR.swf", "wb") as code:
                code.write(tfmAIR)
            with open(mice + "/META-INF/signatures.xml", "wb") as code:
                code.write(signatures)
            with open(mice + "/META-INF/AIR/application.xml", "wb") as code:
                code.write(application.encode('utf-8'))  # Codificando a string em bytes
            messagebox.showinfo(title='Standalone Generator', message='A standalone do ' + str(mice) + ' foi criada com sucesso.')


# Janela principal
root = tk.Tk()
root.geometry('400x250')  # Tamanho inicial da janela
root.title('Criador de Standalone')
root.configure(bg='black')  # Fundo preto
parent = tk.Frame(root, padx=10, pady=10, bg='black')
parent.pack(fill=tk.BOTH, expand=True)

# Adicionando o Label com a mensagem "Criado por Rikka Totsuka"
header_label = tk.Label(parent, text="Criado por Rikka Totsuka", font=("Helvetica", 12, "bold"), bg='black', fg='white')
header_label.pack(side=tk.TOP, pady=(5, 10))  # Mais espaçamento acima do header

mice_name = make_entry(parent, 'Nome do Mice:', 16, bg='black', fg='white')
mice_swfL = make_entry(parent, 'Link da swf:', 150, bg='black', fg='white')

b = tk.Button(parent, borderwidth=4, text='Criar Standalone', width=20, pady=8, command=create, bg='gray', fg='black', font=("Helvetica", 10))
b.pack(side=tk.TOP, pady=(10, 0))  # Adiciona espaçamento acima do botão

mice_swfL.bind('<Return>', enter)
mice_name.focus_set()

# Adicionando o botão de acesso ao GitHub
github_button = tk.Button(parent, text='Acessar meu GitHub', command=open_github, bg='gray', fg='black', font=("Helvetica", 10))
github_button.pack(side=tk.LEFT, padx=(10, 0), pady=(10, 0))  # Colocando o botão à esquerda com espaçamento

parent.mainloop()
