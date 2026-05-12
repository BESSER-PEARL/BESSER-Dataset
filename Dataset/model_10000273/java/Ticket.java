




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Ticket  {

    private LocalDate dateofjourney;
    private String destination;
    private String flight_No;
    private int time;
    private String source;
    private String flight_name;





    private Customer customer;




    private Booking_counter booking_counter;




    private Agent agent;


    public Ticket(
        LocalDate dateofjourney,        String destination,        String flight_No,        int time,        String source,        String flight_name    ) {
        this.dateofjourney = dateofjourney;
        this.destination = destination;
        this.flight_No = flight_No;
        this.time = time;
        this.source = source;
        this.flight_name = flight_name;
    }


    public LocalDate getDateofjourney() {
        return dateofjourney;
    }

    public void setDateofjourney(LocalDate dateofjourney) {
        this.dateofjourney = dateofjourney;
    }
    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }
    public String getFlight_no() {
        return flight_No;
    }

    public void setFlight_no(String flight_No) {
        this.flight_No = flight_No;
    }
    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getFlight_name() {
        return flight_name;
    }

    public void setFlight_name(String flight_name) {
        this.flight_name = flight_name;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public Booking_counter getBooking_counter() {
        return booking_counter;
    }

    public void setBooking_counter(Booking_counter booking_counter) {
        this.booking_counter = booking_counter;
    }
    public Agent getAgent() {
        return agent;
    }

    public void setAgent(Agent agent) {
        this.agent = agent;
    }

}