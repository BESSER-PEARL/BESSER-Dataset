





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private int Calories;
    private boolean Vegetarian;
    private int Price;





    private List<FoodPackage> foodpackages;




    private List<FoodItem> fooditems;


    public Food(
        int Calories,        boolean Vegetarian,        int Price    ) {
        this.Calories = Calories;
        this.Vegetarian = Vegetarian;
        this.Price = Price;
        this.foodpackages = new ArrayList<>();
        this.fooditems = new ArrayList<>();
    }

    public Food(
        int Calories,        boolean Vegetarian,        int Price        ArrayList<FoodPackage> foodpackages,        ArrayList<FoodItem> fooditems    ) {
        this.Calories = Calories;
        this.Vegetarian = Vegetarian;
        this.Price = Price;
        this.foodpackages = foodpackages;
        this.fooditems = fooditems;
    }

    public int getCalories() {
        return Calories;
    }

    public void setCalories(int Calories) {
        this.Calories = Calories;
    }
    public boolean getVegetarian() {
        return Vegetarian;
    }

    public void setVegetarian(boolean Vegetarian) {
        this.Vegetarian = Vegetarian;
    }
    public int getPrice() {
        return Price;
    }

    public void setPrice(int Price) {
        this.Price = Price;
    }

    public List<FoodPackage> getFoodpackages() {
        return foodpackages;
    }

    public void addFoodpackage(Foodpackage foodpackage) {
        this.foodpackages.add(foodpackage);
    }
    public List<FoodItem> getFooditems() {
        return fooditems;
    }

    public void addFooditem(Fooditem fooditem) {
        this.fooditems.add(fooditem);
    }

}