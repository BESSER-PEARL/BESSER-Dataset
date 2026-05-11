





import java.util.List;
import java.util.ArrayList;

public class forms_Model  {






    private List<forms_Enumeration> forms_enumerations;


    public forms_Model(
    ) {
        this.forms_enumerations = new ArrayList<>();
    }

    public forms_Model(
        ArrayList<forms_Enumeration> forms_enumerations    ) {
        this.forms_enumerations = forms_enumerations;
    }


    public List<forms_Enumeration> getForms_enumerations() {
        return forms_enumerations;
    }

    public void addForms_enumeration(Forms_enumeration forms_enumeration) {
        this.forms_enumerations.add(forms_enumeration);
    }

}