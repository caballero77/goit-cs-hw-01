section .data
    a db 5
    b db 3
    c db 2
    resultMsg db 'Result: '
    newline db 10

section .bss
    result resb 1

section .text
    global _start

_start:
    mov al, [b]
    sub al, [c]
    add al, [a]

    add al, '0'

    mov [result], al

    mov eax, 4
    mov ebx, 1
    mov ecx, resultMsg
    mov edx, 8
    int 0x80

    mov eax, 4
    mov ebx, 1
    mov ecx, result
    mov edx, 1
    int 0x80

    mov eax, 4
    mov ebx, 1
    mov ecx, newline
    mov edx, 1
    int 0x80

    mov eax, 1
    xor ebx, ebx
    int 0x80