





import java.util.List;
import java.util.ArrayList;

public class pivot_Constraint extends NamedElement {

    private String isCallable;





    private pivot_State pivot_state;




    private pivot_Operation pivot_operation;




    private pivot_Transition pivot_transition;




    private pivot_Operation pivot_operation;


    public pivot_Constraint(
        String isCallable    ) {
        super(
        );
        this.isCallable = isCallable;
    }


    public String getIscallable() {
        return isCallable;
    }

    public void setIscallable(String isCallable) {
        this.isCallable = isCallable;
    }

    public pivot_State getPivot_state() {
        return pivot_state;
    }

    public void setPivot_state(pivot_State pivot_state) {
        this.pivot_state = pivot_state;
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public pivot_Transition getPivot_transition() {
        return pivot_transition;
    }

    public void setPivot_transition(pivot_Transition pivot_transition) {
        this.pivot_transition = pivot_transition;
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }

}