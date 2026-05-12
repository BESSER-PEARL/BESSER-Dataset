





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String name;
    private String Note;
    private float price;
    private String food_id;





    private Order order;


    public Product(
        String name,        String Note,        float price,        String food_id    ) {
        this.name = name;
        this.Note = Note;
        this.price = price;
        this.food_id = food_id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNote() {
        return Note;
    }

    public void setNote(String Note) {
        this.Note = Note;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getFood_id() {
        return food_id;
    }

    public void setFood_id(String food_id) {
        this.food_id = food_id;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}