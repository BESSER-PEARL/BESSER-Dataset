





import java.util.List;
import java.util.ArrayList;

public class trip_model_location  {

    private String name;





    private trip_model_TravelService trip_model_travelservice;




    private trip_model_OtherService trip_model_otherservice;




    private trip_model_TravelService trip_model_travelservice;


    public trip_model_location(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public trip_model_TravelService getTrip_model_travelservice() {
        return trip_model_travelservice;
    }

    public void setTrip_model_travelservice(trip_model_TravelService trip_model_travelservice) {
        this.trip_model_travelservice = trip_model_travelservice;
    }
    public trip_model_OtherService getTrip_model_otherservice() {
        return trip_model_otherservice;
    }

    public void setTrip_model_otherservice(trip_model_OtherService trip_model_otherservice) {
        this.trip_model_otherservice = trip_model_otherservice;
    }
    public trip_model_TravelService getTrip_model_travelservice() {
        return trip_model_travelservice;
    }

    public void setTrip_model_travelservice(trip_model_TravelService trip_model_travelservice) {
        this.trip_model_travelservice = trip_model_travelservice;
    }

}