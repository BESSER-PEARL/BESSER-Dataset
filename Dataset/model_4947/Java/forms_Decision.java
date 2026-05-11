





import java.util.List;
import java.util.ArrayList;

public class forms_Decision extends ItemType {






    private List<forms_Option> forms_options;


    public forms_Decision(
    ) {
        super(
        );
        this.forms_options = new ArrayList<>();
    }

    public forms_Decision(
        ArrayList<forms_Option> forms_options    ) {
        this.forms_options = forms_options;
    }


    public List<forms_Option> getForms_options() {
        return forms_options;
    }

    public void addForms_option(Forms_option forms_option) {
        this.forms_options.add(forms_option);
    }

}