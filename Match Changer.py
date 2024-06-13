import obspython as obs
import pandas as pd
from urllib.parse import quote

partit_id = 0
spreadsheet_id = ""
sheet_name = "Sheet1"
source_nameA = ""
source_nameB = ""
source_pronomA = ""
source_pronomB = ""
source_pbA = ""
source_pbB = ""
source_twitchA = ""
source_twitchB = ""
hotkey_id_next_match = None
hotkey_id_refresh = None
infos = ["Nombre","Pronombre","PB","Nombre2","Pronombre2","PB2","Nombre3","Pronombre3","PB3","Nombre4","Pronombre4","PB4","Nombre5","Pronombre5","PB5","Nombre6","Pronombre6","PB6","Nombre7","Pronombre7","PB7","Nombre8","Pronombre8","PB8","Nombre9","Pronombre9","PB9","Nombre10","Pronombre10","PB10","Nombre11","Pronombre11","PB11","Nombre12","Pronombre12","PB12","Nombre13","Pronombre13","PB13","Nombre14","Pronombre14","PB14","Nombre15","Pronombre15","PB15","Nombre16","Pronombre16","PB16","Nombre17","Pronombre17","PB17","Nombre18","Pronombre18","PB18","Nombre19","Pronombre19","PB19","Nombre20","Pronombre20","PB20","Nombre21","Pronombre21","PB21","Nombre22","Pronombre22","PB22","Nombre23","Pronombre23","PB23","Nombre24","Pronombre24","PB24","Nombre25","Pronombre25","PB25","Nombre26","Pronombre26","PB26","Nombre27","Pronombre27","PB27","Nombre28","Pronombre28","PB28","Nombre29","Pronombre29","PB29","Nombre30","Pronombre30","PB30","Nombre31","Pronombre31","PB31","Nombre32","Pronombre32","PB32","Nombre33","Pronombre33","PB33","Nombre34","Pronombre34","PB34","Nombre35","Pronombre35","PB35","Nombre36","Pronombre36","PB36","Nombre37","Pronombre37","PB37","Nombre38","Pronombre38","PB38","Nombre39","Pronombre39","PB39","Nombre40","Pronombre40","PB40","Nombre41","Pronombre41","PB41","Nombre42","Pronombre42","PB42","Nombre43","Pronombre43","PB43","Nombre44","Pronombre44","PB44","Nombre45","Pronombre45","PB45","Nombre46","Pronombre46","PB46","Nombre47","Pronombre47","PB47","Nombre48","Pronombre48","PB48"]
url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
streamServiceBaseUrl = "https://www.twitch.tv/"

# ------------------------------------------------------------

def update_text():
	global infos
	global source_nameA
	global source_nameB
	global source_pronomA
	global source_pronomB
	global source_pbA
	global source_pbB
	global source_twitchA
	global source_twitchB
	global partit_id
	
	_source_nameA = obs.obs_get_source_by_name(source_nameA)
	_source_nameB = obs.obs_get_source_by_name(source_nameB)
	_source_pronomA = obs.obs_get_source_by_name(source_pronomA)
	_source_pronomB = obs.obs_get_source_by_name(source_pronomB)
	_source_pbA = obs.obs_get_source_by_name(source_pbA)
	_source_pbB = obs.obs_get_source_by_name(source_pbB)
	_source_TwitchA = obs.obs_get_source_by_name(source_twitchA)
	_source_TwitchB = obs.obs_get_source_by_name(source_twitchB)

	_source_nameA_text = obs.obs_data_create()
	obs.obs_data_set_string(_source_nameA_text, "text", infos[partit_id])
	obs.obs_source_update(_source_nameA, _source_nameA_text)
	obs.obs_data_release(_source_nameA_text)

	_source_nameB_text = obs.obs_data_create()
	obs.obs_data_set_string(_source_nameB_text, "text", infos[partit_id+4])
	obs.obs_source_update(_source_nameB, _source_nameB_text)
	obs.obs_data_release(_source_nameB_text)

	_source_pronomA_text = obs.obs_data_create()
	obs.obs_data_set_string(_source_pronomA_text, "text", infos[partit_id+1])
	obs.obs_source_update(_source_pronomA, _source_pronomA_text)
	obs.obs_data_release(_source_pronomA_text)

	_source_pronomB_text = obs.obs_data_create()
	obs.obs_data_set_string(_source_pronomB_text, "text", infos[partit_id+5])
	obs.obs_source_update(_source_pronomB, _source_pronomB_text)
	obs.obs_data_release(_source_pronomB_text)

	_source_pbA_text = obs.obs_data_create()
	obs.obs_data_set_string(_source_pbA_text, "text", infos[partit_id+2])
	obs.obs_source_update(_source_pbA, _source_pbA_text)
	obs.obs_data_release(_source_pbA_text)

	_source_pbB_text = obs.obs_data_create()
	obs.obs_data_set_string(_source_pbB_text, "text", infos[partit_id+6])
	obs.obs_source_update(_source_pbB, _source_pbB_text)
	obs.obs_data_release(_source_pbB_text)

	_source_TwitchA_text = obs.obs_data_create()
	obs.obs_data_set_string(_source_TwitchA_text, "url", streamServiceBaseUrl + infos[partit_id+3])
	obs.obs_source_update(_source_TwitchA, _source_TwitchA_text)
	obs.obs_data_release(_source_TwitchA_text)

	_source_TwitchB_text = obs.obs_data_create()
	obs.obs_data_set_string(_source_TwitchB_text, "url", streamServiceBaseUrl + infos[partit_id+7])
	obs.obs_source_update(_source_TwitchB, _source_TwitchB_text)
	obs.obs_data_release(_source_TwitchB_text)

	obs.obs_source_release(_source_nameA)
	obs.obs_source_release(_source_nameB)
	obs.obs_source_release(_source_pronomA)
	obs.obs_source_release(_source_pronomB)
	obs.obs_source_release(_source_pbA)
	obs.obs_source_release(_source_pbB)
	obs.obs_source_release(_source_TwitchA)
	obs.obs_source_release(_source_TwitchB)

