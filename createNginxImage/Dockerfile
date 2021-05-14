# Base image (FROM)
FROM debian:buster-slim

# Execute the following commands (RUN)
RUN apt-get update
RUN apt-get install -y nginx

# Startup command (CM)
CMD nginx -g 'daemon off;'
