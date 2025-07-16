# Use official Node.js image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Allow passing VITE_API_URL as a build argument


ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL


# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Optional: Print the API URL for debug purposes during build
RUN echo "Building with VITE_API_URL=$VITE_API_URL"

# Build the Vite frontend using the env var
RUN npm run build

# Expose port for development (adjust if needed)
EXPOSE 5173

# Start the development server
CMD ["npm", "run", "dev", "--", "--host"]
