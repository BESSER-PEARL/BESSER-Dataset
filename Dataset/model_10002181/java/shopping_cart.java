





import java.util.List;
import java.util.ArrayList;

public class Shopping_cart  {

    private String Dishname;
    private String time;
    private int price;
    private String attribute;
    private int Quantity;



    public Shopping_cart(
        String Dishname,        String time,        int price,        String attribute,        int Quantity    ) {
        this.Dishname = Dishname;
        this.time = time;
        this.price = price;
        this.attribute = attribute;
        this.Quantity = Quantity;
    }


    public String getDishname() {
        return Dishname;
    }

    public void setDishname(String Dishname) {
        this.Dishname = Dishname;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }


}