import json

with open("new_visit_rwanda_sentiment_analysis.ipynb", encoding = "UTF-8") as file:
    data = json.load(file)

# get the programming language info
programming_language = data["metadata"]["kernelspec"]

# list comprehension to get the necessary information for each cell:
cells = [ [x["cell_type"], x["source"]] for x in data["cells"] ]

author = "Israel"
date = "January 9th, 2022"

yaml_config = f"""---
title: |
  <center>Visit Rwanda Sentiment Analysis</center>  
  <center>Using Twitter API</center>
  <br />
author: |
  <p style="float: right">{author}</p>
  <br />
date: |
  <p style="float: right">{date}</p>
  <br />
output:
  html_document:
    highlight: textmate
    theme: flatly
    number_sections: yes
    toc: yes
    toc_float:
      collapse: yes
      smooth_scroll: yes
---

"""

file_text = yaml_config
for cell_type, source in cells:
    if cell_type == "markdown" and source:
        file_text += "".join(source) + "\n\n"
    elif cell_type == "code" and source:
        code_block = (
f"""```{{{programming_language}}}
{''.join(source)}
```\n\n"""
        )
        
        file_text += code_block + "\n\n"
        
        
with open("converted_notebook.Rmd", "w", encoding = "UTF-8") as file:
    file.write(file_text)