# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.interested_party import IPTerritoryOfControlRecord
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Writer Territory of Control (SWT) records grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

_data = _config.load_field_config('table')
_data.update(_config.load_field_config('common'))

_factory_field = DefaultFieldFactory(_data, CWRTables())

_prefixer = PrefixBuilder(_config.record_types())
_factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

"""
General fields.
"""

"""
Patterns.
"""

territory = _factory_record.get_transaction_record('writer_territory')

"""
Parsing actions for the patterns.
"""

territory.setParseAction(lambda p: _to_writerterritory(p))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_writerterritory(parsed):
    """
    Transforms the final parsing result into an IPTerritoryRecord instance.

    :param parsed: result of parsing the Territory record
    :return: an IPTerritoryRecord created from the parsed record
    """
    return IPTerritoryOfControlRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                      parsed.ip_n, parsed.inclusion_exclusion_indicator, parsed.tis_numeric_code,
                                      parsed.sequence_n,
                                      parsed.pr_share, parsed.mr_share, parsed.sr_share, parsed.shares_change)