#!/bin/sh

PYTHONPATH={{ PROJECT_DIR }}
MODULE="django.core.handlers.wsgi:WSGIHandler()"

### BEGIN INIT INFO
# Provides:          uwsgi-{{ INSTANCE_NAME }}
# Required-Start:    $all
# Required-Stop:     $all
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: starts the uwsgi app server
# Description:       starts uwsgi app server using start-stop-daemon
### END INIT INFO

PATH=/opt/uwsgi:/sbin:/bin:/usr/sbin:/usr/bin
DAEMON={{ ENV_DIR }}/bin/uwsgi

OWNER=uwsgi

NAME=uwsgi-{{ INSTANCE_NAME }}
DESC=uwsgi-{{ INSTANCE_NAME }}

test -x $DAEMON || exit 0

set -e

DAEMON_OPTS="-s 127.0.0.1:{{ UWSGI_PORT }} \
--master \
--harakiri 30 \
--sharedarea 4  \
--processes 4  \
--daemonize /var/log/uwsgi/{{ SERVER_NAME }}.log \
--pythonpath $PYTHONPATH --module $MODULE \
--env DJANGO_SETTINGS_ENVIRONMENT={{ NAME }} --env DJANGO_SETTINGS_MODULE=settings --home {{ ENV_DIR }}/"

case "$1" in
  start)
        echo -n "Starting $DESC: "
        start-stop-daemon --start --chuid $OWNER:$OWNER --user $OWNER \
                --exec $DAEMON -- $DAEMON_OPTS || true
        echo "$NAME."
        ;;
  stop)
        echo -n "Stopping $DESC: "
        start-stop-daemon --signal 3 --user $OWNER --quiet --retry 2 --stop \
                --exec $DAEMON || true
        echo "$NAME."
        ;;
  reload)
        killall -1 $DAEMON
        ;;
  force-reload)
        killall -15 $DAEMON
       ;;
  restart)
        echo -n "Restarting $DESC: "
        start-stop-daemon --signal 3 --user $OWNER --quiet --retry 2 --stop \
                --exec $DAEMON  || true
        sleep 1
        start-stop-daemon --user $OWNER --start --quiet --chuid $OWNER:$OWNER \
               --exec $DAEMON -- $DAEMON_OPTS || true
        echo "$NAME."
        ;;
  status)
        killall -10 $DAEMON
        ;;
      *)
            N=/etc/init.d/$NAME
            echo "Usage: $N {start|stop|restart|reload|force-reload|status}" >&2
            exit 1
            ;;
    esac
    exit 0