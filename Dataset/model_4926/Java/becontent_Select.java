





import java.util.List;
import java.util.ArrayList;

public class becontent_Select extends NotStructuredElement {

    private String name;
    private String values;
    private boolean isMandatory;
    private String label;



    public becontent_Select(
        String name,        String values,        boolean isMandatory,        String label    ) {
        super(
        );
        this.name = name;
        this.values = values;
        this.isMandatory = isMandatory;
        this.label = label;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }
    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}