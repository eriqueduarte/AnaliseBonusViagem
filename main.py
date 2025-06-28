import pandas as pd
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "AS###################"
auth_token  = "#####################"
client = Client(account_sid, auth_token)

# Passo a passo para a solução

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
#    print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
#    print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any ():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta. Seguem as informações: Vendedor: {vendedor}, Vendas: {vendas} ')
        message = client.messages.create(
            to="+55###$$$###",
            from_="+1 507 436 2604",
            body=f'No mês de {mes} alguém bateu a meta. Seguem as informações: Vendedor: {vendedor}, Vendas: {vendas} ')
        print(message.sid)








