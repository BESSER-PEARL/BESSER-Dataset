





import java.util.List;
import java.util.ArrayList;

public class book_Move extends Animation {

    private String fromLocation;
    private String toLocation;



    public book_Move(
        String fromLocation,        String toLocation    ) {
        super(
        );
        this.fromLocation = fromLocation;
        this.toLocation = toLocation;
    }


    public String getFromlocation() {
        return fromLocation;
    }

    public void setFromlocation(String fromLocation) {
        this.fromLocation = fromLocation;
    }
    public String getTolocation() {
        return toLocation;
    }

    public void setTolocation(String toLocation) {
        this.toLocation = toLocation;
    }


}