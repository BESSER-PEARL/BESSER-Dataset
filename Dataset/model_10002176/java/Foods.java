





import java.util.List;
import java.util.ArrayList;

public class Foods  {

    private None Foodname;
    private None Catogory;
    private None price;
    private boolean Ready;





    private Order order;


    public Foods(
        None Foodname,        None Catogory,        None price,        boolean Ready    ) {
        this.Foodname = Foodname;
        this.Catogory = Catogory;
        this.price = price;
        this.Ready = Ready;
    }


    public None getFoodname() {
        return Foodname;
    }

    public void setFoodname(None Foodname) {
        this.Foodname = Foodname;
    }
    public None getCatogory() {
        return Catogory;
    }

    public void setCatogory(None Catogory) {
        this.Catogory = Catogory;
    }
    public None getPrice() {
        return price;
    }

    public void setPrice(None price) {
        this.price = price;
    }
    public boolean getReady() {
        return Ready;
    }

    public void setReady(boolean Ready) {
        this.Ready = Ready;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}