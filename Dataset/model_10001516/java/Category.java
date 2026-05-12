





import java.util.List;
import java.util.ArrayList;

public class Category  {

    private String Type;
    private int ID;





    private List<Food_Items> food_itemss;


    public Category(
        String Type,        int ID    ) {
        this.Type = Type;
        this.ID = ID;
        this.food_itemss = new ArrayList<>();
    }

    public Category(
        String Type,        int ID        ArrayList<Food_Items> food_itemss    ) {
        this.Type = Type;
        this.ID = ID;
        this.food_itemss = food_itemss;
    }

    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }

    public List<Food_Items> getFood_itemss() {
        return food_itemss;
    }

    public void addFood_items(Food_items food_items) {
        this.food_itemss.add(food_items);
    }

}