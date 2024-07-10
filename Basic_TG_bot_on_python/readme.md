<!-- Improved compatibility of back to top link: See: https://docs.python-telegram-bot.org/en/v21.1.1/ -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="[https://github.com/Rendition739/Portfolio/blob/main/Basic_TG_bot_on_python]">
    <img src="images/logo.png" alt="Logo" width="280" height="280">
  </a>

  <h3 align="center">Telegram bot on python</h3>

  <p align="center">
    Telegram bot written in Python.
    <br />
    <a href="https://docs.python-telegram-bot.org/en"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  <p align="center">
    That's the modification of original README file.</p>
    <a href="https://github.com/othneildrew/Best-README-Template">View the original</a>
    .
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

There are a lot of bots in different is various messenger platforms, that improve experience and can solve various problems easily. Sometimes, users face with regular issues from time to time, so that's why bots exist.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should implement DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this template!

Use the `BLANK_README.md` to get started.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Preparation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Choose any free API from that list [https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/](https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/)
2. Clone the repo
   ```sh
   git clone https://gitlab.skillbox.ru/aleksandr_belovanov/python_basic_diploma
   ```
3. Obtain API key from BotFather - https://telegram.me/BotFather.
Note: BotFather located exclusively in Telegram application.
4. Enter in official BotFather channel few commands to create new API key for a new bot: /start -> /newbot -> type any name for a bot -> type any name which ends up with "bot".
5. Copy your generated API key in `.env` file.
   ```
   TG_API_KEY = 'YOUR_API_KEY'
   ```

6. Insert any chosen API into the same `.env` file.
    ```
   EXAMPLE_API = 'https://example.com/api'
    ```
* 'YOUR_API_KEY' - should be replaced with generated API key from BotFather.
* 'https://example.com/api' - should be replaced with chosen API.
* Note: Both of those components (especially API key) should be stored in private file, because if API key will become public, anyone will be able to control the bot.
* To use API key from .env file without using it directly in the code, use 2 libraries "os" and "python-dotenv".

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USED APIS -->
## Example of adding API into the code

- [x] Correct
```
from dotenv import load_dotenv
import os

load_dotenv()
API = os.getenv("tg_api_key")
```
By that code, you'll be able to use API key from .env without revealing it.


- Incorrect
```
API = "YOUR_API_KEY"
```
It's bad practice to use API key directly in the code. By using API key in the code, it creates a risk of revealing API key to the public,
therefore a risk of losing bot completely or even rewring bot's code for malicious purposes, to deliver different kinds of malware or something even worse.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USED APIS -->
## Used APIs

Used APIs in that bot:
```sh
1. https://v2.jokeapi.dev/joke/Any?type=single
Example of API query:

{
    "error": false,
    "category": "Misc",
    "type": "single",
    "joke": "I went to the zoo the other day. There was only a dog in it – it was a shihtzu.",
    "flags": {
        "nsfw": false,
        "religious": false,
        "political": false,
        "racist": false,
        "sexist": false,
        "explicit": true
    },
    "safe": false,
    "id": 307,
    "lang": "en"
}

2. https://v2.jokeapi.dev/joke/Any?type=twopart
Example of API query:

{
    "error": false,
    "category": "Misc",
    "type": "single",
    "joke": "What does the MacBook have in common with Donald Trump?\n\nI would tell you....\nBut I don't compare apples to oranges.",
    "flags": {
        "nsfw": false,
        "religious": false,
        "political": true,
        "racist": false,
        "sexist": false,
        "explicit": false
    },
    "id": 233,
    "safe": false,
    "lang": "en"
}

Both APIs could be classified as one API due to their subtle differences of their URLs.
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- HONORABLE MENTIONS -->
## Honorable Mentions
API source: https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/
Current list has 230 different APIs. Any API from that list can be used - no account required, free of charge, no authentication required.
But for the bot any API can be used: free or paid APIs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Current space shows, which commands that bot can offer. They'll appear in the list after typing command "/help".

<!-- Commands -->
## Commands

/random_joke - shows random joke
```
Category: Spooky
Joke: I'm not saying my son is ugly...
Delivery: But on Halloween he went to tell the neighbors to turn down their TV and they gave him some candy.
```

/single_joke - same as /random_joke, but more simple.
```
Random joke: How do you make holy water? You freeze it and drill holes in it.
```

/start - activates bot and introduces itself.
```
Hello. My name is Test_bot. I am telegram bot, written on "Python" programming language.
And let me type that dear user, programming languages and regular languages are completely different things. 
Regular languages are for people, while programming languages are for us.
They're used for apps, systems, bots - like me.
I've introduced myself, so let's begin, shall we?
If you want to know, what I can offer - type '/help' 
```

/help - Bot will show all commands, that it can offer.
```
If you have some trouble - here's the list of commands that can help:
/random_joke - I'll show random joke to you.
/single_joke - Same as /random_joke, but more simple.
/start - I'll activate (how original)
/help - I'll show all commands, that I can offer.
/cancel - I'll stop a conversation.
/gen_rand_num - I'll generate random number from 1 to 1 million.
```

/cancel - Bot will stop conversation.
```
As you wish. You can type /start, if you wish to talk to me later.
I'm gonna sleep right now.
```

/gen_rand_num - Bot will generate completely random number from 1 to 1 million.
```
"Your generated number is: 345167
```

For more examples, please refer to the [Documentation](https://docs.python-telegram-bot.org/en/v21.1.1) or [Bot Examples](https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Added necessary files (.env, .gitignore, readme.md, etc.) 
- [x] Created bot architecture.
- [x] Added documentation, referring to other aspects of the project.
- [x] Add "components" document to easily copy & paste sections of the readme


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

My Email - s.belovanov.wham657@slmail.me

Project Link: [https://gitlab.skillbox.ru/aleksandr_belovanov/python_basic_diploma](https://gitlab.skillbox.ru/aleksandr_belovanov/python_basic_diploma)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. Some other links have been included, that might be useful.

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
