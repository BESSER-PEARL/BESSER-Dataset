





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private boolean Vegetarian;
    private int Calories;
    private int Price;





    private List<FoodItem> fooditems;


    public Food(
        boolean Vegetarian,        int Calories,        int Price    ) {
        this.Vegetarian = Vegetarian;
        this.Calories = Calories;
        this.Price = Price;
        this.fooditems = new ArrayList<>();
    }

    public Food(
        boolean Vegetarian,        int Calories,        int Price        ArrayList<FoodItem> fooditems    ) {
        this.Vegetarian = Vegetarian;
        this.Calories = Calories;
        this.Price = Price;
        this.fooditems = fooditems;
    }

    public boolean getVegetarian() {
        return Vegetarian;
    }

    public void setVegetarian(boolean Vegetarian) {
        this.Vegetarian = Vegetarian;
    }
    public int getCalories() {
        return Calories;
    }

    public void setCalories(int Calories) {
        this.Calories = Calories;
    }
    public int getPrice() {
        return Price;
    }

    public void setPrice(int Price) {
        this.Price = Price;
    }

    public List<FoodItem> getFooditems() {
        return fooditems;
    }

    public void addFooditem(Fooditem fooditem) {
        this.fooditems.add(fooditem);
    }

}