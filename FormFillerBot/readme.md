<!-- PROJECT LOGO -->
<br />
<div align="center">
<h1 align="center">Form Filler Automation 🤖</h1>
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
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is used to allow bot users to fill out forms within desktop and web applications. Bot users can fill out forms within any application without lifting a finger. <br/>Just execute the bot!


### Built With

[![Python][Python]][Python-url]
[![PyAutoGUI][PyAutoGUI]][PyAutoGUI-url]
[![Selenium][Selenium]][Selenium-url]
[![OpenCV][OpenCV]][OpenCV-url]


[Python]: https://img.shields.io/badge/python-black?style=for-the-badge&logo=python
[PyAutoGUI]: https://img.shields.io/badge/pyautogui-black?style=for-the-badge&logo=python
[Selenium]: https://img.shields.io/badge/selenium-black?style=for-the-badge&logo=selenium
[OpenCV]: https://img.shields.io/badge/opencv-black?style=for-the-badge&logo=opencv

[Python-url]: https://www.python.org/
[PyAutoGUI-url]: https://pyautogui.readthedocs.io/
[Selenium-url]: https://www.selenium.dev/
[OpenCV-url]: https://opencv.org/

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

From now on, I will guide you on how to prepare the environments for talented developers loving Python.

### Prerequisites

First, you need to set up Python 3.12.4 to start the development.<br/>
You can download Python 3.12.4 here : https://www.python.org/downloads/

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/EasyMerchant/FormFillerBot.git
   ```
2. Go to the directory and make the venv file to manage python packages all
   ```sh
   python -m venv .venv
   ```
3. Activate this venv file to use in development<br/>
   For WindowsOS
   ```sh
   .venv/Scripts/activate
   ```
   For MacOS
   ```sh
   source .venv/bin/activate
   ```
4. Install the python packages using requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
5. Run python script
   ```sh
   python main.py
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage - How to stop the bot?
```
If you move your mouse during the bot do its action, the bot will be stopped perfectly.
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

1. Open the Chrome browser using `Selenium`
2. Go to the specific web site.
3. Finds the primary monitor from connected devices using `screeninfo` library. The bot decides to do its actions on the primary monitor.
4. Bot analyzes the input.json file and acts as the workflow mentioned in input.json. In input.json mention the keywords for bot actions. Using `pyautogui` library, the bot will act by its keyword(for example, "action": "mouse_move").
5. If the bot meets dropdown, the bot will use `OpenCV`.
6. During the bot does its action, the bot will be stopped perfectly if you move mouse device using `mouse` and `threading` library.

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features.

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


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
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