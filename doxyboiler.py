#! /usr/bin/env python2.7

from __future__ import print_function

import sys, os, re

import CppHeaderParser 

#cpph.classes['elem_t']['methods']['public'][0]
#{'line_number': 18, 'unresolved_parameters': True, 'parent': {'inherits': [], 'line_number': 13, 'forward_declares': {'protected': [], 'public': [], 'private': []}, 'name': 'elem_t', 'parent': None, 'abstract': False, 'namespace': '', 'declaration_method': 'struct', 'properties': {'protected': [], 'public': [{'line_number': 14, 'constant': 0, 'reference': 0, 'raw_type': 'int', 'static': 0, 'array': 0, 'pointer': 0, 'aliases': [], 'typedef': None, 'namespace': '', 'function_pointer': 0, 'mutable': False, 'type': 'int', 'property_of_class': 'elem_t', 'parent': None, 'ctypes_type': 'ctypes.c_int', 'typedefs': 0, 'extern': False, 'class': 0, 'unresolved': False, 'name': 'int_a', 'fundamental': True}, {'line_number': 15, 'constant': 0, 'reference': 0, 'raw_type': 'float', 'static': 0, 'array': 0, 'pointer': 0, 'aliases': [], 'typedef': None, 'namespace': '', 'function_pointer': 0, 'mutable': False, 'type': 'float', 'property_of_class': 'elem_t', 'parent': None, 'ctypes_type': 'ctypes.c_float', 'typedefs': 0, 'extern': False, 'class': 0, 'unresolved': False, 'name': 'float_a', 'fundamental': True}, {'line_number': 16, 'constant': 0, 'reference': 0, 'raw_type': 'double', 'static': 0, 'array': 0, 'pointer': 0, 'aliases': [], 'typedef': None, 'namespace': '', 'function_pointer': 0, 'mutable': False, 'type': 'double', 'property_of_class': 'elem_t', 'parent': None, 'ctypes_type': 'ctypes.c_double', 'typedefs': 0, 'extern': False, 'class': 0, 'unresolved': False, 'name': 'double_a', 'fundamental': True}, {'line_number': 17, 'constant': 0, 'reference': 0, 'raw_type': 'std::string', 'static': 0, 'array': 0, 'pointer': 0, 'aliases': ['std::string'], 'typedef': None, 'namespace': '', 'function_pointer': 0, 'mutable': False, 'type': 'std::string', 'property_of_class': 'elem_t', 'parent': None, 'ctypes_type': 'ctypes.c_void_p', 'typedefs': 0, 'extern': False, 'class': 0, 'unresolved': True, 'name': 'string_a', 'fundamental': 0}], 'private': []}, 'typedefs': {'protected': [], 'public': [], 'private': []}, 'structs': {'protected': [], 'public': [], 'private': []}, 'enums': {'protected': [], 'public': [], 'private': []}, 'final': False, 'nested_classes': [], 'methods': {'protected': [], 'public': [{...}], 'private': []}}, 'defined': False, 'namespace': '', 'operator': False, 'static': False, 'returns_fundamental': True, 'rtnType': 'long', 'extern': False, 'path': 'elem_t', 'returns_pointer': 0, 'parameters': [{'raw_type': 'std::string', 'line_number': 18, 'typedef': None, 'unresolved': True, 'constant': 1, 'name': 'msg', 'parent': None, 'pointer': 0, 'ctypes_type': 'ctypes.c_void_p', 'function_pointer': 0, 'method': {...}, 'static': 0, 'fundamental': 0, 'mutable': False, 'extern': False, 'typedefs': 0, 'array': 0, 'type': 'const std::string &', 'class': 0, 'reference': 1, 'aliases': ['std::string']}], 'class': None, 'returns_reference': False, 'const': False, 'name': 'foomethod', 'pure_virtual': False, 'debug': '\t long foomethod ( const std::string & msg ) ;', 'explicit': False, 'virtual': False, 'destructor': False, 'returns': 'long', 'template': False, 'constructor': False, 'override': False, 'inline': False, 'final': False, 'friend': False, 'returns_class': False}
#cpph.classes['elem_t']['methods']['public'][0].keys()
#['line_number', 'unresolved_parameters', 'parent', 'defined', 'namespace', 'operator', 'static', 'returns_fundamental', 'rtnType', 'extern', 'path', 'returns_pointer', 'parameters', 'class', 'returns_reference', 'const', 'name', 'pure_virtual', 'debug', 'explicit', 'virtual', 'destructor', 'returns', 'template', 'constructor', 'override', 'inline', 'final', 'friend', 'returns_class']
#sorted(cpph.classes['elem_t']['methods']['public'][0].keys())
#['class', 'const', 'constructor', 'debug', 'defined', 'destructor', 'explicit', 'extern', 'final', 'friend', 'inline', 'line_number', 'name', 'namespace', 'operator', 'override', 'parameters', 'parent', 'path', 'pure_virtual', 'returns', 'returns_class', 'returns_fundamental', 'returns_pointer', 'returns_reference', 'rtnType', 'static', 'template', 'unresolved_parameters', 'virtual']
#cpph.classes['elem_t']['methods']['public'][0]['name']
#'foomethod'
#cpph.classes['elem_t']['methods']['public'][0]['parameters']
#[{'raw_type': 'std::string', 'line_number': 18, 'typedef': None, 'unresolved': True, 'constant': 1, 'name': 'msg', 'parent': None, 'pointer': 0, 'ctypes_type': 'ctypes.c_void_p', 'function_pointer': 0, 'method': {'line_number': 18, 'unresolved_parameters': True, 'parent': {'inherits': [], 'line_number': 13, 'forward_declares': {'protected': [], 'public': [], 'private': []}, 'name': 'elem_t', 'parent': None, 'abstract': False, 'namespace': '', 'declaration_method': 'struct', 'properties': {'protected': [], 'public': [{'line_number': 14, 'constant': 0, 'reference': 0, 'raw_type': 'int', 'static': 0, 'array': 0, 'pointer': 0, 'aliases': [], 'typedef': None, 'namespace': '', 'function_pointer': 0, 'mutable': False, 'type': 'int', 'property_of_class': 'elem_t', 'parent': None, 'ctypes_type': 'ctypes.c_int', 'typedefs': 0, 'extern': False, 'class': 0, 'unresolved': False, 'name': 'int_a', 'fundamental': True}, {'line_number': 15, 'constant': 0, 'reference': 0, 'raw_type': 'float', 'static': 0, 'array': 0, 'pointer': 0, 'aliases': [], 'typedef': None, 'namespace': '', 'function_pointer': 0, 'mutable': False, 'type': 'float', 'property_of_class': 'elem_t', 'parent': None, 'ctypes_type': 'ctypes.c_float', 'typedefs': 0, 'extern': False, 'class': 0, 'unresolved': False, 'name': 'float_a', 'fundamental': True}, {'line_number': 16, 'constant': 0, 'reference': 0, 'raw_type': 'double', 'static': 0, 'array': 0, 'pointer': 0, 'aliases': [], 'typedef': None, 'namespace': '', 'function_pointer': 0, 'mutable': False, 'type': 'double', 'property_of_class': 'elem_t', 'parent': None, 'ctypes_type': 'ctypes.c_double', 'typedefs': 0, 'extern': False, 'class': 0, 'unresolved': False, 'name': 'double_a', 'fundamental': True}, {'line_number': 17, 'constant': 0, 'reference': 0, 'raw_type': 'std::string', 'static': 0, 'array': 0, 'pointer': 0, 'aliases': ['std::string'], 'typedef': None, 'namespace': '', 'function_pointer': 0, 'mutable': False, 'type': 'std::string', 'property_of_class': 'elem_t', 'parent': None, 'ctypes_type': 'ctypes.c_void_p', 'typedefs': 0, 'extern': False, 'class': 0, 'unresolved': True, 'name': 'string_a', 'fundamental': 0}], 'private': []}, 'typedefs': {'protected': [], 'public': [], 'private': []}, 'structs': {'protected': [], 'public': [], 'private': []}, 'enums': {'protected': [], 'public': [], 'private': []}, 'final': False, 'nested_classes': [], 'methods': {'protected': [], 'public': [{...}], 'private': []}}, 'defined': False, 'namespace': '', 'operator': False, 'static': False, 'returns_fundamental': True, 'rtnType': 'long', 'extern': False, 'path': 'elem_t', 'returns_pointer': 0, 'parameters': [...], 'class': None, 'returns_reference': False, 'const': False, 'name': 'foomethod', 'pure_virtual': False, 'debug': '\t long foomethod ( const std::string & msg ) ;', 'explicit': False, 'virtual': False, 'destructor': False, 'returns': 'long', 'template': False, 'constructor': False, 'override': False, 'inline': False, 'final': False, 'friend': False, 'returns_class': False}, 'static': 0, 'fundamental': 0, 'mutable': False, 'extern': False, 'typedefs': 0, 'array': 0, 'type': 'const std::string &', 'class': 0, 'reference': 1, 'aliases': ['std::string']}]


