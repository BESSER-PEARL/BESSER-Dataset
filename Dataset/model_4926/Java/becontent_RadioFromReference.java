





import java.util.List;
import java.util.ArrayList;

public class becontent_RadioFromReference extends NotStructuredElement {

    private String name;
    private String restrictCondition;
    private boolean isMandatory;
    private String label;



    public becontent_RadioFromReference(
        String name,        String restrictCondition,        boolean isMandatory,        String label    ) {
        super(
        );
        this.name = name;
        this.restrictCondition = restrictCondition;
        this.isMandatory = isMandatory;
        this.label = label;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRestrictcondition() {
        return restrictCondition;
    }

    public void setRestrictcondition(String restrictCondition) {
        this.restrictCondition = restrictCondition;
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