





import java.util.List;
import java.util.ArrayList;

public class Ticket  {

    private String class;
    private int date;
    private None age;
    private None arrival;
    private None Flightnumber;
    private None destination;
    private int Ticketnumber;
    private int price;
    private None username;





    private Flight flight;




    private User user;


    public Ticket(
        String class,        int date,        None age,        None arrival,        None Flightnumber,        None destination,        int Ticketnumber,        int price,        None username    ) {
        this.class = class;
        this.date = date;
        this.age = age;
        this.arrival = arrival;
        this.Flightnumber = Flightnumber;
        this.destination = destination;
        this.Ticketnumber = Ticketnumber;
        this.price = price;
        this.username = username;
    }


    public String getClass() {
        return class;
    }

    public void setClass(String class) {
        this.class = class;
    }
    public int getDate() {
        return date;
    }

    public void setDate(int date) {
        this.date = date;
    }
    public None getAge() {
        return age;
    }

    public void setAge(None age) {
        this.age = age;
    }
    public None getArrival() {
        return arrival;
    }

    public void setArrival(None arrival) {
        this.arrival = arrival;
    }
    public None getFlightnumber() {
        return Flightnumber;
    }

    public void setFlightnumber(None Flightnumber) {
        this.Flightnumber = Flightnumber;
    }
    public None getDestination() {
        return destination;
    }

    public void setDestination(None destination) {
        this.destination = destination;
    }
    public int getTicketnumber() {
        return Ticketnumber;
    }

    public void setTicketnumber(int Ticketnumber) {
        this.Ticketnumber = Ticketnumber;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public None getUsername() {
        return username;
    }

    public void setUsername(None username) {
        this.username = username;
    }

    public Flight getFlight() {
        return flight;
    }

    public void setFlight(Flight flight) {
        this.flight = flight;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}