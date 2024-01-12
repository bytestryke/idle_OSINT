# config.py
import configparser
import os

class Config:
    config = configparser.ConfigParser()
    config.read('config.ini')

    @classmethod
    def save(cls):
        with open('config.ini', 'w') as configfile:
            cls.config.write(configfile)

    @classmethod
    def load(cls):
        if not cls.config.has_section('APIKeys'):
            cls.config.add_section('APIKeys')

        cls.shodan_api_key = cls.config.get('APIKeys', 'shodan_api_key', fallback='')
        cls.virus_total_api_key = cls.config.get('APIKeys', 'virus_total_api_key', fallback='')
        cls.censys_api_key = cls.config.get('APIKeys', 'censys_api_key', fallback='')
        cls.alienvault_otx_api_key = cls.config.get('APIKeys', 'alienvault_otx_api_key', fallback='')

    @classmethod
    def set_api_keys(cls, shodan_api_key, virus_total_api_key, censys_api_key, alienvault_otx_api_key):
        current_config = configparser.ConfigParser()
        current_config.read('config.ini')

        # Check if the API keys are blank in the settings_dialog
        if shodan_api_key:
            cls.config.set('APIKeys', 'shodan_api_key', shodan_api_key)
        else:
            cls.config.set('APIKeys', 'shodan_api_key', current_config.get('APIKeys', 'shodan_api_key', fallback=''))

        if virus_total_api_key:
            cls.config.set('APIKeys', 'virus_total_api_key', virus_total_api_key)
        else:
            cls.config.set('APIKeys', 'virus_total_api_key', current_config.get('APIKeys', 'virus_total_api_key', fallback=''))

        if censys_api_key:
            cls.config.set('APIKeys', 'censys_api_key', censys_api_key)
        else:
            cls.config.set('APIKeys', 'censys_api_key', current_config.get('APIKeys', 'censys_api_key', fallback=''))

        if alienvault_otx_api_key:
            cls.config.set('APIKeys', 'alienvault_otx_api_key', alienvault_otx_api_key)
        else:
            cls.config.set('APIKeys', 'alienvault_otx_api_key', current_config.get('APIKeys', 'alienvault_otx_api_key', fallback=''))

        cls.save()
