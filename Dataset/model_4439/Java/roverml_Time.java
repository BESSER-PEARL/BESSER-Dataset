





import java.util.List;
import java.util.ArrayList;

public class roverml_Time extends SingleQuantity {

    private String timeUnit;





    private roverml_Wait roverml_wait;


    public roverml_Time(
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

    public roverml_Wait getRoverml_wait() {
        return roverml_wait;
    }

    public void setRoverml_wait(roverml_Wait roverml_wait) {
        this.roverml_wait = roverml_wait;
    }

}