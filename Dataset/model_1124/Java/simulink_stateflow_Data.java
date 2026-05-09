





import java.util.List;
import java.util.ArrayList;

public class simulink_stateflow_Data extends StateflowElement {

    private String type;
    private String value;
    private String name;
    private String size;



    public simulink_stateflow_Data(
        String type,        String value,        String name,        String size    ) {
        super(
        );
        this.type = type;
        this.value = value;
        this.name = name;
        this.size = size;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }


}