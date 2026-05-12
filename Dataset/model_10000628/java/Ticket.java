





import java.util.List;
import java.util.ArrayList;

public class Ticket  {

    private String Booking_Class;
    private None Clients;
    private String Id;
    private String Seat;





    private Client client;




    private Booking booking;


    public Ticket(
        String Booking_Class,        None Clients,        String Id,        String Seat    ) {
        this.Booking_Class = Booking_Class;
        this.Clients = Clients;
        this.Id = Id;
        this.Seat = Seat;
    }


    public String getBooking_class() {
        return Booking_Class;
    }

    public void setBooking_class(String Booking_Class) {
        this.Booking_Class = Booking_Class;
    }
    public None getClients() {
        return Clients;
    }

    public void setClients(None Clients) {
        this.Clients = Clients;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public String getSeat() {
        return Seat;
    }

    public void setSeat(String Seat) {
        this.Seat = Seat;
    }

    public Client getClient() {
        return client;
    }

    public void setClient(Client client) {
        this.client = client;
    }
    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }

}