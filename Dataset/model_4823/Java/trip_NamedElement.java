





import java.util.List;
import java.util.ArrayList;

public class trip_NamedElement  {

    private String name;





    private trip_TripModel trip_tripmodel;


    public trip_NamedElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public trip_TripModel getTrip_tripmodel() {
        return trip_tripmodel;
    }

    public void setTrip_tripmodel(trip_TripModel trip_tripmodel) {
        this.trip_tripmodel = trip_tripmodel;
    }

}