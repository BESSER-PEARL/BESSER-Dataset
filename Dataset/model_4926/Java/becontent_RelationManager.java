





import java.util.List;
import java.util.ArrayList;

public class becontent_RelationManager extends NotStructuredElement {

    private String label;
    private String orientation;
    private String name;
    private String restrictCondition;



    public becontent_RelationManager(
        String label,        String orientation,        String name,        String restrictCondition    ) {
        super(
        );
        this.label = label;
        this.orientation = orientation;
        this.name = name;
        this.restrictCondition = restrictCondition;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
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


}