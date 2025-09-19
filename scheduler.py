import schedule
import time
from script import run_stock_job

from datetime import datetime

def basic_job():
    print("Job started at:", datetime.now())


# Run every minute
schedule.every().minute.do(basic_job)
# Run every minute
schedule.every().minute.do(run_stock_job)

while True:
    schedule.run_pending()
    time.sleep(1)