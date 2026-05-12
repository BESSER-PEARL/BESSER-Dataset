





import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private String Origin;
    private String Destination;
    private String Id;
    private String Time;
    private String Luggage;
    private None Tickets;





    private Client client;


    public Booking(
        String Origin,        String Destination,        String Id,        String Time,        String Luggage,        None Tickets    ) {
        this.Origin = Origin;
        this.Destination = Destination;
        this.Id = Id;
        this.Time = Time;
        this.Luggage = Luggage;
        this.Tickets = Tickets;
    }


    public String getOrigin() {
        return Origin;
    }

    public void setOrigin(String Origin) {
        this.Origin = Origin;
    }
    public String getDestination() {
        return Destination;
    }

    public void setDestination(String Destination) {
        this.Destination = Destination;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public String getTime() {
        return Time;
    }

    public void setTime(String Time) {
        this.Time = Time;
    }
    public String getLuggage() {
        return Luggage;
    }

    public void setLuggage(String Luggage) {
        this.Luggage = Luggage;
    }
    public None getTickets() {
        return Tickets;
    }

    public void setTickets(None Tickets) {
        this.Tickets = Tickets;
    }

    public Client getClient() {
        return client;
    }

    public void setClient(Client client) {
        this.client = client;
    }

}