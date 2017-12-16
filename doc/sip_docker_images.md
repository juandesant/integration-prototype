# SIP Docker images


## Building images with `docker-compose`

SIP docker images can be build with the `docker-compose.yml` script
found in the top level directory of the repository.

To build all SIP images use the following command(s):

```bash
docker-compose build
docker-compose -f docker-compose_rest.yml build
```

or to build an individual images:

```bash
docker-compose build [service]
```

where `[service]` is the name of the service (from the list in the 
`docker-compose.yml`) that you want to build.


## SIP Docker image names

SIP images are prefixed with `skasip/`

The current list of SIP images is:

- `skasip/master_rpyc`<br> 
   The Master Controller Service with an RPyC interface.
 
- `skasip/master_rest`<br>
  The Master Controller Service with an REST interface.

- `skasip/qa_rpyc`<br>
  The Quality Assessment Service with an RPyC interface.
