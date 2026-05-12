





import java.util.List;
import java.util.ArrayList;

public class Menu  {

    private None drinksItem;
    private String category;
    private None foodItem;





    private MenuItem menuitem;


    public Menu(
        None drinksItem,        String category,        None foodItem    ) {
        this.drinksItem = drinksItem;
        this.category = category;
        this.foodItem = foodItem;
    }


    public None getDrinksitem() {
        return drinksItem;
    }

    public void setDrinksitem(None drinksItem) {
        this.drinksItem = drinksItem;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public None getFooditem() {
        return foodItem;
    }

    public void setFooditem(None foodItem) {
        this.foodItem = foodItem;
    }

    public MenuItem getMenuitem() {
        return menuitem;
    }

    public void setMenuitem(MenuItem menuitem) {
        this.menuitem = menuitem;
    }

}