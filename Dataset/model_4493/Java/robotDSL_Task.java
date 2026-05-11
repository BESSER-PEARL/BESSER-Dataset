





import java.util.List;
import java.util.ArrayList;

public class robotDSL_Task  {

    private int prio;
    private String name;





    private List<robotDSL_Action> robotdsl_actions;




    private List<robotDSL_Trigger> robotdsl_triggers;




    private robotDSL_Mission robotdsl_mission;


    public robotDSL_Task(
        int prio,        String name    ) {
        this.prio = prio;
        this.name = name;
        this.robotdsl_actions = new ArrayList<>();
        this.robotdsl_triggers = new ArrayList<>();
    }

    public robotDSL_Task(
        int prio,        String name        ArrayList<robotDSL_Action> robotdsl_actions,        ArrayList<robotDSL_Trigger> robotdsl_triggers    ) {
        this.prio = prio;
        this.name = name;
        this.robotdsl_actions = robotdsl_actions;
        this.robotdsl_triggers = robotdsl_triggers;
    }

    public int getPrio() {
        return prio;
    }

    public void setPrio(int prio) {
        this.prio = prio;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<robotDSL_Action> getRobotdsl_actions() {
        return robotdsl_actions;
    }

    public void addRobotdsl_action(Robotdsl_action robotdsl_action) {
        this.robotdsl_actions.add(robotdsl_action);
    }
    public List<robotDSL_Trigger> getRobotdsl_triggers() {
        return robotdsl_triggers;
    }

    public void addRobotdsl_trigger(Robotdsl_trigger robotdsl_trigger) {
        this.robotdsl_triggers.add(robotdsl_trigger);
    }
    public robotDSL_Mission getRobotdsl_mission() {
        return robotdsl_mission;
    }

    public void setRobotdsl_mission(robotDSL_Mission robotdsl_mission) {
        this.robotdsl_mission = robotdsl_mission;
    }

}