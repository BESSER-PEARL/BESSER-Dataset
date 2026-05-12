





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private None Customer;
    private None Restaurant;
    private None ItemList;





    private List<MenuItem> menuitems;




    private Restaurant restaurant;




    private List<OrderController> ordercontrollers;


    public Order(
        None Customer,        None Restaurant,        None ItemList    ) {
        this.Customer = Customer;
        this.Restaurant = Restaurant;
        this.ItemList = ItemList;
        this.menuitems = new ArrayList<>();
        this.ordercontrollers = new ArrayList<>();
    }

    public Order(
        None Customer,        None Restaurant,        None ItemList        ArrayList<MenuItem> menuitems,        ArrayList<OrderController> ordercontrollers    ) {
        this.Customer = Customer;
        this.Restaurant = Restaurant;
        this.ItemList = ItemList;
        this.menuitems = menuitems;
        this.ordercontrollers = ordercontrollers;
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
    public None getItemlist() {
        return ItemList;
    }

    public void setItemlist(None ItemList) {
        this.ItemList = ItemList;
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
    public List<OrderController> getOrdercontrollers() {
        return ordercontrollers;
    }

    public void addOrdercontroller(Ordercontroller ordercontroller) {
        this.ordercontrollers.add(ordercontroller);
    }

}