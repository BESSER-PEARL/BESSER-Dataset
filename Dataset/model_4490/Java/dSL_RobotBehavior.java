





import java.util.List;
import java.util.ArrayList;

public class dSL_RobotBehavior  {






    private List<dSL_Behaviors> dsl_behaviorss;


    public dSL_RobotBehavior(
    ) {
        this.dsl_behaviorss = new ArrayList<>();
    }

    public dSL_RobotBehavior(
        ArrayList<dSL_Behaviors> dsl_behaviorss    ) {
        this.dsl_behaviorss = dsl_behaviorss;
    }


    public List<dSL_Behaviors> getDsl_behaviorss() {
        return dsl_behaviorss;
    }

    public void addDsl_behaviors(Dsl_behaviors dsl_behaviors) {
        this.dsl_behaviorss.add(dsl_behaviors);
    }

}