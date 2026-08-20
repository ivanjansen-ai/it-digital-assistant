import os
from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN")


@app.route("/", methods=["GET"])
def home():
    return "I&T Digital Assistant is running", 200


@app.route("/privacy", methods=["GET"])
def privacy():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Privacy Policy - I&T Digital Assistant</title>
        <meta charset="UTF-8">
    </head>
    <body style="font-family:Arial;max-width:850px;margin:40px auto;line-height:1.6;padding:20px;">
        <h1>Privacy Policy</h1>

        <p><strong>I&T Real Estate and More</strong> respects the privacy of its
        customers and users of the I&T Digital Assistant.</p>

        <h2>Information We Collect</h2>
        <p>When you communicate with us through WhatsApp, we may receive your
        phone number, name, message content, and information you voluntarily
        provide for customer service or appointment scheduling.</p>

        <h2>How We Use Information</h2>
        <p>Your information may be used to answer inquiries, provide customer
        service, schedule appointments, and communicate regarding services
        requested from I&T Real Estate and More.</p>

        <h2>Sharing of Information</h2>
        <p>We do not sell personal information. Information may only be shared
        with service providers when necessary to operate our communication
        and appointment systems or when required by law.</p>

        <h2>Data Security</h2>
        <p>Reasonable measures are used to protect information processed
        through our systems.</p>

        <h2>Data Deletion</h2>
        <p>You may request deletion of your information by contacting
        I&T Real Estate and More or by following our data deletion instructions.</p>

        <h2>Contact</h2>
        <p>Email: iandtrealestatedev@gmail.com</p>

        <p>Last updated: August 2026</p>
    </body>
    </html>
    """, 200


@app.route("/terms", methods=["GET"])
def terms():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Terms of Service - I&T Digital Assistant</title>
        <meta charset="UTF-8">
    </head>
    <body style="font-family:Arial;max-width:850px;margin:40px auto;line-height:1.6;padding:20px;">
        <h1>Terms of Service</h1>

        <p>The I&T Digital Assistant is provided by
        <strong>I&T Real Estate and More</strong> to assist customers with
        inquiries, customer service and appointment scheduling.</p>

        <p>Information provided through the assistant is intended for general
        business communication and does not constitute a binding agreement
        unless separately confirmed by I&T Real Estate and More.</p>

        <p>Users agree not to misuse the service or submit unlawful,
        fraudulent or abusive content.</p>

        <p>I&T Real Estate and More may modify or discontinue the service when
        necessary.</p>

        <h2>Contact</h2>
        <p>Email: iandtrealestatedev@gmail.com</p>

        <p>Last updated: August 2026</p>
    </body>
    </html>
    """, 200


@app.route("/data-deletion", methods=["GET"])
def data_deletion():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Data Deletion Instructions - I&T Digital Assistant</title>
        <meta charset="UTF-8">
    </head>
    <body style="font-family:Arial;max-width:850px;margin:40px auto;line-height:1.6;padding:20px;">
        <h1>Data Deletion Instructions</h1>

        <p>If you would like information associated with your interaction with
        the I&T Digital Assistant to be deleted, please send a request to:</p>

        <p><strong>iandtrealestatedev@gmail.com</strong></p>

        <p>Please include the phone number used to communicate with our
        WhatsApp account so that we can identify the relevant information.</p>

        <p>After verification of the request, applicable personal information
        will be deleted unless retention is required by law or for legitimate
        business recordkeeping obligations.</p>

        <p>Last updated: August 2026</p>
    </body>
    </html>
    """, 200


@app.route("/webhook", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200

    return "Verification failed", 403


@app.route("/webhook", methods=["POST"])
def receive_webhook():
    data = request.get_json(silent=True)

    print("WhatsApp webhook received:")
    print(data)

    return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
