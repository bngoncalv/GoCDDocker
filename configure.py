#!/usr/bin/env python
from gomatic import *

configurator = GoCdConfigurator(HostRestClient("localhost:8153", ssl=False))
configurator.agent_auto_register_key = '388b633a88de126531afa41eff9aa69e'

pipeline = configurator\
	.ensure_pipeline_group("defaultGroup")\
	.ensure_replacement_of_pipeline("react-pipeline")\
	.set_git_url("https://github.com/bngoncalv/react-example")
stage = pipeline.ensure_stage("defaultStage")
job = stage.ensure_job("build")
job.add_task(ExecTask(['npm', 'install']))
job = stage.ensure_job("test")
job.add_task(ExecTask(['bash', '-c', 'CI=true npm test']))
job = stage.ensure_job("deploy")
job.add_task(ExecTask(['bash', '-c', 'npm run deploy']))

configurator.save_updated_config()
