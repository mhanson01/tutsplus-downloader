Tutsplus Course Downloader
==========================

This is for paid user only!
===========================

Before anything else let's clarify that this script is for paid users only.

This script will simply don't work if you don't provide a valid username and password. The account you provide must be a valid tutsplus premium's account.

Why this script?
================

Tutsplus already allow us to download their video. In fact in each lesson's page there is a shiny download button.

I wanted a way to bulk download the courses. This script just automates this process.

Installation
=============

1. Clone this repository
2. Install dependencies with ```pip install -r requirements.txt``


Example
========

First thing is to update the config.yaml file with your username and password.

Then copy and paste in the links to the courses you want to download.  I've already put a couple in place as an example.

Once you're all set, run with ```python downloader.py```

Contributions
=============

Make sure not to commit your personal username and password!  Please copy the config.yaml file and save a copy as local.yaml.  The local.yaml file will be used in place of the config.yaml and is gitignored so it will not be committed with the project.
