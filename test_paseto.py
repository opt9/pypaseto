import pytest
import paseto


def _set_unit_test_only_nonce(nonce):
    """
    If you are trying to figure out how to set a nonce, DONT!

    When calling parse/create, the nonce is automatically generated
    using the libsodium functions, which are likely more secure than another
    source.

    Even when accessing PasetoV2 directly (not recommended), you should never
    need to generate your own nonce.

    The tests set a nonce because the tests need a deterministic nonce because
    they have to compare the newly generated tokens with a pre-generated token.
    """
    paseto.PasetoV2.nonce_for_unit_testing = nonce  # don't do this in your code


sym_key = bytes.fromhex('707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f')
null_key = b'\0'*32
full_key = b'\xff'*32
nonce = b'\0'*24
nonce2 = bytes.fromhex('45742c976d684ff84ebdc0de59809a97cda2f64c84fda19b')
private_key = bytes.fromhex(
    'b4cbfb43df4ce210727d953e4a713307fa19bb7d9f85041438d9e11b942a37741'
    'eb9dbbbbc047c03fd70604e0071f0987e16b28b757225c11f00415d0e20b1a2')
public_key = bytes.fromhex(
    '1eb9dbbbbc047c03fd70604e0071f0987e16b28b757225c11f00415d0e20b1a2'
)

@pytest.mark.parametrize("token", [
    {
        'raw': b'v2.local.driRNhM20GQPvlWfJCepzh6HdijAq-yNUtKpdy5KXjKfpSKrOlqQvQ',
        'message': b'',
        'key': null_key,
        'footer': b'',
        'nonce': nonce
    },
    {
        'raw': b'v2.local.driRNhM20GQPvlWfJCepzh6HdijAq-yNSOvpveyCsjPYfe9mtiJDVg',
        'message': b'',
        'key': full_key,
        'footer': b'',
        'nonce': nonce
    },
    {
        'raw': b'v2.local.driRNhM20GQPvlWfJCepzh6HdijAq-yNkIWACdHuLiJiW16f2GuGYA',
        'message': b'',
        'key': sym_key,
        'footer': b'',
        'nonce': nonce
    },
    {
        'raw': b'v2.local.driRNhM20GQPvlWfJCepzh6HdijAq-yNfzz6yGkE4ZxojJAJwKLfvg.Q3VvbiBBbHBpbnVz',
        'message': b'',
        'key': null_key,
        'footer': b'Cuon Alpinus',
        'nonce': nonce
    },
    {
        'raw': b'v2.local.driRNhM20GQPvlWfJCepzh6HdijAq-yNJbTJxAGtEg4ZMXY9g2LSoQ.Q3VvbiBBbHBpbnVz',
        'message': b'',
        'key': full_key,
        'footer': b'Cuon Alpinus',
        'nonce': nonce
    },
    {
        'raw': b'v2.local.driRNhM20GQPvlWfJCepzh6HdijAq-yNreCcZAS0iGVlzdHjTf2ilg.Q3VvbiBBbHBpbnVz',
        'message': b'',
        'key': sym_key,
        'footer': b'Cuon Alpinus',
        'nonce': nonce
    },
    {
        'raw': b'v2.local.BEsKs5AolRYDb_O-bO-lwHWUextpShFSvu6cB-KuR4wR9uDMjd45cPiOF0zxb7rrtOB5tRcS7dWsFwY4ONEuL5sWeunqHC9jxU0',
        'message': b'Love is stronger than hate or fear',
        'key': null_key,
        'footer': b'',
        'nonce': nonce
    },
    {
        'raw': b'v2.local.BEsKs5AolRYDb_O-bO-lwHWUextpShFSjvSia2-chHyMi4LtHA8yFr1V7iZmKBWqzg5geEyNAAaD6xSEfxoET1xXqahe1jqmmPw',
        'message': b'Love is stronger than hate or fear',
        'key': full_key,
        'footer': b'',
        'nonce': nonce
    },
    {
        'raw': b'v2.local.BEsKs5AolRYDb_O-bO-lwHWUextpShFSXlvv8MsrNZs3vTSnGQG4qRM9ezDl880jFwknSA6JARj2qKhDHnlSHx1GSCizfcF019U',
        'message': b'Love is stronger than hate or fear',
        'key': sym_key,
        'footer': b'',
        'nonce': nonce
    },
    {
        'raw': b'v2.local.FGVEQLywggpvH0AzKtLXz0QRmGYuC6yvbcqXgWxM3vJGrJ9kWqquP61Xl7bz4ZEqN5XwH7xyzV0QqPIo0k52q5sWxUQ4LMBFFso.Q3VvbiBBbHBpbnVz',
        'message': b'Love is stronger than hate or fear',
        'key': null_key,
        'footer': b'Cuon Alpinus',
        'nonce': nonce2
    },
    {
        'raw': b'v2.local.FGVEQLywggpvH0AzKtLXz0QRmGYuC6yvZMW3MgUMFplQXsxcNlg2RX8LzFxAqj4qa2FwgrUdH4vYAXtCFrlGiLnk-cHHOWSUSaw.Q3VvbiBBbHBpbnVz',
        'message': b'Love is stronger than hate or fear',
        'key': full_key,
        'footer': b'Cuon Alpinus',
        'nonce': nonce2
    },
    {
        'raw': b'v2.local.FGVEQLywggpvH0AzKtLXz0QRmGYuC6yvl05z9GIX0cnol6UK94cfV77AXnShlUcNgpDR12FrQiurS8jxBRmvoIKmeMWC5wY9Y6w.Q3VvbiBBbHBpbnVz',
        'message': b'Love is stronger than hate or fear',
        'key': sym_key,
        'footer': b'Cuon Alpinus',
        'nonce': nonce2
    }
])
def test_encrypt(token):
    _set_unit_test_only_nonce(token['nonce'])
    output_token = paseto.PasetoV2.encrypt(
        plaintext=token['message'],
        key=token['key'],
        footer=token['footer'],
    )
    assert output_token == token['raw']

    decrypted = paseto.PasetoV2.decrypt(
        token=token['raw'],
        key=token['key'],
    )
    assert decrypted['message'] == token['message']
    if decrypted['footer']:
        assert decrypted['footer']== token['footer']


