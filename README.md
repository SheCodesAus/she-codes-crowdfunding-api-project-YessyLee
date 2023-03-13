# Title: FutureProofME

This is a crowdfunding app for people looking to upskill and transform their career quickly through short courses, bootcamps, masterclasses etc. These courses are usually not funded by HECS, hence requesting the fund through crowdfunding would be ideal. Form of payment would be monetary donation. Donation will be released to the education institution at the end of the projects closed date.

## Features

### User Accounts

- [X] Username
- [X] Email Address
- [X] Password

### Project

- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Target Amount to Fundraise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
- [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge
  
### Implement suitable update delete

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [ ] Destroy - I will likely implement "CLOSE" instead of Destroy, in case there are portion of money been donated, which can be returned to supporters if the owners decided not to go ahead with the study.
- Pledge
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [ ] Destroy - Not implementing this, due to the same reason as above
- User
  - [X] Create
  - [X] Retrieve
  - [X] Update - Password
  - [ ] Destroy - Will implement close account perhaps - Admin has the ability to Destroy

### Implement suitable permissions

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Limit who can create
  - [ ] Limit who can retrieve - - everyone can view but unable to do anything else
  - [X] Limit who can update
  - [X] Limit who can delete
- Pledge
  - [X] Limit who can create
  - [ ] Limit who can retrieve - - everyone can view but unable to do anything else
  - [X] Limit who can update
  - [X] Limit who can delete
- Pledge
  - [ ] Limit who can retrieve - everyone can view but unable to do anything else
  - [X] Limit who can update
  - [X] Limit who can delete

### Implement relevant status codes

- [X] Get returns 200
- [X] Create returns 201
- [X] Not found returns 404

### Handle failed requests gracefully 

- [X] 404 response returns JSON rather than text

### Use token authentication

- [X] implement /api-token-auth/

## Additional features

- [X] Update Password

Users have the ability to change password

- [X] Filtering/Global Search on Project

Everyone has the ability to search across projects

- [ ] {Title Feature 3} - To be confirmed

{{ description of feature 3 }}

### External libraries used

- [X] django-filter


## Part A Submission 

Please see PDF called "Submission Docs for DRF - Yessy Rayner" saved in this repo.

- [X] A link to the deployed project.
- [X] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [X] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [X] A screenshot of Insomnia, demonstrating a token being returned.
- [X] Your refined API specification and Database Schema.

### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).

1. Create User

```shell
curl --request POST \
  --url http://127.0.0.1:8000/users/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser",
	"email": "not@myemail.com",
	"password": "not-my-password"
}'
```

2. Sign in User

```shell
curl --request POST \
  --url http://127.0.0.1:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser",
	"password": "not-my-password"
}'
```

3. Create Project

```shell
curl --request POST \
  --url http://127.0.0.1:8000/projects/ \
  --header 'Authorization: Token 5b8c82ec35c8e8cb1fac24f8eb6d480a367f322a' \
  --header 'Content-Type: application/json' \
  --data '{
	"title": "Donate a cat",
	"description": "Please help, we need a cat for she codes plus, our class lacks meows.",
	"goal": 1,
	"image": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Dollar_bill_and_small_change.jpg",
	"is_open": true,
	"date_created": "2023-01-28T05:53:46.113Z"
}'
```
