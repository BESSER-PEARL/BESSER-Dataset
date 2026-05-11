





import java.util.List;
import java.util.ArrayList;

public class forms_Entity extends EntityModelElement, NamedElement {






    private forms_Attribute forms_attribute;




    private forms_Relationship forms_relationship;




    private forms_Entity forms_entity;


    public forms_Entity(
    ) {
        super(
        );
    }



    public forms_Attribute getForms_attribute() {
        return forms_attribute;
    }

    public void setForms_attribute(forms_Attribute forms_attribute) {
        this.forms_attribute = forms_attribute;
    }
    public forms_Relationship getForms_relationship() {
        return forms_relationship;
    }

    public void setForms_relationship(forms_Relationship forms_relationship) {
        this.forms_relationship = forms_relationship;
    }
    public forms_Entity getForms_entity() {
        return forms_entity;
    }

    public void setForms_entity(forms_Entity forms_entity) {
        this.forms_entity = forms_entity;
    }

}