





import java.util.List;
import java.util.ArrayList;

public class tracker_MovedOut extends Event {

    private String destinationPin;



    public tracker_MovedOut(
        String destinationPin    ) {
        super(
        );
        this.destinationPin = destinationPin;
    }


    public String getDestinationpin() {
        return destinationPin;
    }

    public void setDestinationpin(String destinationPin) {
        this.destinationPin = destinationPin;
    }


}