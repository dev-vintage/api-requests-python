# Once you’ve installed the library, you’ll need to import it. Let’s start with that important step: 

import requests

# Making Our First API Request
# There are many different types of requests. The most commonly used one, a GET request, is used to retrieve data. Because we’ll just be working with retrieving data, our focus will be on making ‘get’ requests.
# When we make a request, the response from the API comes with a response code which tells us whether our request was successful. Response codes are important because they immediately tell us if something went wrong.
# To make a ‘GET’ request, we’ll use the requests.get() function, which requires one argument — the URL we want to make the request to. We’ll start by making a request to an API endpoint that doesn’t exist, so we can see what that response code looks like. 

reponse = requests.get("https://api.open-notify.org/this-api-doesnt-exist")

# The get() function returns a response object. We can use the response.status_code attribute to receive the status code for our request:

print(response.status_code)

# API Documentation
# In order to ensure we make a successful request, when we work with APIs it’s important to consult
# the documentation. Documentation can seem scary at first, but as you use documentation more
# and more you’ll find it gets easier.

# If you click the link above to look at the documentation for this endpoint, you’ll see that it says This API takes no inputs. This makes it a simple API for us to get started with. We’ll start by making a GET request to the endpoint using the requests library: 

response = requests.get("https://api.open-notify.org/astros.json")
print(response.status_code)

# We received a ‘200’ code which tells us our request was successful. The documentation tells us that the API response we’ll get is in JSON format. In the next section we’ll learn about JSON, but first let’s use the response.json() method to see the data we received back from the API:

print(response.json())



