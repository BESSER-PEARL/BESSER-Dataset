





import java.util.List;
import java.util.ArrayList;

public class form_Editable extends Element {

    private String name;
    private boolean disabled;





    private form_Label form_label;


    public form_Editable(
        String name,        boolean disabled    ) {
        super(
        );
        this.name = name;
        this.disabled = disabled;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getDisabled() {
        return disabled;
    }

    public void setDisabled(boolean disabled) {
        this.disabled = disabled;
    }

    public form_Label getForm_label() {
        return form_label;
    }

    public void setForm_label(form_Label form_label) {
        this.form_label = form_label;
    }

}