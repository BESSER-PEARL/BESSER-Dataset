





import java.util.List;
import java.util.ArrayList;

public class robotDSL_Negation  {

    private String NOT;





    private robotDSL_Trigger robotdsl_trigger;


    public robotDSL_Negation(
        String NOT    ) {
        this.NOT = NOT;
    }


    public String getNot() {
        return NOT;
    }

    public void setNot(String NOT) {
        this.NOT = NOT;
    }

    public robotDSL_Trigger getRobotdsl_trigger() {
        return robotdsl_trigger;
    }

    public void setRobotdsl_trigger(robotDSL_Trigger robotdsl_trigger) {
        this.robotdsl_trigger = robotdsl_trigger;
    }

}