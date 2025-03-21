terraform {
  required_providers {
    customs3 = {
      source = "hashicorp.com/edu/custom-s3"
    }
  }
}

provider "customs3" {
  region     = "us-west-1"  # or your preferred region
  access_key = "AKIA57VDL2ULOG5D6ZGM"
  secret_key = "+DvoNQEvlWDK5jOEgPbb9ahw8vsBeIPGGqkRphnq"
}

resource "customs3_s3_bucket" "test" {
  buckets = [{
    name = "test-bucket-2398756-mn"
    tags = "yourbucket"
  }]
}