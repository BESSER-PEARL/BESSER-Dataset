





import java.util.List;
import java.util.ArrayList;

public class forms_Enumeration  {

    private String name;





    private forms_Attribute forms_attribute;


    public forms_Enumeration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public forms_Attribute getForms_attribute() {
        return forms_attribute;
    }

    public void setForms_attribute(forms_Attribute forms_attribute) {
        this.forms_attribute = forms_attribute;
    }

}