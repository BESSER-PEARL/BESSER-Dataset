





import java.util.List;
import java.util.ArrayList;

public class forms_Attribute  {

    private String type;
    private String name;
    private boolean mandatory;



    public forms_Attribute(
        String type,        String name,        boolean mandatory    ) {
        this.type = type;
        this.name = name;
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
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }


}