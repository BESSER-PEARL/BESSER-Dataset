





import java.util.List;
import java.util.ArrayList;

public class thingML_PropertyAssign extends AnnotatedElement {






    private thingML_Expression thingml_expression;




    private List<thingML_Expression> thingml_expressions;




    private thingML_Property thingml_property;


    public thingML_PropertyAssign(
    ) {
        super(
        );
        this.thingml_expressions = new ArrayList<>();
    }

    public thingML_PropertyAssign(
        ArrayList<thingML_Expression> thingml_expressions    ) {
        this.thingml_expressions = thingml_expressions;
    }


    public thingML_Expression getThingml_expression() {
        return thingml_expression;
    }

    public void setThingml_expression(thingML_Expression thingml_expression) {
        this.thingml_expression = thingml_expression;
    }
    public List<thingML_Expression> getThingml_expressions() {
        return thingml_expressions;
    }

    public void addThingml_expression(Thingml_expression thingml_expression) {
        this.thingml_expressions.add(thingml_expression);
    }
    public thingML_Property getThingml_property() {
        return thingml_property;
    }

    public void setThingml_property(thingML_Property thingml_property) {
        this.thingml_property = thingml_property;
    }

}