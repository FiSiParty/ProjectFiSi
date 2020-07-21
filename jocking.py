import configparser
import os


for i in range (5):
    
    config = configparser.ConfigParser()
    a1 = [i, i+1]
    config[a1[0]] = {"Register": a1[1]}

    with open('jocker.ini','w') as configfile:
        config.write(configfile)


