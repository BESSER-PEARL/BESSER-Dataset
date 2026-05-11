





import java.util.List;
import java.util.ArrayList;

public class diva_PropertyValue extends DiVAModelElement {

    private String value;



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


}