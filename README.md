# Visualizing Bank Marketing Dataset

This web app is a demo for a web-based dashboard visualizing Bank Marketing dataset. Built with D3.js and Django. The productionized application is deployed using Docker, Nginx on an AWS EC2 instance (t2.small).

Includes an interactive predictive modelling segment with an interactive chart where users are able to key in their customer inputs to generate the probability of the customer subscribing.

You may view the demo here: http://13.250.99.99

## Quickstart

* As this is a production model, port 80 will be used. If you are running this app locally, please ensure that port 80 is not being used.
* Ensure docker and docker-compose is installed
* On the root project folder, run the command:
```{bash}
docker-compose up
```

The app should be up and running. You can access it via the machine IPV4 address (0.0.0.0) for local machine. 
