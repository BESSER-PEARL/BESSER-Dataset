





import java.util.List;
import java.util.ArrayList;

public class Menu  {

    private int Availability;
    private String MenuItem;
    private float Price;
    private String Category;





    private List<OrderList> orderlists;


    public Menu(
        int Availability,        String MenuItem,        float Price,        String Category    ) {
        this.Availability = Availability;
        this.MenuItem = MenuItem;
        this.Price = Price;
        this.Category = Category;
        this.orderlists = new ArrayList<>();
    }

    public Menu(
        int Availability,        String MenuItem,        float Price,        String Category        ArrayList<OrderList> orderlists    ) {
        this.Availability = Availability;
        this.MenuItem = MenuItem;
        this.Price = Price;
        this.Category = Category;
        this.orderlists = orderlists;
    }

    public int getAvailability() {
        return Availability;
    }

    public void setAvailability(int Availability) {
        this.Availability = Availability;
    }
    public String getMenuitem() {
        return MenuItem;
    }

    public void setMenuitem(String MenuItem) {
        this.MenuItem = MenuItem;
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

    public List<OrderList> getOrderlists() {
        return orderlists;
    }

    public void addOrderlist(Orderlist orderlist) {
        this.orderlists.add(orderlist);
    }

}