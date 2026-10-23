# Clementine's Skillet

A small recipe website for **Clementine Brooks**, a fictional home cook in a Savannah apartment kitchen. Built with [Reflex](https://reflex.dev/) (pure Python).

Search the recipe box, filter by vegetarian, quick, and dessert, open a card, rescale the ingredient list by changing the servings, tick off the steps, and run the kitchen timer. The abstract painting behind the page stays fixed while you scroll.

## Python version

This project targets **Python 3.14.4**.

Current Reflex (**0.10.0**) supports it. Reflex 0.10 requires Python `>=3.11,<4` and lists 3.14 in its package classifiers. Python 3.14 support itself landed in Reflex 0.8.15 (October 2025). Python 3.10 is no longer supported.

## Run it on Ubuntu

Ubuntu 24.04 does not ship Python 3.14, so the first block installs **3.14.4**. After that, `python3.14` is the interpreter used for the virtual environment.

```bash
git clone https://github.com/Gooberin95/Plato8.git
cd Plato8

sudo apt update
sudo apt install -y curl ca-certificates
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"
uv python install 3.14.4
export PATH="$HOME/.local/bin:$PATH"
python3.14 --version

python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

# rxconfig.py and the app package are already in this repo, so init is not required.
# Run it only if those files are missing:
if [ ! -f rxconfig.py ]; then reflex init; fi

reflex run
```

Open **http://localhost:3000**.

The first `reflex run` compiles the frontend and downloads its JavaScript toolchain. That can take a few minutes. Reflex also listens on port 8000 for the backend; you use the site at port 3000.

`python3.14 --version` should print `Python 3.14.4`.

## Deploying to Azure

Pushes to `main` build a production package for Azure App Service (Linux, the built-in Python 3.14 runtime, no Docker). The staging and production deploy jobs stay skipped until the repository variable `AZURE_DEPLOY_ENABLED` is `true`. Setup is in [DEPLOY.md](DEPLOY.md).
