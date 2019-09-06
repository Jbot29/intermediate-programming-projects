# Time Based Key Value Store


The goal of this project is to make a simple time based key value store. What that means is you
can add multiple keys and then each key can have multiple values based on a date range.

So the returned value of the get will differ based on when you ask.

This allows time box of values. This can be used for various different tasks. The original
problem that it was created to solve was serving custom branded content on a website.

Prior to using a version of this code, there needed to be a prod push everytime that content changed. Which was time consuming and error prone. There was a clear schedule that could be setup ahead time and was perfectly timed.

The tool started to be used for different use cases. Another being used to lock parts of the website
just internal users for a set time period. This was used to push a feature live to production but then restrict it for testing.

It has a pretty simple interface

get db key [optional date, if not present then current time] [optional default value if key, time not found]


set db key start-date end-date value


set db "site-content" (datetime 2019 9 1 12)  (datetime 2019 9 15 12) "cvalue")
set db "site-content" (datetime 2019 9 15 12)  (datetime 2019 9 30 12) "different cvalue")

Then a get depending on when the request was made or with an optional time passed in will return
different values.

That's it.

I think this is a cool small self-contained program and I think it is a useful tool. This could, like the original store it's data in a persistent date store.