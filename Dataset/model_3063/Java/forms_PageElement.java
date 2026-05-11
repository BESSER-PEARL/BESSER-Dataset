





import java.util.List;
import java.util.ArrayList;

public class forms_PageElement  {

    private String elementID;
    private String label;





    private forms_Page forms_page;




    private forms_Condition forms_condition;


    public forms_PageElement(
        String elementID,        String label    ) {
        this.elementID = elementID;
        this.label = label;
    }


    public String getElementid() {
        return elementID;
    }

    public void setElementid(String elementID) {
        this.elementID = elementID;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public forms_Page getForms_page() {
        return forms_page;
    }

    public void setForms_page(forms_Page forms_page) {
        this.forms_page = forms_page;
    }
    public forms_Condition getForms_condition() {
        return forms_condition;
    }

    public void setForms_condition(forms_Condition forms_condition) {
        this.forms_condition = forms_condition;
    }

}