





import java.util.List;
import java.util.ArrayList;

public class forms_Form  {

    private String description;
    private String name;
    private String title;
    private String isWelcomeForm;





    private forms_Model forms_model;


    public forms_Form(
        String description,        String name,        String title,        String isWelcomeForm    ) {
        this.description = description;
        this.name = name;
        this.title = title;
        this.isWelcomeForm = isWelcomeForm;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getIswelcomeform() {
        return isWelcomeForm;
    }

    public void setIswelcomeform(String isWelcomeForm) {
        this.isWelcomeForm = isWelcomeForm;
    }

    public forms_Model getForms_model() {
        return forms_model;
    }

    public void setForms_model(forms_Model forms_model) {
        this.forms_model = forms_model;
    }

}