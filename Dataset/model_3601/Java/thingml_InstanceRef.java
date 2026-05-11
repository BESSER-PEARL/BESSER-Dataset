





import java.util.List;
import java.util.ArrayList;

public class thingml_InstanceRef  {






    private thingml_Instance thingml_instance;




    private List<thingml_ConfigInclude> thingml_configincludes;




    private thingml_Connector thingml_connector;




    private thingml_ConfigPropertyAssign thingml_configpropertyassign;




    private thingml_Connector thingml_connector;


    public thingml_InstanceRef(
    ) {
        this.thingml_configincludes = new ArrayList<>();
    }

    public thingml_InstanceRef(
        ArrayList<thingml_ConfigInclude> thingml_configincludes    ) {
        this.thingml_configincludes = thingml_configincludes;
    }


    public thingml_Instance getThingml_instance() {
        return thingml_instance;
    }

    public void setThingml_instance(thingml_Instance thingml_instance) {
        this.thingml_instance = thingml_instance;
    }
    public List<thingml_ConfigInclude> getThingml_configincludes() {
        return thingml_configincludes;
    }

    public void addThingml_configinclude(Thingml_configinclude thingml_configinclude) {
        this.thingml_configincludes.add(thingml_configinclude);
    }
    public thingml_Connector getThingml_connector() {
        return thingml_connector;
    }

    public void setThingml_connector(thingml_Connector thingml_connector) {
        this.thingml_connector = thingml_connector;
    }
    public thingml_ConfigPropertyAssign getThingml_configpropertyassign() {
        return thingml_configpropertyassign;
    }

    public void setThingml_configpropertyassign(thingml_ConfigPropertyAssign thingml_configpropertyassign) {
        this.thingml_configpropertyassign = thingml_configpropertyassign;
    }
    public thingml_Connector getThingml_connector() {
        return thingml_connector;
    }

    public void setThingml_connector(thingml_Connector thingml_connector) {
        this.thingml_connector = thingml_connector;
    }

}