COMMENT = """/**
 *
 */
"""

class CommentTarget(object):
  
  head_comment_regex = re.compile(r"^\s*/\*{2}")
  bogus_head_comment_regex = re.compile(r"^\s*/\*[^\*]")
  tail_comment_regex = re.compile(r"^\s*\*/")
  indent_regex = re.compile("\s*")
  
  def __init__(self, record, comment_template=None):
    self.line_number = record['line_number'] - 1 
    self.record = record
    self.comment_template = comment_template or COMMENT
    
    
  def allChildren(self):
    return []
  
  
  def test_or_remove_comment(self, lines):
    """
    @return (do_insert, at_line, indent)
    """
    if( self.line_number == 0 ):
      return (False, 0) # do nothing
    
    bogus_remove_end = start = self.line_number - 1

    match = self.tail_comment_regex.match(lines[start])
    if not match:
      return True, self.line_number
    
    
    while start >= 0:
      
      if self.bogus_head_comment_regex.match(lines[start]):
        lines[start:bogus_remove_end+1] = [] # delete
        return True, self.line_number - (self.line_number - start )
    
      
      if self.head_comment_regex.match(lines[start]):
        return False, 0 
      start -= 1
      
    # @todo strip rancid comment
    return False, 0 # for now
      
  def applyToLines(self, lines):
    isinstance(lines, list)
      
    (doit, atline) = self.test_or_remove_comment(lines)
    if not doit:
      return
    
    indent = self.indent_regex.match(lines[atline]).group(0)
    
    comment = self.comment_template.strip().split("\n")
    for idx, l in enumerate(comment):
      comment[idx] = indent + l + "\n"

    lines[atline:atline] = comment
      
  def __repr__(self):
    return "{0}:{1}".format(self.record['name'], self.line_number)
  

