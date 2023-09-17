from ctm_python_client.core.workflow import Workflow, WorkflowDefaults
from ctm_python_client.core.comm import Environment
# from ctm_python_client.ext.viz import get_graph
from aapi import *


workflow = Workflow(Environment.create_workbench(), WorkflowDefaults(run_as='workbench'))

workflow.clear_all()

workflow.chain(
    [
        JobCommand('HelloWorld', 'echo "Hello"'),
        JobCommand('CountFiles', 'ls -l | wc')
    ],
    inpath='TestMonitor'
)

run = workflow.run()

import time
time.sleep(4)

# A few seconds should be enough for all jobs to finish
run.print_statuses()

print(run.get_status('CountFiles'))


print(run.run_id)

output = run.get_output('CountFiles')
print(output)