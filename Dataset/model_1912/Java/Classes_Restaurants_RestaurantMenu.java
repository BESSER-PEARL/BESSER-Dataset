





import java.util.List;
import java.util.ArrayList;

public class Classes_Restaurants_RestaurantMenu  {

    private String items;
    private String name;



    public Classes_Restaurants_RestaurantMenu(
        String items,        String name    ) {
        this.items = items;
        this.name = name;
    }


    public String getItems() {
        return items;
    }

    public void setItems(String items) {
        this.items = items;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}