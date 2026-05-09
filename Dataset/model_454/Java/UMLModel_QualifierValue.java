





import java.util.List;
import java.util.ArrayList;

public class UMLModel_QualifierValue extends Element {

    private String value;
    private String qualifier;



    public UMLModel_QualifierValue(
        String value,        String qualifier    ) {
        super(
        );
        this.value = value;
        this.qualifier = qualifier;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getQualifier() {
        return qualifier;
    }

    public void setQualifier(String qualifier) {
        this.qualifier = qualifier;
    }


}