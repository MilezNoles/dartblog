import os
import sys
import zipfile
import django
import time

import xml.etree.ElementTree as ET

proj = os.path.dirname(os.path.abspath("manage.py"))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "siteblog.settings"

django.setup()

from blog.models import *


def testtest():
    start = time.time()
    Catalog.objects.all().delete()
    Brand.objects.all().delete()
    People.objects.all().delete()
    Group.objects.all().delete()
    Shops.objects.all().delete()
    Shcode.objects.all().delete()

    catalog = []
    with zipfile.ZipFile('../dataxml/catalog.zip', 'r') as zip:
        zip.printdir()
        zip.extractall(path='../dataxml/catalog/')

    brands = []
    with zipfile.ZipFile('../dataxml/brands.zip', 'r') as zip:
        zip.printdir()
        zip.extractall(path='../dataxml/brands/')

    cards = []
    with zipfile.ZipFile('../dataxml/cards.zip', 'r') as zip:
        zip.printdir()
        zip.extractall(path='../dataxml/cards/')

    groups = []
    with zipfile.ZipFile('../dataxml/catalog_groups.zip', 'r') as zip:
        zip.printdir()
        zip.extractall(path='../dataxml/catalog_groups/')

    objects = []
    with zipfile.ZipFile('../dataxml/objects.zip', 'r') as zip:
        zip.printdir()
        zip.extractall(path='../dataxml/objects/')

    shcodes = []
    with zipfile.ZipFile('../dataxml/shcodes.zip', 'r') as zip:
        zip.printdir()
        zip.extractall(path='../dataxml/shcodes/')

    tree = ET.parse('../dataxml/brands/brands.xml')
    root = tree.getroot()
    for child in root:
        b = {}
        for el in child:
            b[el.tag] = el.text
        if b.get("parent_id"):
            pass
        else:
            b["parent_id"] = None
        brands.append(Brand(id=b["id"], name=b["name"], child_id=b["parent_id"]))

    Brand.objects.bulk_create(brands)

    tree = ET.parse('../dataxml/catalog_groups/catalog_groups.xml')
    root = tree.getroot()
    for child in root:
        b = {}
        for el in child:
            b[el.tag] = el.text
        if b.get("parent_id"):
            pass
        else:
            b["parent_id"] = None
        groups.append(
            Group(id=b["id"], name=b["name"], level=b["level"], child_id=b["parent_id"], ))
    Group.objects.bulk_create(groups)

    tree = ET.parse('../dataxml/catalog/catalog.xml')
    root = tree.getroot()
    for child in root:
        b = {}
        for el in child:
            b[el.tag] = el.text
        if b.get("group_id"):
            pass
        else:
            b["group_id"] = None
        if b.get("brand_id"):
            pass
        else:
            b["brand_id"] = None

        catalog.append(
            Catalog(id=b["id"], name=b["name"], group_id_id=b["group_id"], brand_id_id=b["brand_id"], ei=b["ei"],
                    price=b["price"], price_old=b["price_old"], ksales=b["ksales"],
                    pVAT=b["pVAT"]))
    Catalog.objects.bulk_create(catalog)

    tree = ET.parse('../dataxml/shcodes/shcodes.xml')
    root = tree.getroot()
    for child in root:
        b = {}
        for el in child:
            b[el.tag] = el.text
        shcodes.append(
            Shcode(catalog_id=b["id"], shcode=b["shk"], ))
    Shcode.objects.bulk_create(shcodes)

    tree = ET.parse('../dataxml/cards/cards.xml')
    root = tree.getroot()
    for child in root:
        b = {}
        for el in child:
            b[el.tag] = el.text
        if b.get("telephone"):
            pass
        else:
            b["telephone"] = None
        cards.append(
            People(id=b["ID"], name=b["name"], surname=b["surname"], fname=b["fname"], type=b["type"],
                   birthday=b["birthday"],
                   discont=b["Discont"], telephone=b["telephone"], ))
    People.objects.bulk_create(cards)

    tree = ET.parse('../dataxml/objects/objects.xml')
    root = tree.getroot()
    for child in root:
        b = {}
        for el in child:
            b[el.tag] = el.text
        objects.append(
            Shops(id=b["id"], name=b["name"], address=b["address"], city=b["city"], timestart=b["timestart"],
                  timefinish=b["timefinish"], activefororder=b["activefororder"]))
    Shops.objects.bulk_create(objects)

    # checking whether file exists or not
    if os.path.exists('../dataxml/brands/brands.xml'):
        # removing the file using the os.remove() method
        os.remove('../dataxml/brands/brands.xml')
    else:
        # file not found message
        print("File not found in the directory")
    if os.path.exists('../dataxml/catalog_groups/catalog_groups.xml'):
        # removing the file using the os.remove() method
        os.remove('../dataxml/catalog_groups/catalog_groups.xml')
    else:
        # file not found message
        print("File not found in the directory")
    if os.path.exists('../dataxml/catalog/catalog.xml'):
        # removing the file using the os.remove() method
        os.remove('../dataxml/catalog/catalog.xml')
    else:
        # file not found message
        print("File not found in the directory")
    if os.path.exists('../dataxml/shcodes/shcodes.xml'):
        # removing the file using the os.remove() method
        os.remove('../dataxml/shcodes/shcodes.xml')
    else:
        # file not found message
        print("File not found in the directory")
    if os.path.exists('../dataxml/cards/cards.xml'):
        # removing the file using the os.remove() method
        os.remove('../dataxml/cards/cards.xml')
    else:
        # file not found message
        print("File not found in the directory")
    if os.path.exists('../dataxml/objects/objects.xml'):
        # removing the file using the os.remove() method
        os.remove('../dataxml/objects/objects.xml')
    else:
        # file not found message
        print("File not found in the directory")

    end = time.time()
    print('[*] Время выполнения: {} секунд.'.format(end - start))


testtest()
