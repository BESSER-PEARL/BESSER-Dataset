





import java.util.List;
import java.util.ArrayList;

public class MenuItem  {

    private String Description;





    private List<Restaurant> restaurants;


    public MenuItem(
        String Description    ) {
        this.Description = Description;
        this.restaurants = new ArrayList<>();
    }

    public MenuItem(
        String Description        ArrayList<Restaurant> restaurants    ) {
        this.Description = Description;
        this.restaurants = restaurants;
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

}