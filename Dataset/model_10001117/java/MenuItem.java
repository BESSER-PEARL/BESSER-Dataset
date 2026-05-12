





import java.util.List;
import java.util.ArrayList;

public class MenuItem  {

    private String Description;





    private List<Restaurant> restaurants;




    private List<FoodItem> fooditems;




    private List<Order> orders;


    public MenuItem(
        String Description    ) {
        this.Description = Description;
        this.restaurants = new ArrayList<>();
        this.fooditems = new ArrayList<>();
        this.orders = new ArrayList<>();
    }

    public MenuItem(
        String Description        ArrayList<Restaurant> restaurants,        ArrayList<FoodItem> fooditems,        ArrayList<Order> orders    ) {
        this.Description = Description;
        this.restaurants = restaurants;
        this.fooditems = fooditems;
        this.orders = orders;
    }

    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }

    public List<Restaurant> getRestaurants() {
        return restaurants;
    }

    public void addRestaurant(Restaurant restaurant) {
        this.restaurants.add(restaurant);
    }
    public List<FoodItem> getFooditems() {
        return fooditems;
    }

    public void addFooditem(Fooditem fooditem) {
        this.fooditems.add(fooditem);
    }
    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}