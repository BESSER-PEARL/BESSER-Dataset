





import java.util.List;
import java.util.ArrayList;

public class Shopping_cart1  {

    private String Dishname;
    private String attribute;
    private int Quantity;
    private int price;
    private String time;





    private Menu1 menu1;




    private Menu1 menu1;


    public Shopping_cart1(
        String Dishname,        String attribute,        int Quantity,        int price,        String time    ) {
        this.Dishname = Dishname;
        this.attribute = attribute;
        this.Quantity = Quantity;
        this.price = price;
        this.time = time;
    }


    public String getDishname() {
        return Dishname;
    }

    public void setDishname(String Dishname) {
        this.Dishname = Dishname;
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
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public Menu1 getMenu1() {
        return menu1;
    }

    public void setMenu1(Menu1 menu1) {
        this.menu1 = menu1;
    }
    public Menu1 getMenu1() {
        return menu1;
    }

    public void setMenu1(Menu1 menu1) {
        this.menu1 = menu1;
    }

}