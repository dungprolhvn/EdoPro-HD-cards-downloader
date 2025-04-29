# YGO HD card downloader

## Description

This simple Python script download all HD card images from [YGOPRODeck](https://ygoprodeck.com/card-database/) card database for apps like EdoPro

## Features

* Download all YGO card images and save them to a folder on your computer

## Requirements

* Windows machine with the latest version of Python 3 installed
* At least 3 GB of free disk space
* A decent internet connection

## Installation

1. **Open Windows Terminal, CMD or any terminal of your choice**

2. **Clone the repository:**

```bash
git clone https://github.com/dungprolhvn/EdoPro-HD-cards-downloader.git
cd EdoPro-HD-cards-downloader
```

3. **Install dependencies:**

After cloning the repository, run the following command

```bash
pip install -r requirements.txt
```

* This command will install all necessary modules needed by the script

## Usage

Inside the same terminal, run

``` bash
python ygo_downloader.py -f [Target folder] -a [Download attempts] -r [Number of retries]
```

* `Target folder` is the **absolute path** of the folder to save all of those downloaded image, default is `C:\ProjectIgnis\pics`
* `Download attempts` is the maximum number of attempt the script will try to download a single card image in case of failure, default is `3`
* `Number of retries` is the maximum number of times the program will try to download card images that failed to download after all attempt, default is `3`
* Any arguments (-f, -a, -r) can be omitted and the program will use a default value
* If default is fine, you can simply run `python ygo_downloader.py` to download all cards image.

## Support

* All card images are downloaded at no cost from [YGOPRODeck](https://ygoprodeck.com/card-database/), you can buy the [Premium subscription](https://ygoprodeck.com/premium/) to support them
