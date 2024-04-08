# Synthetic Data Generation

This repo contains the code for implementing synthetic textbook generation based on the paper:

[Textbooks Are All You Need](https://arxiv.org/pdf/2306.11644.pdf).

![Synthetic Data Generation](https://github.com/PeytonCleveland/Synthetic-Data/blob/main/assets/wizard.jpg?raw=true)

## Installation

This project requires Python 3.10 or later, and uses poetry for dependency management. To install the dependencies, run:

```bash
poetry install
```

## Usage

Scripts for generating synthetic data are located at the root of the project.

### Generate Titles

To generate synthetic titles, run:

```bash
poetry run python generate_titles.py [topic] --number [number of titles] --output [output file]
```

For example, to generate 10 titles on the topic of "mathematics" and save them to a file called "titles.txt", run:

```bash
poetry run python generate_titles.py mathematics --number 10 --output titles.txt
```

By default, the script generates 10 titles on the given topic and saves them to "output/titles.json".
