from ctm_python_client.core.workflow import Workflow, WorkflowDefaults
from ctm_python_client.core.comm import Environment
from aapi import JobCommand, Folder


# create workflow
wf = Workflow(
    Environment.create_workbench(
        host="localhost",
        port="8443",
    ),
    WorkflowDefaults(
        run_as="workbench",
    ),
)


# create job
my_job = JobCommand(
    object_name="print_time_now",
    command="date",
)


# add job to workflow
folder = Folder("print_time_now", job_list=[my_job])
wf.add(folder)


# # deploy workflow
# if wf.deploy().is_ok():
#     print("The workflow is valid")

# run workflow
run = wf.run()

# print output
run.print_output(job_name="print_time_now")
