





import java.util.List;
import java.util.ArrayList;

public class forms_AttributeValueCondition extends Condition {

    private String value;





    private forms_AttributePageElement forms_attributepageelement;


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

    public forms_AttributePageElement getForms_attributepageelement() {
        return forms_attributepageelement;
    }

    public void setForms_attributepageelement(forms_AttributePageElement forms_attributepageelement) {
        this.forms_attributepageelement = forms_attributepageelement;
    }

}