# UpChecker

UpChecker is a simple opensource project to host it fast on your server and check is server up, view statistic, get messages if it is down. UpChecker - just run file and use project easy

## Main idea of project

- Lite to install
- Lite to use

## Install pip packadges

```bash
pip install "fastapi[all]" sqlalchemy pytest
```

## Supported message types

- E-mail
- Telegram

## Supported check types

- status code
- respoinse body(some part and full)

## TODO

- [x] Architecture
- [x] Design DB(<https://dbdesigner.page.link/Dc8BxqfhVZsLMeEA9>)
- [ ] Server
- [ ] Utils
- [ ] Web client
- [ ] Script to easy install UpChecker

## Ideas

- Utils can be on other device

## Server TODO

- [x] Write DB models
- [x] Write /api/websites/ (CRUD)
- [ ] Write /api/websites/categories (CRUD)
- [ ] Write /api/checks/ (CR)
- [ ] Settings
- [ ] Auth(just one jwt token)
