import sys
from jinja2 import Template
from argparse import ArgumentParser

parser = ArgumentParser(description="Generator of pathological runner files")
parser.add_argument("--num-arrays", type=int, default=1000)
parser.add_argument("--check-cuda-errors", choices=["CHECK_CUDA_ERRORS_ASSERT", "CHECK_CUDA_ERRORS_ABORT", 
                                                    "CHECK_CUDA_ERRORS_ABORT_NO_PRINT", "CHECK_CUDA_ERRORS_EXCEPTION",
                                                    "CHECK_CUDA_ERRORS_EXCEPTION_NO_MESSAGE"], default="CHECK_CUDA_ERRORS_EXCEPTION")
parser.add_argument("--fake-cuda", action="store_true")
parser.add_argument("--stdout", action="store_true")
args = parser.parse_args()


with open("runner.cc.template", "r") as file:
    template = Template(file.read())

arrays = [{"name": f"array_{i}", "size": 1000} for i in range(args.num_arrays)]


output = template.render(arrays=arrays, host=True, check_cuda_errors=args.check_cuda_errors, 
                         fake_cuda=args.fake_cuda)

if args.stdout:
    print(output)
else:
    with open(f"test_{args.num_arrays}_{args.check_cuda_errors.lower()}.cc", "w") as file:
        file.write(output)
