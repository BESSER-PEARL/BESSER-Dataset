





import java.util.List;
import java.util.ArrayList;

public class CoachBus_PrivateTrip extends Trip {

    private String extras;



    public CoachBus_PrivateTrip(
        String extras    ) {
        super(
        );
        this.extras = extras;
    }


    public String getExtras() {
        return extras;
    }

    public void setExtras(String extras) {
        this.extras = extras;
    }


}