





import java.util.List;
import java.util.ArrayList;

public class adl301_Attribute  {

    private String name;
    private String value;





    private adl301_Attributes adl301_attributes;


    public adl301_Attribute(
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

    public adl301_Attributes getAdl301_attributes() {
        return adl301_attributes;
    }

    public void setAdl301_attributes(adl301_Attributes adl301_attributes) {
        this.adl301_attributes = adl301_attributes;
    }

}