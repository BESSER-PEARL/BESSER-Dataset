





import java.util.List;
import java.util.ArrayList;

public class forms_Item  {

    private String explanation;
    private String text;





    private forms_Group forms_group;


    public forms_Item(
        String explanation,        String text    ) {
        this.explanation = explanation;
        this.text = text;
    }


    public String getExplanation() {
        return explanation;
    }

    public void setExplanation(String explanation) {
        this.explanation = explanation;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public forms_Group getForms_group() {
        return forms_group;
    }

    public void setForms_group(forms_Group forms_group) {
        this.forms_group = forms_group;
    }

}