def next_partit():
	global partit_id
	global infos

	partit_id += 8
	if partit_id >= len(infos):
		partit_id = 0

def getData():
	global spreadsheet_id
	global sheet_name
	global url
	global infos

	url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
	safe_url = quote(url, safe='/:&=?')

	data = pd.read_csv(safe_url)

	infos = []
	_i = 0
	while not pd.isna(data.loc[_i,'PlayerA']):
		infos.append(data.loc[_i,'PlayerA'])
		infos.append(data.loc[_i,'PronA'])
		infos.append(data.loc[_i,'PbA'])
		infos.append(data.loc[_i,'TwitchA'])
		infos.append(data.loc[_i,'PlayerB'])
		infos.append(data.loc[_i,'PronB'])
		infos.append(data.loc[_i,'PbB'])
		infos.append(data.loc[_i,'TwitchB'])
		_i += 1

def next_match_pressed(props, prop):
	getData()
	next_partit()
	update_text()

def refresh_pressed(props, prop):
	getData()
	update_text()

def nM_HK(pressed):
	if pressed:
		getData()
		next_partit()
		update_text()
		
def r_HK(pressed):
	if pressed:
		getData()
		update_text()

# ------------------------------------------------------------

def script_load(settings):
    global hotkey_id_next_match, hotkey_id_refresh
    hotkey_id_next_match = obs.obs_hotkey_register_frontend("next_match", "Next Match", nM_HK)
    hotkey_id_refresh = obs.obs_hotkey_register_frontend("refresh", "Refresh", r_HK)

def script_unload():
    global hotkey_id_next_match, hotkey_id_refresh
    if hotkey_id_next_match is not None:
        obs.obs_hotkey_unregister(hotkey_id_next_match)
    if hotkey_id_refresh is not None:
        obs.obs_hotkey_unregister(hotkey_id_refresh)

def script_description():
	return '''Updates a series of sources to the ones retrieved from a google spreadsheet.
Made with ♥ by Selur91'''

def script_update(settings):
	global source_nameA
	global source_nameB
	global source_pronomA
	global source_pronomB
	global source_pbA
	global source_pbB
	global source_twitchA
	global source_twitchB

	global spreadsheet_id
	global sheet_name

	global streamServiceBaseUrl

	source_nameA = obs.obs_data_get_string(settings, "source_nameA")
	source_nameB = obs.obs_data_get_string(settings, "source_nameB")
	source_pronomA = obs.obs_data_get_string(settings, "source_pronomA")
	source_pronomB = obs.obs_data_get_string(settings, "source_pronomB")
	source_pbA = obs.obs_data_get_string(settings, "source_pbA")
	source_pbB = obs.obs_data_get_string(settings, "source_pbB")

	source_twitchA = obs.obs_data_get_string(settings, "source_twitchA")
	source_twitchB = obs.obs_data_get_string(settings, "source_twitchB")

	spreadsheet_id = obs.obs_data_get_string(settings, "spreadsheet_id")
	sheet_name = obs.obs_data_get_string(settings, "sheet_name")
	streamServiceBaseUrl = obs.obs_data_get_string(settings, "streamServiceBaseUrl")

def script_defaults(settings):
	obs.obs_data_set_default_string(settings, "streamServiceBaseUrl", "https://www.twitch.tv/")

def script_properties():
	props = obs.obs_properties_create()

	obs.obs_properties_add_text(props, "spreadsheet_id", "Spreadsheet ID", obs.OBS_TEXT_DEFAULT)
	obs.obs_properties_add_text(props, "sheet_name", "Sheet Name", obs.OBS_TEXT_DEFAULT)
	obs.obs_properties_add_text(props, "streamServiceBaseUrl", "Stream Service Base URL", obs.OBS_TEXT_DEFAULT)

	ps = [obs.obs_properties_add_list(props, "source_nameA", "Source Name A", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING),
	   	obs.obs_properties_add_list(props, "source_nameB", "Source Name B", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING),
		obs.obs_properties_add_list(props, "source_pronomA", "Source Pronom A", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING),
		obs.obs_properties_add_list(props, "source_pronomB", "Source Pronom B", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING),
		obs.obs_properties_add_list(props, "source_pbA", "Source PB A", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING),
		obs.obs_properties_add_list(props, "source_pbB", "Source PB B", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING)]
	
	pst = [obs.obs_properties_add_list(props, "source_twitchA", "Source Twitch A", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING),
		obs.obs_properties_add_list(props, "source_twitchB", "Source Twitch B", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING)]
		
	sources = obs.obs_enum_sources()
	if sources is not None:
		for source in sources:
			source_id = obs.obs_source_get_unversioned_id(source)
			if source_id == "text_gdiplus" or source_id == "text_ft2_source":
				name = obs.obs_source_get_name(source)
				for p in ps:
					obs.obs_property_list_add_string(p, name, name)
			elif source_id == "browser_source":
				name = obs.obs_source_get_name(source)
				for p in pst:
					obs.obs_property_list_add_string(p, name, name)

		obs.source_list_release(sources)


	obs.obs_properties_add_button(props, "button1", "Next Match", next_match_pressed)
	obs.obs_properties_add_button(props, "button2", "Refresh", refresh_pressed)
	return props
