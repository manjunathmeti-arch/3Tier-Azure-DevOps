# Use an official Node runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /app/task-manager

# Copy local package.json and package-lock.json into the Docker container
COPY package.json package-lock.json ./

# Install all dependencies defined in package.json
RUN npm install

# Copy the local public directory into the Docker container
COPY public/ public/

# Copy local React source files into the Docker container
COPY src/ src/

# Expose port 3000 to the host
EXPOSE 3000

# Command to run the app
CMD ["npm", "start"]
