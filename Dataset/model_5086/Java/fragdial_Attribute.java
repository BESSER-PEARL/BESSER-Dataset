





import java.util.List;
import java.util.ArrayList;

public class fragdial_Attribute  {

    private String name;
    private String value;





    private fragdial_Attributes fragdial_attributes;


    public fragdial_Attribute(
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

    public fragdial_Attributes getFragdial_attributes() {
        return fragdial_attributes;
    }

    public void setFragdial_attributes(fragdial_Attributes fragdial_attributes) {
        this.fragdial_attributes = fragdial_attributes;
    }

}