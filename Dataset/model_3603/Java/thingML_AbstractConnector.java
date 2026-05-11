





import java.util.List;
import java.util.ArrayList;

public class thingML_AbstractConnector extends AnnotatedElement {

    private String name;





    private thingML_Configuration thingml_configuration;


    public thingML_AbstractConnector(
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

    public thingML_Configuration getThingml_configuration() {
        return thingml_configuration;
    }

    public void setThingml_configuration(thingML_Configuration thingml_configuration) {
        this.thingml_configuration = thingml_configuration;
    }

}