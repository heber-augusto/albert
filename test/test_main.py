import shutil
from albert.albert import handle_command
from albert.jobcommands.jobcommand import (
    load_and_config_parser,
    load_config_json_to_dict)

def test_main_inference_create():
    parser = load_and_config_parser()
    args = parser.parse_args(["create", "inference", "inference_test", '.'])
    handle_command(args)

    inference_config = load_config_json_to_dict('./inference_test/config.json')
    assert inference_config['type'] == 'inference'
    assert inference_config['name'] == 'inference_test'

    shutil.rmtree('inference_test', ignore_errors=True)     