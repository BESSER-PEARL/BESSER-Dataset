





import java.util.List;
import java.util.ArrayList;

public class Plane  {

    private String PlaneName;
    private int Capacity;
    private String PlaneId;





    private List<Flight> flights;


    public Plane(
        String PlaneName,        int Capacity,        String PlaneId    ) {
        this.PlaneName = PlaneName;
        this.Capacity = Capacity;
        this.PlaneId = PlaneId;
        this.flights = new ArrayList<>();
    }

    public Plane(
        String PlaneName,        int Capacity,        String PlaneId        ArrayList<Flight> flights    ) {
        this.PlaneName = PlaneName;
        this.Capacity = Capacity;
        this.PlaneId = PlaneId;
        this.flights = flights;
    }

    public String getPlanename() {
        return PlaneName;
    }

    public void setPlanename(String PlaneName) {
        this.PlaneName = PlaneName;
    }
    public int getCapacity() {
        return Capacity;
    }

    public void setCapacity(int Capacity) {
        this.Capacity = Capacity;
    }
    public String getPlaneid() {
        return PlaneId;
    }

    public void setPlaneid(String PlaneId) {
        this.PlaneId = PlaneId;
    }

    public List<Flight> getFlights() {
        return flights;
    }

    public void addFlight(Flight flight) {
        this.flights.add(flight);
    }

}