# vineyard

## Data

### Puppeteer

Install package.json like requirements.txt with npm install.

Selection based on [id](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors).

[Puppeteer recorder](https://github.com/checkly/puppeteer-recorder) is a handy tool to record steps.

https://pptr.dev/

You have to use method `page.waitForSelector()` if you change tab/login, ... 

Run the script `node fetch-weather-station-data.js`

Provide credentials in file `credentials.js` in format:

```
module.exports = {
    username: 'username',
    password: 'password'
}
```

[Good tutorial](https://medium.com/@e_mad_ehsan/getting-started-with-puppeteer-and-chrome-headless-for-web-scrapping-6bf5979dee3e)

Do not set [input value](https://stackoverflow.com/questions/47966510/how-to-fill-an-input-field-using-puppeteer) with `page.type()`.

### Data sources

### Data contract

## Background

### Downey mildew

*Plasmopara viticola* causes downy mildew. Mostly occurs in rainy areas (e.g. Belgium). *Plasmopara viticola* has 2 infection cycles:

* asexual (primary infection)
* sexual (secundary infection)

 Since the disease spreads very fast during the secondary infection cycles, successful control depends on controlling the primary infections.

### 3-10 rule

Traditionally the *3-10* rule is used as a "model". This rule says there will be an infection when:

* temperature > 10 degrees
* vine shoots > 10 cm
* 10 mm of rainfall in last 24-48 hours
* 
The *3-10* rule can be assumed to be a minimum acceptancecriterium for our own model. In addition it can be usedas a sanity check for our own model. If our own model deviates too far from the rule it probably means something is wrong with our model and not the rule(although the rule is far from perfect).

## Model

### Verification model

The dependent variable (the presence of downy mildew) is not present in the data set provided. It is thus impossible to verify the model.

### mechanistic model

The model simulates the infection process from germination to symptoms.

![](development-plasmopara-viticola.png)

When weather conditions are favourable (e.g. high temperature, enough rainfall) a cohort will be simulated until disease appearance; otherwise, the simulation for the cohort stops at any stage of pathogen development. 

Important is cohorts are used because that's what they had modelling problems with in Excel. The issue is multiple cohorts can be developing at the same time.

### variables

Weather variables are logged by a weather station in the vineyard. These weather variables are the input of the model.

- relative humidity
- temperature
  - min
  - max
  - average
- wetness leaf (bladnat)
- light
- barrometric pressure

Barometric pressure can be used to predict state variables like temperature, rainfall coming days.

### Goal

Goal is to get each hour an estimate of the probability of downy mildew using a mechanistic model detailed in the following papers:

* A model predicting primary infections of Plasmopara viticola in different grapevine-growing areas of Italy
* A mechanistic model simulating primary infections
of downy mildew in grapevine

Based on this probability notifications are sent.

A secundary goal is to visualize the actions taken, input variables and mildew probability.

## Requirements

* modular
* hourly updates
* configurable
* model should not be black-box
* model can be tweaked
* logging
 
Configurable in the sense you have to be able to specify fixed parameters for the model like:

* type of terrain
* type of grape
* sensitivity
* type of pesticide used

Sensitivity refers to giving certain variables more weight than others based on the state of the terrain the previous year (e.g. the surface is still very wet so put more emphasis on rainfall than temperature)

Model should not be black-box so people can be convinced of its value. 

The model should be tweaked next year based on the results of this year.

Logging:

* when pesticide was used
* presence/absence of downy mildey

## Parts application

* model
* service
* notifications
* web app

Advantage of using a service here:

* both notifications and web app don't need to know directly about how the model works
* safety checks can be made on the data
* easier to test

The service can be written in [Flask](https://palletsprojects.com/p/flask/).

Notifications can be done either with:

* the `notifiers` library
* native implementation of an app

The web app itself can be done with:

* Flask in combination with a templating engine
* web framework like [Vue](https://vuejs.org/)

If we use Flask to render the data the page will be static. If we use a web framework dynamic options are possible.

These libraries are chosen because they have a minimalistic vision enabling us to:

* write code that's easy to understand by others
* quickly set up a proof of concept

## Deliverables

* application
* documentation
  * how to configure model
  * how to deploy app
* basic tests

## Notifications

Spraying should be done if both:

* model predictions exceed threshold
* hasn't been sprayed for at least a certain time

This certain time has be to verified (let's take a week as an example).

There's a Python library called [notifiers](https://github.com/notifiers/notifiers) which seems well maintained. It's a wrapper around several popular notification application.

Another option is to use the native Python library of a notification application. E.g. [Simplepush](https://simplepush.io/) seems a good match.

Simple test Simplepush which sends a notification to your phone. 5nCvuY is my username.

```
curl 'https://api.simplepush.io/send/5nCvuY/Wow/So easy'
```

## Security

By default Flask enable CORS (cross-origin scripting). However, for developing this hinders more than it helps. To disable it there's a `Flask-CORS` [library](https://flask-cors.readthedocs.io/en/latest/).

Pay attention, this should be removed in a real production deployment.

## Deployment

The following should be deployed:

* database
* service
* web app

Use [Heroku](https://www.heroku.com/) with [tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku).

* install Heroku cli
* login to Heroku with cli
* create app
* add WSGI entry 
* push to Heroku

The app is automatically linked to GitHub if it has the same name as the repo. So to be able to deploy each part independently, they each have a separate git repository.

To update the Heroku branch:

```
git push heroku master
```

If you have no Heroku remote linked automatically you can add one [this way](https://devcenter.heroku.com/articles/git#creating-a-heroku-remote):

```
heroku git:remote -a app-name
```

### file based database

The database we use is `sqlite` which is file based. Files are cleaned every now and so often on Heroku so the database is wiped clean again. Might not be much of an issue if data is refetched/model is recalculated entirely each hour.

### web server

Flask itself (the web application) is not sufficient, you need a also need a webserver. [This](https://vsupalov.com/what-is-gunicorn/) explains it well:

```
Gunicorn takes care of everything which happens in-between the web server and your web application.
```

So no need to get into the nitty-gritty of load balancing, etc...

The link between the web server (`gunicorn`) and web application (`flask`) is formed by the `WSGI`:

```
The Python Web Server Gateway Interface (WSGI) is a way to make sure that web servers and python web applications can talk to each other.
```

To [setup the WSGI](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04) you need to create an entrypoint.