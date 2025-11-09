FROM ubuntu:latest
LABEL authors="jorda"

ENTRYPOINT ["top", "-b"]