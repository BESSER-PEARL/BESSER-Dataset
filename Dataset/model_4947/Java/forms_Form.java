





import java.util.List;
import java.util.ArrayList;

public class forms_Form  {

    private String caption;





    private List<forms_Group> forms_groups;


    public forms_Form(
        String caption    ) {
        this.caption = caption;
        this.forms_groups = new ArrayList<>();
    }

    public forms_Form(
        String caption        ArrayList<forms_Group> forms_groups    ) {
        this.caption = caption;
        this.forms_groups = forms_groups;
    }

    public String getCaption() {
        return caption;
    }

    public void setCaption(String caption) {
        this.caption = caption;
    }

    public List<forms_Group> getForms_groups() {
        return forms_groups;
    }

    public void addForms_group(Forms_group forms_group) {
        this.forms_groups.add(forms_group);
    }

}