





import java.util.List;
import java.util.ArrayList;

public class CoachBusWithEDataType_Coach  {

    private int noOfSeats;
    private String name;
    private int id;
    private String model;





    private CoachBusWithEDataType_Trip coachbuswithedatatype_trip;




    private List<CoachBusWithEDataType_SecurityGuard> coachbuswithedatatype_securityguards;




    private List<CoachBusWithEDataType_BookingOffice> coachbuswithedatatype_bookingoffices;




    private CoachBusWithEDataType_SecurityGuard coachbuswithedatatype_securityguard;




    private CoachBusWithEDataType_BookingOffice coachbuswithedatatype_bookingoffice;




    private List<CoachBusWithEDataType_Trip> coachbuswithedatatype_trips;


    public CoachBusWithEDataType_Coach(
        int noOfSeats,        String name,        int id,        String model    ) {
        this.noOfSeats = noOfSeats;
        this.name = name;
        this.id = id;
        this.model = model;
        this.coachbuswithedatatype_securityguards = new ArrayList<>();
        this.coachbuswithedatatype_bookingoffices = new ArrayList<>();
        this.coachbuswithedatatype_trips = new ArrayList<>();
    }

    public CoachBusWithEDataType_Coach(
        int noOfSeats,        String name,        int id,        String model        ArrayList<CoachBusWithEDataType_SecurityGuard> coachbuswithedatatype_securityguards,        ArrayList<CoachBusWithEDataType_BookingOffice> coachbuswithedatatype_bookingoffices,        ArrayList<CoachBusWithEDataType_Trip> coachbuswithedatatype_trips    ) {
        this.noOfSeats = noOfSeats;
        this.name = name;
        this.id = id;
        this.model = model;
        this.coachbuswithedatatype_securityguards = coachbuswithedatatype_securityguards;
        this.coachbuswithedatatype_bookingoffices = coachbuswithedatatype_bookingoffices;
        this.coachbuswithedatatype_trips = coachbuswithedatatype_trips;
    }

    public int getNoofseats() {
        return noOfSeats;
    }

    public void setNoofseats(int noOfSeats) {
        this.noOfSeats = noOfSeats;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public CoachBusWithEDataType_Trip getCoachbuswithedatatype_trip() {
        return coachbuswithedatatype_trip;
    }

    public void setCoachbuswithedatatype_trip(CoachBusWithEDataType_Trip coachbuswithedatatype_trip) {
        this.coachbuswithedatatype_trip = coachbuswithedatatype_trip;
    }
    public List<CoachBusWithEDataType_SecurityGuard> getCoachbuswithedatatype_securityguards() {
        return coachbuswithedatatype_securityguards;
    }

    public void addCoachbuswithedatatype_securityguard(Coachbuswithedatatype_securityguard coachbuswithedatatype_securityguard) {
        this.coachbuswithedatatype_securityguards.add(coachbuswithedatatype_securityguard);
    }
    public List<CoachBusWithEDataType_BookingOffice> getCoachbuswithedatatype_bookingoffices() {
        return coachbuswithedatatype_bookingoffices;
    }

    public void addCoachbuswithedatatype_bookingoffice(Coachbuswithedatatype_bookingoffice coachbuswithedatatype_bookingoffice) {
        this.coachbuswithedatatype_bookingoffices.add(coachbuswithedatatype_bookingoffice);
    }
    public CoachBusWithEDataType_SecurityGuard getCoachbuswithedatatype_securityguard() {
        return coachbuswithedatatype_securityguard;
    }

    public void setCoachbuswithedatatype_securityguard(CoachBusWithEDataType_SecurityGuard coachbuswithedatatype_securityguard) {
        this.coachbuswithedatatype_securityguard = coachbuswithedatatype_securityguard;
    }
    public CoachBusWithEDataType_BookingOffice getCoachbuswithedatatype_bookingoffice() {
        return coachbuswithedatatype_bookingoffice;
    }

    public void setCoachbuswithedatatype_bookingoffice(CoachBusWithEDataType_BookingOffice coachbuswithedatatype_bookingoffice) {
        this.coachbuswithedatatype_bookingoffice = coachbuswithedatatype_bookingoffice;
    }
    public List<CoachBusWithEDataType_Trip> getCoachbuswithedatatype_trips() {
        return coachbuswithedatatype_trips;
    }

    public void addCoachbuswithedatatype_trip(Coachbuswithedatatype_trip coachbuswithedatatype_trip) {
        this.coachbuswithedatatype_trips.add(coachbuswithedatatype_trip);
    }

}