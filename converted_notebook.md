---
title: |
  <center>Visit Rwanda Sentiment Analysis</center>  
  <center>Using Twitter API</center>
  <br />
author: |
  <p style="float: right">Mugisha Israel</p>
  <br />
date: |
  <p style="float: right">January 9th, 2022</p>
  <br />
output:
  rmdformats::downcute:
    keep_md: true
    self_contained: true
    thumbnails: true
    lightbox: true
    gallery: false
    highlight: tango
    toc_float:
      collapse: yes
      smooth_scroll: yes
---



# #VisitRwanda Sentiment Analysis

## What is Visit Rwanda.
Visit Rwanda is a Tourism campaign project started by RDB to promote Tourism in Rwanda This campaign partners with ***Arsenal, Paris Saint-Germain F.C(PSG), Tour du Rwanda and Basketball Africa League(BAL)***.
This campaign has increased the level of tourism in Rwanda, hence the development of the country since Tourism in Rwanda is the largest source of foreign exchange earnings in Rwanda and was projected to grow at a rate of 25% every year from 2013-18.

## My Inspiration?
I wanted to collect some feedback from people to what they think about Top Touristic attraction sites  in Rwanda including: **Lake Kivu, Gorillas, and Akagera National Park ** and Top VisitRwanda Partners **PSG and ARSENAL**  and a place to find this feedback was to scrappe some data from Twitter as many people use twitter to share their thoughts on a certain subject and I wanted to see how people are commenting towards these places.

## My Discoveries.
I collected 1000 tweets and preprocessed them, kept them in a dataframe that was letter uploaded to *BigQuery* and did *ETL* in Tableau where I created a *Dashboard* that you can interact with to see my Discoveries. All of these in an Upstream *Pipeline* that updates automatically with any change.
<script type='text/javascript' src='https://dub01.online.tableau.com/javascripts/api/viz_v1.js'></script><div class='tableauPlaceholder' style='width: 1200px; height: 927px;'><object class='tableauViz' width='1200' height='927' style='display:none;'><param name='host_url' value='https%3A%2F%2Fdub01.online.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='&#47;t&#47;mugishaisrael' /><param name='name' value='visit-rwanda-sentiment-analysis&#47;VisitRwandaSentimentAnalysis' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='showAppBanner' value='false' /></object></div>

