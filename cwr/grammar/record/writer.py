# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.grammar.field import society as field_society
from cwr.grammar.field import writer as field_writer
from cwr.grammar.field import publisher as field_publisher
from cwr.interested_party import Writer, WriterRecord
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables


"""
CWR Writer records grammar.

This is for the following records:
- Writer Controlled By Submitter (SWR)
- Other Writer (OWR)
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()
_lookup_factory = DefaultFieldFactory(_config.load_field_config_table(), CWRTables())

"""
Patterns.
"""

writer = field_special.lineStart + field_record.record_prefix(
    _config.record_type('writer'),
    compulsory=True) + field_special.ip_n() + field_writer.writer_last_name + field_writer.writer_first_name + field_writer.unknown + \
         _lookup_factory.get_field(
             'writer_designation_code') + field_publisher.tax_id + field_special.ipi_name_number() + \
         _lookup_factory.get_field('pr_affiliation') + field_society.pr_share() + \
         _lookup_factory.get_field('mr_affiliation') + field_society.mr_share() + \
         _lookup_factory.get_field('sr_affiliation') + field_society.sr_share() + \
         field_writer.reversionary + field_writer.first_recording_refusal + field_writer.for_hire + field_special.blank(
    _config.field_size('writer', 'filler')) + \
         field_special.ipi_base_number() + field_writer.personal_number + _lookup_factory.get_field(
    'usa_license_indicator') + field_special.lineEnd

"""
Parsing actions for the patterns.
"""

writer.setParseAction(lambda p: _to_writerrecord(p))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_writer(parsed):
    """
    Transforms the final parsing result into an Writer instance.

    :param parsed: result of parsing the Writer info in a Writer record
    :return: a Writer created from the parsed record
    """
    return Writer(parsed.ip_n, parsed.personal_number, parsed.ipi_base_n, parsed.writer_first_name,
                  parsed.writer_last_name,
                  parsed.tax_id, parsed.ipi_name_n)


def _to_writerrecord(parsed):
    """
    Transforms the final parsing result into an WriterRecord instance.

    :param parsed: result of parsing a Writer record
    :return: an WriterRecord created from the parsed record
    """
    writer_data = _to_writer(parsed)

    return WriterRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n, writer_data,
                        parsed.writer_designation_code, parsed.work_for_hire, parsed.writer_unknown,
                        parsed.reversionary,
                        parsed.first_recording_refusal, parsed.usa_license_indicator, parsed.pr_affiliation,
                        parsed.pr_share, parsed.mr_affiliation, parsed.mr_share,
                        parsed.sr_affiliation, parsed.sr_share)