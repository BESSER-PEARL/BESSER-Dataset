





import java.util.List;
import java.util.ArrayList;

public class robotDSL_Sound  {

    private String soundName;





    private robotDSL_Action robotdsl_action;


    public robotDSL_Sound(
        String soundName    ) {
        this.soundName = soundName;
    }


    public String getSoundname() {
        return soundName;
    }

    public void setSoundname(String soundName) {
        this.soundName = soundName;
    }

    public robotDSL_Action getRobotdsl_action() {
        return robotdsl_action;
    }

    public void setRobotdsl_action(robotDSL_Action robotdsl_action) {
        this.robotdsl_action = robotdsl_action;
    }

}