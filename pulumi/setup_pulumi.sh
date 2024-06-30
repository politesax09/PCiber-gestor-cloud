#!/bin/bash


# Instalar Pulumi

# Crear proyecto azure
mkdir pulumi/azure
cd pulumi/azure
pulumi new azure-python

# Crear proyecto aws
mkdir pulumi/aws
cd pulumi/aws
pulumi new aws-python