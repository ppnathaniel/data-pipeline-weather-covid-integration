provider "aws" {
  region = "us-west-2"
}

# Define an EC2 security group
resource "aws_security_group" "data_pipeline_sg" {
  name        = "data-pipeline-sg"
  description = "Allow traffic to data pipeline services"
  vpc_id      = "your_vpc_id" # Replace with your VPC ID

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8081
    to_port     = 8081
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 9092
    to_port     = 9092
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 2181
    to_port     = 2181
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Define an EC2 instance for the data pipeline
resource "aws_instance" "data_pipeline_instance" {
  ami           = "ami-0c55b159cbfafe1f0" # Example Ubuntu AMI, replace with your choice
  instance_type = "t2.medium"
  security_groups = [aws_security_group.data_pipeline_sg.name]

  user_data = <<-EOF
              #!/bin/bash
              sudo apt-get update
              sudo apt-get install -y docker.io
              sudo systemctl start docker
              sudo systemctl enable docker

              # Install Docker Compose
              sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
              sudo chmod +x /usr/local/bin/docker-compose

              # Clone the project repository
              git clone https://github.com/your-username/data-pipeline-weather-covid-integration.git /home/ubuntu/data-pipeline
              cd /home/ubuntu/data-pipeline

              # Set environment variable
              echo "WEATHER_API_KEY=your_openweathermap_api_key" >> .env

              # Start Docker Compose
              sudo docker-compose up -d
              EOF

  tags = {
    Name = "Data-Pipeline-Instance"
  }
}

# Outputs
output "instance_public_ip" {
  value = aws_instance.data_pipeline_instance.public_ip
}

output "instance_public_dns" {
  value = aws_instance.data_pipeline_instance.public_dns
}
