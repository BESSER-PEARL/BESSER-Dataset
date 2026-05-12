





import java.util.List;
import java.util.ArrayList;

public class Check_ticket_availability_UseCase  {






    private Railway_website_Actor railway_website_actor;




    private Traveler_Actor traveler_actor;


    public Check_ticket_availability_UseCase(
    ) {
    }



    public Railway_website_Actor getRailway_website_actor() {
        return railway_website_actor;
    }

    public void setRailway_website_actor(Railway_website_Actor railway_website_actor) {
        this.railway_website_actor = railway_website_actor;
    }
    public Traveler_Actor getTraveler_actor() {
        return traveler_actor;
    }

    public void setTraveler_actor(Traveler_Actor traveler_actor) {
        this.traveler_actor = traveler_actor;
    }

}