# ovh-api-scripts
## Intro
Script Library for batch opration in OVHCloud Environement
## Installation
1. Install python3 and pip for your environement OS
2. install Python OVH Wrapper :
>pip install ovh
## Configuration
### 1. Creation of your application keys
Click on the following link: https://eu.api.ovh.com/createApp/, enter your customer ID, your password, and the name of your application. The name will be useful later if you want to allow others to use it.

You get two keys:
- the application key, named AK
- your secret application key, named AS
This keys are not linked to one customer but to your application or your adminitration computer.
### 2. Create config file
```
[default]
; general configuration: default endpoint
endpoint=ovh-eu

[ovh-eu]
; configuration specific to 'ovh-eu' endpoint
application_key=my_app_key
application_secret=my_application_secret
consumer_key=my_consumer_key
```
The client will successively attempt to locate this configuration file in

* Current working directory: ./ovh.conf
* Current user's home directory ~/.ovh.conf
* System wide configuration /etc/ovh.conf
