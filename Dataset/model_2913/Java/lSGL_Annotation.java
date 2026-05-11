





import java.util.List;
import java.util.ArrayList;

public class lSGL_Annotation  {

    private String value;
    private String name;





    private lSGL_Attribute lsgl_attribute;


    public lSGL_Annotation(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
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

    public lSGL_Attribute getLsgl_attribute() {
        return lsgl_attribute;
    }

    public void setLsgl_attribute(lSGL_Attribute lsgl_attribute) {
        this.lsgl_attribute = lsgl_attribute;
    }

}