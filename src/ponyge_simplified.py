#from utilities.algorithm.general import check_python_version
#
#check_python_version()

from stats.stats import get_stats
from algorithm.parameters import params, set_params
import sys
#sys.stdout=open("test.txt","a")
import warnings
warnings.filterwarnings("ignore")

class Transcript(object):

    def __init__(self, filename):
        self.terminal = sys.stdout
        self.logfile = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.logfile.write(message)

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass

def start(filename):
    """Start transcript, appending print output to given filename"""
    sys.stdout = Transcript(filename)

def stop():
    """Stop transcript and return print functionality to normal"""
    sys.stdout.logfile.close()
    sys.stdout = sys.stdout.terminal

from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%Y_%m_%d_%H_%M_%S")

start('log_'+dt_string+'.txt')


params['GRAMMAR_FILE'] = "supervised_learning/trading_engine.bnf"
params['FITNESS_FUNCTION']="supervised_learning.trading_engine"
params['MAX_TREE_DEPTH']=10
params['POPULATION_SIZE']=10
params['SAVE_ALL']=True
params['SAVE_STEP']=True
#params['SAVE_STATE']=True
params['SELECTION_PROPORTION']=0.25
params['GENERATIONS']=5
params['GENERATION_SIZE']=3
params['ELITE_SIZE']=1
params['CROSSOVER_PROBABILITY']=0.4



set_params(sys.argv[1:])  # exclude the ponyge.py arg itself


individuals = params['SEARCH_LOOP']()

# Print final review
get_stats(individuals, end=True)

stop()