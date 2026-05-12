





import java.util.List;
import java.util.ArrayList;

public class Reservation_status  {

    private String report_id;
    private None reservation;





    private Restaurant_Reservation_System restaurant_reservation_system;


    public Reservation_status(
        String report_id,        None reservation    ) {
        this.report_id = report_id;
        this.reservation = reservation;
    }


    public String getReport_id() {
        return report_id;
    }

    public void setReport_id(String report_id) {
        this.report_id = report_id;
    }
    public None getReservation() {
        return reservation;
    }

    public void setReservation(None reservation) {
        this.reservation = reservation;
    }

    public Restaurant_Reservation_System getRestaurant_reservation_system() {
        return restaurant_reservation_system;
    }

    public void setRestaurant_reservation_system(Restaurant_Reservation_System restaurant_reservation_system) {
        this.restaurant_reservation_system = restaurant_reservation_system;
    }

}