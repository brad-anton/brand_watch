# Brand Watcher

This is meant to be run periodically to identify if a new domain was seen in OpenDNS' investigate that matches a defined brand

## Set up 

To use set up a virtualenv and install required packages

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then modify `brand_watch.py` and define your `api_key`

```
api_key='YOUR INVESTIGATE API KEY'
```

## Running

Set up a cron job or periodically run brand_watch with a brand you'd like to watch. For instance, to check out paypal, just provide it as a parameter. 

```
python brand_watch.py paypal
```

If you have a list of known newly registered domains, you can exclude them from results with the `-e` option:

```
python brand_watch.py -e exclude.list paypal
```

