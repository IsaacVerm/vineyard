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

The service can be written in Flask. Notifications can be done either with the Notifiers library or a standard app. The web app itself can just be done with Flask and a templating engine or a bit more involved with a web framework like Vue or Angular.

These libraries are chosen because they have a minimalistic vision enabling us to:

* write code that's easy to understand by others
* quickly set up a proof of concept

## Questions

* explanation variables

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

