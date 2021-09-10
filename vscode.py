#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import PIPE, run
from pathlib import Path
import json

EXTENSIONS = {
    "docker": ["ms-azuretools.vscode-docker"],
    "python": ["ms-python.python"],
    "node": ["dbaeumer.vscode-eslint"],
    "git": ["sidneys1.gitconfig", "eamodio.gitlens"]

}


def run_process(command, fail_message, exit_if_fail):
    """
    Wrapper around subprocess.run, printing a pertinent error on fail.
    command       : command to launch in bash
    fail_message  : message to display on fail
    exit_if_fail  : bool : True: stop process and exit if fail, else continue
    """
    response = run(command, shell=True, stdout=PIPE, stderr=PIPE)
    if response.returncode != 0:
        print('Error: {}'.format(response.stderr))
        if exit_if_fail:
            print(fail_message)
            exit(1)
    return response


def get_vscode_extensions():
    """
    Return a list of pre installed vscode extensions
    """
    # Retrieve list of extensions already installed in VSCode
    result = run_process("code --list-extensions", "Error", True)

    # Parse response and populate global variable.
    installed_extensions = result.stdout.decode('utf-8').split('\n')
    return installed_extensions


def install_vscode_extension(extension):
    """
    Install a vscode extension
    extension  : str : name of extention to install
    """
    if extension in get_vscode_extensions():
        print("  - Skipping, it's already installed")
    else:
        run_process("code --install-extension {}".format(extension), "Error.", True)


def install_extensions():
    """
    Run install of all vscode extensions
    """
    for tech, extensions in EXTENSIONS.items():
        for extension in extensions:
            print(f'Installing {tech} extension: {extension}')
            install_vscode_extension(extension)


def get_settings(settings_folder):
    """
    from the list of preconfigured settings, create a single python dict
    """
    all_settings = {}

    settings_files = settings_folder.glob('*.json')

    for settings_file in settings_files:
        print(f'Collecting settings from: {settings_file.resolve()}')
        with open(settings_file, 'r') as f:
            settings = json.load(f)
        all_settings = {**all_settings, **settings}

    return all_settings


def write_settings(all_settings, settings_file):
    """
    Grab all settings from path dir.  combine settings.
    """
    print(f'Writing settings to: {settings_file.resolve()}')
    # add settings to settings file
    with open(str(settings_file.resolve()), 'w+') as f:
        json.dump(all_settings, f, indent=4, sort_keys=True)


def main():
    # install all extensions
    install_extensions()

    # create .vscode/settings
    settings_file = Path('./.vscode/settings.json')

    # create path if not exists
    settings_file.parent.mkdir(parents=True, exist_ok=True)

    settings_folder = Path('./settings')

    # get all settings object
    all_settings = get_settings(settings_folder)

    # overwrite settings file
    write_settings(all_settings, settings_file)


if __name__ == '__main__':
    main()
