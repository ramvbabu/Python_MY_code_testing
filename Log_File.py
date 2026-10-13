import os
import datetime
import logging


file_path = os.path.dirname(os.path.abspath(__file__))
print (file_path)
filePath = file_path
print("the file path:",filePath)
#scriptPath = os.environ.get('SCRIPT_PATH')
now = datetime.datetime.now()
print ("the now as :",now)
process_time = now.strftime('%Y-%m-%d-%H-%M')
print("the process time: ",process_time)



# Logging setup
LOG_FILE = os.path.join(file_path,'logs','dataloader-{}.log'.format(process_time))
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
#track in log files
stream_handler = logging.StreamHandler() 
# log the info in terminal
stream_handler.setLevel(logging.INFO)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler(LOG_FILE, mode='w'),
                             stream_handler])
logger = logging.getLogger(__name__)


logger.info(str(file_path))

#rootFilePath = r"/apps/sapphire/crt_d/dev/Datasets"
rootFilePath = os.path.join(filePath,'Datasets15Q')
NUM_SECONDS_IN_A_MIN = 60


# scenario_args = args['scenario_args']
# logger.info(scenario_args)
# scenario=scenario_args['scenario']
for i in range(1,10):
    logger.info("the value of i: %s", i)