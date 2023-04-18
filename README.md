<h2 align="center">MailTM</h2>

<div align="center">
 <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/prtolem/MailTM">
 <img alt="GitHub Repo stars" src="https://img.shields.io/github/languages/code-size/prtolem/MailTM">
 <img alt="GitHub" src="https://img.shields.io/github/license/prtolem/MailTM">
</div>

## Description
Asynchronous API wrapper for https://docs.mail.tm/

## Navigation
* [Usage example](#Usage-example)
* [API methods](#API-methods)
  * [Authentication](#Authentication)
  * [Get domains list](#Get-domains-list)
  * [Get domain by id](#Get-domain-by-id)
  * [Get account](#Get-account)
  * [Get account by id](#Get-account-by-id)
  * [Delete account by id](#Delete-account-by-id)
  * [Get me](#Get-me)
  * [Get messages](#Get-messages)
  * [Get message by id](#Get-message-by-id)
  * [Delete message by id](#Delete-message-by-id)
  * [Set read message by id](#Set-read-message-by-id)
  * [Get message source by id](#Get-message-source-by-id)

## Usage example
```python
from mailtm import MailTM


def main() -> None:
    mailtm = MailTM()
    result = await mailtm.get_account_token(address="example", password="example")
    print(result)


if __name__ == '__main__':
    main()
```

## API methods
A list of all available methods with their parameters and response.

### Authentication
```python 
get_account_token(address, password)
```

| Parameter   | Type     | Description                                  |
|:------------| :------- |:---------------------------------------------|
| `address`   | `string` | Account's address. Example: user@example.com |
| `password`  | `string` | Account's password                           |

Returns token and id after successful authorization.

### Get domains list
```python 
await get_domains()
```

| Description             |
|:------------------------|
| Doesn't take parameters |

Returns a list of domains.

### Get domain by id
```python 
await get_domain(domain_id)
```

| Parameter    | Type     | Description                         |
|:-------------| :------- |:------------------------------------|
| `domain_id`  | `string` | The domain you want to get with id  |

Returns a domain by its id (Useful for deleted/private domains).

### Get account
```python 
await get_account(address, password)
```

| Parameter   | Type     | Description                                  |
|:------------| :------- |:---------------------------------------------|
| `address`   | `string` | Account's address. Example: user@example.com |
| `password`  | `string` | Account's password                           |

Creates an Account resource (Registration).

### Get account by id
```python 
await get_account_by_id(account_id, token)
```

| Parameter    | Type     | Description                                  |
|:-------------| :------- |:---------------------------------------------|
| `account_id` | `string` | Account's address. Example: user@example.com |
| `token`      | `string` | Account's token                              |

Get an Account resource by its id (Obviously, the Bearer token needs to be the one of the account you are trying to retrieve).

### Delete account by id
```python 
await delete_account_by_id(account_id, token)
```

| Parameter    | Type     | Description                          |
|:-------------| :------- |:-------------------------------------|
| `account_id` | `string` | The account you want to delete by id |
| `token`      | `string` | Account's token                      |

Deletes the Account resource.

### Get me
```python 
await get_me(token)
```

| Parameter  | Type     | Description     |
|:-----------| :------- |:----------------|
| `token`    | `string` | Account's token |

Returns the Account resource that matches the Bearer token that sent the request.

### Get messages
```python 
await get_messages(token, page)
```

| Parameter | Type     | Description                |
|:----------|:---------|:---------------------------|
| `token`   | `string` | Account's token            |
| `page`    | `int`    | The collection page number |

Returns all the Message resources of a given page.

### Get message by id
```python 
await get_message_by_id(message_id, token)
```

| Parameter     | Type       | Description                         |
|:--------------|:-----------|:------------------------------------|
| `message_id`  | `string`   | The message you want to get by id   |
| `token`       | `string`   | Account's token                     |

Retrieves a Message resource with a specific id.

### Delete message by id
```python 
await delete_message_by_id(message_id, token)
```

| Parameter     | Type       | Description                         |
|:--------------|:-----------|:------------------------------------|
| `message_id`  | `string`   | The message you want to delete's id |
| `token`       | `string`   | Account's token                     |

Deletes the Message resource.

### Set read message by id
```python 
await set_read_message_by_id(message_id, token)
```

| Parameter     | Type       | Description                        |
|:--------------|:-----------|:-----------------------------------|
| `message_id`  | `string`   | The message you want to read's id  |
| `token`       | `string`   | Account's token                    |

Marks a Message resource as read.

### Get message source by id
```python 
await get_message_source_by_id(message_id, token)
```

| Parameter     | Type       | Description                       |
|:--------------|:-----------|:----------------------------------|
| `message_id`  | `string`   | The source you want to get by id  |
| `token`       | `string`   | Account's token                   |

Gets a Message's Source resource.
