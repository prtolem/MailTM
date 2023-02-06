import logging

from aiohttp import ClientSession

from .schemas.account import Account, Token
from .schemas.domains import Domains, Domain
from .schemas.message import Messages, OneMessage, MessageSource
from .utils.exceptions import MailTMInvalidResponse
from .utils.misc import random_string, validate_response

logger = logging.getLogger('mailtm')


class MailTM:
    API_URL = "https://api.mail.tm"

    def __init__(self, session: ClientSession = None):
        self.session = session or ClientSession()

    async def get_account_token(self, address, password) -> Token:
        """
        https://docs.mail.tm/#authentication
        """
        payload = {
            "address": address,
            "password": password
        }
        response = await self.session.post(f"{self.API_URL}/token", json=payload)
        logger.debug(f'Response for {self.API_URL}/token: {response}')
        if await validate_response(response):
            return Token(**(await response.json()))
        logger.debug(f'Error response for {self.API_URL}/token: {response}')
        raise MailTMInvalidResponse

    async def get_domains(self) -> Domains:
        """
        https://docs.mail.tm/#get-domains
        """
        response = await self.session.get(f"{self.API_URL}/domains")
        logger.debug(f'Response for {self.API_URL}/domains: {response}')
        if await validate_response(response):
            return Domains(**(await response.json()))
        logger.debug(f'Error response for {self.API_URL}/domains: {response}')
        raise MailTMInvalidResponse

    async def get_domain(self, domain_id) -> Domain:
        """
        https://docs.mail.tm/#get-domainsid
        """
        response = await self.session.get(f"{self.API_URL}/domains/{domain_id}")
        logger.debug(f'Response for {self.API_URL}/domains/{domain_id}: {response}')
        if await validate_response(response):
            return Domain(**(await response.json()))
        logger.debug(f'Error response for {self.API_URL}/domains/{domain_id}: {response}')
        raise MailTMInvalidResponse

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
        logger.debug(f'Create account with payload: {payload}')
        response = await self.session.post(f"{self.API_URL}/accounts", json=payload)
        logger.debug(f'Response for {self.API_URL}/accounts: {response}')
        if await validate_response(response):
            return Account(**(await response.json()))
        logger.debug(f'Error response for {self.API_URL}/accounts: {response}')
        raise MailTMInvalidResponse

    async def get_account_by_id(self, account_id, token) -> Account:
        """
        https://docs.mail.tm/#get-accountsid
        """
        response = await self.session.get(f"{self.API_URL}/accounts/{account_id}",
                                          headers={"Authorization": f"Bearer {token}"})
        logger.debug(f'Response for {self.API_URL}/accounts/{account_id}: {response}')
        if await validate_response(response):
            return Account(**(await response.json()))
        logger.debug(f'Error response for {self.API_URL}/accounts/{account_id}: {response}')
        raise MailTMInvalidResponse

    async def delete_account_by_id(self, account_id, token) -> bool:
        """
        https://docs.mail.tm/#delete-accountsid
        """
        response = await self.session.delete(f"{self.API_URL}/accounts/{account_id}",
                                             headers={'Authorization': f'Bearer {token}'})
        logger.debug(f'Response for {self.API_URL}/accounts/{account_id}: {response}')
        if await validate_response(response):
            return response.status == 204
        logger.debug(f'Error response for {self.API_URL}/accounts/{account_id}: {response}')
        raise MailTMInvalidResponse

    async def get_me(self, token) -> Account:
        """
        https://docs.mail.tm/#get-me
        """
        response = await self.session.get(f"{self.API_URL}/me", headers={'Authorization': f'Bearer {token}'})
        logger.debug(f'Response for {self.API_URL}/me: {response}')
        if await validate_response(response):
            return Account(**(await response.json()))
        logger.debug(f'Error response for {self.API_URL}/me: {response}')
        raise MailTMInvalidResponse

    async def get_messages(self, token, page=1) -> Messages:
        """
        https://docs.mail.tm/#get-messages
        """
        response = await self.session.get(f"{self.API_URL}/messages?page={page}",
                                          headers={'Authorization': f'Bearer {token}'})
        logger.debug(f'Response for {self.API_URL}/messages: {response}')
        if await validate_response(response):
            return Messages(**(await response.json()))
        logger.debug(f'Error response for {self.API_URL}/messages: {response}')
        raise MailTMInvalidResponse

    async def get_message_by_id(self, message_id, token) -> OneMessage:
        """
        https://docs.mail.tm/#get-messagesid
        """
        response = await self.session.get(f"{self.API_URL}/messages/{message_id}",
                                          headers={'Authorization': f'Bearer {token}'})
        logger.debug(f'Response for {self.API_URL}/messages/{message_id}: {response}')
        if await validate_response(response):
            return OneMessage(**(await response.json()))
        logger.debug(f'Error response for {self.API_URL}/messages/{message_id}: {response}')
        raise MailTMInvalidResponse

    async def delete_message_by_id(self, message_id, token) -> bool:
        """
        https://docs.mail.tm/#delete-messagesid
        """
        response = await self.session.delete(f"{self.API_URL}/messages/{message_id}",
                                             headers={'Authorization': f'Bearer {token}'})
        logger.debug(f'Response for {self.API_URL}/messages/{message_id}: {response}')
        if await validate_response(response):
            return response.status == 204
        logger.debug(f'Error response for {self.API_URL}/messages/{message_id}: {response}')
        raise MailTMInvalidResponse

    async def set_read_message_by_id(self, message_id, token) -> bool:
        """
        https://docs.mail.tm/#patch-messagesid
        """
        response = await self.session.put(f"{self.API_URL}/messages/{message_id}/read",
                                          headers={'Authorization': f'Bearer {token}'})
        logger.debug(f'Response for {self.API_URL}/messages/{message_id}/read: {response}')
        if await validate_response(response):
            return (await response.json())['seen'] == "read"
        logger.debug(f'Error response for {self.API_URL}/messages/{message_id}/read: {response}')
        raise MailTMInvalidResponse

    async def get_message_source_by_id(self, message_id, token) -> MessageSource:
        """
        https://docs.mail.tm/#get-messagesidsource
        """
        response = await self.session.get(f"{self.API_URL}/messages/{message_id}/source",
                                          headers={'Authorization': f'Bearer {token}'})
        logger.debug(f'Response for {self.API_URL}/messages/{message_id}/source: {response}')
        if await validate_response(response):
            return MessageSource(**(await response.json()))
        logger.debug(f'Error response for {self.API_URL}/messages/{message_id}/source: {response}')
        raise MailTMInvalidResponse
