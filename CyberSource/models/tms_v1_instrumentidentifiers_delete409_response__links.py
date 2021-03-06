# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TmsV1InstrumentidentifiersDelete409ResponseLinks(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'payment_instruments': 'TmsV1InstrumentidentifiersDelete409ResponseLinksPaymentInstruments'
    }

    attribute_map = {
        'payment_instruments': 'paymentInstruments'
    }

    def __init__(self, payment_instruments=None):
        """
        TmsV1InstrumentidentifiersDelete409ResponseLinks - a model defined in Swagger
        """

        self._payment_instruments = None

        if payment_instruments is not None:
          self.payment_instruments = payment_instruments

    @property
    def payment_instruments(self):
        """
        Gets the payment_instruments of this TmsV1InstrumentidentifiersDelete409ResponseLinks.

        :return: The payment_instruments of this TmsV1InstrumentidentifiersDelete409ResponseLinks.
        :rtype: TmsV1InstrumentidentifiersDelete409ResponseLinksPaymentInstruments
        """
        return self._payment_instruments

    @payment_instruments.setter
    def payment_instruments(self, payment_instruments):
        """
        Sets the payment_instruments of this TmsV1InstrumentidentifiersDelete409ResponseLinks.

        :param payment_instruments: The payment_instruments of this TmsV1InstrumentidentifiersDelete409ResponseLinks.
        :type: TmsV1InstrumentidentifiersDelete409ResponseLinksPaymentInstruments
        """

        self._payment_instruments = payment_instruments

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TmsV1InstrumentidentifiersDelete409ResponseLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
