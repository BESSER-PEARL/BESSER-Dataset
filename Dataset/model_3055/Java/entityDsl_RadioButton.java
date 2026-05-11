





import java.util.List;
import java.util.ArrayList;

public class entityDsl_RadioButton  {

    private String text;





    private entityDsl_RadioButtonGroup entitydsl_radiobuttongroup;


    public entityDsl_RadioButton(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public entityDsl_RadioButtonGroup getEntitydsl_radiobuttongroup() {
        return entitydsl_radiobuttongroup;
    }

    public void setEntitydsl_radiobuttongroup(entityDsl_RadioButtonGroup entitydsl_radiobuttongroup) {
        this.entitydsl_radiobuttongroup = entitydsl_radiobuttongroup;
    }

}