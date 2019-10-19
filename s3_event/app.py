from chalice import Chalice

app = chalice.Chalice(app_name='s3eventdemo')
app.debug = True

@app.on_s3_event(bucket='badnera',
                 events=['s3:ObjectCreated:*'])
def handle_s3_event(event):
    app.log.debug("Received event for bucket: %s, key: %s",
                  event.bucket, event.key)
