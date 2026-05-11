





import java.util.List;
import java.util.ArrayList;

public class dSL_ActionList  {






    private List<dSL_Action> dsl_actions;




    private dSL_Rule dsl_rule;


    public dSL_ActionList(
    ) {
        this.dsl_actions = new ArrayList<>();
    }

    public dSL_ActionList(
        ArrayList<dSL_Action> dsl_actions    ) {
        this.dsl_actions = dsl_actions;
    }


    public List<dSL_Action> getDsl_actions() {
        return dsl_actions;
    }

    public void addDsl_action(Dsl_action dsl_action) {
        this.dsl_actions.add(dsl_action);
    }
    public dSL_Rule getDsl_rule() {
        return dsl_rule;
    }

    public void setDsl_rule(dSL_Rule dsl_rule) {
        this.dsl_rule = dsl_rule;
    }

}