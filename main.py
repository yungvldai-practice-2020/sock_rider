import eventlet
import socketio
import mech

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

mech.init()


@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


@sio.on('go')
def go(sid, data):
    mech.go(data)


@sio.on('turn')
def turn(sid, data):
    mech.turn(data)


@sio.on('stop')
def stop(sid, data):
    mech.stop()


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8765)), app)
