





import java.util.List;
import java.util.ArrayList;

public class thingML_Property extends AnnotatedElement, ReferencedElmt, Variable {

    private String name;
    private boolean changeable;





    private thingML_Expression thingml_expression;




    private thingML_State thingml_state;


    public thingML_Property(
        String name,        boolean changeable    ) {
        super(
        );
        this.name = name;
        this.changeable = changeable;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getChangeable() {
        return changeable;
    }

    public void setChangeable(boolean changeable) {
        this.changeable = changeable;
    }

    public thingML_Expression getThingml_expression() {
        return thingml_expression;
    }

    public void setThingml_expression(thingML_Expression thingml_expression) {
        this.thingml_expression = thingml_expression;
    }
    public thingML_State getThingml_state() {
        return thingml_state;
    }

    public void setThingml_state(thingML_State thingml_state) {
        this.thingml_state = thingml_state;
    }

}