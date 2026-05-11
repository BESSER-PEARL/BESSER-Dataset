





import java.util.List;
import java.util.ArrayList;

public class party_Custom extends ContactInfo {

    private String location;



    public party_Custom(
        String location    ) {
        super(
        );
        this.location = location;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}