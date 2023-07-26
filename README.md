# EDGAR GHG Data Downloader

This Python script utilizes the Selenium library to download a ZIP file containing greenhouse gas (GHG) data from the website [https://edgar.jrc.ec.europa.eu/dataset_ghg70#p1](https://edgar.jrc.ec.europa.eu/dataset_ghg70#p1). The website provides access to European GHG emission data and stores the output in a csv file in dynamic location.

## Prerequisites

1. Python 3.x installed on your system.
2. Install required packages by running `pip install selenium`.

## Webdriver Setup

1. Download the appropriate WebDriver for your browser:
   - Chrome: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
   - Firefox: [GeckoDriver](https://github.com/mozilla/geckodriver/releases)

2. Place the WebDriver executable in the same directory as the Python script.

## Configuration

Open the Python script `edgar_ghg_downloader.py` and modify the following variables as per your environment:

```python
output_zip_file = "ghg_data.zip"
```

Set the `output_zip_file` variable to the desired name for the ZIP file where the downloaded GHG data will be stored. By default, it will be saved in the same directory as the script.

## Running the Script

Run the Python script `edgar_ghg_downloader.py`:

```bash
python edgar_ghg_downloader.py
```

The script will use Selenium to navigate to the [https://edgar.jrc.ec.europa.eu/dataset_ghg70#p1](https://edgar.jrc.ec.europa.eu/dataset_ghg70#p1) website, locate and click on the download link for the GHG data ZIP file, and dynamically store the downloaded file in the specified location.

## Important Notes

- Ensure that you have the necessary permissions to access and download data from the website.
- Always comply with the terms of service and usage policies of the website.
- Use this script responsibly and avoid causing any load or strain on the website's server.

Feel free to explore and modify the script according to your specific requirements for downloading and handling GHG data. Happy coding!
