





import java.util.List;
import java.util.ArrayList;

public class thingml_Instance extends AnnotatedElement {






    private thingml_Configuration thingml_configuration;




    private List<thingml_PropertyAssign> thingml_propertyassigns;


    public thingml_Instance(
    ) {
        super(
        );
        this.thingml_propertyassigns = new ArrayList<>();
    }

    public thingml_Instance(
        ArrayList<thingml_PropertyAssign> thingml_propertyassigns    ) {
        this.thingml_propertyassigns = thingml_propertyassigns;
    }


    public thingml_Configuration getThingml_configuration() {
        return thingml_configuration;
    }

    public void setThingml_configuration(thingml_Configuration thingml_configuration) {
        this.thingml_configuration = thingml_configuration;
    }
    public List<thingml_PropertyAssign> getThingml_propertyassigns() {
        return thingml_propertyassigns;
    }

    public void addThingml_propertyassign(Thingml_propertyassign thingml_propertyassign) {
        this.thingml_propertyassigns.add(thingml_propertyassign);
    }

}