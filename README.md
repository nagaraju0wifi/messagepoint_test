# messagepoint_test


messagepoint_testment

            |                                                                                                         
            |                                                                                                               
            - - Application_code  -> It has complete application code for create,list and render templtes
                        |                                                                                 
                        |
                        -------- app_with_sqlite.py  -> application work with sqlite database
                        |
                        -------- app_with_mysql.py    -> application work with mysql database
            |
            |
            |
            - - Deployment_script  -> It has a shell script to do the deployment
                (Note: the deployment steps are added in CloudFormation template client data to start the application on b
            oot)
            |
		|
		---- AWS_CloudFormation_templates - It has aws cloudFormation Templates are there
