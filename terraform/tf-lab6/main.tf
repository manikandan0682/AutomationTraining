terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region  = "us-west-1"
}

resource "aws_instance" "tf_example_import" {
    ami="ami-01eb4eefd88522422"
    instance_type = "t2.micro"
    count = 3

    tags= {
        Name = "tf_example_import"
        role = "terraform"
    }
  
}