





import java.util.List;
import java.util.ArrayList;

public class forms_Attribute extends Feature {

    private String type;
    private boolean mandatory;



    public forms_Attribute(
        String type,        boolean mandatory    ) {
        super(
        );
        this.type = type;
        this.mandatory = mandatory;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }


}