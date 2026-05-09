





import java.util.List;
import java.util.ArrayList;

public class restaurant_Restaurant  {






    private List<restaurant_Booking> restaurant_bookings;




    private List<restaurant_Waiter> restaurant_waiters;




    private List<restaurant_Table> restaurant_tables;


    public restaurant_Restaurant(
    ) {
        this.restaurant_bookings = new ArrayList<>();
        this.restaurant_waiters = new ArrayList<>();
        this.restaurant_tables = new ArrayList<>();
    }

    public restaurant_Restaurant(
        ArrayList<restaurant_Booking> restaurant_bookings,        ArrayList<restaurant_Waiter> restaurant_waiters,        ArrayList<restaurant_Table> restaurant_tables    ) {
        this.restaurant_bookings = restaurant_bookings;
        this.restaurant_waiters = restaurant_waiters;
        this.restaurant_tables = restaurant_tables;
    }


    public List<restaurant_Booking> getRestaurant_bookings() {
        return restaurant_bookings;
    }

    public void addRestaurant_booking(Restaurant_booking restaurant_booking) {
        this.restaurant_bookings.add(restaurant_booking);
    }
    public List<restaurant_Waiter> getRestaurant_waiters() {
        return restaurant_waiters;
    }

    public void addRestaurant_waiter(Restaurant_waiter restaurant_waiter) {
        this.restaurant_waiters.add(restaurant_waiter);
    }
    public List<restaurant_Table> getRestaurant_tables() {
        return restaurant_tables;
    }

    public void addRestaurant_table(Restaurant_table restaurant_table) {
        this.restaurant_tables.add(restaurant_table);
    }

}