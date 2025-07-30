import os

def interleave(file1, file2, out_file, stride):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2, open(out_file, 'wb') as out:
        while True:
            chunk1 = f1.read(stride)
            chunk2 = f2.read(stride)
            if not chunk1 and not chunk2:
                break
            out.write(chunk1)
            out.write(chunk2)

def uninterleave(input_file, out1, out2, stride):
    with open(input_file, 'rb') as f, open(out1, 'wb') as f1, open(out2, 'wb') as f2:
        while True:
            chunk1 = f.read(stride)
            chunk2 = f.read(stride)
            if not chunk1:
                break
            f1.write(chunk1)
            if chunk2:
                f2.write(chunk2)

def main():
    print("\033[96m=== Interleave & Uninterleave Tool by Sheikh Nightshader ===\033[0m")
    choice = input("Interleave (i) or Uninterleave (u)? ").strip().lower()
    stride = int(input("Byte difference (stride): ").strip())

    if choice == 'i':
        file1 = input("First file: ").strip()
        file2 = input("Second file: ").strip()
        out = input("Output file: ").strip()
        interleave(file1, file2, out, stride)
        print("\033[92mInterleaving complete.\033[0m")
    elif choice == 'u':
        infile = input("Interleaved file: ").strip()
        out1 = input("Output file 1: ").strip()
        out2 = input("Output file 2: ").strip()
        uninterleave(infile, out1, out2, stride)
        print("\033[92mUninterleaving complete.\033[0m")
    else:
        print("\033[91mInvalid choice.\033[0m")

if __name__ == "__main__":
    main()
