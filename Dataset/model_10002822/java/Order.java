





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private None Restaurant;
    private None Customer;
    private None ItemList;





    private Restaurant restaurant;




    private List<MenuItem> menuitems;


    public Order(
        None Restaurant,        None Customer,        None ItemList    ) {
        this.Restaurant = Restaurant;
        this.Customer = Customer;
        this.ItemList = ItemList;
        this.menuitems = new ArrayList<>();
    }

    public Order(
        None Restaurant,        None Customer,        None ItemList        ArrayList<MenuItem> menuitems    ) {
        this.Restaurant = Restaurant;
        this.Customer = Customer;
        this.ItemList = ItemList;
        this.menuitems = menuitems;
    }

    public None getRestaurant() {
        return Restaurant;
    }

    public void setRestaurant(None Restaurant) {
        this.Restaurant = Restaurant;
    }
    public None getCustomer() {
        return Customer;
    }

    public void setCustomer(None Customer) {
        this.Customer = Customer;
    }
    public None getItemlist() {
        return ItemList;
    }

    public void setItemlist(None ItemList) {
        this.ItemList = ItemList;
    }

    public Restaurant getRestaurant() {
        return restaurant;
    }

    public void setRestaurant(Restaurant restaurant) {
        this.restaurant = restaurant;
    }
    public List<MenuItem> getMenuitems() {
        return menuitems;
    }

    public void addMenuitem(Menuitem menuitem) {
        this.menuitems.add(menuitem);
    }

}