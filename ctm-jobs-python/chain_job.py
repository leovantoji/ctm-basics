from ctm_python_client.core.workflow import Workflow, WorkflowDefaults
from ctm_python_client.core.comm import Environment
from aapi import JobCommand, JobDummy


# create workflow
workflow = Workflow(
    Environment.create_workbench(
        host="localhost",
        port="8443",
    ),
    WorkflowDefaults(
        run_as="workbench",
    ),
)

workflow.clear_all()

workflow.chain(
    [
        JobDummy('Dummy'),
        JobCommand('MyJob1', command='echo "Hello"'),
        JobCommand('MyJob2', command='echo "Hello2"'),
    ],
    inpath='TestJobDummy'
)

run = workflow.run()

import time
time.sleep(2) # Give some time for the flow to finish

# No output for a JobDummy
output = run.get_output('Dummy')
assert output is None

# Output for a JobCommand
output = run.get_output('MyJob1')
assert output is not None
print(output)

# Output for a JobCommand
output = run.get_output('MyJob2')
assert output is not None
print(output)

print(run.get_jobid("MyJob1"))

