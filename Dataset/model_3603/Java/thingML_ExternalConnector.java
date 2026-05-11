





import java.util.List;
import java.util.ArrayList;

public class thingML_ExternalConnector extends AbstractConnector {






    private thingML_Protocol thingml_protocol;




    private thingML_Port thingml_port;




    private thingML_InstanceRef thingml_instanceref;


    public thingML_ExternalConnector(
    ) {
        super(
        );
    }



    public thingML_Protocol getThingml_protocol() {
        return thingml_protocol;
    }

    public void setThingml_protocol(thingML_Protocol thingml_protocol) {
        this.thingml_protocol = thingml_protocol;
    }
    public thingML_Port getThingml_port() {
        return thingml_port;
    }

    public void setThingml_port(thingML_Port thingml_port) {
        this.thingml_port = thingml_port;
    }
    public thingML_InstanceRef getThingml_instanceref() {
        return thingml_instanceref;
    }

    public void setThingml_instanceref(thingML_InstanceRef thingml_instanceref) {
        this.thingml_instanceref = thingml_instanceref;
    }

}