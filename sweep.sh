#/bin/bash

for NUM_ARRAYS in 50000
do
    for CHECK_CUDA_ERRORS in CHECK_CUDA_ERRORS_ASSERT CHECK_CUDA_ERRORS_ABORT CHECK_CUDA_ERRORS_ABORT_NO_PRINT CHECK_CUDA_ERRORS_EXCEPTION CHECK_CUDA_ERRORS_EXCEPTION_NO_MESSAGE
    do
        echo $NUM_ARRAYS $CHECK_CUDA_ERRORS
    
        # Generate code
        python generate.py --num-arrays $NUM_ARRAYS --check-cuda-errors $CHECK_CUDA_ERRORS --stdout > test.cc
        
        OUTPUT_FILENAME="output_${NUM_ARRAYS}_${CHECK_CUDA_ERRORS}.txt"
        ls -all test.cc > $OUTPUT_FILENAME
        timeout -s 41943040 ./build.sh test.cc &>> $OUTPUT_FILENAME
    done
done
