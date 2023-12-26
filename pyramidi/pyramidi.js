const pyramid = function (layers) {
  const output = [];
  const blankSpace = layers * 2 - 2;

  for (let i = 0; i < layers; i++) {
    let str = "*";
    for (let y = 0; y < i; y++) str += "**";

    const spaces = blankSpace / 2 - i;
    str = " ".repeat(spaces) + str + " ".repeat(spaces);
    output.push(str);
  }

  return output;
};

const amount = prompt("Amount of layers?");
const result = pyramid(amount);
for (const x of result) console.log(x);
