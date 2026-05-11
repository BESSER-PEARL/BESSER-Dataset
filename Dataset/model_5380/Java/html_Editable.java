





import java.util.List;
import java.util.ArrayList;

public class html_Editable extends FormElement {

    private boolean required;
    private int name;





    private html_Label html_label;


    public html_Editable(
        boolean required,        int name    ) {
        super(
        );
        this.required = required;
        this.name = name;
    }


    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public int getName() {
        return name;
    }

    public void setName(int name) {
        this.name = name;
    }

    public html_Label getHtml_label() {
        return html_label;
    }

    public void setHtml_label(html_Label html_label) {
        this.html_label = html_label;
    }

}