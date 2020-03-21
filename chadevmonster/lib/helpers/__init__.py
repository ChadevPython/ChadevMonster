# # -*- coding: utf-8 -*-
#
# from threading import Thread
# from flask_mail import Message
# from flask import render_template
# from chadevmonster import mail
# from config import config
# from chadevmonster import app
#
# logging_on = config.LOGGING_ON
# print_log = config.PRINTLOG
#
#
# def send_async_email(app, msg):
#     with app.app_context():
#         mail.send(msg)
#
#
# def send_email(to, subject, template, **kwargs):
#     if not config.NOTIFICATIONS_ON:
#         return
#     #    if kwargs.get('sender'):
#     #        sender = kwargs.get('sender')
#     #    else:
#     sender = config.MAIL_SENDER
#
#     try:
#         msg = Message(
#             config.MAIL_SUBJECT_PREFIX + " " + subject,
#             sender=sender,
#             recipients=to,
#             bcc=[config.CATCH_ALL_EMAIL_ADDRESS],
#         )
#         #        if kwargs.get('reply_to'):
#         #            msg.reply_to = kwargs.get('reply_to')
#         msg.reply_to = config.MAIL_SENDER
#         msg.to = to
#         msg.body = render_template(template + ".txt", **kwargs)
#         msg.html = render_template(template + ".html", **kwargs)
#         thr = Thread(target=send_async_email, args=[app, msg])
#         thr.start()
#         # mail.send(msg)
#     except Exception as e:
#         logit(e)
#         logit("Email Error")
#
#
# def logit(data):
#     """Writes data to a text file for logging purposes."""
#     if logging_on:
#         try:
#             with open("log.txt", "a") as f:
#                 f.write(data)
#                 f.write("\n")
#         except Exception:
#             pass
#         if print_log:
#             print(data)
#     else:
#         print(data)
