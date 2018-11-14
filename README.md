# SFMC Deployment & Backup scripts

WIP

A collection of quick & dirty Python scripts to Automate backing up assets and moving them between Business Units.

## Setup

First, you need to [create and Installed Package](https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-app-development.meta/mc-app-development/install-packages.htm) 

and [add API Integration](https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-app-development.meta/mc-app-development/api-integration.htm).

Make sure the API Integration has permissions to use Content Builder.

After that, rename `config.template.py` to `config.py` and add access credentials. The scripts will use the new per-tenant base URLs, so don't forget these. 

## Downloading Assets

After that, open the command line, go to the directory containing the script file and run `downloadAssets.py`. This should save your assets to a JSON file.

