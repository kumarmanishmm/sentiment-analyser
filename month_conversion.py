month_conversion = {
	"jan" : "january",
	"feb" : "february",
	"mar" : "march",
	"aprl" : "april",
	"may" : "may",
	"jun" : "june",
	"jul" : "july",
	"aug" : "august",
	"sept": "september",
	"oct" : "october",
	"nov" : "november",
	"dec" : "december"
}

print(month_conversion.get("nov","not a  valid key"))
print(month_conversion.get("luv","not a valid key"))