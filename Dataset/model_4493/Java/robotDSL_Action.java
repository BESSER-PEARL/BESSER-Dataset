





import java.util.List;
import java.util.ArrayList;

public class robotDSL_Action  {

    private String cent;
    private int duration;
    private int degr;





    private List<robotDSL_Trigger> robotdsl_triggers;




    private robotDSL_Goal robotdsl_goal;


    public robotDSL_Action(
        String cent,        int duration,        int degr    ) {
        this.cent = cent;
        this.duration = duration;
        this.degr = degr;
        this.robotdsl_triggers = new ArrayList<>();
    }

    public robotDSL_Action(
        String cent,        int duration,        int degr        ArrayList<robotDSL_Trigger> robotdsl_triggers    ) {
        this.cent = cent;
        this.duration = duration;
        this.degr = degr;
        this.robotdsl_triggers = robotdsl_triggers;
    }

    public String getCent() {
        return cent;
    }

    public void setCent(String cent) {
        this.cent = cent;
    }
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public int getDegr() {
        return degr;
    }

    public void setDegr(int degr) {
        this.degr = degr;
    }

    public List<robotDSL_Trigger> getRobotdsl_triggers() {
        return robotdsl_triggers;
    }

    public void addRobotdsl_trigger(Robotdsl_trigger robotdsl_trigger) {
        this.robotdsl_triggers.add(robotdsl_trigger);
    }
    public robotDSL_Goal getRobotdsl_goal() {
        return robotdsl_goal;
    }

    public void setRobotdsl_goal(robotDSL_Goal robotdsl_goal) {
        this.robotdsl_goal = robotdsl_goal;
    }

}