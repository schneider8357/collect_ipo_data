# collect_ipo_data

Collection of scripts to collect and process IPO-related data from the SEC Edgar platform


## Quickstart

```
git clone https://github.com/schneider8357/collect_ipo_data
cd collect_ipo_data
pip install -r requirements.txt
python3 get_form_urls.py PICS
```

## Usage

```
$ python3 get_forms_urls.py PICS
Starting search for F-1s and S-1s for company cik=1841644
Found the following F-1s and S-1s:
https://www.sec.gov/Archives/edgar/data/1841644/0001213900-21-022408.txt
```

Alternatively, you can pass the `-q` option to print only the URLs:
```
$ python3 get_forms_urls.py PICS -q
https://www.sec.gov/Archives/edgar/data/1841644/0001213900-21-022408.txt
```
