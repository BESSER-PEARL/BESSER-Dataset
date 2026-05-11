





import java.util.List;
import java.util.ArrayList;

public class ardlers_Component  {

    private String name;





    private ardlers_SensorImport ardlers_sensorimport;




    private ardlers_Node ardlers_node;




    private ardlers_Attribute ardlers_attribute;


    public ardlers_Component(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ardlers_SensorImport getArdlers_sensorimport() {
        return ardlers_sensorimport;
    }

    public void setArdlers_sensorimport(ardlers_SensorImport ardlers_sensorimport) {
        this.ardlers_sensorimport = ardlers_sensorimport;
    }
    public ardlers_Node getArdlers_node() {
        return ardlers_node;
    }

    public void setArdlers_node(ardlers_Node ardlers_node) {
        this.ardlers_node = ardlers_node;
    }
    public ardlers_Attribute getArdlers_attribute() {
        return ardlers_attribute;
    }

    public void setArdlers_attribute(ardlers_Attribute ardlers_attribute) {
        this.ardlers_attribute = ardlers_attribute;
    }

}