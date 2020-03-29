## this Includes Notes, to-dos, Commands and everything
## else relating to the project Alfred

command:
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose

python -m rasa_core.train interactive -o models/dialogue -d domain.yml -c nlu_config.yml -s data/stories.md --nlu models/current/nlu --skip_visualization   #--endpoints endpoint.yml

python -m rasa_core.train interactive -o models/dialogue -d domain.yml -c nlu_config.yml -s data/stories.md 
   #--endpoints endpoint.yml

python -m rasa_core.run --nlu models/current/nlu --core models/dialogue --debug --endpoints endpoints.yml

python -m rasa_core_sdk.endpoint --actions actions

to do
- organise everything on GIT.
- train the new model.
- get o work it on the console.
- understand how nlu and dialogues are stored.
- get it on slack.
- get the database ready.
- understand logarithmic scale
- manage everything brilliantly

MVP deliverable
- first all details
- second specific statistics
- third trends
- fourth plots and prediction
- time - series

timeline
- it needs to be functional within no time, before 6th April