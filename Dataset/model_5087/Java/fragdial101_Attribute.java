





import java.util.List;
import java.util.ArrayList;

public class fragdial101_Attribute  {

    private String name;
    private String value;





    private fragdial101_Attributes fragdial101_attributes;


    public fragdial101_Attribute(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
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

    public fragdial101_Attributes getFragdial101_attributes() {
        return fragdial101_attributes;
    }

    public void setFragdial101_attributes(fragdial101_Attributes fragdial101_attributes) {
        this.fragdial101_attributes = fragdial101_attributes;
    }

}