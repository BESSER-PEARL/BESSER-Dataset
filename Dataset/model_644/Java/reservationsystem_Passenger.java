





import java.util.List;
import java.util.ArrayList;

public class reservationsystem_Passenger extends Person {

    private String foodPref;
    private String specialNeeds;



    public reservationsystem_Passenger(
        String foodPref,        String specialNeeds    ) {
        super(
        );
        this.foodPref = foodPref;
        this.specialNeeds = specialNeeds;
    }


    public String getFoodpref() {
        return foodPref;
    }

    public void setFoodpref(String foodPref) {
        this.foodPref = foodPref;
    }
    public String getSpecialneeds() {
        return specialNeeds;
    }

    public void setSpecialneeds(String specialNeeds) {
        this.specialNeeds = specialNeeds;
    }


}