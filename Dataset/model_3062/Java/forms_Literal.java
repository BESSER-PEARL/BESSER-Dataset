





import java.util.List;
import java.util.ArrayList;

public class forms_Literal  {

    private String Value;
    private String name;





    private forms_Enumeration forms_enumeration;


    public forms_Literal(
        String Value,        String name    ) {
        this.Value = Value;
        this.name = name;
    }


    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public forms_Enumeration getForms_enumeration() {
        return forms_enumeration;
    }

    public void setForms_enumeration(forms_Enumeration forms_enumeration) {
        this.forms_enumeration = forms_enumeration;
    }

}