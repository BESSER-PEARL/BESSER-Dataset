





import java.util.List;
import java.util.ArrayList;

public class thingML_ExternalConnector extends AbstractConnector {






    private thingML_Instance thingml_instance;




    private thingML_Port thingml_port;




    private thingML_Protocol thingml_protocol;


    public thingML_ExternalConnector(
    ) {
        super(
        );
    }



    public thingML_Instance getThingml_instance() {
        return thingml_instance;
    }

    public void setThingml_instance(thingML_Instance thingml_instance) {
        this.thingml_instance = thingml_instance;
    }
    public thingML_Port getThingml_port() {
        return thingml_port;
    }

    public void setThingml_port(thingML_Port thingml_port) {
        this.thingml_port = thingml_port;
    }
    public thingML_Protocol getThingml_protocol() {
        return thingml_protocol;
    }

    public void setThingml_protocol(thingML_Protocol thingml_protocol) {
        this.thingml_protocol = thingml_protocol;
    }

}