





import java.util.List;
import java.util.ArrayList;

public class forms_Entity  {

    private String name;





    private forms_Form forms_form;




    private forms_Entity forms_entity;




    private forms_Model forms_model;


    public forms_Entity(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public forms_Form getForms_form() {
        return forms_form;
    }

    public void setForms_form(forms_Form forms_form) {
        this.forms_form = forms_form;
    }
    public forms_Entity getForms_entity() {
        return forms_entity;
    }

    public void setForms_entity(forms_Entity forms_entity) {
        this.forms_entity = forms_entity;
    }
    public forms_Model getForms_model() {
        return forms_model;
    }

    public void setForms_model(forms_Model forms_model) {
        this.forms_model = forms_model;
    }

}