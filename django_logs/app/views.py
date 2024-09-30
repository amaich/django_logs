from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def main(request):
    logger.info('logged')
    return HttpResponse('<h1>LOGGED</h1>')