# Scraper

A tool that allows for the gathering of information from an inputted website

# Libraries needed:

    requests
    beautifulsoup4
    svelte
    cors 
    express

# Setup

The Frontend UI is created by Svelte (Javascript framework) which interacts with the python script via the server using express. 

To get it running on a local enviroment you will need to install all required dependancies and then run:

```npm run start```

from within the webapp folder and then go to localhost.8000

# Features ToDo: 

Output gathered data into a pdf via python 

Gather dns information for the selected site

Pass information through to the frontend

Make it so it is using svelte routing instead of doing a 'hard redirect'

# Possible in future

Have so users can select what information they want from sites via radioboxes or some similar method 

Be able to work with javascript websites (Selenium?)