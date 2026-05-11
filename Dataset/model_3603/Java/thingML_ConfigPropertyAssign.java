





import java.util.List;
import java.util.ArrayList;

public class thingML_ConfigPropertyAssign  {






    private thingML_Property thingml_property;




    private List<thingML_PlatformAnnotation> thingml_platformannotations;




    private thingML_Expression thingml_expression;




    private List<thingML_Expression> thingml_expressions;




    private thingML_Configuration thingml_configuration;


    public thingML_ConfigPropertyAssign(
    ) {
        this.thingml_platformannotations = new ArrayList<>();
        this.thingml_expressions = new ArrayList<>();
    }

    public thingML_ConfigPropertyAssign(
        ArrayList<thingML_PlatformAnnotation> thingml_platformannotations,        ArrayList<thingML_Expression> thingml_expressions    ) {
        this.thingml_platformannotations = thingml_platformannotations;
        this.thingml_expressions = thingml_expressions;
    }


    public thingML_Property getThingml_property() {
        return thingml_property;
    }

    public void setThingml_property(thingML_Property thingml_property) {
        this.thingml_property = thingml_property;
    }
    public List<thingML_PlatformAnnotation> getThingml_platformannotations() {
        return thingml_platformannotations;
    }

    public void addThingml_platformannotation(Thingml_platformannotation thingml_platformannotation) {
        this.thingml_platformannotations.add(thingml_platformannotation);
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
    public thingML_Configuration getThingml_configuration() {
        return thingml_configuration;
    }

    public void setThingml_configuration(thingML_Configuration thingml_configuration) {
        this.thingml_configuration = thingml_configuration;
    }

}