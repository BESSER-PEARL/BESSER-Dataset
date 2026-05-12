





import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private String Destination;
    private String Luggage;
    private String Time;
    private None Tickets;
    private String Origin;
    private String Id;





    private Client client;


    public Booking(
        String Destination,        String Luggage,        String Time,        None Tickets,        String Origin,        String Id    ) {
        this.Destination = Destination;
        this.Luggage = Luggage;
        this.Time = Time;
        this.Tickets = Tickets;
        this.Origin = Origin;
        this.Id = Id;
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
    public String getTime() {
        return Time;
    }

    public void setTime(String Time) {
        this.Time = Time;
    }
    public None getTickets() {
        return Tickets;
    }

    public void setTickets(None Tickets) {
        this.Tickets = Tickets;
    }
    public String getOrigin() {
        return Origin;
    }

    public void setOrigin(String Origin) {
        this.Origin = Origin;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }

    public Client getClient() {
        return client;
    }

    public void setClient(Client client) {
        this.client = client;
    }

}