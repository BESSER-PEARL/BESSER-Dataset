





import java.util.List;
import java.util.ArrayList;

public class forms_Form  {

    private String description;
    private String name;
    private String title;





    private forms_FormModel forms_formmodel;




    private forms_Entity forms_entity;




    private forms_FormModel forms_formmodel;




    private forms_Page forms_page;




    private List<forms_Page> forms_pages;


    public forms_Form(
        String description,        String name,        String title    ) {
        this.description = description;
        this.name = name;
        this.title = title;
        this.forms_pages = new ArrayList<>();
    }

    public forms_Form(
        String description,        String name,        String title        ArrayList<forms_Page> forms_pages    ) {
        this.description = description;
        this.name = name;
        this.title = title;
        this.forms_pages = forms_pages;
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

    public forms_FormModel getForms_formmodel() {
        return forms_formmodel;
    }

    public void setForms_formmodel(forms_FormModel forms_formmodel) {
        this.forms_formmodel = forms_formmodel;
    }
    public forms_Entity getForms_entity() {
        return forms_entity;
    }

    public void setForms_entity(forms_Entity forms_entity) {
        this.forms_entity = forms_entity;
    }
    public forms_FormModel getForms_formmodel() {
        return forms_formmodel;
    }

    public void setForms_formmodel(forms_FormModel forms_formmodel) {
        this.forms_formmodel = forms_formmodel;
    }
    public forms_Page getForms_page() {
        return forms_page;
    }

    public void setForms_page(forms_Page forms_page) {
        this.forms_page = forms_page;
    }
    public List<forms_Page> getForms_pages() {
        return forms_pages;
    }

    public void addForms_page(Forms_page forms_page) {
        this.forms_pages.add(forms_page);
    }

}