try:
    import PySimpleGUI as sg
    import wikipediaapi
except ImportError as e:
    print(e)

sg.theme("DarkGrey 13")

layout = [
    [sg.Text("Digite um assunto que deseja pesquisar...")],
    [sg.InputText(key="assunto")],
    [sg.Button("Buscar", size=(18, 1)), sg.Button("Cancelar", size=(18, 1))],
    [sg.Text("", key="resposta")]
]

window = sg.Window('Search Wikipedia', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        sg.popup_ok("Obrigado por usar o Search Wiki!")
        break
    elif event == "Buscar":
        dado = values["assunto"]
    
        wiki = wikipediaapi.Wikipedia(
            language = "pt",
            extract_format = wikipediaapi.ExtractFormat.WIKI
        )

        page_wiki = wiki.page(dado)
        ex = page_wiki.exists()

        if ex == True:
            window["resposta"].update(page_wiki.summary)
        elif ex == False:
            window["resposta"].update("Erro, o assunto procurado não foi encontrado!")

window.close()