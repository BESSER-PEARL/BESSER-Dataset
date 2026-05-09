





import java.util.List;
import java.util.ArrayList;

public class reservationsystem_Plane  {

    private String id;
    private int crewNum;
    private String model;
    private int capacity;





    private List<reservationsystem_SpecificFlight> reservationsystem_specificflights;




    private reservationsystem_Seat reservationsystem_seat;




    private List<reservationsystem_Seat> reservationsystem_seats;




    private reservationsystem_SpecificFlight reservationsystem_specificflight;


    public reservationsystem_Plane(
        String id,        int crewNum,        String model,        int capacity    ) {
        this.id = id;
        this.crewNum = crewNum;
        this.model = model;
        this.capacity = capacity;
        this.reservationsystem_specificflights = new ArrayList<>();
        this.reservationsystem_seats = new ArrayList<>();
    }

    public reservationsystem_Plane(
        String id,        int crewNum,        String model,        int capacity        ArrayList<reservationsystem_SpecificFlight> reservationsystem_specificflights,        ArrayList<reservationsystem_Seat> reservationsystem_seats    ) {
        this.id = id;
        this.crewNum = crewNum;
        this.model = model;
        this.capacity = capacity;
        this.reservationsystem_specificflights = reservationsystem_specificflights;
        this.reservationsystem_seats = reservationsystem_seats;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getCrewnum() {
        return crewNum;
    }

    public void setCrewnum(int crewNum) {
        this.crewNum = crewNum;
    }
    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public List<reservationsystem_SpecificFlight> getReservationsystem_specificflights() {
        return reservationsystem_specificflights;
    }

    public void addReservationsystem_specificflight(Reservationsystem_specificflight reservationsystem_specificflight) {
        this.reservationsystem_specificflights.add(reservationsystem_specificflight);
    }
    public reservationsystem_Seat getReservationsystem_seat() {
        return reservationsystem_seat;
    }

    public void setReservationsystem_seat(reservationsystem_Seat reservationsystem_seat) {
        this.reservationsystem_seat = reservationsystem_seat;
    }
    public List<reservationsystem_Seat> getReservationsystem_seats() {
        return reservationsystem_seats;
    }

    public void addReservationsystem_seat(Reservationsystem_seat reservationsystem_seat) {
        this.reservationsystem_seats.add(reservationsystem_seat);
    }
    public reservationsystem_SpecificFlight getReservationsystem_specificflight() {
        return reservationsystem_specificflight;
    }

    public void setReservationsystem_specificflight(reservationsystem_SpecificFlight reservationsystem_specificflight) {
        this.reservationsystem_specificflight = reservationsystem_specificflight;
    }

}