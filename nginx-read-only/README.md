# README

To execute the image with the _--read-only__ flag, we need to providy the __--tmpfs__ flag as well with the right directory.

```sh
docker container run --tmpfs /var/www/html/ --name read-only-nginx -p 80:80 ctrillo/nginx:latest
```