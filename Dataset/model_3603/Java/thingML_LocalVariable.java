





import java.util.List;
import java.util.ArrayList;

public class thingML_LocalVariable extends ReferencedElmt, AnnotatedElement, Action, Variable {

    private boolean changeable;
    private String name;





    private thingML_Expression thingml_expression;




    private thingML_Stream thingml_stream;


    public thingML_LocalVariable(
        boolean changeable,        String name    ) {
        super(
        );
        this.changeable = changeable;
        this.name = name;
    }


    public boolean getChangeable() {
        return changeable;
    }

    public void setChangeable(boolean changeable) {
        this.changeable = changeable;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public thingML_Expression getThingml_expression() {
        return thingml_expression;
    }

    public void setThingml_expression(thingML_Expression thingml_expression) {
        this.thingml_expression = thingml_expression;
    }
    public thingML_Stream getThingml_stream() {
        return thingml_stream;
    }

    public void setThingml_stream(thingML_Stream thingml_stream) {
        this.thingml_stream = thingml_stream;
    }

}