def test_encrypt_with_footer_not_set():
    _set_unit_test_only_nonce(nonce)
    message = b'Love is stronger than hate or fear'
    raw_token = b'v2.local.BEsKs5AolRYDb_O-bO-lwHWUextpShFSXlvv8MsrNZs3vTSnGQG4qRM9ezDl880jFwknSA6JARj2qKhDHnlSHx1GSCizfcF019U'
    output_token = paseto.PasetoV2.encrypt(
        plaintext=message,
        key=sym_key,
    )
    assert output_token == raw_token

    decrypted = paseto.PasetoV2.decrypt(
        token=raw_token,
        key=sym_key,
    )
    assert decrypted['message'] == message


@pytest.mark.parametrize("token", [
    {
        'raw': b'v2.public.xnHHprS7sEyjP5vWpOvHjAP2f0HER7SWfPuehZ8QIctJRPTrlZLtRCk9_iNdugsrqJoGaO4k9cDBq3TOXu24AA',
        'message': b'',
        'key': private_key,
        'footer': b''
    },
    {
        'raw': b'v2.public.Qf-w0RdU2SDGW_awMwbfC0Alf_nd3ibUdY3HigzU7tn_4MPMYIKAJk_J_yKYltxrGlxEdrWIqyfjW81njtRyDw.Q3VvbiBBbHBpbnVz',
        'message': b'',
        'key': private_key,
        'footer': b'Cuon Alpinus'
    },
    {
        'raw': b'v2.public.RnJhbmsgRGVuaXMgcm9ja3NBeHgns4TLYAoyD1OPHww0qfxHdTdzkKcyaE4_fBF2WuY1JNRW_yI8qRhZmNTaO19zRhki6YWRaKKlCZNCNrQM',
        'message': b'Frank Denis rocks',
        'key': private_key,
        'footer': b''
    },
    {
        'raw': b'v2.public.RnJhbmsgRGVuaXMgcm9ja3qIOKf8zCok6-B5cmV3NmGJCD6y3J8fmbFY9KHau6-e9qUICrGlWX8zLo-EqzBFIT36WovQvbQZq4j6DcVfKCML',
        'message': b'Frank Denis rockz',
        'key': private_key,
        'footer': b''
    },
    {
        'raw': b'v2.public.RnJhbmsgRGVuaXMgcm9ja3O7MPuu90WKNyvBUUhAGFmi4PiPOr2bN2ytUSU-QWlj8eNefki2MubssfN1b8figynnY0WusRPwIQ-o0HSZOS0F.Q3VvbiBBbHBpbnVz',
        'message': b'Frank Denis rocks',
        'key': private_key,
        'footer': b'Cuon Alpinus'
    }
])
def test_sign(token):
    result = paseto.PasetoV2.sign(
        token['message'],
        token['key'],
        token['footer']
    )
    assert result == token['raw']
    verify = paseto.PasetoV2.verify(result, public_key)
    assert verify['message'] == token['message']
    assert verify['footer'] == token['footer']


