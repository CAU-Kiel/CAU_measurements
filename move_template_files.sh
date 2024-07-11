#!/bin/sh

rsync -avh nomad-dls_measurements/ .
rm -rfv nomad-dls_measurements
