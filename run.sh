#!/bin/bash
set -e

case "$1" in
  build_generator)
    docker build -t hw3-generator ./generator
    ;;
  run_generator)
    docker run --rm -v "$(pwd)/data:/data" hw3-generator
    ;;
  create_local_data)
    python3 generator/generate.py local_data
    ;;
  build_reporter)
    docker build -t hw3-reporter ./reporter
    ;;
  run_reporter)
    docker run --rm -v "$(pwd)/data:/data" hw3-reporter
    ;;
  structure)
    find . -not -path '*/.*'
    ;;
  clear_data)
    rm -f data/*.csv data/*.html
    ;;
  inside_generator)
    docker run --rm -v "$(pwd)/data:/data" hw3-generator ls -la /data
    ;;
  inside_reporter)
    docker run --rm -v "$(pwd)/data:/data" hw3-reporter ls -la /data
    ;;
  report_server)
    docker run --rm -v "$(pwd)/data:/usr/share/nginx/html:ro" -p 8080:80 nginx
    ;;
  *)
    echo "Неизвестная команда: $1"
    ;;
esac