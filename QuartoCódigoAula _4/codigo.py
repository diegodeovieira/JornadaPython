# Titulo: Hashzap
# Botão de iniciar o chat
   # Clicou no botão
      # Popup / Modal
         # Titulo: Bem vido a Hashzap
         # Campo: Escreva seu nome no chat
         # Botão : entra no chat
# chat
# Embaixo  do chat
   # Campo de digite sua mensagem 
   # Botão de enviar

# flet -> framework do Python


import flet as ft

def main(pagina):
   texto = ft.Text("Hashzap")

   chat = ft.Column()


   def enviar_mensagem_tunel(mensagem):
      print(mensagem)
      texto_mensagem = ft.Text(mensagem)
      chat.controls.append(texto_mensagem)

      pagina.update()


   pagina.pubsub.subscribe(enviar_mensagem_tunel)


   def enviar_mensagem(evento):
      print("enviar_mensagem")
      pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")

      campo_mensagem.value = ""

      pagina.update()


   campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
   botao_enviar = ft.ElevatedButton("enviar", on_click=enviar_mensagem)
   linha_enviar = ft.Row(campo_mensagem, botao_enviar)

   def entra_chat(evento):
      print("Entra no chat")
      # Fechar o popup
      popup.open = False
      # Tira o botão iniciar chat
      pagina.remove(botao_iniciar)
      # Tira o titulo hashzap
      pagina.remove(texto)
      # Criar o chat
      pagina.add(chat)
      pagina.pubsub.send_all(f"{nome_usuario.value} entro no chat")
      # Colocar o capo de digitar mensagem
      #pagina.add(campo_mensagem)
      # Criar o botão de enviar
      #pagina.add(botao_enviar)

      pagina.update()
      

   
   titulo_popup = ft.Text("Bem vindo ao hashzap")
   nome_usuario = ft.TextField(label="Escreva seu nome no chat")
   botao_entra = ft.ElevatedButton("Entra no chat", on_click=entra_chat)
   popup = ft.AlertDialog(
      open=False,
      modal=True,
      title=titulo_popup,
      content=nome_usuario,
      actions=[botao_entra]
   )
   
   
   def abrir_popup(evento):
      pagina.dialog = popup
      popup.open = True
      pagina.update()
      
   botao_iniciar = ft.ElevatedButton("iniciar Chat", on_click=abrir_popup)

   pagina.add(texto)
   pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)