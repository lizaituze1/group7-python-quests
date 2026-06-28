dragon_scales = 3
scale_price = 10

elf_tears = 5
tear_price = 3

total = (dragon_scales * scale_price) + (elf_tears * tear_price)

print(f"Dragon scales: {dragon_scales} x {scale_price}g = {dragon_scales * scale_price}g")
print(f"Elf tears:     {elf_tears} x {tear_price}g  = {elf_tears * tear_price}g")
print(f"Total cost:    {total} gold")