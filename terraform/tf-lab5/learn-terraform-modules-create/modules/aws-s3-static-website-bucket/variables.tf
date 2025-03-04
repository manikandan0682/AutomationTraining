variable "bucket_name"{
description="Name of S3 bucket. Must be unique"
type=string
}

variable "tags"{
description= "Tags to set on bucket."
type= map(string)
default= {}
}
