





import java.util.List;
import java.util.ArrayList;

public class MCRightAnswer  {

    private float price;
    private int quantity;



    public MCRightAnswer(
        float price,        int quantity    ) {
        this.price = price;
        this.quantity = quantity;
    }


    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }


}