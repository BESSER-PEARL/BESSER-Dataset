





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private None ItemList;
    private None Restaurant;
    private None Customer;





    private List<MenuItem> menuitems;




    private Restaurant restaurant;


    public Order(
        None ItemList,        None Restaurant,        None Customer    ) {
        this.ItemList = ItemList;
        this.Restaurant = Restaurant;
        this.Customer = Customer;
        this.menuitems = new ArrayList<>();
    }

    public Order(
        None ItemList,        None Restaurant,        None Customer        ArrayList<MenuItem> menuitems    ) {
        this.ItemList = ItemList;
        this.Restaurant = Restaurant;
        this.Customer = Customer;
        this.menuitems = menuitems;
    }

    public None getItemlist() {
        return ItemList;
    }

    public void setItemlist(None ItemList) {
        this.ItemList = ItemList;
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

    public List<MenuItem> getMenuitems() {
        return menuitems;
    }

    public void addMenuitem(Menuitem menuitem) {
        this.menuitems.add(menuitem);
    }
    public Restaurant getRestaurant() {
        return restaurant;
    }

    public void setRestaurant(Restaurant restaurant) {
        this.restaurant = restaurant;
    }

}