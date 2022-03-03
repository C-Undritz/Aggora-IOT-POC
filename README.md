# Simple IoT temperature display function using TTN webhooks

## Introduction
This is a simple flask app that is an http endpoint for a webhook set up to run from an application setup on The Things Network (TTN).  The application has connected a couple of temperature sensor end devices.

## Setup
Once logged into the TTN console (from here https://www.thethingsnetwork.org/), navigate to your applications and select the required application.  There select from the left handf menu 'integrations' and select 'Webhooks'

A webhook was added with the following parameters:

- Webhook ID: flaskapp-webhook
- Webhook format: JSON
- Base URL: https://5000-cundritz-aggoraiotpoc-h4xw57hsrec.ws-eu34xl.gitpod.io/
- Uplink message - Enabled with value '/webhook'

This then allowed for the JSON data to be read by the app in a dictionary format where it could be queried to provide the value of the required variables.
