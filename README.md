# eia-data-wrangling
Eia data wrangling project

### Setup
You will need python@3 to run the script.

register on opendata [here](https://www.eia.gov/opendata/register.php) and obtain your API key

then add API key to `.env` file

```
API_KEY=<OBTAINED_KEY>
```

install dependencies,

if using pipenv

```
pipenv install  // install all dependencies listed in Pipfile
```

or 
```
pip install requests python-dotenv pandas
```

then run script

```
python3 scripts/gas-prices.py
```

### Data
generated data is exported to the csv files in the `/data` directory
