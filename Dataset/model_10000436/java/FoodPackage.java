





import java.util.List;
import java.util.ArrayList;

public class FoodPackage  {

    private None FoodList;





    private List<MenuItem> menuitems;


    public FoodPackage(
        None FoodList    ) {
        this.FoodList = FoodList;
        this.menuitems = new ArrayList<>();
    }

    public FoodPackage(
        None FoodList        ArrayList<MenuItem> menuitems    ) {
        this.FoodList = FoodList;
        this.menuitems = menuitems;
    }

    public None getFoodlist() {
        return FoodList;
    }

    public void setFoodlist(None FoodList) {
        this.FoodList = FoodList;
    }

    public List<MenuItem> getMenuitems() {
        return menuitems;
    }

    public void addMenuitem(Menuitem menuitem) {
        this.menuitems.add(menuitem);
    }

}