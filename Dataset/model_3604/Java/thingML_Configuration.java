





import java.util.List;
import java.util.ArrayList;

public class thingML_Configuration extends AnnotatedElement, NamedElement {






    private List<thingML_AbstractConnector> thingml_abstractconnectors;




    private List<thingML_Instance> thingml_instances;


    public thingML_Configuration(
    ) {
        super(
        );
        this.thingml_abstractconnectors = new ArrayList<>();
        this.thingml_instances = new ArrayList<>();
    }

    public thingML_Configuration(
        ArrayList<thingML_AbstractConnector> thingml_abstractconnectors,        ArrayList<thingML_Instance> thingml_instances    ) {
        this.thingml_abstractconnectors = thingml_abstractconnectors;
        this.thingml_instances = thingml_instances;
    }


    public List<thingML_AbstractConnector> getThingml_abstractconnectors() {
        return thingml_abstractconnectors;
    }

    public void addThingml_abstractconnector(Thingml_abstractconnector thingml_abstractconnector) {
        this.thingml_abstractconnectors.add(thingml_abstractconnector);
    }
    public List<thingML_Instance> getThingml_instances() {
        return thingml_instances;
    }

    public void addThingml_instance(Thingml_instance thingml_instance) {
        this.thingml_instances.add(thingml_instance);
    }

}