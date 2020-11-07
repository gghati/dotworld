# My Portfolio ([Website](http://gauravghati.herokuapp.com/))

![](https://img.shields.io/badge/Gaurav-Ghati-red)
![](https://img.shields.io/github/languages/top/gauravghati/dotworld)
![](https://img.shields.io/github/last-commit/gauravghati/dotworld)

### Website API + Github Pages = :fire:

So I accidentally figured out that we can return JSON response instead of the standard HTML when we access a GitHub Pages site.

So I thought instead of creating static website why not do some dev fun 😉 and create a REST API about me.

For example, if you do

    curl https://gauravghati.github.io/apis/home.json

Gives the following result on the terminal:

    {
        "name": "Gaurav Ghati",
        "phone": "+91 9067365762",
        "mail": "gauravghati225@gmail.com",

        "bio": "I wish to raise my understanding of the nuances of Computer Science field and use this knowledge to become better in Software development/ML Research.",
        "fun": "I made this inspite of not being a frontend developer!",

        "github": "https://github.com/gauravghati/",
        "twitter": "https://twitter.com/GauravGhati/",
        "linkedin": "http://linkedin.com/in/gauravghati/",

        "main": {
            "field1": "Open Source",
            "field2": "Backend",
            "field3": "Deep Learning"
        },

        "aboutme": {
            "para1": "My interest towards Computer Science field sparked when I was working on a project and I extracted data form inspect element of a website using regex function in JAVA by inputing HTML code as string, since then I started believing that coding can do magical things, so I have been incessantly working on improving my skills. I have done various projects on web/Software Development and would continue to do so.",
            "para2": "I'm an open-source enthusiast, and like to contribute in open source projects. After doing web dev, I stumbled upon machine learning, and found it very fascinating branch of Computer Science field, I would like continue my carrer as a ML Researcher."
        },

        "volunteer": {
            "tfi": {
                "heading": "Teach For India",
                "description": "Teach For India (TFI), a program of Teach To Lead, aims to address educational inequity by building a movement of leaders that are committed to expanding educational opportunity"
            },
            "pisb": {
                "heading": "PICT IEEE Student Branch",
                "description": "PICT IEEE Student Branch (PISB) was established with an aim of inculcating a sense of technical awareness amongst its student members in PICT."
            }
        }
    }

I used this Json Data to provide my website data, now each time the website loads django fetch data from this urls and put the data into the website!

Now each time when i have to add, delete or edit any data i just have to change the .json files and push it to my github pages repo.

What do you think? let me Know on [http://gauravghati.herokuapp.com/](http://gauravghati.herokuapp.com/)
