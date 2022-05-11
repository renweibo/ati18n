FROM jupyter/scipy-notebook:latest
ENV TZ=Asia/Shanghai 
USER root
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends tzdata git-core wget curl \
    && ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/*
USER jovyan
RUN pip3 install -U flask sh httpie openpyxl typer
RUN pip3 install -U -r requirements_dev.txt