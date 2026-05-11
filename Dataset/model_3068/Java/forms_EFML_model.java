





import java.util.List;
import java.util.ArrayList;

public class forms_EFML_model  {






    private List<Form> forms;




    private Form form;


    public forms_EFML_model(
    ) {
        this.forms = new ArrayList<>();
    }

    public forms_EFML_model(
        ArrayList<Form> forms    ) {
        this.forms = forms;
    }


    public List<Form> getForms() {
        return forms;
    }

    public void addForm(Form form) {
        this.forms.add(form);
    }
    public Form getForm() {
        return form;
    }

    public void setForm(Form form) {
        this.form = form;
    }

}