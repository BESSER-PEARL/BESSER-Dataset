





import java.util.List;
import java.util.ArrayList;

public class tracker_Mastitis extends MedicalCondition {

    private String origin;
    private String location;



    public tracker_Mastitis(
        String origin,        String location    ) {
        super(
        );
        this.origin = origin;
        this.location = location;
    }


    public String getOrigin() {
        return origin;
    }

    public void setOrigin(String origin) {
        this.origin = origin;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}