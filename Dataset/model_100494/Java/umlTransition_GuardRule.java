





import java.util.List;
import java.util.ArrayList;

public class umlTransition_GuardRule  {

    private String constraint;





    private umlTransition_TransitionRule umltransition_transitionrule;


    public umlTransition_GuardRule(
        String constraint    ) {
        this.constraint = constraint;
    }


    public String getConstraint() {
        return constraint;
    }

    public void setConstraint(String constraint) {
        this.constraint = constraint;
    }

    public umlTransition_TransitionRule getUmltransition_transitionrule() {
        return umltransition_transitionrule;
    }

    public void setUmltransition_transitionrule(umlTransition_TransitionRule umltransition_transitionrule) {
        this.umltransition_transitionrule = umltransition_transitionrule;
    }

}