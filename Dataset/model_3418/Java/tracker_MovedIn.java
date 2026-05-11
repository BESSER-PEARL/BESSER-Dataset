





import java.util.List;
import java.util.ArrayList;

public class tracker_MovedIn extends Event {

    private String sourcePin;



    public tracker_MovedIn(
        String sourcePin    ) {
        super(
        );
        this.sourcePin = sourcePin;
    }


    public String getSourcepin() {
        return sourcePin;
    }

    public void setSourcepin(String sourcePin) {
        this.sourcePin = sourcePin;
    }


}