





import java.util.List;
import java.util.ArrayList;

public class forms_EnumerationLiteral  {

    private String value;
    private String name;





    private forms_EnumerationType forms_enumerationtype;


    public forms_EnumerationLiteral(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public forms_EnumerationType getForms_enumerationtype() {
        return forms_enumerationtype;
    }

    public void setForms_enumerationtype(forms_EnumerationType forms_enumerationtype) {
        this.forms_enumerationtype = forms_enumerationtype;
    }

}