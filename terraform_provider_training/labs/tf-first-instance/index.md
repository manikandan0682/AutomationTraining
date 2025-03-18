# Terraform - Create your first instance

# Overview
This lab walks through setting up Terraform and creating your first resources. 

## Setup 
These instructions are intended to be run in Visual Studio Code **Bash Terminal**, but you can accomplish the same thing by using the UI.

Create and enter the working directory:

```sh
mkdir -p $HOME/$(date +%Y%m%d)/terraform
cd 
```


## Create Terraform configuration

In the working directory, create a directory for the lab files:
```sh
mkdir tf-lab1
cd $_
```
Terraform loads all files in the working directory that end in `.tf`.

Create a `main.tf` file with the following: 
```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region  = "us-west-1"
}

resource "aws_instance" "lab1-tf-example" {
  ami           = "ami-06e4ca05d431835e9"
  instance_type = "t2.micro"

  tags = {
    Name = "Lab1-TF-example"
  }
}
```

This is a complete configuration that Terraform is ready to apply. We'll review each configuration block in more detail in the following sections.

## Providers 
Each Terraform module must declare which providers it requires so that Terraform can install and use them. Provider requirements are stated in a `required_providers` block.

A provider requirement consists of a local name, a source location, and a version constraint:
The `provider` block configures the named provider, which in our case is `aws`. The provider is responsible for understanding the API and translating the Terraform configuration, so it works with the vendor's API. Because Terraform has many providers, you can represent almost any infrastructure type as a `resource` in Terraform.

You can optionally specify a `profile` attribute in your provider block. This attribute refers to credentials stored in your AWS Configuration. 

**NOTE:** You should NEVER hard-code credentials into your `*.tf` files. 

## Resources 
The `resource` block defines the infrastructure you want to create. This resource can be a physical component like an EC2 instance, GCP VM, or VMware machine, or it can be logical like a Heroku application. 

Our resource block has two strings before the block: a resource type and resource name. 
In the above example, the type is `aws_instance,` and the name is `lab1-tf-example` - this prefix of type maps to the provider. The `aws_instance` type tells Terraform the aws provider manages it.

We provide configuration data for our resource inside the resource block. These arguments are for machine size, image, VPC IDs, SSH usernames, etc. 

## Initialize the directory
Now that we have our configuration file created, run `terraform init` to download the providers used in our configuration.

Terraform uses a plugin-based architecture to support hundreds of infrastructure and service providers. Subsequent commands will use local settings and data during initialization.

Output will be similar to: 
```
Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/aws...
- Installing hashicorp/aws v3.34.0...
- Installed hashicorp/aws v3.34.0 (signed by HashiCorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

Terraform downloads the `aws` provider and installs it in a hidden subdirectory of the current working directory. The output shows which version of the plugin was installed.

Confirm the plugin was downloaded: 
```sh
choco install -y tree 
tree .terraform/
```

You should see output like: 
```
.terraform/
`-- providers
    `-- registry.terraform.io
        `-- hashicorp
            `-- aws
                `-- 5.80.0
                    `-- windows_amd64
                        |-- LICENSE.txt
                        `-- terraform-provider-aws_v5.80.0_x5.exe

6 directories, 2 files
```

As you can see above Terraform download the aws provider from the official Hashicorp registry. 

## Format and validate configuration 
Terraform includes a `fmt` argument to ensure consistent formatting in files and modules written by different teams. It automatically updates configurations for easy readability and consistency. 

The `main.tf` file created is very basic, and is already formatted. 
```sh
terraform fmt 
```

If there were any formatting issues, like equal signs not aligned or wrong indentation `fmt` will fix them.

If any files are formatted Terraform will output the name of the file. If there are not formatting changes there is not output.

Now use the built-in `terraform validate` command to check and report any errors in modules, attribute names, and value types.

## Create infrastructure 
Now that the provider is downloaded, configuration files are formatted and validated it's time to create the infrastructure. 

Run `terraform plan` to review the changes Terraform will make. 

This output shows the execution plan, describing which actions Terraform will take in order to change real infrastructure to match the configuration.

Run `terraform apply`

The output has a + next to `aws_instance.lab1-tf-example`, meaning that Terraform will create this resource. Beneath that, it shows the attributes that will be set. When the value displayed is (known after apply), it means that the value won't be known until the resource is created.

Terraform will now pause and wait for your approval before proceeding. If anything in the plan seems incorrect or dangerous, it is safe to abort here with no changes made to your infrastructure.

In this case, the plan is acceptable, so type `yes` at the confirmation prompt to proceed. Executing the plan will take a few minutes since Terraform waits for the EC2 instance to become available.




# Cleanup
Destroy the infrastructure you created 
```sh
terraform destroy -auto-approve
```
**Note:** You can also use `-auto-approve` with `terraform apply`

# Congrats! 
