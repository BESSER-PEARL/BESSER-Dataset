





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String user_id;
    private String name;
    private String type;





    private Restaurant_Reservation_System restaurant_reservation_system;


    public Staff(
        String user_id,        String name,        String type    ) {
        this.user_id = user_id;
        this.name = name;
        this.type = type;
    }


    public String getUser_id() {
        return user_id;
    }

    public void setUser_id(String user_id) {
        this.user_id = user_id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Restaurant_Reservation_System getRestaurant_reservation_system() {
        return restaurant_reservation_system;
    }

    public void setRestaurant_reservation_system(Restaurant_Reservation_System restaurant_reservation_system) {
        this.restaurant_reservation_system = restaurant_reservation_system;
    }

}