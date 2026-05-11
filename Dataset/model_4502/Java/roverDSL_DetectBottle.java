





import java.util.List;
import java.util.ArrayList;

public class roverDSL_DetectBottle  {

    private int maxDistance;





    private roverDSL_Mission roverdsl_mission;


    public roverDSL_DetectBottle(
        int maxDistance    ) {
        this.maxDistance = maxDistance;
    }


    public int getMaxdistance() {
        return maxDistance;
    }

    public void setMaxdistance(int maxDistance) {
        this.maxDistance = maxDistance;
    }

    public roverDSL_Mission getRoverdsl_mission() {
        return roverdsl_mission;
    }

    public void setRoverdsl_mission(roverDSL_Mission roverdsl_mission) {
        this.roverdsl_mission = roverdsl_mission;
    }

}