





import java.util.List;
import java.util.ArrayList;

public class Ticket  {

    private String flightname;
    private String ticketid;
    private int price;
    private String passengername;
    private String source;
    private String destination;





    private List<User> users;


    public Ticket(
        String flightname,        String ticketid,        int price,        String passengername,        String source,        String destination    ) {
        this.flightname = flightname;
        this.ticketid = ticketid;
        this.price = price;
        this.passengername = passengername;
        this.source = source;
        this.destination = destination;
        this.users = new ArrayList<>();
    }

    public Ticket(
        String flightname,        String ticketid,        int price,        String passengername,        String source,        String destination        ArrayList<User> users    ) {
        this.flightname = flightname;
        this.ticketid = ticketid;
        this.price = price;
        this.passengername = passengername;
        this.source = source;
        this.destination = destination;
        this.users = users;
    }

    public String getFlightname() {
        return flightname;
    }

    public void setFlightname(String flightname) {
        this.flightname = flightname;
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
    public String getPassengername() {
        return passengername;
    }

    public void setPassengername(String passengername) {
        this.passengername = passengername;
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

    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}