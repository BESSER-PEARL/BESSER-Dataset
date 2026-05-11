





import java.util.List;
import java.util.ArrayList;

public class smalluml_Enumeration extends Type, NamedElement {

    private String values;



    public smalluml_Enumeration(
        String values    ) {
        super(
        );
        this.values = values;
    }


    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }


}