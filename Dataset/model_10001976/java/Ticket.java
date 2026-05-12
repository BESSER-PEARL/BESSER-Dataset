





import java.util.List;
import java.util.ArrayList;

public class Ticket  {

    private String DateTime;
    private String TicketID;
    private String TicketType;
    private String Price;
    private String Gate;





    private List<Flight> flights;


    public Ticket(
        String DateTime,        String TicketID,        String TicketType,        String Price,        String Gate    ) {
        this.DateTime = DateTime;
        this.TicketID = TicketID;
        this.TicketType = TicketType;
        this.Price = Price;
        this.Gate = Gate;
        this.flights = new ArrayList<>();
    }

    public Ticket(
        String DateTime,        String TicketID,        String TicketType,        String Price,        String Gate        ArrayList<Flight> flights    ) {
        this.DateTime = DateTime;
        this.TicketID = TicketID;
        this.TicketType = TicketType;
        this.Price = Price;
        this.Gate = Gate;
        this.flights = flights;
    }

    public String getDatetime() {
        return DateTime;
    }

    public void setDatetime(String DateTime) {
        this.DateTime = DateTime;
    }
    public String getTicketid() {
        return TicketID;
    }

    public void setTicketid(String TicketID) {
        this.TicketID = TicketID;
    }
    public String getTickettype() {
        return TicketType;
    }

    public void setTickettype(String TicketType) {
        this.TicketType = TicketType;
    }
    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }
    public String getGate() {
        return Gate;
    }

    public void setGate(String Gate) {
        this.Gate = Gate;
    }

    public List<Flight> getFlights() {
        return flights;
    }

    public void addFlight(Flight flight) {
        this.flights.add(flight);
    }

}