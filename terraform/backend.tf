terraform {
  backend "s3" {
    bucket = "terraform-state-flaskbb"
    key    = "core/terraform.tfstate"
    region = "us-east-1"
  }
}