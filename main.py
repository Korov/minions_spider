
from apscheduler.schedulers.blocking import BlockingScheduler
from scheduler import hero_scheduler

def my_job():
    print('hello world')

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(hero_scheduler.hero_spider_scheduler, 'interval', seconds=240)
    scheduler.start()
