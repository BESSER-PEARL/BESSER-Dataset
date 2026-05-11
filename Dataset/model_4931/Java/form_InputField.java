





import java.util.List;
import java.util.ArrayList;

public class form_InputField extends PageElement {

    private String label;
    private boolean mandatory;



    public form_InputField(
        String label,        boolean mandatory    ) {
        super(
        );
        this.label = label;
        this.mandatory = mandatory;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }


}