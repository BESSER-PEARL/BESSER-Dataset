





import java.util.List;
import java.util.ArrayList;

public class entityDsl_Label  {

    private String text;





    private entityDsl_Attribute entitydsl_attribute;


    public entityDsl_Label(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public entityDsl_Attribute getEntitydsl_attribute() {
        return entitydsl_attribute;
    }

    public void setEntitydsl_attribute(entityDsl_Attribute entitydsl_attribute) {
        this.entitydsl_attribute = entitydsl_attribute;
    }

}