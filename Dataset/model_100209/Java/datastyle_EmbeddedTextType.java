





import java.util.List;
import java.util.ArrayList;

public class datastyle_EmbeddedTextType  {

    private String position;
    private String mixed;





    private datastyle_NumberType datastyle_numbertype;


    public datastyle_EmbeddedTextType(
        String position,        String mixed    ) {
        this.position = position;
        this.mixed = mixed;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public datastyle_NumberType getDatastyle_numbertype() {
        return datastyle_numbertype;
    }

    public void setDatastyle_numbertype(datastyle_NumberType datastyle_numbertype) {
        this.datastyle_numbertype = datastyle_numbertype;
    }

}