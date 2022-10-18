#!/usr/bin/env python
import pika, sys, os
import logging
import ssl
def main():
    logging.basicConfig(filename = 'logFile.log',
                        level = logging.INFO,
                        format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    logging.info('Start')                   
    user = 'guest'
    password = 'guest'    
    host = '8.tcp.ngrok.io'
    vHost = '/'
    userWB = ''
    passwordWB = ''
    queueWB = userWB+'-'+passwordWB
    port = 15532
    credentials = pika.PlainCredentials(user, password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host,
                                                                   port,
                                                                   vHost,
                                                                   credentials))
     
    channel = connection.channel()
    
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        logging.info(" [x] Received %r", body)

    # channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=False)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
