





import java.util.List;
import java.util.ArrayList;

public class simulink_BusElement  {

    private String name;
    private String type;
    private String dimensions;





    private simulink_Bus simulink_bus;




    private simulink_Bus simulink_bus;


    public simulink_BusElement(
        String name,        String type,        String dimensions    ) {
        this.name = name;
        this.type = type;
        this.dimensions = dimensions;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDimensions() {
        return dimensions;
    }

    public void setDimensions(String dimensions) {
        this.dimensions = dimensions;
    }

    public simulink_Bus getSimulink_bus() {
        return simulink_bus;
    }

    public void setSimulink_bus(simulink_Bus simulink_bus) {
        this.simulink_bus = simulink_bus;
    }
    public simulink_Bus getSimulink_bus() {
        return simulink_bus;
    }

    public void setSimulink_bus(simulink_Bus simulink_bus) {
        this.simulink_bus = simulink_bus;
    }

}