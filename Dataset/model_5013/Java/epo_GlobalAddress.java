





import java.util.List;
import java.util.ArrayList;

public class epo_GlobalAddress extends GlobalLocation, Address {

    private String location;



    public epo_GlobalAddress(
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