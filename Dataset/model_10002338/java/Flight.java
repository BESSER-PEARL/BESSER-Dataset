





import java.util.List;
import java.util.ArrayList;

public class Flight  {

    private String Time;
    private String Company;
    private String Origin;
    private String Destination;
    private String Id;
    private int Max_Passangers;





    private List<Ticket> tickets;


    public Flight(
        String Time,        String Company,        String Origin,        String Destination,        String Id,        int Max_Passangers    ) {
        this.Time = Time;
        this.Company = Company;
        this.Origin = Origin;
        this.Destination = Destination;
        this.Id = Id;
        this.Max_Passangers = Max_Passangers;
        this.tickets = new ArrayList<>();
    }

    public Flight(
        String Time,        String Company,        String Origin,        String Destination,        String Id,        int Max_Passangers        ArrayList<Ticket> tickets    ) {
        this.Time = Time;
        this.Company = Company;
        this.Origin = Origin;
        this.Destination = Destination;
        this.Id = Id;
        this.Max_Passangers = Max_Passangers;
        this.tickets = tickets;
    }

    public String getTime() {
        return Time;
    }

    public void setTime(String Time) {
        this.Time = Time;
    }
    public String getCompany() {
        return Company;
    }

    public void setCompany(String Company) {
        this.Company = Company;
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
    public int getMax_passangers() {
        return Max_Passangers;
    }

    public void setMax_passangers(int Max_Passangers) {
        this.Max_Passangers = Max_Passangers;
    }

    public List<Ticket> getTickets() {
        return tickets;
    }

    public void addTicket(Ticket ticket) {
        this.tickets.add(ticket);
    }

}