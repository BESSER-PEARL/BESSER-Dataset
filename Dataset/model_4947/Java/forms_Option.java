





import java.util.List;
import java.util.ArrayList;

public class forms_Option  {

    private String text;
    private String id;





    private forms_Item forms_item;


    public forms_Option(
        String text,        String id    ) {
        this.text = text;
        this.id = id;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public forms_Item getForms_item() {
        return forms_item;
    }

    public void setForms_item(forms_Item forms_item) {
        this.forms_item = forms_item;
    }

}