





import java.util.List;
import java.util.ArrayList;

public class FoodPackage  {

    private None FoodList;





    private List<Food> foods;




    private List<MenuItem> menuitems;


    public FoodPackage(
        None FoodList    ) {
        this.FoodList = FoodList;
        this.foods = new ArrayList<>();
        this.menuitems = new ArrayList<>();
    }

    public FoodPackage(
        None FoodList        ArrayList<Food> foods,        ArrayList<MenuItem> menuitems    ) {
        this.FoodList = FoodList;
        this.foods = foods;
        this.menuitems = menuitems;
    }

    public None getFoodlist() {
        return FoodList;
    }

    public void setFoodlist(None FoodList) {
        this.FoodList = FoodList;
    }

    public List<Food> getFoods() {
        return foods;
    }

    public void addFood(Food food) {
        this.foods.add(food);
    }
    public List<MenuItem> getMenuitems() {
        return menuitems;
    }

    public void addMenuitem(Menuitem menuitem) {
        this.menuitems.add(menuitem);
    }

}