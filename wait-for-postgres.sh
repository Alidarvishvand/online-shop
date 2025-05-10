#!/bin/sh

echo "⏳ Waiting for PostgreSQL to be ready..."

until pg_isready -h db -p 5432 > /dev/null 2>&1; do
  sleep 1
done

echo "✅ PostgreSQL is ready!"
exec "$@"
