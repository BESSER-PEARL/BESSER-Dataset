





import java.util.List;
import java.util.ArrayList;

public class RestaurantController  {

    private None Restaurant;





    private List<Restaurant> restaurants;


    public RestaurantController(
        None Restaurant    ) {
        this.Restaurant = Restaurant;
        this.restaurants = new ArrayList<>();
    }

    public RestaurantController(
        None Restaurant        ArrayList<Restaurant> restaurants    ) {
        this.Restaurant = Restaurant;
        this.restaurants = restaurants;
    }

    public None getRestaurant() {
        return Restaurant;
    }

    public void setRestaurant(None Restaurant) {
        this.Restaurant = Restaurant;
    }

    public List<Restaurant> getRestaurants() {
        return restaurants;
    }

    public void addRestaurant(Restaurant restaurant) {
        this.restaurants.add(restaurant);
    }

}