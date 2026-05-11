





import java.util.List;
import java.util.ArrayList;

public class becontent_SelectFromReference extends NotStructuredElement {

    private String name;
    private String label;
    private boolean isMandatory;
    private String restrictCondition;



    public becontent_SelectFromReference(
        String name,        String label,        boolean isMandatory,        String restrictCondition    ) {
        super(
        );
        this.name = name;
        this.label = label;
        this.isMandatory = isMandatory;
        this.restrictCondition = restrictCondition;
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
    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }
    public String getRestrictcondition() {
        return restrictCondition;
    }

    public void setRestrictcondition(String restrictCondition) {
        this.restrictCondition = restrictCondition;
    }


}