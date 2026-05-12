




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private String startTime;
    private String Restaurant_id;
    private LocalDate date;
    private String reservedTables;
    private int booking_id;
    private String customer_id;
    private String endTime;
    private int person;





    private Restaurant_Reservation_System restaurant_reservation_system;


    public Booking(
        String startTime,        String Restaurant_id,        LocalDate date,        String reservedTables,        int booking_id,        String customer_id,        String endTime,        int person    ) {
        this.startTime = startTime;
        this.Restaurant_id = Restaurant_id;
        this.date = date;
        this.reservedTables = reservedTables;
        this.booking_id = booking_id;
        this.customer_id = customer_id;
        this.endTime = endTime;
        this.person = person;
    }


    public String getStarttime() {
        return startTime;
    }

    public void setStarttime(String startTime) {
        this.startTime = startTime;
    }
    public String getRestaurant_id() {
        return Restaurant_id;
    }

    public void setRestaurant_id(String Restaurant_id) {
        this.Restaurant_id = Restaurant_id;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getReservedtables() {
        return reservedTables;
    }

    public void setReservedtables(String reservedTables) {
        this.reservedTables = reservedTables;
    }
    public int getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(int booking_id) {
        this.booking_id = booking_id;
    }
    public String getCustomer_id() {
        return customer_id;
    }

    public void setCustomer_id(String customer_id) {
        this.customer_id = customer_id;
    }
    public String getEndtime() {
        return endTime;
    }

    public void setEndtime(String endTime) {
        this.endTime = endTime;
    }
    public int getPerson() {
        return person;
    }

    public void setPerson(int person) {
        this.person = person;
    }

    public Restaurant_Reservation_System getRestaurant_reservation_system() {
        return restaurant_reservation_system;
    }

    public void setRestaurant_reservation_system(Restaurant_Reservation_System restaurant_reservation_system) {
        this.restaurant_reservation_system = restaurant_reservation_system;
    }

}