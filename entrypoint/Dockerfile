FROM nginx:1.13.8

ENV NGINX_PORT 80

COPY proxy.conf /etc/nginx/conf.d/default.conf 
COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]