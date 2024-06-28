#IMDb Top 250 TV Shows Scraper
This project scrapes the IMDb website for the top 250 TV shows and saves the extracted data into Excel and CSV files.

##Prerequisites
Before you begin, ensure you have the following installed:
    Python 3.x
    ChromeDriver
    The required Python libraries:
        selenium
        beautifulsoup4
        openpyxl
        pandas
You can install the required libraries using pip:
    pip install selenium beautifulsoup4 openpyxl pandas

##Setup
    Download ChromeDriver:
    Download the ChromeDriver executable that matches your version of Chrome and place it in the same directory as your script or specify its path in the code.
    Clone or Download the Repository:
    Ensure all the files are in the same directory.

##Code Explanation
The script consists of three main classes:
    SearchIMBD: Handles the search operations on Google to find the IMDb Top 250 TV Shows page.
    ScrapData: Inherits from SearchIMBD and is responsible for scraping the data from the IMDb page.
    ExportData: Inherits from ScrapData and handles exporting the scraped data to Excel and CSV files.
    
    ##How to Run
        Navigate to the Project Directory:
        Open your terminal or command prompt and navigate to the directory containing the script.
        Run the Script:
        Execute the script using Python:
            python Searchimbd.py

##Script Details
    ###SearchIMBD Class
    This class opens a Chrome browser, searches for "IMDb Top 250 TV Shows" on Google, and retrieves the link to the IMDb page.
        open_google: Opens the Google search page.
        search_imbd: Inputs "IMDb Top 250 TV Shows" in the search box and searches.
        Top_250_TV_Shows: Finds and stores the link to the "Top 250 TV Shows" page.
        time_before_quit: Waits for 10 seconds before closing the browser.

    ###ScrapData Class
    Inherits from SearchIMBD and scrapes the data from the IMDb page.
        get_data: Navigates to the IMDb Top 250 TV Shows page and extracts the required data (rank, name, year, episodes, and rating).

    ###ExportData Class
    Inherits from ScrapData and exports the scraped data to Excel and CSV files.
        export_to_excel: Saves the data into an Excel file.
        export_to_csv: Saves the data into a CSV file.

    ###Main Function
        The main function orchestrates the process:
        Creates an instance of SearchIMBD and performs the search.
        Creates an instance of ScrapData, reuses the driver and link from SearchIMBD, and extracts the data.
        Creates an instance of ExportData, passes the scraped data, and exports it to Excel and CSV.
        Waits for 10 seconds before closing the browser.

##Troubleshooting
    Ensure chromedriver.exe is in the same directory as the script or specify the path in the code.
    Make sure all required libraries are installed.