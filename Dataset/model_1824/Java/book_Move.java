





import java.util.List;
import java.util.ArrayList;

public class book_Move extends Animation {

    private String toLocation;
    private String fromLocation;



    public book_Move(
        String toLocation,        String fromLocation    ) {
        super(
        );
        this.toLocation = toLocation;
        this.fromLocation = fromLocation;
    }


    public String getTolocation() {
        return toLocation;
    }

    public void setTolocation(String toLocation) {
        this.toLocation = toLocation;
    }
    public String getFromlocation() {
        return fromLocation;
    }

    public void setFromlocation(String fromLocation) {
        this.fromLocation = fromLocation;
    }


}