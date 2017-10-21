# each item in the manifest is an item and its weight
manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]

cargo_weight = 0
cargo_hold = []

for cargo in manifest:
    if cargo_weight + cargo[1] >= 100:
        break
    else:
        cargo_hold.append(cargo[0])
        cargo_weight += cargo[1]

print(cargo_weight)
print(cargo_hold)