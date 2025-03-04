output "instance_id" {
  description    = "ID of the EC2 instance"
  value          = aws_instance.lab2-tf-example.id
}

output "instance_private_ip" {
  description   = "Private IP address of EC2 instance"
  value       = aws_instance.lab2-tf-example.private_ip
}
