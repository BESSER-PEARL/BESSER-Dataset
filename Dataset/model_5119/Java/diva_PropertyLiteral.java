





import java.util.List;
import java.util.ArrayList;

public class diva_PropertyLiteral extends NamedElement {

    private String value;



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


}