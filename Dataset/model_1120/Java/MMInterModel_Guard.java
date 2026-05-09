





import java.util.List;
import java.util.ArrayList;

public class MMInterModel_Guard extends Element {

    private String transition;
    private String specification;





    private MMInterModel_Transition mmintermodel_transition;


    public MMInterModel_Guard(
        String transition,        String specification    ) {
        super(
        );
        this.transition = transition;
        this.specification = specification;
    }


    public String getTransition() {
        return transition;
    }

    public void setTransition(String transition) {
        this.transition = transition;
    }
    public String getSpecification() {
        return specification;
    }

    public void setSpecification(String specification) {
        this.specification = specification;
    }

    public MMInterModel_Transition getMmintermodel_transition() {
        return mmintermodel_transition;
    }

    public void setMmintermodel_transition(MMInterModel_Transition mmintermodel_transition) {
        this.mmintermodel_transition = mmintermodel_transition;
    }

}