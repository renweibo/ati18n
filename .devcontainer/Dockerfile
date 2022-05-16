FROM jupyter/scipy-notebook:latest
ENV TZ=Asia/Shanghai 
USER root

RUN apt-get update && apt-get -y install --no-install-recommends curl && curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt install gh \
    && apt-get -y install --no-install-recommends tzdata git-core wget curl \
    && ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/*
USER jovyan
RUN pip3 install -U pip build flask sh httpie openpyxl typer
# RUN pip3 install -U -r requirements_dev.txt
