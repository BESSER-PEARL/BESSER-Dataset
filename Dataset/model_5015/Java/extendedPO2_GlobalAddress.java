





import java.util.List;
import java.util.ArrayList;

public class extendedPO2_GlobalAddress extends Address {

    private String location;



    public extendedPO2_GlobalAddress(
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