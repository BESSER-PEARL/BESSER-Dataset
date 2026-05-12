





import java.util.List;
import java.util.ArrayList;

public class CoachBusWithEDataType_Passenger  {

    private String name;
    private int age;
    private String sex;
    private String idCard;





    private List<CoachBusWithEDataType_Trip> coachbuswithedatatype_trips;




    private CoachBusWithEDataType_Trip coachbuswithedatatype_trip;




    private List<CoachBusWithEDataType_Ticket> coachbuswithedatatype_tickets;




    private CoachBusWithEDataType_Ticket coachbuswithedatatype_ticket;


    public CoachBusWithEDataType_Passenger(
        String name,        int age,        String sex,        String idCard    ) {
        this.name = name;
        this.age = age;
        this.sex = sex;
        this.idCard = idCard;
        this.coachbuswithedatatype_trips = new ArrayList<>();
        this.coachbuswithedatatype_tickets = new ArrayList<>();
    }

    public CoachBusWithEDataType_Passenger(
        String name,        int age,        String sex,        String idCard        ArrayList<CoachBusWithEDataType_Trip> coachbuswithedatatype_trips,        ArrayList<CoachBusWithEDataType_Ticket> coachbuswithedatatype_tickets    ) {
        this.name = name;
        this.age = age;
        this.sex = sex;
        this.idCard = idCard;
        this.coachbuswithedatatype_trips = coachbuswithedatatype_trips;
        this.coachbuswithedatatype_tickets = coachbuswithedatatype_tickets;
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
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
    public String getIdcard() {
        return idCard;
    }

    public void setIdcard(String idCard) {
        this.idCard = idCard;
    }

    public List<CoachBusWithEDataType_Trip> getCoachbuswithedatatype_trips() {
        return coachbuswithedatatype_trips;
    }

    public void addCoachbuswithedatatype_trip(Coachbuswithedatatype_trip coachbuswithedatatype_trip) {
        this.coachbuswithedatatype_trips.add(coachbuswithedatatype_trip);
    }
    public CoachBusWithEDataType_Trip getCoachbuswithedatatype_trip() {
        return coachbuswithedatatype_trip;
    }

    public void setCoachbuswithedatatype_trip(CoachBusWithEDataType_Trip coachbuswithedatatype_trip) {
        this.coachbuswithedatatype_trip = coachbuswithedatatype_trip;
    }
    public List<CoachBusWithEDataType_Ticket> getCoachbuswithedatatype_tickets() {
        return coachbuswithedatatype_tickets;
    }

    public void addCoachbuswithedatatype_ticket(Coachbuswithedatatype_ticket coachbuswithedatatype_ticket) {
        this.coachbuswithedatatype_tickets.add(coachbuswithedatatype_ticket);
    }
    public CoachBusWithEDataType_Ticket getCoachbuswithedatatype_ticket() {
        return coachbuswithedatatype_ticket;
    }

    public void setCoachbuswithedatatype_ticket(CoachBusWithEDataType_Ticket coachbuswithedatatype_ticket) {
        this.coachbuswithedatatype_ticket = coachbuswithedatatype_ticket;
    }

}