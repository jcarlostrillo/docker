# Base image (FROM)
FROM debian:buster-slim

# Execute the following commands (RUN)
RUN apt-get update
RUN apt-get install -y nginx

# Redirect the logs
RUN rm /var/log/nginx/access.log && ln -s /dev/stdout /var/log/nginx/access.log
RUN rm /var/log/nginx/error.log && ln -s /dev/stderr /var/log/nginx/error.log

# Copy some files
COPY ./html/*.html /var/www/html/

# Startup command (CM)
CMD nginx -g 'daemon off;'
