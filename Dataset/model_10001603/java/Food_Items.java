





import java.util.List;
import java.util.ArrayList;

public class Food_Items  {

    private int quantity;
    private int Items_id;
    private int Food_id;
    private int Material_id;



    public Food_Items(
        int quantity,        int Items_id,        int Food_id,        int Material_id    ) {
        this.quantity = quantity;
        this.Items_id = Items_id;
        this.Food_id = Food_id;
        this.Material_id = Material_id;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public int getItems_id() {
        return Items_id;
    }

    public void setItems_id(int Items_id) {
        this.Items_id = Items_id;
    }
    public int getFood_id() {
        return Food_id;
    }

    public void setFood_id(int Food_id) {
        this.Food_id = Food_id;
    }
    public int getMaterial_id() {
        return Material_id;
    }

    public void setMaterial_id(int Material_id) {
        this.Material_id = Material_id;
    }


}