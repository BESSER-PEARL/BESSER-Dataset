





import java.util.List;
import java.util.ArrayList;

public class Flight  {

    private String Company;
    private String Destination;
    private int Max_Passangers;
    private String Origin;
    private String Time;
    private String Id;





    private List<Ticket> tickets;


    public Flight(
        String Company,        String Destination,        int Max_Passangers,        String Origin,        String Time,        String Id    ) {
        this.Company = Company;
        this.Destination = Destination;
        this.Max_Passangers = Max_Passangers;
        this.Origin = Origin;
        this.Time = Time;
        this.Id = Id;
        this.tickets = new ArrayList<>();
    }

    public Flight(
        String Company,        String Destination,        int Max_Passangers,        String Origin,        String Time,        String Id        ArrayList<Ticket> tickets    ) {
        this.Company = Company;
        this.Destination = Destination;
        this.Max_Passangers = Max_Passangers;
        this.Origin = Origin;
        this.Time = Time;
        this.Id = Id;
        this.tickets = tickets;
    }

    public String getCompany() {
        return Company;
    }

    public void setCompany(String Company) {
        this.Company = Company;
    }
    public String getDestination() {
        return Destination;
    }

    public void setDestination(String Destination) {
        this.Destination = Destination;
    }
    public int getMax_passangers() {
        return Max_Passangers;
    }

    public void setMax_passangers(int Max_Passangers) {
        this.Max_Passangers = Max_Passangers;
    }
    public String getOrigin() {
        return Origin;
    }

    public void setOrigin(String Origin) {
        this.Origin = Origin;
    }
    public String getTime() {
        return Time;
    }

    public void setTime(String Time) {
        this.Time = Time;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }

    public List<Ticket> getTickets() {
        return tickets;
    }

    public void addTicket(Ticket ticket) {
        this.tickets.add(ticket);
    }

}