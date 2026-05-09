





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachine_Expression extends ExpressionElement {

    private String _name;
    private String operator;





    private SimplStateMachine_Transition simplstatemachine_transition;


    public SimplStateMachine_Expression(
        String _name,        String operator    ) {
        super(
        );
        this._name = _name;
        this.operator = operator;
    }


    public String get_name() {
        return _name;
    }

    public void set_name(String _name) {
        this._name = _name;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public SimplStateMachine_Transition getSimplstatemachine_transition() {
        return simplstatemachine_transition;
    }

    public void setSimplstatemachine_transition(SimplStateMachine_Transition simplstatemachine_transition) {
        this.simplstatemachine_transition = simplstatemachine_transition;
    }

}