





import java.util.List;
import java.util.ArrayList;

public class Menu  {

    private String MenuItem;





    private List<Items> itemss;




    private Order order;


    public Menu(
        String MenuItem    ) {
        this.MenuItem = MenuItem;
        this.itemss = new ArrayList<>();
    }

    public Menu(
        String MenuItem        ArrayList<Items> itemss    ) {
        this.MenuItem = MenuItem;
        this.itemss = itemss;
    }

    public String getMenuitem() {
        return MenuItem;
    }

    public void setMenuitem(String MenuItem) {
        this.MenuItem = MenuItem;
    }

    public List<Items> getItemss() {
        return itemss;
    }

    public void addItems(Items items) {
        this.itemss.add(items);
    }
    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}