from Isca_Mentoring.settings import BASE_DIR
from os.path import join

# Location of mentor-form import files
mentor_form_import_dir = join(BASE_DIR, "external_data", "mentor_forms", "import")
# Location of mentor-form parser files
mentor_form_parser_dir = join(BASE_DIR, "external_data", "mentor_forms", "parser")
# Location of mentor-form export files
mentor_form_export_dir = join(BASE_DIR, "external_data", "mentor_forms", "export")

# Location of mentee-form import files
mentee_form_import_dir = join(BASE_DIR, "external_data", "mentee_forms", "import")
# Location of mentee-form parser files
mentee_form_parser_dir = join(BASE_DIR, "external_data", "mentee_forms", "parser")
# Location of mentee-form export files
mentee_form_export_dir = join(BASE_DIR, "external_data", "mentee_forms", "export")