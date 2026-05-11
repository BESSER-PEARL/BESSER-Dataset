





import java.util.List;
import java.util.ArrayList;

public class diva_PropertyValue extends DiVAModelElement {

    private String value;





    private diva_Variant diva_variant;




    private diva_Property diva_property;


    public diva_PropertyValue(
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

    public diva_Variant getDiva_variant() {
        return diva_variant;
    }

    public void setDiva_variant(diva_Variant diva_variant) {
        this.diva_variant = diva_variant;
    }
    public diva_Property getDiva_property() {
        return diva_property;
    }

    public void setDiva_property(diva_Property diva_property) {
        this.diva_property = diva_property;
    }

}