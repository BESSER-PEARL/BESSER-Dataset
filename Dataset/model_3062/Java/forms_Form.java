





import java.util.List;
import java.util.ArrayList;

public class forms_Form  {

    private boolean isWelcomeForm;
    private String title;
    private String name;
    private String description;





    private forms_RelationshipPageElement forms_relationshippageelement;




    private List<forms_Page> forms_pages;




    private forms_Entity forms_entity;


    public forms_Form(
        boolean isWelcomeForm,        String title,        String name,        String description    ) {
        this.isWelcomeForm = isWelcomeForm;
        this.title = title;
        this.name = name;
        this.description = description;
        this.forms_pages = new ArrayList<>();
    }

    public forms_Form(
        boolean isWelcomeForm,        String title,        String name,        String description        ArrayList<forms_Page> forms_pages    ) {
        this.isWelcomeForm = isWelcomeForm;
        this.title = title;
        this.name = name;
        this.description = description;
        this.forms_pages = forms_pages;
    }

    public boolean getIswelcomeform() {
        return isWelcomeForm;
    }

    public void setIswelcomeform(boolean isWelcomeForm) {
        this.isWelcomeForm = isWelcomeForm;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public forms_RelationshipPageElement getForms_relationshippageelement() {
        return forms_relationshippageelement;
    }

    public void setForms_relationshippageelement(forms_RelationshipPageElement forms_relationshippageelement) {
        this.forms_relationshippageelement = forms_relationshippageelement;
    }
    public List<forms_Page> getForms_pages() {
        return forms_pages;
    }

    public void addForms_page(Forms_page forms_page) {
        this.forms_pages.add(forms_page);
    }
    public forms_Entity getForms_entity() {
        return forms_entity;
    }

    public void setForms_entity(forms_Entity forms_entity) {
        this.forms_entity = forms_entity;
    }

}