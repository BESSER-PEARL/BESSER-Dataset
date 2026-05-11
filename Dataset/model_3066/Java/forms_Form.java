





import java.util.List;
import java.util.ArrayList;

public class forms_Form extends NamedElement {

    private boolean welcomeForm;
    private String title;
    private String description;





    private forms_Entity forms_entity;


    public forms_Form(
        boolean welcomeForm,        String title,        String description    ) {
        super(
        );
        this.welcomeForm = welcomeForm;
        this.title = title;
        this.description = description;
    }


    public boolean getWelcomeform() {
        return welcomeForm;
    }

    public void setWelcomeform(boolean welcomeForm) {
        this.welcomeForm = welcomeForm;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public forms_Entity getForms_entity() {
        return forms_entity;
    }

    public void setForms_entity(forms_Entity forms_entity) {
        this.forms_entity = forms_entity;
    }

}