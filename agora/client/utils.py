import decimal

from kin_base import utils

_KIN_TO_QUARKS = decimal.Decimal(10 ** 5)
_PRECISION = decimal.Decimal('0.00001')


def kin_str_to_quarks(kin: str) -> int:
    """Converts a string kin amount to quarks. If the provided Kin amount contains more than 5 decimal places (i.e.
    it contains an inexact number of quarks), additional decimal places will be ignored.

    For example, passing in a value of "0.000009" will result in a value of 0 quarks being returned.

    :param kin: A string Kin amount.
    :return: An integer quark amount.
    """
    rounded = decimal.Decimal(kin).quantize(_PRECISION, decimal.ROUND_DOWN)
    return int((rounded * _KIN_TO_QUARKS).to_integral_value())


def quarks_to_kin_str(quarks: int) -> str:
    """Converts an integer quark amount into a string Kin amount.

    :param quarks: An amount, in quarks.
    :return: A string Kin amount.
    """
    kin = (decimal.Decimal(quarks) / _KIN_TO_QUARKS)
    return str(kin.normalize())


def public_key_to_address(public_key: bytes) -> str:
    """Returns a raw ed25519 public key encoded as a strkey.

    :param public_key: The public key, in raw bytes, of an account.
    :return: The public key encoded as a strkey.
    """
    return utils.encode_check('account', public_key).decode()
