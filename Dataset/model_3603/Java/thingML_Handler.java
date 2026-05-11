





import java.util.List;
import java.util.ArrayList;

public class thingML_Handler extends AnnotatedElement {

    private String name;





    private thingML_Expression thingml_expression;


    public thingML_Handler(
        String name    ) {
        super(
        );
        this.name = name;
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

}