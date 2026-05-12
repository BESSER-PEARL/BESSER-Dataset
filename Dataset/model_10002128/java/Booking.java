





import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private String Time;
    private String Destination;
    private String Luggage;
    private String Id;
    private String Origin;
    private None Tickets;





    private Client client;


    public Booking(
        String Time,        String Destination,        String Luggage,        String Id,        String Origin,        None Tickets    ) {
        this.Time = Time;
        this.Destination = Destination;
        this.Luggage = Luggage;
        this.Id = Id;
        this.Origin = Origin;
        this.Tickets = Tickets;
    }


    public String getTime() {
        return Time;
    }

    public void setTime(String Time) {
        this.Time = Time;
    }
    public String getDestination() {
        return Destination;
    }

    public void setDestination(String Destination) {
        this.Destination = Destination;
    }
    public String getLuggage() {
        return Luggage;
    }

    public void setLuggage(String Luggage) {
        this.Luggage = Luggage;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public String getOrigin() {
        return Origin;
    }

    public void setOrigin(String Origin) {
        this.Origin = Origin;
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