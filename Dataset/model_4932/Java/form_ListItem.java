





import java.util.List;
import java.util.ArrayList;

public class form_ListItem  {

    private String label;





    private form_List form_list;


    public form_ListItem(
        String label    ) {
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public form_List getForm_list() {
        return form_list;
    }

    public void setForm_list(form_List form_list) {
        this.form_list = form_list;
    }

}