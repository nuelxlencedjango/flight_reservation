from bs4 import BeautifulSoup as bs
from urllib import request
import re
import pandas as pd

page_source = request.urlopen("https://gettocenter.com/airports/top-100-airports-in-world")