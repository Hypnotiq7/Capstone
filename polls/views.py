from email.policy import HTTP
from re import template
from sys import last_traceback
from urllib import response
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader
from django.http import Http404
from django.views import generic
from django.utils import timezone

from .models import Choice, Question
