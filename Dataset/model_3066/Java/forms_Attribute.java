





import java.util.List;
import java.util.ArrayList;

public class forms_Attribute extends Feature {

    private String type;
    private boolean mandatory;





    private forms_Enumeration forms_enumeration;




    private forms_Entity forms_entity;


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

    public forms_Enumeration getForms_enumeration() {
        return forms_enumeration;
    }

    public void setForms_enumeration(forms_Enumeration forms_enumeration) {
        this.forms_enumeration = forms_enumeration;
    }
    public forms_Entity getForms_entity() {
        return forms_entity;
    }

    public void setForms_entity(forms_Entity forms_entity) {
        this.forms_entity = forms_entity;
    }

}