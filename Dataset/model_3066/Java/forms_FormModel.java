





import java.util.List;
import java.util.ArrayList;

public class forms_FormModel  {






    private List<forms_Form> forms_forms;


    public forms_FormModel(
    ) {
        this.forms_forms = new ArrayList<>();
    }

    public forms_FormModel(
        ArrayList<forms_Form> forms_forms    ) {
        this.forms_forms = forms_forms;
    }


    public List<forms_Form> getForms_forms() {
        return forms_forms;
    }

    public void addForms_form(Forms_form forms_form) {
        this.forms_forms.add(forms_form);
    }

}