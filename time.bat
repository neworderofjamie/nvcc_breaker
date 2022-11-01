ECHO OFF
ECHO %TIME%
"%CUDA_PATH%\bin\nvcc.exe" -gencode=arch=compute_52,code=\"sm_52,compute_52\" --use-local-env -x cu   -I"%CUDA_PATH%\include" --keep-dir x64\Release  -maxrregcount=0  --machine 64 --compile -cudart static    -DWIN32 -DWIN64 -DNDEBUG -D_CONSOLE -D_MBCS -Xcompiler "/bigobj /EHsc /W3 /nologo /O2 /Fdx64\Release\vc142.pdb /FS   /MD " -o x64\Release\test_10000_check_cuda_errors_exception.cc.obj "%1"
ECHO %TIME%