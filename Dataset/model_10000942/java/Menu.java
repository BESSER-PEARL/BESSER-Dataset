





import java.util.List;
import java.util.ArrayList;

public class Menu  {

    private String MenuItem;
    private String Category;
    private int Availability;
    private float Price;





    private List<OrderItem> orderitems;


    public Menu(
        String MenuItem,        String Category,        int Availability,        float Price    ) {
        this.MenuItem = MenuItem;
        this.Category = Category;
        this.Availability = Availability;
        this.Price = Price;
        this.orderitems = new ArrayList<>();
    }

    public Menu(
        String MenuItem,        String Category,        int Availability,        float Price        ArrayList<OrderItem> orderitems    ) {
        this.MenuItem = MenuItem;
        this.Category = Category;
        this.Availability = Availability;
        this.Price = Price;
        this.orderitems = orderitems;
    }

    public String getMenuitem() {
        return MenuItem;
    }

    public void setMenuitem(String MenuItem) {
        this.MenuItem = MenuItem;
    }
    public String getCategory() {
        return Category;
    }

    public void setCategory(String Category) {
        this.Category = Category;
    }
    public int getAvailability() {
        return Availability;
    }

    public void setAvailability(int Availability) {
        this.Availability = Availability;
    }
    public float getPrice() {
        return Price;
    }

    public void setPrice(float Price) {
        this.Price = Price;
    }

    public List<OrderItem> getOrderitems() {
        return orderitems;
    }

    public void addOrderitem(Orderitem orderitem) {
        this.orderitems.add(orderitem);
    }

}