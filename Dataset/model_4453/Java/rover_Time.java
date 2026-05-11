





import java.util.List;
import java.util.ArrayList;

public class rover_Time extends SingleQuantity {

    private String timeUnit;





    private rover_Wait rover_wait;


    public rover_Time(
        String timeUnit    ) {
        super(
        );
        this.timeUnit = timeUnit;
    }


    public String getTimeunit() {
        return timeUnit;
    }

    public void setTimeunit(String timeUnit) {
        this.timeUnit = timeUnit;
    }

    public rover_Wait getRover_wait() {
        return rover_wait;
    }

    public void setRover_wait(rover_Wait rover_wait) {
        this.rover_wait = rover_wait;
    }

}