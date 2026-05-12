





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachine_Expression extends ExpressionElement {

    private String operator;
    private String _name;





    private SimplStateMachine_ExpressionElement simplstatemachine_expressionelement;




    private SimplStateMachine_Transition simplstatemachine_transition;




    private SimplStateMachine_ExpressionElement simplstatemachine_expressionelement;


    public SimplStateMachine_Expression(
        String operator,        String _name    ) {
        super(
        );
        this.operator = operator;
        this._name = _name;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public String get_name() {
        return _name;
    }

    public void set_name(String _name) {
        this._name = _name;
    }

    public SimplStateMachine_ExpressionElement getSimplstatemachine_expressionelement() {
        return simplstatemachine_expressionelement;
    }

    public void setSimplstatemachine_expressionelement(SimplStateMachine_ExpressionElement simplstatemachine_expressionelement) {
        this.simplstatemachine_expressionelement = simplstatemachine_expressionelement;
    }
    public SimplStateMachine_Transition getSimplstatemachine_transition() {
        return simplstatemachine_transition;
    }

    public void setSimplstatemachine_transition(SimplStateMachine_Transition simplstatemachine_transition) {
        this.simplstatemachine_transition = simplstatemachine_transition;
    }
    public SimplStateMachine_ExpressionElement getSimplstatemachine_expressionelement() {
        return simplstatemachine_expressionelement;
    }

    public void setSimplstatemachine_expressionelement(SimplStateMachine_ExpressionElement simplstatemachine_expressionelement) {
        this.simplstatemachine_expressionelement = simplstatemachine_expressionelement;
    }

}