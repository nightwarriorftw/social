<p align="center">
<img src="graphics/social.png">
</p>

[![Open Issues](https://img.shields.io/github/issues/nightwarrior-xxx/social?style=for-the-badge&logo=github)](https://github.com/nightwarrior-xxx/social/issues) [![Forks](https://img.shields.io/github/forks/nightwarrior-xxx/social?style=for-the-badge&logo=github)](https://github.com/nightwarrior-xxx/social/network/members) [![Stars](https://img.shields.io/github/stars/nightwarrior-xxx/social?style=for-the-badge&logo=reverbnation)](hhttps://github.com/nightwarrior-xxx/social/stargazers) ![Maintained](https://img.shields.io/maintenance/yes/2019?style=for-the-badge&logo=github) ![Made with Python](https://img.shields.io/badge/Made%20with-Python-blueviolet?style=for-the-badge&logo=python) ![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red?style=for-the-badge&logo=open-source-initiative) ![Built with Love](https://img.shields.io/badge/Built%20With-%E2%99%A5-critical?style=for-the-badge&logo=ko-fi) [![Follow Me](https://img.shields.io/twitter/follow/nightwarrior_xx?color=blue&label=Follow%20%40nightwarrior_xx&logo=twitter&style=for-the-badge)](https://twitter.com/intent/follow?screen_name=nightwarrior_xx) [![Telegram](https://img.shields.io/badge/Telegram-Chat-informational?style=for-the-badge&logo=telegram)](https://telegram.me/nightwarrior_xxx)

## :ledger: Index

- [About](#beginner-about)
- [Usage](#zap-usage)
  - [Commands](#package-commands)
- [Development](#wrench-development)
  - [Pre-Requisites](#notebook-pre-requisites)
  - [Developmen Environment](#nut_and_bolt-development-environment)
  - [File Structure](#file_folder-file-structure)
- [Community](#cherry_blossom-community)
  - [Contribution](#fire-contribution)
  - [Branches](#cactus-branches)
  - [Guideline](#exclamation-guideline)
- [Gallery](#camera-gallery)
- [Credit/Acknowledgment](#star2-creditacknowledgment)
- [License](#lock-license)

## :beginner: About

Gaming is evolving in India day-by-day. There must be a Social platform where Gamers can share their experience and acheivements. Every Gamer was once a noob and other noobs learn from pros. Pro Gamers and even Noobs can share their statistics here.

## :zap: Usage

The project will be hosted online and even on TOR.

### :package: Commands

```BASH
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## :wrench: Development

Everyone is welcome to contribute just follow the steps.

### :notebook: Pre-Requisites

List all the pre-requisites the system needs to develop this project.

- Basic knowledge on virtual environment
- Minimal knowledge of django

### :nut_and_bolt: Development Environment

#### 1. Create & activate the virtual environment

```Bash
python3 -m venv test
source test/bin/activate
```

#### 2. Clone the Repository

```Bash
git clone https://github.com/nightwarrior-xxx/social.git
cd social
```

#### 3. Install the dependencies

```BASH
pip install -r requirements.txt
```

#### 4. Generate Secret key for django

After installing django (which will be automatically installed by the above command), use this

```BASH
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Now paste this secret key in `social/social/settings.py` file.
Remember to use environment variables for setting secret key. And don't push secret key on your branch. Check out how to setup environment variables in Python3 [here](https://stackoverflow.com/questions/5971312/how-to-set-environment-variables-in-python)

#### 5. Setup postgress database

Check out this link to setup postgress database [here](https://djangocentral.com/using-postgresql-with-django/)

#### 6. Create a super user & Run server:

```BASH
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### :file_folder: File Structure

```
├── LICENSE
├── README.md
├── requirements.txt
├── social
│   ├── accounts
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── templates
│   │   │   ├── auth
│   │   │   │   ├── login.html
│   │   │   │   └── register.html
│   │   │   ├── profile
│   │   │   │   └── user.html
│   │   │   └── social
│   │   │       ├── feed.html
│   │   │       ├── home.html
│   │   │       └── post.html
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   ├── test_forms.py
│   │   │   ├── test_models.py
│   │   │   ├── test_urls.py
│   │   │   └── test_views.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── cred.sh
│   ├── manage.py
│   ├── post
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_auto_20190913_1447.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── posts
│   │   │       └── post.html
│   │   ├── tests.py
│   │   └── views.py
│   ├── social
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── img
│   │       └── logo.svg
│   └── templates
│       ├── base
│       │   ├── css.html
│       │   ├── js.html
│       │   └── navbar.html
│       └── base.html

```

## :cherry_blossom: Community

### :fire: Contribution

Your contributions are always welcome and appreciated. Following are the things you can do to contribute to this project.

1.  **Report a bug** <br>
    If you think you have encountered a bug, and I should know about it, feel free to report by making an issue and I will take care of it.

2.  **Request a feature** <br>
    You can also request for a feature. Just make an issue, and if it will viable, it will be picked for development.

3.  **Create a pull request** <br>
    It can't get better then this, your pull request will be appreciated.

### :cactus: Branches

I use an agile continuous integration methodology, so the version is frequently updated and development is really fast.

1. **`dev`** is the development branch.

2. **`master`** is the production branch.

**Steps to work with feature branch**

1. To start working on a new feature, create a new branch prefixed with `FEATURE` and followed by feature name. (ie. `FEATURE-<feature name>`)
2. Once you are done with your changes, you can raise PR.

**Steps to create a pull request**

1. Make a PR to `dev` branch.
2. Comply with the best practices and guidelines e.g. where the PR concerns visual elements it should have an image showing the effect.

After this, changes will be merged.

### :exclamation: Guideline

Make sure that there is onle one extra line after the file ends and remember the indentation.

## :camera: Gallery

Pictures of project.

## :star2: Credit/Acknowledgment

Credits goes to me and other contributors

## :lock: License

[LICENSE](/LICENSE)
