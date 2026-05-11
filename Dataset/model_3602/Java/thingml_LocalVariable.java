





import java.util.List;
import java.util.ArrayList;

public class thingml_LocalVariable extends Action, Variable {

    private boolean changeable;





    private thingml_Expression thingml_expression;


    public thingml_LocalVariable(
        boolean changeable    ) {
        super(
        );
        this.changeable = changeable;
    }


    public boolean getChangeable() {
        return changeable;
    }

    public void setChangeable(boolean changeable) {
        this.changeable = changeable;
    }

    public thingml_Expression getThingml_expression() {
        return thingml_expression;
    }

    public void setThingml_expression(thingml_Expression thingml_expression) {
        this.thingml_expression = thingml_expression;
    }

}