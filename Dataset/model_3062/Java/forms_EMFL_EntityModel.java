





import java.util.List;
import java.util.ArrayList;

public class forms_EMFL_EntityModel  {






    private List<forms_Entity> forms_entitys;




    private List<forms_Enumeration> forms_enumerations;


    public forms_EMFL_EntityModel(
    ) {
        this.forms_entitys = new ArrayList<>();
        this.forms_enumerations = new ArrayList<>();
    }

    public forms_EMFL_EntityModel(
        ArrayList<forms_Entity> forms_entitys,        ArrayList<forms_Enumeration> forms_enumerations    ) {
        this.forms_entitys = forms_entitys;
        this.forms_enumerations = forms_enumerations;
    }


    public List<forms_Entity> getForms_entitys() {
        return forms_entitys;
    }

    public void addForms_entity(Forms_entity forms_entity) {
        this.forms_entitys.add(forms_entity);
    }
    public List<forms_Enumeration> getForms_enumerations() {
        return forms_enumerations;
    }

    public void addForms_enumeration(Forms_enumeration forms_enumeration) {
        this.forms_enumerations.add(forms_enumeration);
    }

}