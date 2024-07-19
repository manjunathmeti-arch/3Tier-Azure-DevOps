#!/bin/bash

# Stop the execution of the script on any error
set -e

sudo apt-get update && sudo apt-get install -y gnupg software-properties-common

# Import the HashiCorp GPG key and add it to the trusted keyring
wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

# Display the fingerprint for verification
gpg --no-default-keyring --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg --fingerprint

# Add the HashiCorp repository to the system
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

sudo apt update

# Install Terraform
sudo apt-get install terraform

# Display help for the 'terraform plan' command
terraform -help plan

echo "Terraform has been installed successfully and is ready to use."
