# -*- encoding: utf-8 -*-

import pyparsing as pp

from data.accessor import CWRConfiguration, CWRTables
from cwr.grammar import field_special, record
from cwr.agreement import AgreementTerritoryRecord


"""
CWR Territory in Agreement grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_tables = CWRTables()
_config = CWRConfiguration()

"""
Territory in Agreement fields.
"""

# Record Type for the territory in agreement
record_prefix_tir = record.record_prefix(_config.record_type('agreement_territory'))

# Inclusion/Exclusion Indicator
ie_indicator = pp.oneOf(_config.field_value('agreement_territory', 'ie_indicator'))
ie_indicator = ie_indicator.setName('Inclusion/Exclusion Indicator').setResultsName('ie_indicator')

# TIS Numeric Code
tis_code = pp.oneOf(_tables.tis_codes())
tis_code = tis_code.setName('TIS Numeric Code').setResultsName('tis_code')
tis_code.setParseAction(lambda c: int(c[0]))

"""
Territory in Agreement patterns.
"""

territory_in_agreement = field_special.lineStart + record_prefix_tir + ie_indicator + tis_code + field_special.lineEnd

"""
Parsing actions for the patterns.
"""

territory_in_agreement.setParseAction(lambda p: _to_agreementterritory(p))

"""
Parsing actions for the patterns.
"""


def _to_agreementterritory(parsed):
    """
    Transforms the final parsing result into a AgreementTerritoryRecord instance.

    :param parsed: result of parsing a Territory in Agreement transaction header
    :return: a AgreementTerritoryRecord created from the parsed record
    """
    return AgreementTerritoryRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                    parsed.tis_code, parsed.ie_indicator)