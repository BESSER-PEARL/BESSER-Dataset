





import java.util.List;
import java.util.ArrayList;

public class becontent_LongDate extends NotStructuredElement {

    private boolean isMandatory;
    private String name;
    private String label;



    public becontent_LongDate(
        boolean isMandatory,        String name,        String label    ) {
        super(
        );
        this.isMandatory = isMandatory;
        this.name = name;
        this.label = label;
    }


    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}