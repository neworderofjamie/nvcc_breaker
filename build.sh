#!/bin/bash
/usr/bin/time -v nvcc -c  -x cu -arch sm_86 -std=c++11 --compiler-options "-fPIC -Wno-return-type-c-linkage -ftime-report" -Xcudafe "--diag_suppress=extern_entity_treated_as_static" $1
