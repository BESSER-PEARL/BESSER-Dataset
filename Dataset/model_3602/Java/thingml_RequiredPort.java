





import java.util.List;
import java.util.ArrayList;

public class thingml_RequiredPort extends Port {

    private boolean optional;





    private thingml_Connector thingml_connector;


    public thingml_RequiredPort(
        boolean optional    ) {
        super(
        );
        this.optional = optional;
    }


    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }

    public thingml_Connector getThingml_connector() {
        return thingml_connector;
    }

    public void setThingml_connector(thingml_Connector thingml_connector) {
        this.thingml_connector = thingml_connector;
    }

}