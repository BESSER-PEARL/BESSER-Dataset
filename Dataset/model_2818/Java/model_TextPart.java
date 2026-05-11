





import java.util.List;
import java.util.ArrayList;

public class model_TextPart  {

    private boolean editable;
    private String text;





    private model_EAttribute model_eattribute;




    private model_TextValue model_textvalue;


    public model_TextPart(
        boolean editable,        String text    ) {
        this.editable = editable;
        this.text = text;
    }


    public boolean getEditable() {
        return editable;
    }

    public void setEditable(boolean editable) {
        this.editable = editable;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public model_EAttribute getModel_eattribute() {
        return model_eattribute;
    }

    public void setModel_eattribute(model_EAttribute model_eattribute) {
        this.model_eattribute = model_eattribute;
    }
    public model_TextValue getModel_textvalue() {
        return model_textvalue;
    }

    public void setModel_textvalue(model_TextValue model_textvalue) {
        this.model_textvalue = model_textvalue;
    }

}