
DATA_VALUE = 0
DATA_RESOURCE = 1

DATA_COLUMNS = [
    {
        'name': 'time',
        'type': DATA_VALUE,
        'predicate': {
            'prefix': 'te',
            'value': 'begins'
        }
    },
    {
        'name': 'latitude',
        'type': DATA_VALUE,
        'predicate': {
            'prefix': 'geo',
            'value': 'lat'
        }
    },
    {
        'name': 'longitude',
        'type': DATA_VALUE,
        'predicate': {
            'prefix': 'geo',
            'value': 'long'
        }
    },
    {
        'name': 'depth',
        'type': DATA_VALUE,
        'predicate': {
            'prefix': 'dbpedia-owl',
            'value': 'depth'
        }
    },
    {
        'name': 'magnitude',
        'type': DATA_RESOURCE,
        'predicate': {
            'prefix': 'utpl_geo',
            'value': 'magnitude'
        },
        'value': {
            'prefix': 'utpl_geo',
            'value_prefix': 'Mag'
        }
    },
    {
        'name': 'magnitudeType',
        'type': DATA_RESOURCE,
        'predicate': {
            'prefix': 'utpl_geo',
            'value': 'magnitudeType'
        },
        'value': {
            'prefix': 'utpl_geo',
            'value_prefix': 'MagType'
        }
    },
    {
        'name': 'number of seismic stations',
        'type': DATA_VALUE,
        'predicate': {
            'prefix': 'utpl_geo',
            'value': 'nst'
        }
    },
    {
        'name': 'gap',
        'type': DATA_VALUE,
        'predicate': {
            'prefix': 'utpl_geo',
            'value': 'gap'
        }
    },
    {
        'name': 'dmin',
        'type': DATA_VALUE,
        'predicate': {
            'prefix': 'utpl_geo',
            'value': 'dmin'
        }
    },
    {
        'name': 'rms',
        'type': DATA_VALUE,
        'predicate': {
            'prefix': 'utpl_geo',
            'value': 'rms'
        }
    },
    {
        'name': 'prefered source network',
        'type': DATA_RESOURCE,
        'predicate': {
            'prefix': 'utpl_geo',
            'value': 'net'
        },
        'value': {
            'prefix': 'utpl_geo',
            'value_prefix': 'Net'
        }
    },
    {
        'name': 'id',
        'type': DATA_VALUE,
        'predicate': {
            'prefix': 'dce',
            'value': 'identifier'
        }
    },
    {
        'name': 'updated',
        'type': DATA_VALUE,
        'predicate': {
            'prefix': 'dbpedia-owl',
            'value': 'updated'
        }
    },
    {
        'name': 'place',
        'type': DATA_VALUE,
        'predicate': {
            'prefix': 'place',
            'value': 'in'
        }
    },
    {
        'name': 'type',
        'type': DATA_RESOURCE,
        'predicate': {
            'prefix': 'foaf',
            'value': 'type'
        },
        'value': {
            'prefix': 'dbpedia',
            'value_prefix': 'Earthquake'
        }
    },
    {
        'name': 'horizontalError',
        'type': DATA_VALUE,
        'predicate': {
            'prefix': 'utpl_geo',
            'value': 'horErr'
        }
    },
    {
        'name': 'depthError',
        'type': DATA_VALUE,
        'predicate': {
            'prefix': 'utpl_geo',
            'value': 'depErr'
        }
    },
    {
        'name': 'magnitudError',
        'type': DATA_VALUE,
        'predicate': {
            'prefix': 'utpl_geo',
            'value': 'magErr'
        }
    },
    {
        'name': 'magnitudNst',
        'type': DATA_VALUE,
        'predicate': {
            'prefix': 'utpl_geo',
            'value': 'magNst'
        }
    },
    {
        'name': 'status',
        'type': DATA_RESOURCE,
        'predicate': {
            'prefix': 'utpl_geo',
            'value': 'dataStatus'
        },
        'value': {
            'prefix': 'utpl_geo',
            'value_prefix': 'Status'
        }
    },
    {
        'name': 'locationSource',
        'type': DATA_RESOURCE,
        'predicate': {
            'prefix': 'utpl_geo',
            'value': 'locationSource'
        },
        'value': {
            'prefix': 'utpl_geo',
            'value_prefix': 'Source'
        }
    },
    {
        'name': 'magnitudSource',
        'type': DATA_RESOURCE,
        'predicate': {
            'prefix': 'utpl_geo',
            'value': 'magnitudSource'
        },
        'value': {
            'prefix': 'utpl_geo',
            'value_prefix': 'Source'
        }
    },
]

DATA_ID = 0
DATA_RESOURCE_MAP = {
    'col': {
        'pos': DATA_ID,
        'name': DATA_COLUMNS[DATA_ID]['name']
    },
    'value': {
        'prefix': 'utpl_geo',
        'value_prefix': 'EQ',
        'value_proc': {
            'rm': ['-', ':']
        }
    }
}
