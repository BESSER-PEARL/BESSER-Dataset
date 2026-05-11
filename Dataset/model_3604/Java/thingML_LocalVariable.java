





import java.util.List;
import java.util.ArrayList;

public class thingML_LocalVariable extends Action, Variable {

    private boolean readonly;





    private thingML_Expression thingml_expression;


    public thingML_LocalVariable(
        boolean readonly    ) {
        super(
        );
        this.readonly = readonly;
    }


    public boolean getReadonly() {
        return readonly;
    }

    public void setReadonly(boolean readonly) {
        this.readonly = readonly;
    }

    public thingML_Expression getThingml_expression() {
        return thingml_expression;
    }

    public void setThingml_expression(thingML_Expression thingml_expression) {
        this.thingml_expression = thingml_expression;
    }

}