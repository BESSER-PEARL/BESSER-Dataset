





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private None Restaurant;
    private None ItemList;
    private None Customer;





    private List<MenuItem> menuitems;


    public Order(
        None Restaurant,        None ItemList,        None Customer    ) {
        this.Restaurant = Restaurant;
        this.ItemList = ItemList;
        this.Customer = Customer;
        this.menuitems = new ArrayList<>();
    }

    public Order(
        None Restaurant,        None ItemList,        None Customer        ArrayList<MenuItem> menuitems    ) {
        this.Restaurant = Restaurant;
        this.ItemList = ItemList;
        this.Customer = Customer;
        this.menuitems = menuitems;
    }

    public None getRestaurant() {
        return Restaurant;
    }

    public void setRestaurant(None Restaurant) {
        this.Restaurant = Restaurant;
    }
    public None getItemlist() {
        return ItemList;
    }

    public void setItemlist(None ItemList) {
        this.ItemList = ItemList;
    }
    public None getCustomer() {
        return Customer;
    }

    public void setCustomer(None Customer) {
        this.Customer = Customer;
    }

    public List<MenuItem> getMenuitems() {
        return menuitems;
    }

    public void addMenuitem(Menuitem menuitem) {
        this.menuitems.add(menuitem);
    }

}