int main() {
  int mushroom = 0;
  String pepperoni;
  List all_ingredients = [];

  for (int i = 0; i < 5; i++) {
    print("Mushrooms: ${mushroom}");
    mushroom++;
  }

  pepperoni = "pepperoni";
  all_ingredients.add(pepperoni);

  print("There's also ${all_ingredients[0]}!");

  return 0;
}
