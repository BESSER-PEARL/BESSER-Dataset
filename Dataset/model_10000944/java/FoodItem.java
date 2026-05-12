





import java.util.List;
import java.util.ArrayList;

public class FoodItem  {

    private None Food;





    private List<MenuItem> menuitems;


    public FoodItem(
        None Food    ) {
        this.Food = Food;
        this.menuitems = new ArrayList<>();
    }

    public FoodItem(
        None Food        ArrayList<MenuItem> menuitems    ) {
        this.Food = Food;
        this.menuitems = menuitems;
    }

    public None getFood() {
        return Food;
    }

    public void setFood(None Food) {
        this.Food = Food;
    }

    public List<MenuItem> getMenuitems() {
        return menuitems;
    }

    public void addMenuitem(Menuitem menuitem) {
        this.menuitems.add(menuitem);
    }

}