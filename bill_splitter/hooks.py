app_name = "bill_splitter"
app_title = "Bill Splitter"
app_publisher = "Azimkhan Yerzhan"
app_description = "Let\'s you and your friends split the bill and track history of spendings"
app_email = "wanrossen@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "bill_splitter",
# 		"logo": "/assets/bill_splitter/logo.png",
# 		"title": "Bill Splitter",
# 		"route": "/bill_splitter",
# 		"has_permission": "bill_splitter.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bill_splitter/css/bill_splitter.css"
# app_include_js = "/assets/bill_splitter/js/bill_splitter.js"

# include js, css files in header of web template
# web_include_css = "/assets/bill_splitter/css/bill_splitter.css"
# web_include_js = "/assets/bill_splitter/js/bill_splitter.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "bill_splitter/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "bill_splitter/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "bill_splitter.utils.jinja_methods",
# 	"filters": "bill_splitter.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "bill_splitter.install.before_install"
# after_install = "bill_splitter.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "bill_splitter.uninstall.before_uninstall"
# after_uninstall = "bill_splitter.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "bill_splitter.utils.before_app_install"
# after_app_install = "bill_splitter.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "bill_splitter.utils.before_app_uninstall"
# after_app_uninstall = "bill_splitter.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bill_splitter.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"bill_splitter.tasks.all"
# 	],
# 	"daily": [
# 		"bill_splitter.tasks.daily"
# 	],
# 	"hourly": [
# 		"bill_splitter.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bill_splitter.tasks.weekly"
# 	],
# 	"monthly": [
# 		"bill_splitter.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "bill_splitter.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "bill_splitter.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bill_splitter.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "bill_splitter.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["bill_splitter.utils.before_request"]
# after_request = ["bill_splitter.utils.after_request"]

# Job Events
# ----------
# before_job = ["bill_splitter.utils.before_job"]
# after_job = ["bill_splitter.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"bill_splitter.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

website_route_rules = [
    {"from_route": "/bill/<path:app_path>", "to_route": "_bill"},
    {"from_route": "/bill", "to_route": "_bill"},
]
