





import java.util.List;
import java.util.ArrayList;

public class workflow_TypedElement  {

    private String valueAsString;
    private String typeAsString;



    public workflow_TypedElement(
        String valueAsString,        String typeAsString    ) {
        this.valueAsString = valueAsString;
        this.typeAsString = typeAsString;
    }


    public String getValueasstring() {
        return valueAsString;
    }

    public void setValueasstring(String valueAsString) {
        this.valueAsString = valueAsString;
    }
    public String getTypeasstring() {
        return typeAsString;
    }

    public void setTypeasstring(String typeAsString) {
        this.typeAsString = typeAsString;
    }


}