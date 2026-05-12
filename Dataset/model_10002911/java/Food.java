





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private boolean Vegetarian;
    private int Price;
    private int Calories;





    private List<FoodItem> fooditems;




    private List<FoodPackage> foodpackages;


    public Food(
        boolean Vegetarian,        int Price,        int Calories    ) {
        this.Vegetarian = Vegetarian;
        this.Price = Price;
        this.Calories = Calories;
        this.fooditems = new ArrayList<>();
        this.foodpackages = new ArrayList<>();
    }

    public Food(
        boolean Vegetarian,        int Price,        int Calories        ArrayList<FoodItem> fooditems,        ArrayList<FoodPackage> foodpackages    ) {
        this.Vegetarian = Vegetarian;
        this.Price = Price;
        this.Calories = Calories;
        this.fooditems = fooditems;
        this.foodpackages = foodpackages;
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
    public int getCalories() {
        return Calories;
    }

    public void setCalories(int Calories) {
        this.Calories = Calories;
    }

    public List<FoodItem> getFooditems() {
        return fooditems;
    }

    public void addFooditem(Fooditem fooditem) {
        this.fooditems.add(fooditem);
    }
    public List<FoodPackage> getFoodpackages() {
        return foodpackages;
    }

    public void addFoodpackage(Foodpackage foodpackage) {
        this.foodpackages.add(foodpackage);
    }

}