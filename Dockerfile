FROM scratch
ADD x86_64/01a9e6267b872b64590704ae846f38780e643dfa71f24c6094687d6949ea759d.tar.xz /
ADD x86_64/3eb274027648a40a24a435e0f08002c5e47f2d0a18de9833066d14f03c07355f.tar.xz /
ADD x86_64/5942ae88b0a03ce69e12360b55a0127e39f21618a93b5ea90dc8229024f63e02.tar.xz /
ADD x86_64/66c21bc1a2b7ab155f61f25a890a062da3614896ad0d2af391d84e35b0eef2a4.tar.xz /
ADD x86_64/6c8f51580b46d4fbf7295957057398bc688b3b9c73ab50d10be4625a2f6a9c37.tar.xz /
ADD x86_64/9ffe916f24347030c7fe9b544a349eebc4e28f523854bc85054d2796a34ded6e.tar.xz /

ENV LANG=en_US.UTF-8
ENV TZ=:/etc/localtime
ENV PATH=/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
ENV LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib
ENV LAMBDA_TASK_ROOT=/var/task
ENV LAMBDA_RUNTIME_DIR=/var/runtime

WORKDIR /var/task

ENTRYPOINT ["/lambda-entrypoint.sh"]
