#!/bin/bash

set -e

export PATH=/root/.local/bin:$PATH
sleep 0.1

exec "$@"