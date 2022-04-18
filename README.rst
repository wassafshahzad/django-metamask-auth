=========================
MetaMask Authentication
=========================

This is a Django Application which allows you to create one click SignUp and Logins 
with Meta Mask extension. This application does need a metamask extension installed 
in your browser to work.

This app using djangorestframework-simplejwt to manage JWT tokens and you can refer to their `documentation <https://django-rest-framework-simplejwt.readthedocs.io/en/latest/>`_

Quick start
-----------

1. Add "metaMaskAuth" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'metaMaskAuth',
    ]

2. Include the metaMaskAuth URLconf in your project urls.py like this::

    path('metamask/', include('metaMaskAuth.urls')),

3. Run ``python manage.py migrate`` to create the metaMask models.

URLS
------

Create User instance with meta mask wallets public address
===========================================================

- To create a user and wallet instance based on public address of metamask wallet, send a **POST** request to the base url for the application. Using the above
  example it would be **metamask/**

- By default the url will expect the following data::

    {
        user: {
            <USER_MODEL_REQUIRED_FIELDS>

        }
        public_address: <public_address>
    }

- Example using the django default user model::

    {
        user: {
            username: Example,
            email: example@gmail.com
        }
        public_address: examplepublicaddress123
    }

- **You dont need to send a password. An unsable password is set for the user model since we wont be needing it for validation**
- An automatic nonce is generated for the user on creation

Retrieve Nonce for Created User
================================
- To retreive the nonce of an instance send a **GET** request to the base url for the application with public_address as a path param. Using the above
  example it would be **metamask/<int: public_address>**
- This will fetch the wallet data as per serializer

Login User to get JWT Token
============================
- To login a user send a **POST** request to the baseurl + `login/<int:public_address>` post fix. Using the above
  example it would be **metamask/login/<int: public_address>**
- By default the url will expect the following data::

    {
        signature : <signed by meta mask>
    }
- This will reqturn an JWT token in reponse which can be used for authentication.

- **The rest is same as using djangorestframework-simplejwt to manage JWT tokens and you can refer to their `documentation <https://django-rest-framework-simplejwt.readthedocs.io/en/latest/>`_ for configurationa and customizations**

Settings
==========
You can provide `MetaMaskAuth` settings like this::

    DEFAULTS = {
        "UPDATE_LAST_LOGIN": False,
        "NONCE_LEN": 24,
        "VALIDATION_SERIALIZER": "metaMaskAuth.serializers.WalletTokenObtainSerializer",
        "WALLET_AUTHENTICATION_SERIALIZER": "metaMaskAuth.serializers.WalletAuthSerializer",
        "USE_SLIDING_TOKEN": False,
    }


- UPDATE_LAST_LOGIN

    - A boolean value, which is used to update last login of user on login


- NONCE_LEN

    - An int value, which controls the length of nonce generated. Default is 24


- VALIDATION_SERIALIZER

    - This is a string import, for the serializer which contains the logic for validation.
      You can override this serializer to customize the validation method. This would then be inherited by 
      TokenObtainPairSerializer aswell as TokenObtainSlidingSerializer.

- USE_SLIDING_TOKEN

    - A boolean value, used to set whether to use sliding token or not.