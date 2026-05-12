





import java.util.List;
import java.util.ArrayList;

public class CoachBus_Coach  {

    private String model;
    private int id;
    private int noOfSeats;
    private String name;





    private List<CoachBus_BookingOffice> coachbus_bookingoffices;




    private CoachBus_BookingOffice coachbus_bookingoffice;




    private CoachBus_SecurityGuard coachbus_securityguard;




    private List<CoachBus_SecurityGuard> coachbus_securityguards;




    private CoachBus_Trip coachbus_trip;




    private List<CoachBus_Trip> coachbus_trips;


    public CoachBus_Coach(
        String model,        int id,        int noOfSeats,        String name    ) {
        this.model = model;
        this.id = id;
        this.noOfSeats = noOfSeats;
        this.name = name;
        this.coachbus_bookingoffices = new ArrayList<>();
        this.coachbus_securityguards = new ArrayList<>();
        this.coachbus_trips = new ArrayList<>();
    }

    public CoachBus_Coach(
        String model,        int id,        int noOfSeats,        String name        ArrayList<CoachBus_BookingOffice> coachbus_bookingoffices,        ArrayList<CoachBus_SecurityGuard> coachbus_securityguards,        ArrayList<CoachBus_Trip> coachbus_trips    ) {
        this.model = model;
        this.id = id;
        this.noOfSeats = noOfSeats;
        this.name = name;
        this.coachbus_bookingoffices = coachbus_bookingoffices;
        this.coachbus_securityguards = coachbus_securityguards;
        this.coachbus_trips = coachbus_trips;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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

    public List<CoachBus_BookingOffice> getCoachbus_bookingoffices() {
        return coachbus_bookingoffices;
    }

    public void addCoachbus_bookingoffice(Coachbus_bookingoffice coachbus_bookingoffice) {
        this.coachbus_bookingoffices.add(coachbus_bookingoffice);
    }
    public CoachBus_BookingOffice getCoachbus_bookingoffice() {
        return coachbus_bookingoffice;
    }

    public void setCoachbus_bookingoffice(CoachBus_BookingOffice coachbus_bookingoffice) {
        this.coachbus_bookingoffice = coachbus_bookingoffice;
    }
    public CoachBus_SecurityGuard getCoachbus_securityguard() {
        return coachbus_securityguard;
    }

    public void setCoachbus_securityguard(CoachBus_SecurityGuard coachbus_securityguard) {
        this.coachbus_securityguard = coachbus_securityguard;
    }
    public List<CoachBus_SecurityGuard> getCoachbus_securityguards() {
        return coachbus_securityguards;
    }

    public void addCoachbus_securityguard(Coachbus_securityguard coachbus_securityguard) {
        this.coachbus_securityguards.add(coachbus_securityguard);
    }
    public CoachBus_Trip getCoachbus_trip() {
        return coachbus_trip;
    }

    public void setCoachbus_trip(CoachBus_Trip coachbus_trip) {
        this.coachbus_trip = coachbus_trip;
    }
    public List<CoachBus_Trip> getCoachbus_trips() {
        return coachbus_trips;
    }

    public void addCoachbus_trip(Coachbus_trip coachbus_trip) {
        this.coachbus_trips.add(coachbus_trip);
    }

}