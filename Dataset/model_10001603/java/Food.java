





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private int food_id;
    private String food_name;
    private int Category_id;



    public Food(
        int food_id,        String food_name,        int Category_id    ) {
        this.food_id = food_id;
        this.food_name = food_name;
        this.Category_id = Category_id;
    }


    public int getFood_id() {
        return food_id;
    }

    public void setFood_id(int food_id) {
        this.food_id = food_id;
    }
    public String getFood_name() {
        return food_name;
    }

    public void setFood_name(String food_name) {
        this.food_name = food_name;
    }
    public int getCategory_id() {
        return Category_id;
    }

    public void setCategory_id(int Category_id) {
        this.Category_id = Category_id;
    }


}