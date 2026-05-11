





import java.util.List;
import java.util.ArrayList;

public class forms_entityModeling_Attribute  {

    private boolean mandatory;
    private String type;
    private String name;





    private Enumeration enumeration;


    public forms_entityModeling_Attribute(
        boolean mandatory,        String type,        String name    ) {
        this.mandatory = mandatory;
        this.type = type;
        this.name = name;
    }


    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
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

    public Enumeration getEnumeration() {
        return enumeration;
    }

    public void setEnumeration(Enumeration enumeration) {
        this.enumeration = enumeration;
    }

}