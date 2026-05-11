





import java.util.List;
import java.util.ArrayList;

public class robotDSL_Color  {

    private String colorName;





    private robotDSL_Trigger robotdsl_trigger;


    public robotDSL_Color(
        String colorName    ) {
        this.colorName = colorName;
    }


    public String getColorname() {
        return colorName;
    }

    public void setColorname(String colorName) {
        this.colorName = colorName;
    }

    public robotDSL_Trigger getRobotdsl_trigger() {
        return robotdsl_trigger;
    }

    public void setRobotdsl_trigger(robotDSL_Trigger robotdsl_trigger) {
        this.robotdsl_trigger = robotdsl_trigger;
    }

}