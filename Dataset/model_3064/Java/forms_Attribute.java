





import java.util.List;
import java.util.ArrayList;

public class forms_Attribute  {

    private boolean mandatory;
    private String name;
    private String type;





    private forms_Entity forms_entity;




    private forms_EnumerationType forms_enumerationtype;




    private forms_Entity forms_entity;




    private forms_Entity forms_entity;


    public forms_Attribute(
        boolean mandatory,        String name,        String type    ) {
        this.mandatory = mandatory;
        this.name = name;
        this.type = type;
    }


    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public forms_Entity getForms_entity() {
        return forms_entity;
    }

    public void setForms_entity(forms_Entity forms_entity) {
        this.forms_entity = forms_entity;
    }
    public forms_EnumerationType getForms_enumerationtype() {
        return forms_enumerationtype;
    }

    public void setForms_enumerationtype(forms_EnumerationType forms_enumerationtype) {
        this.forms_enumerationtype = forms_enumerationtype;
    }
    public forms_Entity getForms_entity() {
        return forms_entity;
    }

    public void setForms_entity(forms_Entity forms_entity) {
        this.forms_entity = forms_entity;
    }
    public forms_Entity getForms_entity() {
        return forms_entity;
    }

    public void setForms_entity(forms_Entity forms_entity) {
        this.forms_entity = forms_entity;
    }

}