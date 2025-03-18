# Custom Terraform Provider Development Lab

## Overview
You will create a custom Terraform provider in this lab that manages AWS S3 buckets. You'll learn how Terraform providers work and implement basic CRUD (Create, Read, Update, Delete) operations using the Go programming language.

## Prerequisites
- Go 1.21+ installed and configured
- Terraform v1.15+
- AWS credentials (access key and secret key)
- Basic understanding of Terraform (no Go experience required)

## Environment Setup

### Windows Setup
1. Install Go:
   
   Use chocolatey to install Go
   
   ```powershell
   choco install -y golang
   ```

   Confirm it was installed successfully.
   
   ```powershell
   go version
   ```
   
   

## Lab Setup

### 1. Create Development Directory

Windows:
```powershell
mkdir custom-tf-provider
cd custom-tf-provider
```



### 2. Configure Terraform Development Overrides

Create a Terraform configuration file:

Windows:
```powershell
New-Item -Path "$env:APPDATA\terraform.rc" -ItemType File
```

Add the following content:
```hcl
provider_installation {
  dev_overrides {
      "hashicorp.com/edu/custom-s3" = "C:/Users/TEKstudent/go/bin"  # Windows path
  }
  direct {}
}
```



### 3. Initialize Go Module

```sh
go mod init terraform-provider-custom-s3
```

This creates a `go.mod` file to manage dependencies.

## Provider Structure

Create the following directory structure:

Windows:
```powershell
mkdir internal
mkdir internal\provider
```

The provider will have this structure:
```
custom-tf-provider/
├── go.mod
├── main.go
└── internal/
    └── provider/
        ├── provider.go
        ├── bucket_data_source.go
        └── bucket_resource.go
```

### 1. Create the Main Entry Point

Create `main.go` in the root directory with the following content:

```go
package main

import (
    "context"
    "flag"
    "log"
    "terraform-provider-custom-s3/internal/provider"
    "github.com/hashicorp/terraform-plugin-framework/providerserver"
)

var version string = "dev"

func main() {
    var debug bool

    flag.BoolVar(&debug, "debug", false, "set to true to run the provider with support for debuggers")
    flag.Parse()

    opts := providerserver.ServeOpts{
        Address: "hashicorp.com/edu/custom-s3",
        Debug:   debug,
    }

    err := providerserver.Serve(context.Background(), provider.New(version), opts)
    if err != nil {
        log.Fatal(err.Error())
    }
}
```

This file serves several purposes:
- Entry point for the provider plugin
- Sets up the provider server process
- Configures debugging options
- Defines the provider's registry address
- Initializes error handling

### 2. Install Dependencies

Run:
```sh
go mod tidy
```

This will download required dependencies and update `go.mod`.

### 3. Implement the Provider

Create `internal/provider/provider.go`:

```go
package provider

import (
    "context"
    "os"
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/credentials"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/hashicorp/terraform-plugin-framework/datasource"
    "github.com/hashicorp/terraform-plugin-framework/provider"
    "github.com/hashicorp/terraform-plugin-framework/provider/schema"
    "github.com/hashicorp/terraform-plugin-framework/resource"
    "github.com/hashicorp/terraform-plugin-framework/types"
)

// Provider struct holds version information
type cs3Provider struct {
    version string
}

// Provider model for AWS credentials
type cs3ProviderModel struct {
    Region    types.String `tfsdk:"region"`
    AccessKey types.String `tfsdk:"access_key"`
    SecretKey types.String `tfsdk:"secret_key"`
}

func New(version string) func() provider.Provider {
    return func() provider.Provider {
        return &cs3Provider{
            version: version,
        }
    }
}

// Schema defines provider configuration
func (p *cs3Provider) Schema(_ context.Context, _ provider.SchemaRequest, resp *provider.SchemaResponse) {
    resp.Schema = schema.Schema{
        Attributes: map[string]schema.Attribute{
            "region": schema.StringAttribute{
                Optional: true,
            },
            "access_key": schema.StringAttribute{
                Optional: true,
            },
            "secret_key": schema.StringAttribute{
                Optional:  true,
                Sensitive: true,
            },
        },
    }
}

// Configure creates AWS session
func (p *cs3Provider) Configure(ctx context.Context, req provider.ConfigureRequest, resp *provider.ConfigureResponse) {
    var config cs3ProviderModel
    diags := req.Config.Get(ctx, &config)
    resp.Diagnostics.Append(diags...)
    if resp.Diagnostics.HasError() {
        return
    }

    // Get AWS credentials
    region := os.Getenv("AWS_REGION")
    access_key := os.Getenv("AWS_ACCESS_KEY_ID")
    secret_key := os.Getenv("AWS_SECRET_ACCESS_KEY")

    if !config.Region.IsNull() {
        region = config.Region.ValueString()
    }
    if !config.AccessKey.IsNull() {
        access_key = config.AccessKey.ValueString()
    }
    if !config.SecretKey.IsNull() {
        secret_key = config.SecretKey.ValueString()
    }

    // Create AWS session
    sess, err := session.NewSession(&aws.Config{
        Region:      aws.String(region),
        Credentials: credentials.NewStaticCredentials(access_key, secret_key, ""),
    })
    if err != nil {
        resp.Diagnostics.AddError(
            "Unable to create AWS session",
            err.Error(),
        )
        return
    }

    resp.DataSourceData = sess
    resp.ResourceData = sess
}
```

This file handles:
- Provider configuration schema
- AWS authentication
- Session management
- Error handling and diagnostics

### 4. Build and Install

Windows:
```powershell
go build -o terraform-provider-custom-s3.exe
move terraform-provider-custom-s3.exe %USERPROFILE%\go\bin\
```

## Testing the Provider

### 1. Create Test Directory

Create a new directory for testing:

Windows:
```powershell
mkdir test
cd test
```



### 2. Create Test Configuration

Create `main.tf`:
```hcl
terraform {
  required_providers {
    customs3 = {
      source = "hashicorp.com/edu/custom-s3"
    }
  }
}

provider "customs3" {
  region     = "us-west-1"  # or your preferred region
  access_key = "<YOUR_ACCESS_KEY>"
  secret_key = "<YOUR_SECRET_KEY>"
}

resource "customs3_s3_bucket" "test" {
  name = "my-test-bucket-123"
  tags = {
    Environment = "test"
  }
}
```

### 3. Plan and Apply

```sh
terraform plan
terraform apply
```

### 4. Verify

1. Check AWS Console to verify bucket creation
2. List buckets using AWS CLI:
   ```sh
   aws s3 ls
   ```

### 5. Clean Up

```sh
terraform destroy
```

## Troubleshooting

### Common Windows Issues

1. Path Issues:
   - Ensure `%USERPROFILE%\go\bin` is in your PATH
   - Use `echo %PATH%` to verify

2. Permission Issues:
   - Run PowerShell as Administrator when needed
   - Check file permissions in `%USERPROFILE%\go\bin`

3. Go Build Errors:
   - Clear Go build cache: `go clean -cache`
   - Ensure all dependencies are installed: `go mod tidy`



## Congrats!