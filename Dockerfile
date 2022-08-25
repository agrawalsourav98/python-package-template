FROM python:3.9

WORKDIR /workspace
ENV PIP_ROOT_USER_ACTION=ignore PIP_DISABLE_PIP_VERSION_CHECK=1
COPY . app
WORKDIR /workspace/app
RUN make install
WORKDIR /workspace
RUN rm -rf app
