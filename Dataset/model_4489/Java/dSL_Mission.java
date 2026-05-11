





import java.util.List;
import java.util.ArrayList;

public class dSL_Mission  {

    private String name;





    private dSL_EndCondition dsl_endcondition;




    private dSL_MarsRoverExpedition dsl_marsroverexpedition;




    private List<dSL_BehaviorName> dsl_behaviornames;


    public dSL_Mission(
        String name    ) {
        this.name = name;
        this.dsl_behaviornames = new ArrayList<>();
    }

    public dSL_Mission(
        String name        ArrayList<dSL_BehaviorName> dsl_behaviornames    ) {
        this.name = name;
        this.dsl_behaviornames = dsl_behaviornames;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dSL_EndCondition getDsl_endcondition() {
        return dsl_endcondition;
    }

    public void setDsl_endcondition(dSL_EndCondition dsl_endcondition) {
        this.dsl_endcondition = dsl_endcondition;
    }
    public dSL_MarsRoverExpedition getDsl_marsroverexpedition() {
        return dsl_marsroverexpedition;
    }

    public void setDsl_marsroverexpedition(dSL_MarsRoverExpedition dsl_marsroverexpedition) {
        this.dsl_marsroverexpedition = dsl_marsroverexpedition;
    }
    public List<dSL_BehaviorName> getDsl_behaviornames() {
        return dsl_behaviornames;
    }

    public void addDsl_behaviorname(Dsl_behaviorname dsl_behaviorname) {
        this.dsl_behaviornames.add(dsl_behaviorname);
    }

}