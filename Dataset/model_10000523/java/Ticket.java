





import java.util.List;
import java.util.ArrayList;

public class Ticket  {

    private String passengername;
    private String destination;
    private String ticketid;
    private int price;
    private String source;
    private String flightname;





    private List<User> users;


    public Ticket(
        String passengername,        String destination,        String ticketid,        int price,        String source,        String flightname    ) {
        this.passengername = passengername;
        this.destination = destination;
        this.ticketid = ticketid;
        this.price = price;
        this.source = source;
        this.flightname = flightname;
        this.users = new ArrayList<>();
    }

    public Ticket(
        String passengername,        String destination,        String ticketid,        int price,        String source,        String flightname        ArrayList<User> users    ) {
        this.passengername = passengername;
        this.destination = destination;
        this.ticketid = ticketid;
        this.price = price;
        this.source = source;
        this.flightname = flightname;
        this.users = users;
    }

    public String getPassengername() {
        return passengername;
    }

    public void setPassengername(String passengername) {
        this.passengername = passengername;
    }
    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }
    public String getTicketid() {
        return ticketid;
    }

    public void setTicketid(String ticketid) {
        this.ticketid = ticketid;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getFlightname() {
        return flightname;
    }

    public void setFlightname(String flightname) {
        this.flightname = flightname;
    }

    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}