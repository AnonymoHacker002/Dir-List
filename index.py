from termcolor import colored as color 
from os import system as sys, path

from tools.dorkings.main import dorkings
from tools.dir_list.main import dir_list
from tools.scanning.main import scanning
from tools.scraper.main import scraper
from tools.sair.main import sair

def init():
  banner("Search-Dir")

  menu_principal = input(color("""
############### [ SPIDER-TOOLS ] #################

01) DORKINGS
02) DIR-LIST
03) SCANNING
04) SCRAPERS
00) SAIR

[SPIDER@TOOLS]>> """))

  options = menu_principal

  if ( options == "01" or options == "1"):
    dorkings()
  elif ( options == "02" or options == "2"):
    dir_list()
  elif ( options == "03" or options == "3"):
    scanning()
  elif ( options == "04" or options == "4"):
    scraper()
  elif ( options == "00" or options == "0"):
    sair()

init()
