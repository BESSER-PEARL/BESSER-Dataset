





import java.util.List;
import java.util.ArrayList;

public class Menu  {

    private String MenuItem;
    private int Availability;
    private float Price;
    private String Category;





    private List<OrderItem> orderitems;


    public Menu(
        String MenuItem,        int Availability,        float Price,        String Category    ) {
        this.MenuItem = MenuItem;
        this.Availability = Availability;
        this.Price = Price;
        this.Category = Category;
        this.orderitems = new ArrayList<>();
    }

    public Menu(
        String MenuItem,        int Availability,        float Price,        String Category        ArrayList<OrderItem> orderitems    ) {
        this.MenuItem = MenuItem;
        this.Availability = Availability;
        this.Price = Price;
        this.Category = Category;
        this.orderitems = orderitems;
    }

    public String getMenuitem() {
        return MenuItem;
    }

    public void setMenuitem(String MenuItem) {
        this.MenuItem = MenuItem;
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
    public String getCategory() {
        return Category;
    }

    public void setCategory(String Category) {
        this.Category = Category;
    }

    public List<OrderItem> getOrderitems() {
        return orderitems;
    }

    public void addOrderitem(Orderitem orderitem) {
        this.orderitems.add(orderitem);
    }

}