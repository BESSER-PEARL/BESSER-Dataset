





import java.util.List;
import java.util.ArrayList;

public class Plane  {

    private int Capacity;
    private String PlaneId;
    private String PlaneName;





    private List<Flight> flights;


    public Plane(
        int Capacity,        String PlaneId,        String PlaneName    ) {
        this.Capacity = Capacity;
        this.PlaneId = PlaneId;
        this.PlaneName = PlaneName;
        this.flights = new ArrayList<>();
    }

    public Plane(
        int Capacity,        String PlaneId,        String PlaneName        ArrayList<Flight> flights    ) {
        this.Capacity = Capacity;
        this.PlaneId = PlaneId;
        this.PlaneName = PlaneName;
        this.flights = flights;
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
    public String getPlanename() {
        return PlaneName;
    }

    public void setPlanename(String PlaneName) {
        this.PlaneName = PlaneName;
    }

    public List<Flight> getFlights() {
        return flights;
    }

    public void addFlight(Flight flight) {
        this.flights.add(flight);
    }

}