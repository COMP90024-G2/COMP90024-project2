# COMP90024- project2
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors-)

COMP90024 - Cluster and Cloud Computing - 2022 S1 - Project 2

**Melbourne the Most Liveable City?**

## Table of contents
* [Project Description](#project-description)
* [Team members](#team-members)
* [Demo](#demo)
* [Video](#video)
* [Report](#report)
* [Repository Structure](#repository-structure)
* [Twitter Harvester](#twitter-harvester)


## Project Description
This is an investigation conducted on Twitter social media platform about the livability of Melbourne. The scenario that was chosen for this assignment is related to the topic of language diversity, health and income. We attempt to link these subjects with user activity on Twitter and learn about the city's true opinion. The general system architecture consists of various components and is deployed on the Melbourne Research Cloud (MRC).


## Team members
<table>
  <tr>
    <td align="center"><a href="https://github.com/WAZHANG1"><img src="https://avatars.githubusercontent.com/u/80433256?v=4" width="100px;" alt=""/><br /><sub><b>Claire Zhang (1080915)</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Cassie917"><img src="https://avatars.githubusercontent.com/u/54353253?v=4" width="100px;" alt=""/><br /><sub><b>Yi Yang (1074365)</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/hengzhi-qiu"><img src="https://avatars.githubusercontent.com/u/103925905?v=4" width="100px;" alt=""/><br /><sub><b>Hengzhi Qiu (1253748)</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/yfeng-Pan"><img src="https://avatars.githubusercontent.com/u/69497521?v=4" width="100px;" alt=""/><br /><sub><b>Yifeng Pan (955797)</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/yonghao-hh"><img src="https://avatars.githubusercontent.com/u/80231404?v=4" width="100px;" alt=""/><br /><sub><b>Yonghao Hu (1049814)</b></sub></a><br /></td>
  </tr>
</table>

<table>
  <tr>
  </tr>
</table>

## Demo
http://172.26.129.178

## Video
https://www.youtube.com/watch?v=7l91CaYvbdI&t=1s

## Report
- [Final Report](./report/CCC_Report.pdf)

## Repository Structure
```
  /Aurin_Data
      - Data from Aurin in .json format
| /Data_analytics
      - data analyzer including sentiment analyser, income statistics etc.
  /deployment 
      - ansible scripts and some config files for deployment
  /tweeter-harvester
      - twitter crawler, including searcher and streamer
  /web application
      - web application for visualization
  /report 
      - documentations
  .gitignore 
      - config file, ignored file list when git push
  .README.md
      - homepage file to display project information
```

## Twitter Harvester

### General info
The Twitter harvester is developed in Python language. The [Twitter API](https://developer.twitter.com/en/docs/platform-overview) supports programmatic access to Twitter in a fast and advanced way. In this project, we implemented two main methods to harvest tweets with regards to the topic we were concerned, which exploit the Streaming API and Searching API respectively. Both APIs provide keyword retrieval, which allows us to extract relevant tweets. [Tweepy](https://docs.tweepy.org/en/stable/api.html) is a specialized module for working with the Twitter API in Python.


### Getting Started
The application `Searcher.py` and `Streamer.py` make use of Twitter's Search and Stream API and stores the extracted tweets in CouchDB. The API tokens and some other constants (keywords, couchdb address etc.) are defined in `DB_Constants.py` 
### Prerequisites
#### Python packages
* Tweepy
* Couchdb
* json
* time
* Shapely
* re
### Running
Testing Twitter Havester on localhost:
- Run the Searcher
```
python3 Searcher.py
```
- Run the Streamer
```
python3 Streamer.py
```