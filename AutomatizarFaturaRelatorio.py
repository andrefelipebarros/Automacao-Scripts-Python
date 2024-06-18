import schedule
import time

def generate_report():
    print("OLÁ, Veja como é funcional!")

#Coloquei para a cada 1 segundo rodar esse script(No caso a função "generate_report()").
schedule.every(1).second.do(generate_report)

while 1:
    schedule.run_pending()
    time.sleep(1)
