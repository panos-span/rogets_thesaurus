# Roget's Thesaurus in the 21st Century

## Introduction

Roget's Thesaurus is a widely used reference work for writers and students. It groups words into categories and provides
a list of synonyms for each word. The first edition was published in 1852, and it has been updated many times since
then.
The most recent edition was published in 2019.
Our task in this assignment is to investigate how these categories fare with the meaning of English words as captured
by Machine Learning techniques, namely, their embeddings.

## Project Structure

The project is organized as follows according to the poetry standard for our Assignment:

- [scrapping.ipynb](rogets_thesaurus/scrapping.ipynb): The Jupyter notebook that contains the code to scrape the data
  from the website
  and save the
  embeddings of the words to a ChromaDB database. (1st and 2nd objectives)
- [clust_embed.ipynb](rogets_thesaurus/clust_embed.ipynb): The Jupyter notebook that contains the code for the one and
  two-level
  clustering of the
  embeddings. (3rd objective)
- [cls_embed.ipynb](rogets_thesaurus/cls_embed.ipynb): The Jupyter notebook that contains the code for the
  classification of the
  embeddings. (4th objective)

Lastly, the Notebook [rogets_thesaurus.ipynb](rogets_thesaurus.ipynb) contains the assignment with the details of the
project objectives (4 in total).

## Dependencies for the Project

We will need to use libraries that are not included in the Python Standard Library which are handled using Poetry

In order to install the dependencies, we will need to run the following commands in the terminal

1. (If we haven't already installed Poetry)

```bash
pip install poetry
```

2. After we have installed Poetry, we will need to run the following command in the terminal

```bash
poetry install
```

3. (Optional) If we want to use the Jupyter Notebook with the virtual environment created by Poetry, we will need to run
   the following command in the terminal

```bash
poetry shell
```

4. After we have installed the dependencies, we will need to run the following command in the terminal

```bash
jupyter notebook
```