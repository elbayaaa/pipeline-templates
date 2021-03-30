# """ instantiate the plugin """
# import os
#
# import boto3
#
# from samcli.lib.cookiecutter.interactive_flow_creator import InteractiveFlowCreator
# from samcli.lib.cookiecutter.plugin import Plugin
# from .postprocessor import Postprocessor
# from .preprocessor import Preprocessor
#
#
# def init_plugin(provider):
#     questions_path = os.path.join(os.path.dirname(__file__), "questions.json")
#     context = {"provider": provider, "aws_profiles": boto3.session.Session().available_profiles}
#     return Plugin(
#         interactive_flow=InteractiveFlowCreator.create_flow(questions_path, context),
#         preprocessor=Preprocessor(),
#         postprocessor=Postprocessor(),
#     )
