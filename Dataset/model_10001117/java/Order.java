





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private None Customer;
    private None ItemList;
    private None Restaurant;



    public Order(
        None Customer,        None ItemList,        None Restaurant    ) {
        this.Customer = Customer;
        this.ItemList = ItemList;
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
    public None getRestaurant() {
        return Restaurant;
    }

    public void setRestaurant(None Restaurant) {
        this.Restaurant = Restaurant;
    }


}