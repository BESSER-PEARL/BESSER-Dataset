





import java.util.List;
import java.util.ArrayList;

public class Implementation_OccupancyComponent_Guest  {

    private String firstName;
    private String lastName;





    private Implementation_OccupancyComponent_Occupancy implementation_occupancycomponent_occupancy;


    public Implementation_OccupancyComponent_Guest(
        String firstName,        String lastName    ) {
        this.firstName = firstName;
        this.lastName = lastName;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }

    public Implementation_OccupancyComponent_Occupancy getImplementation_occupancycomponent_occupancy() {
        return implementation_occupancycomponent_occupancy;
    }

    public void setImplementation_occupancycomponent_occupancy(Implementation_OccupancyComponent_Occupancy implementation_occupancycomponent_occupancy) {
        this.implementation_occupancycomponent_occupancy = implementation_occupancycomponent_occupancy;
    }

}