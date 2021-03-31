jq -r 'to_entries[] | "\(.key)\t\(.value)"' ./env-vars.json |
  while read k v
  do
    export $k=$v
  done
