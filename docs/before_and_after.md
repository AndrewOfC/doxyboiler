
# Before

```c++
// -*- mode: c++ -*-
#pragma once
#include <string>

/**
 *
 */
class a {
public:
  long method_a1(const std:string& arg1) ;

  void method_a2(const std::string& arg1, int arg2, int arg3, bool flag) ;

  void method_a3(int xyz) ;

  void method_a4() ;
  
} ;


class b {
public:
  void method_a1(const std:string& arg1) ;
  void method_a2(const std::string& arg1, int arg2, int arg3, bool flag) ;
  void method_a3(int xyz) ;
  
} ;


/**
 *
 */
class c {
public:
  void method_a1(const std:string& arg1) ;
  /*
   * previous(but bogus)
   */
  int method_a2(const std::string& arg1, int arg2, int arg3, bool flag) ;

  // yah

  /** 
   * previous but not boguss
   */
  void method_a3(int xyz) ;
  
} ;

// void function_a(int a, int b) ;


```

# After

```c++

// -*- mode: c++ -*-
#pragma once
#include <string>

/**
 *
 */
class a {
public:
  /** 
   * @brief UNDOCUMENTED
   *
   * @param arg1
   * @return long
   */
  long method_a1(const std:string& arg1) ;

  /** 
   * @brief UNDOCUMENTED
   *
   * @param arg1
   * @param arg2
   * @param arg3
   * @param flag
   */
  void method_a2(const std::string& arg1, int arg2, int arg3, bool flag) ;

  /** 
   * @brief UNDOCUMENTED
   *
   * @param xyz
   */
  void method_a3(int xyz) ;

  /** 
   * @brief UNDOCUMENTED
   *
   */
  void method_a4() ;
  
} ;


/**
 *
 */
class b {
public:
  /** 
   * @brief UNDOCUMENTED
   *
   * @param arg1
   */
  void method_a1(const std:string& arg1) ;
  /** 
   * @brief UNDOCUMENTED
   *
   * @param arg1
   * @param arg2
   * @param arg3
   * @param flag
   */
  void method_a2(const std::string& arg1, int arg2, int arg3, bool flag) ;
  /** 
   * @brief UNDOCUMENTED
   *
   * @param xyz
   */
  void method_a3(int xyz) ;
  
} ;


/**
 *
 */
class c {
public:
  /** 
   * @brief UNDOCUMENTED
   *
   * @param arg1
   */
  void method_a1(const std:string& arg1) ;
  /** 
   * @brief UNDOCUMENTED
   *
   * @param arg1
   * @param arg2
   * @param arg3
   * @param flag
   * @return int
   */
  int method_a2(const std::string& arg1, int arg2, int arg3, bool flag) ;

  // yah

  /** 
   * previous but not boguss
   */
  void method_a3(int xyz) ;
  
} ;

// void function_a(int a, int b) ;


```

