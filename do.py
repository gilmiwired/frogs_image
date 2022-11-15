import time
import schedule
import subprocess

def main():
    # job関数をスケジュールに登録
    schedule.every(10).seconds.do(job) # ②

    while True:
        # job関数を実行
        schedule.run_pending() # ③
        # 無限ループにすると無駄が多いのでsleep
        time.sleep(1)


def job(): # ①
    subprocess.run(['aws','s3','cp','s3://wixbacket/data.txt'])
    subprocess.run(['rm','-r','word.png'])
    subprocess.run(['git','add','.'])
    subprocess.run(['git','commit','-m','"auto up"'])
    subprocess.run(['git','push'])
    subprocess.run(['python3','test.py'])
    subprocess.run(['git','add','.'])
    subprocess.run(['git','commit','-m','auto up'])
    subprocess.run(['git','push'])
    print("HelloWorld")


if __name__ == '__main__':
    main()