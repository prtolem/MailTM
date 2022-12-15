from aiohttp import ClientSession
import logging

from .schemas.domains import Domains, Domain
from .schemas.account import Account, Token
from .schemas.message import Messages, OneMessage, MessageSource
from .utils.misc import random_string


class MailTM:
    def __init__(self):
        self.api_url = "https://api.mail.tm"

    async def __aenter__(self):
        self.session = ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    @staticmethod
    async def validate_response(response):
        if response.status in [200, 201, 204]:
            return await response.json()
        else:
            logging.error(f"Error: {response.status}")
            return None

    async def get_account_token(self, address, password) -> Token:
        """
        https://docs.mail.tm/#authentication
        """
        payload = {
            "address": address,
            "password": password
        }
        async with self.session.post(f"{self.api_url}/token", json=payload) as response:
            if await self.validate_response(response):
                return Token(**(await response.json()))

    async def get_domains(self) -> Domains:
        """
        https://docs.mail.tm/#get-domains
        """
        async with self.session.get(f"{self.api_url}/domains") as response:
            if await self.validate_response(response):
                return Domains(**(await response.json()))

    async def get_domain(self, domain_id) -> Domain:
        """
        https://docs.mail.tm/#get-domainsid
        """
        async with self.session.get(f"{self.api_url}/domains/{domain_id}") as response:
            if await self.validate_response(response):
                return Domain(**(await response.json()))

    async def get_account(self, address=None, password=None) -> Account:
        """
        https://docs.mail.tm/#post-accounts
        """
        if address is None:
            domain = (await self.get_domains()).hydra_member[0].domain
            address = f"{random_string()}@{domain}"
        if password is None:
            password = random_string()
        payload = {
            "address": address,
            "password": password
        }
        async with self.session.post(f"{self.api_url}/accounts", json=payload) as response:
            if await self.validate_response(response):
                return Account(**(await response.json()))

    async def get_account_by_id(self, account_id, token) -> Account:
        """
        https://docs.mail.tm/#get-accountsid
        """
        async with self.session.get(f"{self.api_url}/accounts/{account_id}", headers={"Authorization": f"Bearer {token}"}) as response:
            if await self.validate_response(response):
                return Account(**(await response.json()))

    async def delete_account_by_id(self, account_id, token) -> bool:
        """
        https://docs.mail.tm/#delete-accountsid
        """
        async with self.session.delete(f"{self.api_url}/accounts/{account_id}", headers={'Authorization': f'Bearer {token}'}) as response:
            if await self.validate_response(response):
                return response.status == 204

    async def get_me(self, token) -> Account:
        """
        https://docs.mail.tm/#get-me
        """
        async with self.session.get(f"{self.api_url}/me", headers={'Authorization': f'Bearer {token}'}) as response:
            if await self.validate_response(response):
                return Account(**(await response.json()))

    async def get_messages(self, token, page=1) -> Messages:
        """
        https://docs.mail.tm/#get-messages
        """
        async with self.session.get(f"{self.api_url}/messages?page={page}", headers={'Authorization': f'Bearer {token}'}) as response:
            if await self.validate_response(response):
                return Messages(**(await response.json()))

    async def get_message_by_id(self, message_id, token) -> OneMessage:
        """
        https://docs.mail.tm/#get-messagesid
        """
        async with self.session.get(f"{self.api_url}/messages/{message_id}", headers={'Authorization': f'Bearer {token}'}) as response:
            if await self.validate_response(response):
                return OneMessage(**(await response.json()))

    async def delete_message_by_id(self, message_id, token) -> bool:
        """
        https://docs.mail.tm/#delete-messagesid
        """
        async with self.session.delete(f"{self.api_url}/messages/{message_id}", headers={'Authorization': f'Bearer {token}'}) as response:
            if await self.validate_response(response):
                return response.status == 204

    async def set_read_message_by_id(self, message_id, token) -> bool:
        """
        https://docs.mail.tm/#patch-messagesid
        """
        async with self.session.put(f"{self.api_url}/messages/{message_id}/read", headers={'Authorization': f'Bearer {token}'}) as response:
            if await self.validate_response(response):
                return (await response.json())['seen'] == "read"

    async def get_message_source_by_id(self, message_id, token) -> MessageSource:
        """
        https://docs.mail.tm/#get-messagesidsource
        """
        async with self.session.get(f"{self.api_url}/messages/{message_id}/source", headers={'Authorization': f'Bearer {token}'}) as response:
            if await self.validate_response(response):
                return MessageSource(**(await response.json()))
