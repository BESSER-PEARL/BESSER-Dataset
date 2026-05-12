





import java.util.List;
import java.util.ArrayList;

public class FFP_Members  {

    private String FFP_Qmiles;
    private String FFP_Category;
    private String FFP_ID;





    private Passengers passengers;


    public FFP_Members(
        String FFP_Qmiles,        String FFP_Category,        String FFP_ID    ) {
        this.FFP_Qmiles = FFP_Qmiles;
        this.FFP_Category = FFP_Category;
        this.FFP_ID = FFP_ID;
    }


    public String getFfp_qmiles() {
        return FFP_Qmiles;
    }

    public void setFfp_qmiles(String FFP_Qmiles) {
        this.FFP_Qmiles = FFP_Qmiles;
    }
    public String getFfp_category() {
        return FFP_Category;
    }

    public void setFfp_category(String FFP_Category) {
        this.FFP_Category = FFP_Category;
    }
    public String getFfp_id() {
        return FFP_ID;
    }

    public void setFfp_id(String FFP_ID) {
        this.FFP_ID = FFP_ID;
    }

    public Passengers getPassengers() {
        return passengers;
    }

    public void setPassengers(Passengers passengers) {
        this.passengers = passengers;
    }

}