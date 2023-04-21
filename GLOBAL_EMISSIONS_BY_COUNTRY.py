import os
import time
from zipfile import ZipFile
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

DIR_PATH = os.path.abspath(os.path.dirname(__file__))
folder_name = "\_Output"

def download_file(chromedriver_url):
    DIR_PATH = os.path.abspath(os.path.dirname(__file__))
    options = webdriver.ChromeOptions();
    prefs = {"download.default_directory": DIR_PATH};
    options.add_experimental_option("prefs", prefs);
    driver = webdriver.Chrome(service_log_path=chromedriver_url, options=options)
    driver.get("https://edgar.jrc.ec.europa.eu/dataset_ghg70#p1")
    driver.maximize_window()
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/h3[1]/button[1]/span[1]/span[1]").click()
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[5]/div[1]/a[1]/span[1]").click()
    time.sleep(5)
    driver.close()
   
def unzip_file():
    file_name = "v70_FT2021_GHG_AR4_AR5b.zip"
    with ZipFile(file_name, 'r') as zip:
        zip.extractall()

def get_file(sheetname,AR_type,*args):
    unzip_file()
    df = pd.read_excel(DIR_PATH + "\EDGARv7.0_GHG_AR4_AR5.xlsx", sheet_name=sheetname, header=4,index_col=False)
    df.insert(0, "Global Warming Potential", "GWP-100 "+AR_type, True)
    df.insert(1, "units", "Mton CO2eq", True)
    for arg in args:
        df.insert(2,arg,value="")
    return df

def process_file():
    df1=get_file("Total GHG by sector country AR4", "AR4")
    df2=get_file("Total GHG by country AR4", "AR4", "Sector")
    df3=get_file("Total GHG by sector country AR5", "AR5")
    df4=get_file("Total GHG by country AR5", "AR5", "Sector")
    csv1=pd.concat([df1, df2], ignore_index=True)
    csv2=pd.concat([df3, df4], ignore_index=True)
    combined_csv=pd.concat([csv1, csv2], ignore_index=True)
    pat =DIR_PATH+ folder_name
    try:
        os.mkdir(pat)
    except OSError as error:
        print(error)
    combined_csv.to_csv(os.path.join(pat,'GLOBAL-EMISSIONS-BY-COUNTRY.csv'),index=False)

download_file("D:/selenium/chromedriver.exe")
process_file()
