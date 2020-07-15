import json
import xmltodict
print("Hello World")
json_text = '{"key1": "value1", "key2": "value2"}'
json_dict = json.loads(json_text)
print(json.dumps(json_dict, indent=2))



my_dict = xmltodict.parse("""<?xml version="1.0" encoding="utf-8"?>
<root>
  <duty name="SEC-CIS">
    <RedirAutoCount>10</RedirAutoCount>
    <RedirAuto>006301819352</RedirAuto>
    <RedirAuto>006209715508</RedirAuto>
    <RedirAuto>006303384043</RedirAuto>
    <RedirAuto>006303857308</RedirAuto>
    <RedirAuto>006301819352</RedirAuto>
    <RedirAuto>006209715508</RedirAuto>
    <RedirAuto>006303384043</RedirAuto>
    <RedirAuto>006303857308</RedirAuto>
    <RedirAuto>006209115978</RedirAuto>
    <RedirAuto>006307561122</RedirAuto>
    <RedirManual>NOTSET</RedirManual>
  </duty>
  <duty name="SEC-FORTI">
    <RedirAutoCount>6</RedirAutoCount>
    <RedirAuto>006306700643</RedirAuto>
    <RedirAuto>006704292530</RedirAuto>
    <RedirAuto>006306700643</RedirAuto>
    <RedirAuto>006704292530</RedirAuto>
    <RedirAuto>006303384069</RedirAuto>
    <RedirAuto>006307561122</RedirAuto>
    <RedirManual>NOTSET</RedirManual>
  </duty>
  <duty name="SEC-CP">
    <RedirAutoCount>12</RedirAutoCount>
    <RedirAuto>006204603807</RedirAuto>
    <RedirAuto>006705022040</RedirAuto>
    <RedirAuto>006709347473</RedirAuto>
    <RedirAuto>006303384066</RedirAuto>
    <RedirAuto>006309619311</RedirAuto>
    <RedirAuto>006204603807</RedirAuto>
    <RedirAuto>006705022040</RedirAuto>
    <RedirAuto>006709347473</RedirAuto>
    <RedirAuto>006303384066</RedirAuto>
    <RedirAuto>006309619311</RedirAuto>
    <RedirAuto>006303384069</RedirAuto>
    <RedirAuto>006307561122</RedirAuto>
    <RedirManual>NOTSET</RedirManual>
  </duty>
  <duty name="SEC-MOB">
    <RedirAutoCount>10</RedirAutoCount>
    <RedirAuto>006705159889</RedirAuto>
    <RedirAuto>006202163427</RedirAuto>
    <RedirAuto>006209199351</RedirAuto>
    <RedirAuto>006309400447</RedirAuto>
    <RedirAuto>006705159889</RedirAuto>
    <RedirAuto>006202163427</RedirAuto>
    <RedirAuto>006209199351</RedirAuto>
    <RedirAuto>006309400447</RedirAuto>
    <RedirAuto>006203590295</RedirAuto>
    <RedirAuto>006307561122</RedirAuto>
    <RedirManual>NOTSET</RedirManual>
  </duty>
</root>
""")

# print(json.dumps(my_dict, indent=2))

json_xmldata = """{
  "root": {
    "duty": [
      {
        "@name": "SEC-CIS",
        "RedirAutoCount": "10",
        "RedirAuto": [
          "006301819352",
          "006209715508",
          "006303384043",
          "006303857308",
          "006301819352",
          "006209715508",
          "006303384043",
          "006303857308",
          "006209115978",
          "006307561122"
        ],
        "RedirManual": "NOTSET"
      },
      {
        "@name": "SEC-FORTI",
        "RedirAutoCount": "6",
        "RedirAuto": [
          "006306700643",
          "006704292530",
          "006306700643",
          "006704292530",
          "006303384069",
          "006307561122"
        ],
        "RedirManual": "NOTSET"
      },
      {
        "@name": "SEC-CP",
        "RedirAutoCount": "12",
        "RedirAuto": [
          "006204603807",
          "006705022040",
          "006709347473",
          "006303384066",
          "006309619311",
          "006204603807",
          "006705022040",
          "006709347473",
          "006303384066",
          "006309619311",
          "006303384069",
          "006307561122"
        ],
        "RedirManual": "NOTSET"
      },
      {
        "@name": "SEC-MOB",
        "RedirAutoCount": "10",
        "RedirAuto": [
          "006705159889",
          "006202163427",
          "006209199351",
          "006309400447",
          "006705159889",
          "006202163427",
          "006209199351",
          "006309400447",
          "006203590295",
          "006307561122"
        ],
        "RedirManual": "NOTSET"
      }
    ]
  }
}"""

dict_xmldata = json.loads(json_xmldata)

print(xmltodict.unparse(dict_xmldata, pretty=True))
