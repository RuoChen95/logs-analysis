# logs-analysis
It's an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Example of output
```
Candidate is jerk, alleges rival -- 338647 views
Bears love berries, alleges bear -- 253801 views
Bad things gone, say good people -- 170098 views

Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views

2016-07-17 -- 2.21% errors
```

## Design of the code
 1. connect db
 2. make db cursor
 3. execute sql (using simple join and subqueries)
 4. print results
 5. close db

## How to run it

### Setup Project:
  1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository. The file have a directory called vagrant.
  3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here. The file inside is called newsdata.sql.
  4. Copy the newsdata.sql and logsAnalysis.py file to the vagrant directory.
  
### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:

  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant and look around with ls.
  
### Setting up the database and Creating Views:
  1. Load the data in local database using the command:
  
  ```
    psql -d news -f newsdata.sql
  ```  
  2. Use `psql -d news` to connect to database.
  
  The database includes three tables:
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  * The log table includes one entry for each time a user has accessed the site.

  
### Analyse
  The reporting contains three answers:

  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?

  run it using 
  ```
    python logsAnalysis.py
  ```

### Application code style

  Passing the pycodestyle checking.
