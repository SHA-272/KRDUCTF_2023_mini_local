FROM ubuntu:jammy

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y gcc socat
WORKDIR /pwn

COPY ./main.c main.c

RUN gcc -fno-stack-protector -o main main.c
RUN rm main.c
RUN chmod a+x main

RUN chmod go-rx /usr/bin/passwd

RUN useradd pwn
USER pwn

CMD ["socat", "-d", "-d", "TCP4-LISTEN:31337,fork,reuseaddr", "EXEC:'timeout 180 /pwn/main',pty,echo=0,raw,iexten=0"]
EXPOSE 31337
