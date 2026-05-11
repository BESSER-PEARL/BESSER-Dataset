





import java.util.List;
import java.util.ArrayList;

public class smalluml_EnumerationElement  {

    private String value;





    private smalluml_Enumeration smalluml_enumeration;


    public smalluml_EnumerationElement(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public smalluml_Enumeration getSmalluml_enumeration() {
        return smalluml_enumeration;
    }

    public void setSmalluml_enumeration(smalluml_Enumeration smalluml_enumeration) {
        this.smalluml_enumeration = smalluml_enumeration;
    }

}