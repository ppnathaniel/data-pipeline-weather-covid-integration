provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "data_pipeline" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "data-pipeline-instance"
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo apt-get update
              sudo apt-get install -y openjdk-8-jdk-headless
              sudo apt-get install -y python3-pip
              pip3 install pandas kafka-python
              wget https://downloads.apache.org/kafka/2.8.0/kafka_2.13-2.8.0.tgz
              tar -xzf kafka_2.13-2.8.0.tgz
              cd kafka_2.13-2.8.0
              nohup ./bin/zookeeper-server-start.sh config/zookeeper.properties &
              nohup ./bin/kafka-server-start.sh config/server.properties &
              EOF
}
