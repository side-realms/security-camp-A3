#include <stdio.h>
#include <stdint.h>
#define N 10

static inline uint32_t memaccesstime(void *v) {
  uint32_t rv ;
  asm volatile (
    "mfence\n"
    "lfence\n"
    "rdtscp\n"
    "mov %%eax, %%esi\n"
    "mov (%1), %%eax\n"
    "rdtscp\n"
    "sub %%esi, %%eax\n"
    : "=&a" (rv): "r" (v): "ecx", "edx", "esi");
  return rv;
}

static inline void clflush(void *v) {
  asm volatile ("clflush 0(%0)": : "r" (v):);
}

int main(){
  uint32_t res_cache[N];
  uint32_t res_nocache[N];

  uint32_t target;
  uint16_t t;

  for(int i=0; i<N ; ++i){
    t = memaccesstime(&target);
    res_cache[i] = memaccesstime(&target);
  }

  for(int i=0; i<N ; ++i){
    clflush(&target);
    res_nocache[i] = memaccesstime(&target);
  }

  for(int i=0; i<N ; ++i){
    printf("cache=%d, nocache=%d\n", res_cache[i], res_nocache[i]);
  }
}
