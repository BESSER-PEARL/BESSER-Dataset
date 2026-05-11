





import java.util.List;
import java.util.ArrayList;

public class diva_PropertyLiteral extends NamedElement {

    private String value;





    private diva_Property diva_property;


    public diva_PropertyLiteral(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public diva_Property getDiva_property() {
        return diva_property;
    }

    public void setDiva_property(diva_Property diva_property) {
        this.diva_property = diva_property;
    }

}