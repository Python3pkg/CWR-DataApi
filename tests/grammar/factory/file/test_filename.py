# -*- coding: utf-8 -*-

import unittest

from pyparsing import ParseException

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory

"""
CWR file name grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestFileNameValid(unittest.TestCase):
    """
    Tests that CWRFileNameDecoder decodes correctly formatted CWR file names (using the new format).
    """

    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))
        _data.update(_config.load_field_config('filename'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('filename'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('filename_new')

    def test_s2_r2(self):
        # Sender with 2 digits and receiver with 2 digits
        data = self.grammar.parseString('CW12012311_22.V21')[0]

        self.assertEqual(2012, data.year)
        self.assertEqual(123, data.sequence_n)
        self.assertEqual('11', data.sender)
        self.assertEqual('22', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s3_r2(self):
        # Sender with 3 digits and receiver with 2 digits
        data = self.grammar.parseString('CW130123ABC_23.V22')[0]

        self.assertEqual(2013, data.year)
        self.assertEqual(123, data.sequence_n)
        self.assertEqual('ABC', data.sender)
        self.assertEqual('23', data.receiver)
        self.assertEqual(2.2, data.version)

    def test_s2_r3(self):
        # Sender with 2 digits and receiver with 3 digits
        data = self.grammar.parseString('CW99000022_DEC.V00')[0]

        self.assertEqual(2099, data.year)
        self.assertEqual(0, data.sequence_n)
        self.assertEqual('22', data.sender)
        self.assertEqual('DEC', data.receiver)
        self.assertEqual(0, data.version)

    def test_s3_r3(self):
        # Sender with 3 digits and receiver with 3 digits
        data = self.grammar.parseString('CW000012AB2_234.V02')[0]

        self.assertEqual(2000, data.year)
        self.assertEqual(12, data.sequence_n)
        self.assertEqual('AB2', data.sender)
        self.assertEqual('234', data.receiver)
        self.assertEqual(0.2, data.version)


class TestFileNameValidOld(unittest.TestCase):
    """
    Tests that CWRFileNameDecoder decodes correctly formatted CWR file names (using the old format).
    """

    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))
        _data.update(_config.load_field_config('filename'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('filename'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('filename_old')

    def test_s2_r2(self):
        # Sender with 2 digits and receiver with 2 digits
        data = self.grammar.parseString('CW122311_22.V21')[0]

        self.assertEqual(2012, data.year)
        self.assertEqual(23, data.sequence_n)
        self.assertEqual('11', data.sender)
        self.assertEqual('22', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s3_r2(self):
        # Sender with 3 digits and receiver with 2 digits
        data = self.grammar.parseString('CW1301ABC_23.V22')[0]

        self.assertEqual(2013, data.year)
        self.assertEqual(1, data.sequence_n)
        self.assertEqual('ABC', data.sender)
        self.assertEqual('23', data.receiver)
        self.assertEqual(2.2, data.version)

    def test_s2_r3(self):
        # Sender with 2 digits and receiver with 3 digits
        data = self.grammar.parseString('CW990022_DEC.V00')[0]

        self.assertEqual(2099, data.year)
        self.assertEqual(0, data.sequence_n)
        self.assertEqual('22', data.sender)
        self.assertEqual('DEC', data.receiver)
        self.assertEqual(0, data.version)

    def test_s3_r3(self):
        # Sender with 3 digits and receiver with 3 digits
        data = self.grammar.parseString('CW0012AB2_234.V02')[0]

        self.assertEqual(2000, data.year)
        self.assertEqual(12, data.sequence_n)
        self.assertEqual('AB2', data.sender)
        self.assertEqual('234', data.receiver)
        self.assertEqual(0.2, data.version)


class TestFileNameZIPDecodeValid(unittest.TestCase):
    """
    Tests that CWRFileNameDecoder decodes correctly formatted zip file file names (using the new format).
    """

    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))
        _data.update(_config.load_field_config('filename'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('filename'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('filename_new')

    def test_s2_r2(self):
        # Sender with 2 digits and receiver with 2 digits
        data = self.grammar.parseString('CW12012311_22.zip')[0]

        self.assertEqual(2012, data.year)
        self.assertEqual(123, data.sequence_n)
        self.assertEqual('11', data.sender)
        self.assertEqual('22', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s3_r2(self):
        # Sender with 3 digits and receiver with 2 digits
        data = self.grammar.parseString('CW130123ABC_23.zip')[0]

        self.assertEqual(2013, data.year)
        self.assertEqual(123, data.sequence_n)
        self.assertEqual('ABC', data.sender)
        self.assertEqual('23', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s2_r3(self):
        # Sender with 2 digits and receiver with 3 digits
        data = self.grammar.parseString('CW99000022_DEC.zip')[0]

        self.assertEqual(2099, data.year)
        self.assertEqual(0, data.sequence_n)
        self.assertEqual('22', data.sender)
        self.assertEqual('DEC', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s3_r3(self):
        # Sender with 3 digits and receiver with 3 digits
        data = self.grammar.parseString('CW000012AB2_234.zip')[0]

        self.assertEqual(2000, data.year)
        self.assertEqual(12, data.sequence_n)
        self.assertEqual('AB2', data.sender)
        self.assertEqual('234', data.receiver)
        self.assertEqual(2.1, data.version)


class TestFileNameZIPDecodeValidOld(unittest.TestCase):
    """
    Tests that CWRFileNameDecoder decodes correctly formatted zip file names (using the old format).
    """

    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))
        _data.update(_config.load_field_config('filename'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('filename'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('filename_old')

    def test_s2_r2(self):
        # Sender with 2 digits and receiver with 2 digits
        data = self.grammar.parseString('CW122311_22.zip')[0]

        self.assertEqual(2012, data.year)
        self.assertEqual(23, data.sequence_n)
        self.assertEqual('11', data.sender)
        self.assertEqual('22', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s3_r2(self):
        # Sender with 3 digits and receiver with 2 digits
        data = self.grammar.parseString('CW1301ABC_23.zip')[0]

        self.assertEqual(2013, data.year)
        self.assertEqual(1, data.sequence_n)
        self.assertEqual('ABC', data.sender)
        self.assertEqual('23', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s2_r3(self):
        # Sender with 2 digits and receiver with 3 digits
        data = self.grammar.parseString('CW990022_DEC.zip')[0]

        self.assertEqual(2099, data.year)
        self.assertEqual(0, data.sequence_n)
        self.assertEqual('22', data.sender)
        self.assertEqual('DEC', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s3_r3(self):
        # Sender with 3 digits and receiver with 3 digits
        data = self.grammar.parseString('CW0012AB2_234.zip')[0]

        self.assertEqual(2000, data.year)
        self.assertEqual(12, data.sequence_n)
        self.assertEqual('AB2', data.sender)
        self.assertEqual('234', data.receiver)
        self.assertEqual(2.1, data.version)


class TestFileNameException(unittest.TestCase):
    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))
        _data.update(_config.load_field_config('filename'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('filename'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('filename_new')

    def test_empty(self):
        self.assertRaises(ParseException, self.grammar.parseString, '')

    def test_sequence_too_long(self):
        self.assertRaises(ParseException, self.grammar.parseString, 'CW0000012AB2_234.V21')

    def test_sequence_too_short(self):
        self.assertRaises(ParseException, self.grammar.parseString, 'CW00012AB2_234.V21')

    def test_sender_spaces(self):
        self.assertRaises(ParseException, self.grammar.parseString, 'CW000012A 2_234.V21')

    def test_receiver_spaces(self):
        self.assertRaises(ParseException, self.grammar.parseString, 'CW000012AB2_2 4.V21')


class TestFileNameOldException(unittest.TestCase):
    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))
        _data.update(_config.load_field_config('filename'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('filename'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('filename_old')

    def test_empty(self):
        self.assertRaises(ParseException, self.grammar.parseString, '')
