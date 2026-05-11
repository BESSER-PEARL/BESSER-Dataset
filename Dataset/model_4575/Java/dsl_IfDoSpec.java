





import java.util.List;
import java.util.ArrayList;

public class dsl_IfDoSpec  {






    private dsl_Specification dsl_specification;




    private List<dsl_Action> dsl_actions;




    private dsl_Element dsl_element;


    public dsl_IfDoSpec(
    ) {
        this.dsl_actions = new ArrayList<>();
    }

    public dsl_IfDoSpec(
        ArrayList<dsl_Action> dsl_actions    ) {
        this.dsl_actions = dsl_actions;
    }


    public dsl_Specification getDsl_specification() {
        return dsl_specification;
    }

    public void setDsl_specification(dsl_Specification dsl_specification) {
        this.dsl_specification = dsl_specification;
    }
    public List<dsl_Action> getDsl_actions() {
        return dsl_actions;
    }

    public void addDsl_action(Dsl_action dsl_action) {
        this.dsl_actions.add(dsl_action);
    }
    public dsl_Element getDsl_element() {
        return dsl_element;
    }

    public void setDsl_element(dsl_Element dsl_element) {
        this.dsl_element = dsl_element;
    }

}