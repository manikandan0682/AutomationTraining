resource "aws_s3_bucket" "remote_state" {
    bucket = "remote-state-jrs"
    force_destroy = true
    acl = "private"
    
    tags = {
        Name = "remote state backend"
    }
}