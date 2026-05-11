





import java.util.List;
import java.util.ArrayList;

public class thingML_Configuration extends AnnotatedElement {

    private String name;





    private List<thingML_Instance> thingml_instances;


    public thingML_Configuration(
        String name    ) {
        super(
        );
        this.name = name;
        this.thingml_instances = new ArrayList<>();
    }

    public thingML_Configuration(
        String name        ArrayList<thingML_Instance> thingml_instances    ) {
        this.name = name;
        this.thingml_instances = thingml_instances;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<thingML_Instance> getThingml_instances() {
        return thingml_instances;
    }

    public void addThingml_instance(Thingml_instance thingml_instance) {
        this.thingml_instances.add(thingml_instance);
    }

}