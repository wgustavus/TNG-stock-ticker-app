# %% [markdown]
# ### Sep 2025 - Zach Wilson DataExpert BEGINNER Bootcamp
#  DATA PIPELINE SCHEDULER ONLY 'intro' video -- this is just the scheduler portion of the pipeline lab 
#  NOTES: 
#    - Requires an import for the schedule package
#    - Best practice = store required libraries in a requirements.txt file (use to install: pip install -r requirements.txt)

# %%
import schedule
import time
from datetime import datetime

# %%
from my_script import run_stock_job

def basic_job():
    print("Job started at:", datetime.now())

# Run every 5 minutes
schedule.every(5).minutes.do(basic_job)
# Run every minute
schedule.every(5).minutes.do(run_stock_job)

while True:
    schedule.run_pending()
    time.sleep(1)



