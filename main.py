import openpyxl.workbook
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import openpyxl
import pandas as pd



class SearchIMBD:
    def __init__(self):
        self.service = None
        self.driver = None
        self.input_element = None
        self.link = None
        
    
    def open_google(self):
        '''
        This function opens the browser and go to google search website
        '''
        self.service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://google.com")   #to open the browser and go to the url

    def search_imbd(self):
        '''
        input imbd into search box an search 
        '''
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
        ) #This will wait for upto 5 secs until we locate the element by that classname (The search box). This prevent error incase of slow network
        self.input_element = self.driver.find_element(By.CLASS_NAME, "gLFyf") #get access to the search box

        self.input_element.clear()                                 #This clear the input field before inputing text
        self.input_element.send_keys("Imdb" + Keys.ENTER)   #input Imdb  in the search box and searching

    def Top_250_TV_Shows(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Top 250 TV Shows"))
        ) #This will wait for upto 5 secs until we locate the element by the name "Top 250 TV Shows". This prevent error incase of slow network
        self.link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Top 250 TV Shows").get_attribute("href") #search for a link with the name 'Top 250 TV Show'
        
    
    def time_before_quit(self):
        '''
        The program will wait for 10 secs before closing
        '''
        time.sleep(10)
        self.driver.quit()




class ScrapData(SearchIMBD):
    def __init__(self, name='', rank='', year='', episodes='', rating=''):
        super().__init__()
        self.data=[]
        
    def get_data(self):
        #Navigate to the link obtain
        self.driver.get(self.link)
        
        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        
        # Find all TV shows
        tv_shows = soup.find("ul", class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base")
        
        # Extract data for each TV show
        for tv_show in tv_shows:
            rank = tv_show.find("h3", class_="ipc-title__text").text.split(".")[0]
            name = tv_show.find("h3", class_="ipc-title__text").text.split(".")[1]
            text_element = tv_show.find_all("span", class_="sc-b189961a-8 kLaxqf cli-title-metadata-item")
            if len(text_element) >= 2:
                year = text_element[0].text
                episodes = text_element[1].text
            else:
                year = "N/A"
                episodes = "N/A"
            rating = tv_show.find("span", class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").text
            
            self.data.append([rank, name, year, episodes, rating])

        


class ExportData(ScrapData):
    def __init__(self):
        super().__init__()
    
        
    def export_to_excel(self, filename="IMBD_Top_250_TV_Shows.xlsx"):
        #creating a new excel sheet
        excel = openpyxl.Workbook()  
        #Assigning new varaible to the active sheet
        sheet = excel.active
        #Assigning new name to the excel sheet
        sheet.title = "IMBD Top 250 Rated TV Shows"
        #Append the headings 
        sheet.append(['Rank', 'Name', 'Year', 'Episodes', 'IMBD Rating'])
        for row in self.data:
            sheet.append(row)
        excel.save(filename)
        print(f"Successfully saved as {filename}")

    def export_to_csv(self, filename="IMBD_Top_250_TV_Shows.csv"):
        df = pd.DataFrame(self.data, columns=['Rank', 'Name', 'Year', 'Episodes', 'Rating'])
        df.to_csv(filename, index=False)
        print(f"Successfully saved as {filename}")



     

def main():
        search_imbd = SearchIMBD()
        search_imbd.open_google()
        search_imbd.search_imbd()
        search_imbd.Top_250_TV_Shows()
        
        scrap_data = ScrapData(SearchIMBD)
        scrap_data.driver = search_imbd.driver  # Reuse the driver from SearchIMDB instance
        scrap_data.link = search_imbd.link      # Reuse the link obtained in SearchIMDB instance
        scrap_data.get_data()

        export_data = ExportData()
        export_data.data = scrap_data.data
        export_data.export_to_excel()
        export_data.export_to_csv()

        

        search_imbd.time_before_quit()
            

        

if __name__ == "__main__":
    main()



