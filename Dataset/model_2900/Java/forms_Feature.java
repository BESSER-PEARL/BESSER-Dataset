





import java.util.List;
import java.util.ArrayList;

public class forms_Feature extends NamedElement {

    private String kind;





    private forms_Type forms_type;


    public forms_Feature(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public forms_Type getForms_type() {
        return forms_type;
    }

    public void setForms_type(forms_Type forms_type) {
        this.forms_type = forms_type;
    }

}