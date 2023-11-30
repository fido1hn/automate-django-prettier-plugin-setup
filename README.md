# Automate Prettier Configuration Steps For Django Projects

Prettier is great for code formatting but it breaks Django templates when handling **template tags**.
Thanks to [@sezze](https://github.com/sezze), [prettier-plugin-django-alpine](https://github.com/sezze/prettier-plugin-django-alpine) now offers a starting point to solve this problem with relative ease

## The Challenge

If you use Prettier for code formatting, and find yourself setting up the prettier plugin for your many projects.
You might want to automate the prettier configuration steps since it can be repetitive

### Requirements:

- VSCode
- VSCode Prettier extension(must be installed via extensions tab in VSCode)

## Steps To Automate

1 install prettier(local installation from npm)

```bash
npm install --save-dev --save-exact prettier
```

2 install prettier-plugin-django-alpine

```shell
npm install --save-dev prettier-plugin-django-alpine
```

3 add .prettierrc file to the project root folder

4 add below code to your .prettierrc file to register the plugin

```json
{
  "plugins": ["prettier-plugin-django-alpine"]
}
```

## How To Use

1. Download this script and save it to any folder of your choice on your computer

2. In your project's root folder, open a terminal and **run** the code below

```shell
python ~/path/to/configure_prettier.py
```

### Extra

You can set a bash/cmd/ps alias for the above command on your OS and call just one command(the alias name) to get up and running

Happy Coding 😊
