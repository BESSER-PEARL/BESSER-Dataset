





import java.util.List;
import java.util.ArrayList;

public class simulink_Parameter  {

    private String name;
    private String value;
    private String type;





    private simulink_Element simulink_element;


    public simulink_Parameter(
        String name,        String value,        String type    ) {
        this.name = name;
        this.value = value;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public simulink_Element getSimulink_element() {
        return simulink_element;
    }

    public void setSimulink_element(simulink_Element simulink_element) {
        this.simulink_element = simulink_element;
    }

}