





import java.util.List;
import java.util.ArrayList;

public class CoachBus_Passenger  {

    private String idCard;
    private String name;
    private int age;





    private List<CoachBus_Ticket> coachbus_tickets;




    private List<CoachBus_Trip> coachbus_trips;




    private CoachBus_Ticket coachbus_ticket;




    private CoachBus_Trip coachbus_trip;


    public CoachBus_Passenger(
        String idCard,        String name,        int age    ) {
        this.idCard = idCard;
        this.name = name;
        this.age = age;
        this.coachbus_tickets = new ArrayList<>();
        this.coachbus_trips = new ArrayList<>();
    }

    public CoachBus_Passenger(
        String idCard,        String name,        int age        ArrayList<CoachBus_Ticket> coachbus_tickets,        ArrayList<CoachBus_Trip> coachbus_trips    ) {
        this.idCard = idCard;
        this.name = name;
        this.age = age;
        this.coachbus_tickets = coachbus_tickets;
        this.coachbus_trips = coachbus_trips;
    }

    public String getIdcard() {
        return idCard;
    }

    public void setIdcard(String idCard) {
        this.idCard = idCard;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public List<CoachBus_Ticket> getCoachbus_tickets() {
        return coachbus_tickets;
    }

    public void addCoachbus_ticket(Coachbus_ticket coachbus_ticket) {
        this.coachbus_tickets.add(coachbus_ticket);
    }
    public List<CoachBus_Trip> getCoachbus_trips() {
        return coachbus_trips;
    }

    public void addCoachbus_trip(Coachbus_trip coachbus_trip) {
        this.coachbus_trips.add(coachbus_trip);
    }
    public CoachBus_Ticket getCoachbus_ticket() {
        return coachbus_ticket;
    }

    public void setCoachbus_ticket(CoachBus_Ticket coachbus_ticket) {
        this.coachbus_ticket = coachbus_ticket;
    }
    public CoachBus_Trip getCoachbus_trip() {
        return coachbus_trip;
    }

    public void setCoachbus_trip(CoachBus_Trip coachbus_trip) {
        this.coachbus_trip = coachbus_trip;
    }

}