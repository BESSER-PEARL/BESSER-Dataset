





import java.util.List;
import java.util.ArrayList;

public class xDrone_Wait extends Command {

    private String seconds;



    public xDrone_Wait(
        String seconds    ) {
        super(
        );
        this.seconds = seconds;
    }


    public String getSeconds() {
        return seconds;
    }

    public void setSeconds(String seconds) {
        this.seconds = seconds;
    }


}