





import java.util.List;
import java.util.ArrayList;

public class simulink_Property  {

    private String source;
    private String value;
    private String type;
    private String name;





    private simulink_Block simulink_block;


    public simulink_Property(
        String source,        String value,        String type,        String name    ) {
        this.source = source;
        this.value = value;
        this.type = type;
        this.name = name;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
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

    public simulink_Block getSimulink_block() {
        return simulink_block;
    }

    public void setSimulink_block(simulink_Block simulink_block) {
        this.simulink_block = simulink_block;
    }

}