# Auto-GPT-Commercetools-Plugin
A plugin that adds Commercetools API integration into Auto GPT

### How to use a plugin

1. **Clone the plugin repo** 
1. **Install the plugin's dependencies (if any):**
   Navigate to the cloned directory in your terminal, and run the following command to install any required dependencies:

   ``` shell
      pip install -r requirements.txt
   ```
1. Package the plugin as a Zip file: If you cloned the repository, compress the plugin `src/auto_gpt_commercetools_plugin` folder as a Zip file.
1. Copy the plugin's Zip file: Place the plugin's Zip file in the plugins folder of the Auto-GPT repository.
1. Update your plugins_config.yaml file to enable the plugin. If you skip this step the plugin won't be loaded

   ```shell
   AutoGPT_CT:
      - config: {} # Configs from the plugin README and installation instructions.
      - enabled: true
   ```
1. Add API client to the .env file
```
################################################################################
### Commercetools API
################################################################################

CTP_PROJECT_KEY=<project-key>
CTP_CLIENT_SECRET=<secret>
CTP_CLIENT_ID=<id>
CTP_AUTH_URL=https://auth.<region>.<provider>.commercetools.com
CTP_API_URL=https://api.<region>.<provider>.commercetools.com
CTP_SCOPES=manage_project:<project-key>
```
