FROM python:3.10-alpine as builder

WORKDIR /app

COPY . .

RUN apk update && \
    apk add --no-cache build-base && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev && \
    poetry build && \
    cp -r dist outputs &&\
    cp install-package.py outputs/install-package.py

FROM python:3.10-alpine

ARG DOCKER_MAINTAINER="NAME FAMILY <EMAIL@EMAIL.com>"
LABEL maintainer="$DOCKER_MAINTAINER"
ENV DOCKER_MAINTAINER="$DOCKER_MAINTAINER"

ARG DOCKER_VERSION
LABEL org.label-schema.schema-version="$DOCKER_VERSION"
ENV DOCKER_VERSION="$DOCKER_VERSION"

ARG DOCKER_BUILD_DATE
LABEL org.label-schema.build-date="$DOCKER_BUILD_DATE"
ENV DOCKER_BUILD_DATE="$DOCKER_BUILD_DATE"

ARG VCS_URL="https://github.com/USERNAME/REPO"
LABEL org.label-schema.vcs-url="$VCS_URL"
ENV VCS_URL="$VCS_URL"

ARG BUG_REPORT="$VCS_URL/issues"
ENV BUG_REPORT="$BUG_REPORT"

ARG DOCKER_NAME="HUB_USERNAME/IMAGE_NAME"
LABEL org.label-schema.name="$DOCKER_NAME"
ENV DOCKER_NAME="$DOCKER_NAME"

LABEL org.label-schema.description="DESCRIPTION"

WORKDIR /tmp/app
COPY --from=builder /app/outputs .
RUN python install-package.py . \
    && cd / && rm -r /tmp/app

WORKDIR /app
CMD [ "my-script" ]