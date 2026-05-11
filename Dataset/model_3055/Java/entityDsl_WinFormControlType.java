





import java.util.List;
import java.util.ArrayList;

public class entityDsl_WinFormControlType  {

    private String name;





    private entityDsl_TextBox entitydsl_textbox;




    private entityDsl_Attribute entitydsl_attribute;


    public entityDsl_WinFormControlType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public entityDsl_TextBox getEntitydsl_textbox() {
        return entitydsl_textbox;
    }

    public void setEntitydsl_textbox(entityDsl_TextBox entitydsl_textbox) {
        this.entitydsl_textbox = entitydsl_textbox;
    }
    public entityDsl_Attribute getEntitydsl_attribute() {
        return entitydsl_attribute;
    }

    public void setEntitydsl_attribute(entityDsl_Attribute entitydsl_attribute) {
        this.entitydsl_attribute = entitydsl_attribute;
    }

}