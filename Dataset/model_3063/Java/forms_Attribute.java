





import java.util.List;
import java.util.ArrayList;

public class forms_Attribute  {

    private String isId;
    private String type;
    private boolean mandatory;
    private String name;





    private forms_Enumeration forms_enumeration;




    private forms_Entity forms_entity;


    public forms_Attribute(
        String isId,        String type,        boolean mandatory,        String name    ) {
        this.isId = isId;
        this.type = type;
        this.mandatory = mandatory;
        this.name = name;
    }


    public String getIsid() {
        return isId;
    }

    public void setIsid(String isId) {
        this.isId = isId;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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