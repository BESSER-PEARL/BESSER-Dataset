





import java.util.List;
import java.util.ArrayList;

public class taskDSL_Investigate extends Action {

    private String speed;



    public taskDSL_Investigate(
        String speed    ) {
        super(
        );
        this.speed = speed;
    }


    public String getSpeed() {
        return speed;
    }

    public void setSpeed(String speed) {
        this.speed = speed;
    }


}