





import java.util.List;
import java.util.ArrayList;

public class ktest301_Attribute  {

    private String name;
    private String value;





    private ktest301_Attributes ktest301_attributes;


    public ktest301_Attribute(
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

    public ktest301_Attributes getKtest301_attributes() {
        return ktest301_attributes;
    }

    public void setKtest301_attributes(ktest301_Attributes ktest301_attributes) {
        this.ktest301_attributes = ktest301_attributes;
    }

}