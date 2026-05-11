





import java.util.List;
import java.util.ArrayList;

public class forms_Page  {

    private String title;





    private forms_Condition forms_condition;




    private forms_Form forms_form;


    public forms_Page(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public forms_Condition getForms_condition() {
        return forms_condition;
    }

    public void setForms_condition(forms_Condition forms_condition) {
        this.forms_condition = forms_condition;
    }
    public forms_Form getForms_form() {
        return forms_form;
    }

    public void setForms_form(forms_Form forms_form) {
        this.forms_form = forms_form;
    }

}