@pytest.mark.parametrize("options", [
    {
        'claims': {
            'claim1': True,
            'claim2': 999,
            'claim3': {'nested': 'this is a string', 'array': [1, 2, 3]},
            'claim4': 'string2'
        },
        'footer': {
            'footer field': False
        },
        'key': sym_key,
        'purpose': 'local',
        'expected_header': 'v2.local',
    },
    {
        'claims': {
            'claim1': True,
            'claim2': 999,
            'claim3': {'nested': 'this is a string', 'array': [1, 2, 3]},
            'claim4': 'string2'
        },
        'footer': {
            'footer field': False
        },
        'key': private_key,
        'public_key': public_key,
        'purpose': 'public',
        'expected_header': 'v2.public',
    },
    {
        'claims': {
            'claim1': True,
            'claim2': 999,
            'claim3': {'nested': 'this is a string', 'array': [1, 2, 3]},
            'claim4': 'string2'
        },
        'footer': {
            'footer field': False
        },
        'key': sym_key,
        'purpose': 'local',
        'expected_header': 'v2.local'
    },
])
def test_create(options):
    create_params = {
        'key': options['key'],
        'purpose': options['purpose'],
        'claims': options['claims'],
        'footer': options['footer'],
    }

    token = paseto.create(**create_params)
    assert token.startswith(options['expected_header'].encode())
    parse_key = options.get('public_key', options['key'])
    parsed = paseto.parse(
        key=parse_key,
        purpose=options['purpose'],
        token=token,
    )
    assert parsed['message'] == options['claims']
    assert parsed['footer'] == options['footer']


def test_exp_claim():
    token = paseto.create(
        key=private_key,
        purpose='public',
        claims={'my claims': [1, 2, 3]},
        exp_seconds=300
    )
    parsed = paseto.parse(
        key=public_key,
        purpose='public',
        token=token,
    )
    assert parsed


def test_claim_is_expired():
    token = paseto.create(
        key=private_key,
        purpose='public',
        claims={'my claims': [1, 2, 3]},
        exp_seconds=-300
    )
    with pytest.raises(paseto.PasetoTokenExpired):
        paseto.parse(
            key=public_key,
            purpose='public',
            token=token,
        )


def test_skip_validation_on_expired():
    token = paseto.create(
        key=private_key,
        purpose='public',
        claims={'my claims': [1, 2, 3]},
        exp_seconds=-300
    )
    parsed = paseto.parse(
        key=public_key,
        purpose='public',
        token=token,
        validate=False
    )
    assert parsed


def test_required_claims():
    token = paseto.create(
        key=private_key,
        purpose='public',
        claims={'my claims': [1, 2, 3]},
        exp_seconds=-300
    )
    parsed = paseto.parse(
        key=public_key,
        purpose='public',
        token=token,
        validate=False,
        required_claims=['exp', 'my claims']
    )
    assert 'exp' in parsed['message']
    assert 'my claims' in parsed['message']

    with pytest.raises(paseto.PasetoValidationError):
        paseto.parse(
            key=public_key,
            purpose='public',
            token=token,
            validate=False,
            required_claims=['exp', 'missing']
        )
