#! /bin/env python3

# adds and/or replaces meta tags in html file

import sys
from os import path
from struct import unpack
from urllib.parse import urlparse
import json
import re


# all filesys paths relative to this file's location
INDEX_FILE_PATH = sys.path[0] + "/../../index.html"
SCREENSHOT_FILE_PATH = sys.path[0] + "/../../img/screenshot.png"
TRANSLATION_FILE_PATH = sys.path[0] + "/../../translations/en.json"
SCREENSHOT_URL_PART = "img/screenshot.png"





def __main__():

    if(len(sys.argv)<2):
        print("Please give me a URL. Like for example: https://ec.europa.eu/eurostat/cache/digpub/european_economy/vis/01_01_01/index.html")
        exit()

    url = sys.argv[1]

    with open(INDEX_FILE_PATH, 'r+') as f:
        data=f.read()

        for k,v in getMetaTagContent(
                title = getTextFromTranslations("title.main"),
                description = getTextFromTranslations("title.sub"),
                previewImageUrl = getScreenshotUrl(url),
                imageDimsTuple = getImageDims(SCREENSHOT_FILE_PATH),
                url=url,
                domain=getDomain(url)
            ).items():

                replaceWith = f"""<meta {k[0]}="{k[1]}" content="{v}" />\n"""

                n = re.search(f"<meta\s*{k[0]}\s*=\s*\"{k[1]}\".*>", data)
                if(n):
                    print(f"replacing {k[1]} '{v}'")
                    data = data[:n.start()] + replaceWith + data[n.end():]
                else:
                    print(f"inserting {k[1]} '{v}'")
                    o = data.find("</head>")
                    data = data[:o] + replaceWith + data[o:]

        f.seek(0)
        f.write(data)

    print("ok, done.")


def getTextFromTranslations(id):
    with open(TRANSLATION_FILE_PATH, 'r') as f:
        data=f.read()
        obj = json.loads(data)
        return obj[id]


def getScreenshotUrl(url):
    parsedUri = urlparse(url)
    return parsedUri.scheme + "//" + parsedUri.netloc + path.dirname(parsedUri.path) + "/" + SCREENSHOT_URL_PART


# window.location.host = netloc = domain
def getDomain(url):
    parsedUri = urlparse(url)
    return parsedUri.netloc


def getImageDims(path):
    with open(path, "rb") as f:
        f.seek(8+4+4)
        data = f.read(4)
        width = unpack('!I', data)[0]
        data = f.read(4)
        height = unpack('!I', data)[0]
        return (width,height)


def getMetaTagContent(title, description, previewImageUrl, imageDimsTuple, url, domain):
    b = {}
    b[ ("property","og:type") ] = "website"
    b[ ("property","og:title") ] = title
    b[ ("property","og:locale") ] = "en_GB"
    b[ ("property","og:description") ] = description
    b[ ("property","og:image:alt") ] = description
    b[ ("property","og:image") ] = previewImageUrl
    b[ ("property","og:image:width") ] = imageDimsTuple[0]
    b[ ("property","og:image:height") ] = imageDimsTuple[1]
    b[ ("property","og:url") ] = url
    b[ ("name","twitter:card") ] = previewImageUrl
    b[ ("property","twitter:domain") ] = domain
    b[ ("property","twitter:url") ] = url
    b[ ("name","twitter:title") ] = title
    b[ ("name","twitter:description") ] = description
    b[ ("name","twitter:image") ] = previewImageUrl
    return b

__main__()
