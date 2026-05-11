





import java.util.List;
import java.util.ArrayList;

public class forms_Choice extends ItemType {

    private boolean multiple;





    private List<forms_Option> forms_options;


    public forms_Choice(
        boolean multiple    ) {
        super(
        );
        this.multiple = multiple;
        this.forms_options = new ArrayList<>();
    }

    public forms_Choice(
        boolean multiple        ArrayList<forms_Option> forms_options    ) {
        this.multiple = multiple;
        this.forms_options = forms_options;
    }

    public boolean getMultiple() {
        return multiple;
    }

    public void setMultiple(boolean multiple) {
        this.multiple = multiple;
    }

    public List<forms_Option> getForms_options() {
        return forms_options;
    }

    public void addForms_option(Forms_option forms_option) {
        this.forms_options.add(forms_option);
    }

}