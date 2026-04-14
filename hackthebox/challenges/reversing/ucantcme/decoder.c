#include <stdio.h>
#include <string.h>

int main() {
    // v4 in little-endian bytes
    unsigned long long v4 = 0x5517696626265E6DULL;
    char v5_data[] = "o&kUZ'ZUYUc)";

    unsigned char mem[20];
    // First 8 bytes: v4 in little-endian
    for (int i = 0; i < 8; i++) {
        mem[i] = (v4 >> (i * 8)) & 0xFF;
    }
    // Next 12 bytes: v5 content
    for (int i = 0; i < 12; i++) {
        mem[8 + i] = (unsigned char)v5_data[i];
    }

    char decoded[21];
    for (int i = 0; i < 20; i++) {
        decoded[i] = mem[i] + 10;
    }
    decoded[20] = '\0';

    printf("Password: %s\n", decoded);
    printf("Flag: HTB{%s}\n", decoded);
    return 0;
}
