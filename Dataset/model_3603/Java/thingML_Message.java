





import java.util.List;
import java.util.ArrayList;

public class thingML_Message extends AnnotatedElement, ReferencedElmt {

    private String name;





    private thingML_Port thingml_port;




    private thingML_Port thingml_port;




    private List<thingML_Parameter> thingml_parameters;


    public thingML_Message(
        String name    ) {
        super(
        );
        this.name = name;
        this.thingml_parameters = new ArrayList<>();
    }

    public thingML_Message(
        String name        ArrayList<thingML_Parameter> thingml_parameters    ) {
        this.name = name;
        this.thingml_parameters = thingml_parameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public thingML_Port getThingml_port() {
        return thingml_port;
    }

    public void setThingml_port(thingML_Port thingml_port) {
        this.thingml_port = thingml_port;
    }
    public thingML_Port getThingml_port() {
        return thingml_port;
    }

    public void setThingml_port(thingML_Port thingml_port) {
        this.thingml_port = thingml_port;
    }
    public List<thingML_Parameter> getThingml_parameters() {
        return thingml_parameters;
    }

    public void addThingml_parameter(Thingml_parameter thingml_parameter) {
        this.thingml_parameters.add(thingml_parameter);
    }

}