





import java.util.List;
import java.util.ArrayList;

public class forms_EMFL_FormModel  {






    private List<forms_Condition> forms_conditions;




    private List<forms_Entity> forms_entitys;




    private List<forms_Form> forms_forms;


    public forms_EMFL_FormModel(
    ) {
        this.forms_conditions = new ArrayList<>();
        this.forms_entitys = new ArrayList<>();
        this.forms_forms = new ArrayList<>();
    }

    public forms_EMFL_FormModel(
        ArrayList<forms_Condition> forms_conditions,        ArrayList<forms_Entity> forms_entitys,        ArrayList<forms_Form> forms_forms    ) {
        this.forms_conditions = forms_conditions;
        this.forms_entitys = forms_entitys;
        this.forms_forms = forms_forms;
    }


    public List<forms_Condition> getForms_conditions() {
        return forms_conditions;
    }

    public void addForms_condition(Forms_condition forms_condition) {
        this.forms_conditions.add(forms_condition);
    }
    public List<forms_Entity> getForms_entitys() {
        return forms_entitys;
    }

    public void addForms_entity(Forms_entity forms_entity) {
        this.forms_entitys.add(forms_entity);
    }
    public List<forms_Form> getForms_forms() {
        return forms_forms;
    }

    public void addForms_form(Forms_form forms_form) {
        this.forms_forms.add(forms_form);
    }

}