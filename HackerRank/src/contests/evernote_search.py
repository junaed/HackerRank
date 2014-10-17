'''
Created on Sep 28, 2014

@author: junaed
'''
import sys
import xml.etree.ElementTree as ET
import re
import datetime


def escape_chars(text):
    return text.replace("&"," ").replace("<"," ").replace(">"," ")
#     return text.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def unescape_chars(text):
    return text
#     return text.replace("amp;","").replace("&lt;","<").replace("&gt;",">")

def skip_non_alpha_numeric_chars(text):
    return re.sub(r'[^a-zA-Z0-9\']',' ',text).strip()

def parse_xml(input_xml, notes):
#     input_xml = escape_chars(input_xml)
#     print input_xml
    root = ET.fromstring(input_xml)
    guid = root.find("guid").text
    created = datetime.datetime.strptime(root.find("created").text,'%Y-%m-%dT%H:%M:%SZ')
#     created = dt.parser.parse(root.find("created").text)
    content = root.find("content").text
    content = unescape_chars(content)
    content = skip_non_alpha_numeric_chars(content)
    contents = content.split(" ")
    contentlist = []
    for word in contents:
        word = word.strip()
        if len(word) == 0:
            continue
#         word = skip_non_alpha_numeric_chars(word)
        contentlist.append(word.lower())
    all_tags = root.findall("tag")
    tags = []
    for tag in all_tags:
        tags.append(unescape_chars(skip_non_alpha_numeric_chars(tag.text)))
    
    note = {"guid":guid, "created":created, "content":contentlist, "tags":tags}
    notes[guid] = note
    
def delete_note(guid, notes):
    del notes[guid]

def search_text(dictionary_key, notes, q):
    match = None
    results = set()           
    if q[len(q)-1] == "*":
        #prefix match
        match = q[0:-1]
        match = skip_non_alpha_numeric_chars(match)
        for k,v in notes.iteritems():
            all_items = v[dictionary_key]
            for item in all_items:
                if item.startswith(match):
                    results.add((k,v["created"]))
                    break
    else:
        #exact match
        q = skip_non_alpha_numeric_chars(q)
        for k,v in notes.iteritems():
            all_items = v[dictionary_key]
            if q.lower() in all_items:
                results.add((k,v["created"]))
    return results
def search_note(query, notes):
    query = str(query)
    results = set()
    t_results = set()
    query = query.strip("\n").strip(" ")
    queries = query.split(" ")
    
    for q in queries:
        if q.startswith("tag:"):
            q = q.split(":")[1]
            t_results = search_text("tags", notes, q)
            
        elif q.startswith("created"):
            q = q.split(":")[1]
            ipdt = datetime.datetime.strptime(q, "%Y%m%d")
            dat = datetime.datetime.now()
            dat = dat.replace(year=ipdt.year, month = ipdt.month, day = ipdt.day, hour = 0, minute = 1, second = 0)
            for k,v in notes.iteritems():
                if v["created"] >= dat:
                    t_results.add((k,v["created"]))
        else:
            #search in content
            t_results = search_text("content", notes, q)       
                 
        if len(results) == 0:
            results = results.union(t_results)
        else:
            results = set.intersection(results, t_results)
        t_results.clear()
    return sorted(list_str(results), key=lambda tup:tup[1])

if __name__ == '__main__':
    
    notes = {}
    inputs = []
#     test_cases = open("evernote.txt","r")
#     for test in test_cases:
#         inputs.append(test)
    inputs = sys.stdin.readlines()
    input_len = len(inputs)
    i = 0
    while i < input_len:
#         print inputs[i]
        test = inputs[i].strip()
        if test == "CREATE":
            i += 1
            xml_part = inputs[i].strip() + " "
            xml = ""
            while "</note>" not in xml_part:
                xml += xml_part + " "
                i += 1
                xml_part = inputs[i].strip()
                if ("</note>" not in xml_part) and ("<guid>" not in xml_part) and ("</guid>" not in xml_part) and "<tag>" not in xml_part and "</tag>" not in xml_part and "<created>" not in xml_part and "</created>" not in xml_part and "<content>" not in xml_part and "</content>" not in xml_part:
                    xml_part = escape_chars(xml_part)
                
            xml += xml_part
#             print xml
            parse_xml(xml, notes)
#             print notes
#             print "added"
            pass
        elif test == "UPDATE":
            i += 1
            xml_part = inputs[i].strip()
            xml = ""
            while "</note>" not in xml_part:
                xml += xml_part + " "
                i += 1
                xml_part = inputs[i].strip()
                if "</note>" not in xml_part and "<guid>" not in xml_part and "</guid>" not in xml_part and "<tag>" not in xml_part and "</tag>" not in xml_part and "<created>" not in xml_part and "</created>" not in xml_part and "<content>" not in xml_part and "</content>" not in xml_part:
                    xml_part = escape_chars(xml_part)
            xml += xml_part
            parse_xml(xml, notes)
#             print notes
            pass
        elif test == "DELETE":
            i += 1
            guid = inputs[i].strip()
            delete_note(guid, notes)
            pass
        elif test == "SEARCH":
            i += 1
            query = inputs[i].strip()
            results = search_note(query, notes)
            for l, result in enumerate(results):
                if l>0:
                    sys.stdout.write(",")
                sys.stdout.write(result[0].strip(" "))
            print""
            pass
        else:
            sys.stderr.write("Say What!")
        i += 1
        
    
    pass
