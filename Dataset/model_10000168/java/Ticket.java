




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Ticket  {

    private String source;
    private String destination;
    private String flight_name;
    private String flight_No;
    private int time;
    private LocalDate dateofjourney;





    private Customer customer;




    private Agent agent;




    private Booking_counter booking_counter;


    public Ticket(
        String source,        String destination,        String flight_name,        String flight_No,        int time,        LocalDate dateofjourney    ) {
        this.source = source;
        this.destination = destination;
        this.flight_name = flight_name;
        this.flight_No = flight_No;
        this.time = time;
        this.dateofjourney = dateofjourney;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }
    public String getFlight_name() {
        return flight_name;
    }

    public void setFlight_name(String flight_name) {
        this.flight_name = flight_name;
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
    public LocalDate getDateofjourney() {
        return dateofjourney;
    }

    public void setDateofjourney(LocalDate dateofjourney) {
        this.dateofjourney = dateofjourney;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public Agent getAgent() {
        return agent;
    }

    public void setAgent(Agent agent) {
        this.agent = agent;
    }
    public Booking_counter getBooking_counter() {
        return booking_counter;
    }

    public void setBooking_counter(Booking_counter booking_counter) {
        this.booking_counter = booking_counter;
    }

}