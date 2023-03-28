import psycopg2
import xlsxwriter
from dateutil.parser import parse
import schedule
import time

def generate_report():
    print("OLÁ, Veja como é funcional!")

schedule.every(1).second.do(generate_report)

while 1:
    schedule.run_pending()
    time.sleep(1)