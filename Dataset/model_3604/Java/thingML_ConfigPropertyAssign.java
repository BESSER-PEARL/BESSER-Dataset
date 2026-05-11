





import java.util.List;
import java.util.ArrayList;

public class thingML_ConfigPropertyAssign  {






    private List<thingML_PlatformAnnotation> thingml_platformannotations;




    private thingML_Expression thingml_expression;




    private thingML_Property thingml_property;




    private thingML_Instance thingml_instance;




    private thingML_Expression thingml_expression;




    private thingML_Configuration thingml_configuration;


    public thingML_ConfigPropertyAssign(
    ) {
        this.thingml_platformannotations = new ArrayList<>();
    }

    public thingML_ConfigPropertyAssign(
        ArrayList<thingML_PlatformAnnotation> thingml_platformannotations    ) {
        this.thingml_platformannotations = thingml_platformannotations;
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
    public thingML_Property getThingml_property() {
        return thingml_property;
    }

    public void setThingml_property(thingML_Property thingml_property) {
        this.thingml_property = thingml_property;
    }
    public thingML_Instance getThingml_instance() {
        return thingml_instance;
    }

    public void setThingml_instance(thingML_Instance thingml_instance) {
        this.thingml_instance = thingml_instance;
    }
    public thingML_Expression getThingml_expression() {
        return thingml_expression;
    }

    public void setThingml_expression(thingML_Expression thingml_expression) {
        this.thingml_expression = thingml_expression;
    }
    public thingML_Configuration getThingml_configuration() {
        return thingml_configuration;
    }

    public void setThingml_configuration(thingML_Configuration thingml_configuration) {
        this.thingml_configuration = thingml_configuration;
    }

}