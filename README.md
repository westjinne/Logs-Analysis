# Logs-Analysis
Udacity Nanodegree: Full Stack Web Developer Nanodegree Program Project03

## Project Overview

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.
The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

## Prerequisites
### Programs
- Python 2.7.12: https://www.python.org/downloads/release/python-2714/
- Vagrant: https://www.virtualbox.org/wiki/Downloads
- VirtualBox: https://www.virtualbox.org/wiki/Downloads
- VM configuration files: https://github.com/udacity/fullstack-nanodegree-vm

## Notice
### How to run the project?
1. Install Vagrant, VirtualBox programs by links provided above. 
2. Download VM configuration files by links provided above.
3. By using terminal (or other cmd prompt), change the directory that VM configuration files are downloaded, and start vagrant.

For example: (WHEN VM configuration files are stored at Downloads/FSND-Virtual-Machine/ directory.)
   <pre><code> 
   $ cd Downloads
   $ cd FSND-Virtual-Machine
   $ cd vagrant
   $ vagrant up
   $ vagrant ssh
   $ cd /vagrant
   $ psql -d news -f newsdata.sql</code></pre>
   
   After this process, you'll get news.sql file. 
4. To run myqueries.py file, type <pre><code> $ python myqueries.py</code></pre> at the terminal. 

### Directory
<Logs_Analysis> directory is for submit!!! Please check this directory when you do review.
### Source code
1. There are 1 python file contains query and 1 text file for output.
   <pre><code>myqueries.py</code></pre> will run the query. 

2. The size of "newsdqta.dql" was too big, so I didn't uploaded it. When needed, I'll upload it. 
