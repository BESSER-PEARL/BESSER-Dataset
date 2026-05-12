





import java.util.List;
import java.util.ArrayList;

public class Flight  {

    private int price;
    private String arrival;
    private int time;
    private int Flightnumber;
    private int date;
    private String destination;
    private String Flightname;





    private User user;


    public Flight(
        int price,        String arrival,        int time,        int Flightnumber,        int date,        String destination,        String Flightname    ) {
        this.price = price;
        this.arrival = arrival;
        this.time = time;
        this.Flightnumber = Flightnumber;
        this.date = date;
        this.destination = destination;
        this.Flightname = Flightname;
    }


    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getArrival() {
        return arrival;
    }

    public void setArrival(String arrival) {
        this.arrival = arrival;
    }
    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }
    public int getFlightnumber() {
        return Flightnumber;
    }

    public void setFlightnumber(int Flightnumber) {
        this.Flightnumber = Flightnumber;
    }
    public int getDate() {
        return date;
    }

    public void setDate(int date) {
        this.date = date;
    }
    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }
    public String getFlightname() {
        return Flightname;
    }

    public void setFlightname(String Flightname) {
        this.Flightname = Flightname;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}