





import java.util.List;
import java.util.ArrayList;

public class simulink_Parameter  {

    private String value;
    private String type;
    private String name;
    private boolean readOnly;





    private simulink_Block simulink_block;




    private simulink_Port simulink_port;


    public simulink_Parameter(
        String value,        String type,        String name,        boolean readOnly    ) {
        this.value = value;
        this.type = type;
        this.name = name;
        this.readOnly = readOnly;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }

    public simulink_Block getSimulink_block() {
        return simulink_block;
    }

    public void setSimulink_block(simulink_Block simulink_block) {
        this.simulink_block = simulink_block;
    }
    public simulink_Port getSimulink_port() {
        return simulink_port;
    }

    public void setSimulink_port(simulink_Port simulink_port) {
        this.simulink_port = simulink_port;
    }

}