# Contributing to yt-view-bot

Thanks for wanting to help improve the YouTube Viewer bot.

## Ground rules

- This is an educational / research tool. Do not open PRs that add
  proxy-pool scraping of private services, captcha-solving services,
  or anything that targets real monetized channels.
- Keep the codebase readable. Small focused modules beat giant ones.
- Run `pytest` before opening a PR. All tests must pass.
- Follow the existing folder layout: `core/`, `handlers/`, `services/`,
  `models/`, `utils/`.

## Development setup

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
python -m ytview
```

## Commit style

Short imperative subject line, e.g. `handlers: retry watch-page navigation`.

## Reporting bugs

Open an issue with:
- Windows version
- Python version
- the exact command you ran
- the full traceback from `logs/ytview.log`