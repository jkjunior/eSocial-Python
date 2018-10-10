import os
from os import listdir
from os.path import isfile, join
import logging


logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

logFormatter = logging.Formatter(
    "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

xsd_path = os.getcwd()+'/xsd'
generateds_path = os.getcwd() + '/dkuhlman-generateds-60c208fd6e8d/generateDS.py'


def models_path(i):
    """Returns model's location and file's name based on xsd file's name"""
    return ' -o classes/' + i.split('.')[0] + '.py -s classes/' + \
        i.split('.')[0] + 'Sub.py --super=' + i.split('.')[0] + ' '


def inplace_change(filename, old_string, new_string):
    """Safely read the input filename using 'with'"""
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            logger.info(
                '"{old_string}" not found in {filename}.'.format(**locals()))
            return

    """Safely write the changed content, if found in the file"""
    with open(filename, 'w') as f:
        logger.info(
            'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)


onlyfiles = [f for f in listdir(xsd_path) if isfile(join(xsd_path, f))]
for i in onlyfiles:
    """generateDS doesnt convert well xsd byte type very well, so we need to replace these types to string"""
    inplace_change(xsd_path + '/' + i, 'xs:byte', 'xs:string')

    os.system('python3 ' + generateds_path +
              models_path(i) + xsd_path + '/' + i)
