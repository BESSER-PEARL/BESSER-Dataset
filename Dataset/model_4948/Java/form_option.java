





import java.util.List;
import java.util.ArrayList;

public class form_option  {

    private String value;
    private String content;





    private form_SelectionList form_selectionlist;


    public form_option(
        String value,        String content    ) {
        this.value = value;
        this.content = content;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public form_SelectionList getForm_selectionlist() {
        return form_selectionlist;
    }

    public void setForm_selectionlist(form_SelectionList form_selectionlist) {
        this.form_selectionlist = form_selectionlist;
    }

}