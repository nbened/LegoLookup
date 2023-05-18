# LegoLookup
### Get price estimations on custom sets. Great for:
- #### Book builds (my use case, with 'The Lego Engineer')
- #### MOC's
- #### Youtube tutorials

## Reason
#### I got a book called 'The Lego Engineer' with cool builds and parts listed but no LEGOs, and no way to get prices on the provided parts.
#### I couldn't find anything else that worked, so I built this.
## Steps
- `python main.py` to construct build object
- `python recall.py` to display build object

## Limitations
- your temp folder houses your part objects in case retrieving prices, but will be overwritten if you pass something else there
- to avoid rate limiting, the program waits between requests. this can be very long, so grab a cup of coffee an take a walk. 
    - It should probably use proxies, but waiting seems more ethical and easier to code.