LOGGING_CONFIG = {
  'version': 1,
  'disable_existing_loggers': True,
  'formatters': {
    'standard': {
      'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
      'datefmt': '%Y-%m-%d %H:%M:%S%z'
    },
  },
  'handlers': {
    'default': {
      'level': 'INFO',
      'formatter': 'standard',
      'class': 'logging.StreamHandler',
      'stream': 'ext://sys.stdout',  # Default is stderr
    },
  },
  'loggers': {
    '': {  # root logger
      'handlers': ['default'],
      'level': 'WARNING',
      'propagate': False
    },
    'botocore': {
      'handlers': ['default'],
      'level': 'INFO',
      'propagate': False
    },
    'src': {
      'handlers': ['default'],
      'level': 'DEBUG',
      'propagate': False
    },
    'tests': {
      'handlers': ['default'],
      'level': 'DEBUG',
      'propagate': False
    },
    '__main__': {
      'handlers': ['default'],
      'level': 'INFO',
      'propagate': False
    },
  }
}
