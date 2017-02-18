# ice-rink
Python app for scraping twitter for particular tags/mentions/search terms and plotting them on a map

We are in the process of getting together a slack channel. Also planning on using collect-social as our gateway to social media data. Because we likely to need to iterate rapidly on that for this project for that reason I recommend using my fork initially contributing back as often as possible. https://github.com/westover/collect-social

# Current proposed architecture:

- Storm backed pipeline topology for processing search results from the various sources and transformation
- Redis HLL objects for deduplication of results using MD5 hashes as representations
- Elasticsearch or MongoDB sink for processed results because of their existing restful interfaces
- Tornado based web app for any custom RESTful interfaces
- Front end using something like openlayers or leaflet with react being the framework of choice

# Possible extension ideas:
- React-Native mobile apps for push notifications
