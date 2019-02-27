// -*- mode: c++ -*-
#pragma once
#include <string>

/**
 *
 */
class a {
public:
  /**
   *
   */
  void method_a1(const std:string& arg1) ;
  /**
   *
   */
  void method_a2(const std::string& arg1, int arg2, int arg3, bool flag) ;
  /**
   *
   */
  void method_a3(int xyz) ;
  
} ;


/**
 *
 */
class b {
public:
  /**
   *
   */
  void method_a1(const std:string& arg1) ;
  /**
   *
   */
  void method_a2(const std::string& arg1, int arg2, int arg3, bool flag) ;
  /**
   *
   */
  void method_a3(int xyz) ;
  
} ;


/**
 *
 */
class c {
public:
  /**
   *
   */
  void method_a1(const std:string& arg1) ;
  /**
   * previous(but bogus)
   */
  void method_a2(const std::string& arg1, int arg2, int arg3, bool flag) ;
  /**
   *
   */
  void method_a3(int xyz) ;
  
} ;

// void function_a(int a, int b) ;

