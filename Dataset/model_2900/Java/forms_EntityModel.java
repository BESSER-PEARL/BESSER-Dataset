





import java.util.List;
import java.util.ArrayList;

public class forms_EntityModel  {






    private List<forms_Type> forms_types;


    public forms_EntityModel(
    ) {
        this.forms_types = new ArrayList<>();
    }

    public forms_EntityModel(
        ArrayList<forms_Type> forms_types    ) {
        this.forms_types = forms_types;
    }


    public List<forms_Type> getForms_types() {
        return forms_types;
    }

    public void addForms_type(Forms_type forms_type) {
        this.forms_types.add(forms_type);
    }

}