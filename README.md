# COMP90024- project2
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors-)

COMP90024 - Cluster and Cloud Computing - 2022 S1 - Project 2

**Melbourne the Most Liveable City?**

## Table of contents
* [Project Description](#project-description)
* [Team members](#team-members)
* [Demo Video](#demo-video)
* [Report](#report)
* [Repository Structure](#repository-structure)


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

## Demo Video
https://www.youtube.com/watch?v=7l91CaYvbdI&t=1s

## report
- [report](./docs/Report.pdf)

## Repository Structure
```
| /Data_analytics
      - data analyzer including sentiment analyser, income statistics etc.
  /deployment 
      - ansible scripts and some config files for deployment
  /tweeter-harvester
      - twitter crawler, including searcher and streamer
  /web application
      - web application for visualization
  /docs 
      - documentations
  .gitignore 
      - config file, ignored file list when git push
  .README.md
      - homepage file to display project information
```
