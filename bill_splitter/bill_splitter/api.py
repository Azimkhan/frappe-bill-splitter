import frappe


@frappe.whitelist()
def get_visit(name):
	visit = frappe.get_doc("Visit", name)
	data = visit.as_dict()
	for item in data.get("items", []):
		item["friends"] = frappe.get_all(
			"Visit Item Friend",
			filters={"parent": item["name"], "parentfield": "friends"},
			fields=["name", "friend"],
			order_by="idx asc",
		)
	return data


@frappe.whitelist()
def save_visit(doc):
	doc = frappe.parse_json(doc)
	visit = frappe.get_doc("Visit", doc["name"])

	# Collect old item names to clean up friends
	old_item_names = [item.name for item in visit.items]

	# Delete all old Visit Item Friend rows for this visit's items
	for item_name in old_item_names:
		frappe.db.delete("Visit Item Friend", {"parent": item_name})

	# Rebuild items
	visit.items = []
	for item_data in doc.get("items", []):
		visit.append("items", {
			"menu_item": item_data["menu_item"],
			"price": item_data["price"],
			"quantity": item_data["quantity"],
		})

	visit.save()

	# Now insert Visit Item Friend rows for each item
	for i, item_data in enumerate(doc.get("items", [])):
		item_row = visit.items[i]
		for j, f in enumerate(item_data.get("friends", [])):
			friend_doc = frappe.get_doc({
				"doctype": "Visit Item Friend",
				"parent": item_row.name,
				"parentfield": "friends",
				"parenttype": "Visit Item",
				"friend": f["friend"],
				"idx": j + 1,
			})
			friend_doc.insert()

	frappe.db.commit()
	return get_visit(visit.name)
