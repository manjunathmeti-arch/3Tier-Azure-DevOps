#!/bin/bash

# Stop the execution of the script on any error
set -e

# Step 1: Update repository information
echo "Updating system repositories..."
sudo apt-get update

# Step 2: Install prerequisites
echo "Installing prerequisites..."
sudo apt-get install -y ca-certificates curl apt-transport-https lsb-release gnupg

# Step 3: Add the Microsoft signing key and repository
echo "Adding the Microsoft signing key..."
curl -sL https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -

echo "Adding Azure CLI repository..."
AZ_REPO=$(lsb_release -cs)
echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | sudo tee /etc/apt/sources.list.d/azure-cli.list

# Step 4: Install the Azure CLI
echo "Updating system repositories again..."
sudo apt-get update

echo "Installing Azure CLI..."
sudo apt-get install azure-cli

echo "Azure CLI installation completed successfully."
