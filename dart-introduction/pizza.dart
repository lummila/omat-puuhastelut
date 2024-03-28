import "dart:io";

List<String> margarita_ingredients = [
  "Tomato sauce",
  "Mozzarella",
  "Basil",
  "Parmeriggioni"
];

List<String> hawaii_ingredients = [
  "Tomato sauce",
  "Pineapple",
  "Mozzarella",
  "Ham"
];

class Pizza {
  String name;

  Pizza(this.name) {
    // Margarita and Hawaii are readymade, known pizzas
    if (name == "Margarita") {
      this.present("Margarita", margarita_ingredients);
    } else if (name == "Hawaii") {
      this.present("Hawaii", hawaii_ingredients);
    } else {
      // Build your own pizza
      this.build();
    }
  }

  void build() {
    List<String> ingredients = [];

    print("Build your own pizza!\nEnter main ingredient: ");
    String? main_ingredient = stdin.readLineSync();

    // If user doesn't enter anything, function stops
    if (main_ingredient != null) {
      ingredients.add(main_ingredient);
    } else {
      print("No ingredients chosen, see you again!");
      return;
    }

    print("You can add additional ingredients!\n"
        "Press Enter to continue without. ");
    String? additional_ingredient = stdin.readLineSync();

    /* If user just pressed Enter, going forth without
    additional ingredients */
    while (additional_ingredient != null) {
      ingredients.add(additional_ingredient);
      print("${additional_ingredient} added!");

      additional_ingredient = stdin.readLineSync();
      if (additional_ingredient == "") {
        break;
      }
    }

    // Then moving on to presentation
    this.present(this.name, ingredients);
  }

  // Present the pizza to the user with all the ingredients
  void present(String name, List<String> parts) {
    print("-------------------------------");
    print("Here's your ${name} pizza with:");
    for (String x in parts) {
      print("• $x");
    }

    print("\nThank you for choosing us!");
    print("-------------------------------");
  }
}

int main() {
  print("Enter a pizza name: ");
  String? chosen_name = stdin.readLineSync();

  if (chosen_name == null) {
    print("Goodbye then.");
    return 0;
  } else {
    Pizza(chosen_name);
  }

  return 0;
}
