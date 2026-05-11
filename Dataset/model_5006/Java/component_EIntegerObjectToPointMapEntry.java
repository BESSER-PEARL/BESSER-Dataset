





import java.util.List;
import java.util.ArrayList;

public class component_EIntegerObjectToPointMapEntry  {

    private String key;
    private String value;





    private component_PortConnector component_portconnector;


    public component_EIntegerObjectToPointMapEntry(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public component_PortConnector getComponent_portconnector() {
        return component_portconnector;
    }

    public void setComponent_portconnector(component_PortConnector component_portconnector) {
        this.component_portconnector = component_portconnector;
    }

}