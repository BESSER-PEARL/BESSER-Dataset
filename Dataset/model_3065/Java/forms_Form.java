





import java.util.List;
import java.util.ArrayList;

public class forms_Form  {

    private String title;
    private String description;
    private String name;
    private boolean mainForm;





    private forms_EFML forms_efml;




    private forms_Entity forms_entity;


    public forms_Form(
        String title,        String description,        String name,        boolean mainForm    ) {
        this.title = title;
        this.description = description;
        this.name = name;
        this.mainForm = mainForm;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMainform() {
        return mainForm;
    }

    public void setMainform(boolean mainForm) {
        this.mainForm = mainForm;
    }

    public forms_EFML getForms_efml() {
        return forms_efml;
    }

    public void setForms_efml(forms_EFML forms_efml) {
        this.forms_efml = forms_efml;
    }
    public forms_Entity getForms_entity() {
        return forms_entity;
    }

    public void setForms_entity(forms_Entity forms_entity) {
        this.forms_entity = forms_entity;
    }

}