





import java.util.List;
import java.util.ArrayList;

public class Restaurant  {

    private int PostCode;
    private String Address;
    private None Menu;
    private String Name;





    private List<RestaurantController> restaurantcontrollers;




    private List<Order> orders;


    public Restaurant(
        int PostCode,        String Address,        None Menu,        String Name    ) {
        this.PostCode = PostCode;
        this.Address = Address;
        this.Menu = Menu;
        this.Name = Name;
        this.restaurantcontrollers = new ArrayList<>();
        this.orders = new ArrayList<>();
    }

    public Restaurant(
        int PostCode,        String Address,        None Menu,        String Name        ArrayList<RestaurantController> restaurantcontrollers,        ArrayList<Order> orders    ) {
        this.PostCode = PostCode;
        this.Address = Address;
        this.Menu = Menu;
        this.Name = Name;
        this.restaurantcontrollers = restaurantcontrollers;
        this.orders = orders;
    }

    public int getPostcode() {
        return PostCode;
    }

    public void setPostcode(int PostCode) {
        this.PostCode = PostCode;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public None getMenu() {
        return Menu;
    }

    public void setMenu(None Menu) {
        this.Menu = Menu;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
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

}