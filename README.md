# telegram-bot-updater
Custom bot for daily updates sent to your Telegram chat!

## Introduction

This is a simplified, custom made bot hosted on RPI Zero. Bot collects the information about:

* Amount of registered COVID-19 cases in defined countries and calculates the amount for previous date (# of active cases one day ago - # of active cases one day ago.) For more details please check <i>services/covid_updater.py</i>. Countries object could be modified in <i>/countries.py</i>
* Weather conditions for predefined city (hosted in <i>/city_details.py</i>)
* Air polution level for predefined city (hosted in <i>/city_details.py</i>)


## Example output

 
## How to install

1. Clone and download repository using Github link
2. Create and run a virualenv on your machine: 
```
python3 virtualenv /<path_to_folder>/<env_name>
```

3. Install dependencies from <i>requirements.txt</i> in your environment:
```
pip3 install -r /<path_to_folder>/requirements.txt
```
4. Run <i>main.py</i> file from your terminal or IDE: 

```
python3 main.py
```



