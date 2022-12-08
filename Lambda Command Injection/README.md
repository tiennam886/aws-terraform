# Terraform-AWS-API-Gateway-and-Lambda

## Tutorial
[AWS: API Gateway invoking Lambda function with Terraform](https://www.bogotobogo.com/DevOps/AWS/aws-API-Gateway-Lambda-Terraform.php)

## Command
```cmd
terraform init
terraform apply -var="app_version=1.0.0" --auto-approve
curl https://[uuid].execute-api.us-east-1.amazonaws.com/dev/number?command=10
terraform destroy --auto-approve
```


