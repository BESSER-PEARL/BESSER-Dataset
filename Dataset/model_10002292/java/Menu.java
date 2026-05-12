





import java.util.List;
import java.util.ArrayList;

public class Menu  {

    private float Price;
    private int Availability;
    private String Category;
    private String MenuItem;





    private Order order;


    public Menu(
        float Price,        int Availability,        String Category,        String MenuItem    ) {
        this.Price = Price;
        this.Availability = Availability;
        this.Category = Category;
        this.MenuItem = MenuItem;
    }


    public float getPrice() {
        return Price;
    }

    public void setPrice(float Price) {
        this.Price = Price;
    }
    public int getAvailability() {
        return Availability;
    }

    public void setAvailability(int Availability) {
        this.Availability = Availability;
    }
    public String getCategory() {
        return Category;
    }

    public void setCategory(String Category) {
        this.Category = Category;
    }
    public String getMenuitem() {
        return MenuItem;
    }

    public void setMenuitem(String MenuItem) {
        this.MenuItem = MenuItem;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}