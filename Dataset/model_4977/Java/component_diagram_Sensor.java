





import java.util.List;
import java.util.ArrayList;

public class component_diagram_Sensor extends ElectronicDevice {

    private String type;



    public component_diagram_Sensor(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}