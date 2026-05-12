





import java.util.List;
import java.util.ArrayList;

public class Restaurant  {

    private String Address;
    private int PostCode;
    private String Name;
    private None Menu;





    private List<RestaurantController> restaurantcontrollers;




    private List<Order> orders;




    private List<MenuItem> menuitems;


    public Restaurant(
        String Address,        int PostCode,        String Name,        None Menu    ) {
        this.Address = Address;
        this.PostCode = PostCode;
        this.Name = Name;
        this.Menu = Menu;
        this.restaurantcontrollers = new ArrayList<>();
        this.orders = new ArrayList<>();
        this.menuitems = new ArrayList<>();
    }

    public Restaurant(
        String Address,        int PostCode,        String Name,        None Menu        ArrayList<RestaurantController> restaurantcontrollers,        ArrayList<Order> orders,        ArrayList<MenuItem> menuitems    ) {
        this.Address = Address;
        this.PostCode = PostCode;
        this.Name = Name;
        this.Menu = Menu;
        this.restaurantcontrollers = restaurantcontrollers;
        this.orders = orders;
        this.menuitems = menuitems;
    }

    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getPostcode() {
        return PostCode;
    }

    public void setPostcode(int PostCode) {
        this.PostCode = PostCode;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public None getMenu() {
        return Menu;
    }

    public void setMenu(None Menu) {
        this.Menu = Menu;
    }

    public List<RestaurantController> getRestaurantcontrollers() {
        return restaurantcontrollers;
    }

    public void addRestaurantcontroller(Restaurantcontroller restaurantcontroller) {
        this.restaurantcontrollers.add(restaurantcontroller);
    }
    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }
    public List<MenuItem> getMenuitems() {
        return menuitems;
    }

    public void addMenuitem(Menuitem menuitem) {
        this.menuitems.add(menuitem);
    }

}