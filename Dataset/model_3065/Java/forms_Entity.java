





import java.util.List;
import java.util.ArrayList;

public class forms_Entity  {

    private String name;





    private forms_Attribute forms_attribute;




    private forms_EFML forms_efml;




    private List<forms_Attribute> forms_attributes;




    private forms_Entity forms_entity;


    public forms_Entity(
        String name    ) {
        this.name = name;
        this.forms_attributes = new ArrayList<>();
    }

    public forms_Entity(
        String name        ArrayList<forms_Attribute> forms_attributes    ) {
        this.name = name;
        this.forms_attributes = forms_attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public forms_Attribute getForms_attribute() {
        return forms_attribute;
    }

    public void setForms_attribute(forms_Attribute forms_attribute) {
        this.forms_attribute = forms_attribute;
    }
    public forms_EFML getForms_efml() {
        return forms_efml;
    }

    public void setForms_efml(forms_EFML forms_efml) {
        this.forms_efml = forms_efml;
    }
    public List<forms_Attribute> getForms_attributes() {
        return forms_attributes;
    }

    public void addForms_attribute(Forms_attribute forms_attribute) {
        this.forms_attributes.add(forms_attribute);
    }
    public forms_Entity getForms_entity() {
        return forms_entity;
    }

    public void setForms_entity(forms_Entity forms_entity) {
        this.forms_entity = forms_entity;
    }

}