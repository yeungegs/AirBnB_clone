#!/bin/bash
# this script is a simplified version of docker's generate-authors script
# https://github.com/docker/docker/blob/master/hack/generate-authors.sh
git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf > AUTHORS
