# Prereqs

Install the requirements file with `pip install -r requirements.txt`.

You will need to create a GitHub app if you have not already done so. On your user, go to Settings > Developer Settings > GitHub App > New GitHub App

Give your app a name, URL, disable the webhook. Once you create the app, you will need to note the **application_id** for later.

Once your app has been created, navigate to the general settings page and scroll down to find the Private Keys section. Generate a **private key** and copy it to the folder where this script lives.

Finally, you need to install the application somewhere. I would recommend installing it to your local user's GitHub account for testing purposes. Once installed, you should be able to find a numeric identifier in the URL bar, this is the **installation_id**.

Once you have all those pieces, you can run the script to generate a temporary token:

```sh
python3 generate_github_token.py <application_id> <installation_id> <path_to_private_key_pem_file>
```
