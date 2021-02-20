FROM python:3 as builder
WORKDIR /usr/src/rice
COPY . .
RUN pip install flit \
	&& flit build --format wheel

FROM python:3-alpine
LABEL org.opencontainers.image.source=https://github.com/hugglesfox/rice
COPY --from=builder /usr/src/rice/dist/rice-*.whl .
RUN pip install --no-cache-dir rice-*.whl \
	&& rm rice-*.whl
ENTRYPOINT ["/usr/local/bin/rice"]
