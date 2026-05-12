





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private None ItemList;
    private None Customer;
    private None Restaurant;





    private Restaurant restaurant;




    private List<MenuItem> menuitems;


    public Order(
        None ItemList,        None Customer,        None Restaurant    ) {
        this.ItemList = ItemList;
        this.Customer = Customer;
        this.Restaurant = Restaurant;
        this.menuitems = new ArrayList<>();
    }

    public Order(
        None ItemList,        None Customer,        None Restaurant        ArrayList<MenuItem> menuitems    ) {
        this.ItemList = ItemList;
        this.Customer = Customer;
        this.Restaurant = Restaurant;
        this.menuitems = menuitems;
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
    public None getRestaurant() {
        return Restaurant;
    }

    public void setRestaurant(None Restaurant) {
        this.Restaurant = Restaurant;
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