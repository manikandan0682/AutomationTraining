variable "instance_name" {
  description = "Name tag for EC2 instance"
  type        = string
  default     = "Lab2-TF-example"
}

/* variable "image_id"{
  type=string
  description = "The id of the machine image"
  validation {
    condition = len(image_id)>4 && substr(var.image_id, 0, 4) == "ami-"
    error_message = "should start with ami_"
  }
} */
