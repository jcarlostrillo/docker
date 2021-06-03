# Docker

This repo contain several proyects and test with Docker.

## docker-compose-webapp-full

This folder contains a docker-compose file with several services:

+ pg: postgres database
+ webapp: basic webapp that list all the IP that accesed to the application. It runs in the port 9292
+ lb: reverse proxy for the webapp


## docker-nginx-read-only

A basic configuration and information about the usar of the flags --read-only and tmpfs.

## entrypoint

An example of the usage of the ENTRYPOINT plus the CMD commands in the Dockerfile.