





import java.util.List;
import java.util.ArrayList;

public class Admin  {






    private List<Food_Items> food_itemss;


    public Admin(
    ) {
        this.food_itemss = new ArrayList<>();
    }

    public Admin(
        ArrayList<Food_Items> food_itemss    ) {
        this.food_itemss = food_itemss;
    }


    public List<Food_Items> getFood_itemss() {
        return food_itemss;
    }

    public void addFood_items(Food_items food_items) {
        this.food_itemss.add(food_items);
    }

}