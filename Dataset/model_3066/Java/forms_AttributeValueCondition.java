





import java.util.List;
import java.util.ArrayList;

public class forms_AttributeValueCondition extends Condition {

    private String value;





    private forms_Attribute forms_attribute;


    public forms_AttributeValueCondition(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public forms_Attribute getForms_attribute() {
        return forms_attribute;
    }

    public void setForms_attribute(forms_Attribute forms_attribute) {
        this.forms_attribute = forms_attribute;
    }

}