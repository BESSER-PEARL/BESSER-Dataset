





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachine_Assignment  {

    private String _name;





    private SimplStateMachine_Operation simplstatemachine_operation;




    private SimplStateMachine_Variable simplstatemachine_variable;




    private SimplStateMachine_ExpressionElement simplstatemachine_expressionelement;


    public SimplStateMachine_Assignment(
        String _name    ) {
        this._name = _name;
    }


    public String get_name() {
        return _name;
    }

    public void set_name(String _name) {
        this._name = _name;
    }

    public SimplStateMachine_Operation getSimplstatemachine_operation() {
        return simplstatemachine_operation;
    }

    public void setSimplstatemachine_operation(SimplStateMachine_Operation simplstatemachine_operation) {
        this.simplstatemachine_operation = simplstatemachine_operation;
    }
    public SimplStateMachine_Variable getSimplstatemachine_variable() {
        return simplstatemachine_variable;
    }

    public void setSimplstatemachine_variable(SimplStateMachine_Variable simplstatemachine_variable) {
        this.simplstatemachine_variable = simplstatemachine_variable;
    }
    public SimplStateMachine_ExpressionElement getSimplstatemachine_expressionelement() {
        return simplstatemachine_expressionelement;
    }

    public void setSimplstatemachine_expressionelement(SimplStateMachine_ExpressionElement simplstatemachine_expressionelement) {
        this.simplstatemachine_expressionelement = simplstatemachine_expressionelement;
    }

}