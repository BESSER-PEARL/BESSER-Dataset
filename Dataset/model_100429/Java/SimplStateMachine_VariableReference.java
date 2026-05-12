





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachine_VariableReference extends ExpressionElement {

    private String _name;





    private SimplStateMachine_Variable simplstatemachine_variable;


    public SimplStateMachine_VariableReference(
        String _name    ) {
        super(
        );
        this._name = _name;
    }


    public String get_name() {
        return _name;
    }

    public void set_name(String _name) {
        this._name = _name;
    }

    public SimplStateMachine_Variable getSimplstatemachine_variable() {
        return simplstatemachine_variable;
    }

    public void setSimplstatemachine_variable(SimplStateMachine_Variable simplstatemachine_variable) {
        this.simplstatemachine_variable = simplstatemachine_variable;
    }

}