class ClassEntry(CommentTarget):
  def __init__(self, classRec, access=['public', 'protected', 'private']):
    CommentTarget.__init__(self, classRec)
    self.classRec = classRec 
    self.methods = []
  
    allMethods = []
    for acc in access:
      allMethods.extend(classRec['methods'][acc])
  
    for methodRec in allMethods:
      self.methods.append(MethodEntry(methodRec))
      
  def allChildren(self):
    return self.methods
      

class FunctionEntry(CommentTarget):
  def __init__(self, methodRec):
    CommentTarget.__init__(self, methodRec)
    self.methodRec = methodRec
  

class MethodEntry(FunctionEntry):
  pass


class ClassMethodFile(object):
  def __init__(self, filename, targets):
    self.filename = filename
    self.targets = targets
    
def FileToLines(path):
  lines = []
  
  f = file(path, "r")
  for l in f:
    lines.append(l)
  
  return lines


def LinesToFile(lines, path):
  f = file(path, "w")
  for l in lines:
    f.write(l)
    


def main():
  import argparse
  
  parser = argparse.ArgumentParser()
  
  path = sys.argv[1]
  
  cpph = CppHeaderParser.CppHeader(path)
  
  targets = []
  for key, classRec in cpph.classes.items():
    targets.append(ClassEntry(classRec))
    
  for methodRec in cpph.functions:
    targets.append(FunctionEntry(methodRec))
    
  # flatten
  
  flattened = [] 
  for target in targets:
    flattened.append(target)
    flattened.extend(target.allChildren())
    
  flattened = sorted(flattened, (lambda a,b:  b.line_number-a.line_number))
  
  # insert
  
  lines = FileToLines(path)
  
  for target in flattened:
    isinstance(target, CommentTarget)
    target.applyToLines(lines)
  
  
  LinesToFile(lines, path)
  
  
  return 

if __name__ == '__main__':
  main()