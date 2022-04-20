FROM jupyter/scipy-notebook:latest

USER root
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
&& apt-get -y install --no-install-recommends git-core wget curl
USER jovyan
RUN pip3 install -U flask sh httpie typer
