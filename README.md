# vineyard

## Objectives

* should be modular
* should be easy to configure

Easy in the sense that:

* the model can be easily tweaked

## Modules

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

## Downy mildey

[Wikipedia explanation](https://en.wikipedia.org/wiki/Downy_mildew)

The pathogen tends to become established in late summer.

Therefore, planting early season varieties may further reduce the already minor threat posed by downy mildew.

One way to control downy mildew is to eliminate moisture and humidity around the impacted plants


## Questions

* explanation input variables
* how many updates per day?
* where does the input data come from?
* what is dependent variable?
* deadline
  * does it have to be ready before late summer?
* wikipedia says downy mildew is just a minor threat, why so important?
* 

## Variables model

* neerslag
* gemiddelde dagtemperatuur
* incubatietijd
* verouderingsfactor

## Notifications

There's a Python library called [notifiers](https://github.com/notifiers/notifiers) which seems well maintained. It's a wrapper around several popular notification application.

Another option is to use the native Python library of a notification application. E.g. [Simplepush](https://simplepush.io/) seems a good match.

Simple test Simplepush which sends a notification to your phone. 5nCvuY is my username.

```
curl 'https://api.simplepush.io/send/5nCvuY/Wow/So easy'
```

