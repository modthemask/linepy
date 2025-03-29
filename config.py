# -*- coding: utf-8 -*-
from akad.ttypes import ApplicationType
from random import randint
import random
import re, codecs, json

class Config(object):
    LINE_HOST_DOMAIN            = 'https://legy-jp-addr-long.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com'
    LINE_TIMELINE_API           = 'https://gd2.line.naver.jp/mh/api'
    LINE_TIMELINE_MH            = 'https://gd2.line.naver.jp/mh'
    LINE_TIMELINE_HM            = 'https://legy-jp-addr.line.naver.jp/hm'
    LINE_LIFF_SEND              = 'https://api.line.me/message/v3/share'
    LINE_PERMISSION_API         = 'https://access.line.me/dialog/api/permissions'

    LINE_LOGIN_QUERY_PATH       = '/api/v4p/rs'
    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'

    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_LIFF_QUERY_PATH        = '/LIFF1'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'
    LINE_SHOP_QUERY_PATH        = '/SHOP4'

    CHANNEL_ID = {
        'HELLO_WORLD': '1602289196',
        'LINE_TIMELINE': '1341209850',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440',
        'LINE_MUSIC': '1381425814',
        'LINE_SERVICES': '1459630796'
    }

    APP_VERSION = {
        'IOS': '10.21.5',
        'IOSIPAD': '10.21.5',
        'ANDROID': '10.21.5',
        'ANDROIDLITE': '2.16.0',
        'DESKTOPWIN': random.choice(["9.2.0","9.1.2"]),
        'DESKTOPMAC': '7.5.0',
        'CHROMEOS': '2.4.1',
        'DEFAULT': '10.16.4'
    }

    SYSTEM_VERSION = {
        'IOS': '14.0.1',
        'IOSIPAD': '14.0.1',
        'ANDROID': '10',
        'ANDROIDLITE': '10',
        'DESKTOPWIN': '10.0',
        'DESKTOPMAC': '12.7.2',
        'CHROMEOS': '88',
        'DEFAULT': '10.0'
    }

    APP_TYPE    = 'DESKTOPWIN'
    APP_VER     = '9.1.2'
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = 'WINDOWS'
    SYSTEM_VER  = '10.0'
    IP_ADDR     = '8.8.8.8'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    URL_REGEX   = re.compile(r'^(?:http|ftp)s?://' r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' r'localhost|' r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' r'(?::\d+)?' r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    MID_REGEX   = re.compile(r'u[a-f0-9]{32}')
    GID_REGEX   = re.compile(r'c[a-f0-9]{32}')
    RID_REGEX   = re.compile(r'r[a-f0-9]{32}')
    ALLIDS_REGEX= re.compile(r'[ucr][a-f0-9]{32}')

    def __init__(self, appType=None):
        if appType == "DESKTOPWIN":
            self.APP_NAME = 'DESKTOPWIN\t9.1.2\tWINDOWS\t10.0'
        else:
            self.APP_NAME = '%s\t%s\t%s\t%s' % (self.APP_TYPE, self.APP_VER, self.SYSTEM_NAME, self.SYSTEM_VER)
        self.USER_AGENT = 'Line/%s' % self.APP_VER