jq -r 'to_entries[] | "\(.key)\t\(.value)"' {{cookiecutter.cicd_folder_name}}/env-vars.json |
  while read k v
  do
    export $k=$v
  done
