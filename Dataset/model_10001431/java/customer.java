





import java.util.List;
import java.util.ArrayList;

public class customer  {

    private int Tableno;
    private String Name;
    private String Order;





    private restaurant restaurant;


    public customer(
        int Tableno,        String Name,        String Order    ) {
        this.Tableno = Tableno;
        this.Name = Name;
        this.Order = Order;
    }


    public int getTableno() {
        return Tableno;
    }

    public void setTableno(int Tableno) {
        this.Tableno = Tableno;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getOrder() {
        return Order;
    }

    public void setOrder(String Order) {
        this.Order = Order;
    }

    public restaurant getRestaurant() {
        return restaurant;
    }

    public void setRestaurant(restaurant restaurant) {
        this.restaurant = restaurant;
    }

}