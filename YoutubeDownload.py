import yt_dlp
from tkinter import *
from tkinter import filedialog

# Variável global para armazenar o caminho de download
download_path = ""

def selecionar_pasta():
    global download_path
    pasta = filedialog.askdirectory()
    if pasta:
        download_path = pasta
        pasta_label.config(text=f"Pasta selecionada:\n{pasta}", fg="lightgreen")
    else:
        pasta_label.config(text="Nenhuma pasta selecionada", fg="orange")

def download():
    url = linker.get().strip()

    if "youtube.com/shorts/" in url:
        video_id = url.split("/shorts/")[-1].split("?")[0]
        url = f"https://www.youtube.com/watch?v={video_id}"

    if not url or "youtube.com/watch?v=" not in url:
        status_label.config(text="Link inválido. Tente novamente.", fg="orange")
        return

    if not download_path:
        status_label.config(text="Escolha uma pasta de destino primeiro.", fg="orange")
        return

    try:
        ydl_opts = {
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',
            'format': 'bv*+ba/best[ext=mp4]/best',
            'merge_output_format': 'mp4'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        status_label.config(text="Download concluído com sucesso!", fg="green")
    except Exception as e:
        status_label.config(text=f"Erro: {str(e)}", fg="red")
        print(f"Erro detalhado: {e}")

# Interface Tkinter
janela = Tk()
janela.geometry("500x300")
janela.config(background="#414141")
janela.title("YouTube Download")

titlee = Label(janela, text="YouTube Downloader", fg="#ffffff", background="#414141", font=("Arial", 16, "bold"))
titlee.pack(pady=(20, 10))

linker_title = Label(janela, text="Insira o link do vídeo:", fg="#ffffff", background="#414141", font=("Arial", 10))
linker_title.pack(anchor="w", padx=20)

linker = Entry(janela, width=55)
linker.pack(padx=20, pady=5)
linker.config(background="#2B2B2B", fg="#ffffff", insertbackground="#ffffff")

# Botão de selecionar pasta
select_button = Button(janela, text="Selecionar pasta de download", command=selecionar_pasta)
select_button.pack(pady=(10, 0))
select_button.config(background="#555555", fg="#ffffff", font=("Arial", 10))

# Label da pasta
pasta_label = Label(janela, text="Nenhuma pasta selecionada", fg="orange", background="#414141", font=("Arial", 9))
pasta_label.pack()

# Botão de download
Dow = Button(janela, text="Download", command=download)
Dow.pack(pady=10)
Dow.config(background="green", fg="#ffffff", font=("Arial", 10, "bold"), width=25)

# Status
status_label = Label(janela, text="", fg="#ffffff", background="#414141", font=("Arial", 10))
status_label.pack(pady=(10, 0))

janela.mainloop()
