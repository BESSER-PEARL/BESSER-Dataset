





import java.util.List;
import java.util.ArrayList;

public class dsl_Task  {

    private boolean ignoreBehavior;
    private String name;
    private String action;





    private dsl_Mission dsl_mission;


    public dsl_Task(
        boolean ignoreBehavior,        String name,        String action    ) {
        this.ignoreBehavior = ignoreBehavior;
        this.name = name;
        this.action = action;
    }


    public boolean getIgnorebehavior() {
        return ignoreBehavior;
    }

    public void setIgnorebehavior(boolean ignoreBehavior) {
        this.ignoreBehavior = ignoreBehavior;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public dsl_Mission getDsl_mission() {
        return dsl_mission;
    }

    public void setDsl_mission(dsl_Mission dsl_mission) {
        this.dsl_mission = dsl_mission;
    }

}