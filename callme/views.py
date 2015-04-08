from django.http import HttpResponse
from django_twilio.decorators import twilio_view
from twilio import twiml
from twilio.rest import TwilioRestClient
from django.conf import settings
import tweepy

@twilio_view
def transcribe_incoming(request):

	r = twiml.Response()
	r.say("What is your tweet, Linda?")
	r.record(maxLength=30, transcribeCallback="/playback/")

	return r

@twilio_view
def playback(request):

	transcribed = request.POST['TranscriptionText']
	sent_from = request.POST['From']
	body = "Tweet Sent: " + transcribed

	auth = tweepy.OAuthHandler(settings.TWITTER_CONS_KEY, settings.TWITTER_CONS_SECRET)
	auth.set_access_token(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET)

	api = tweepy.API(auth)
	api.update_status(status=transcribed)

	client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

	msg = client.messages.create(to=sent_from, from_=settings.TWILIO_PHONE_NUM, body=body)

	return HttpResponse("A-OK", status=200)