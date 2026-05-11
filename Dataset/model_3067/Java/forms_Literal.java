





import java.util.List;
import java.util.ArrayList;

public class forms_Literal extends NamedElement {

    private String value;





    private forms_Enumeration forms_enumeration;


    public forms_Literal(
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

    public forms_Enumeration getForms_enumeration() {
        return forms_enumeration;
    }

    public void setForms_enumeration(forms_Enumeration forms_enumeration) {
        this.forms_enumeration = forms_enumeration;
    }

}