





import java.util.List;
import java.util.ArrayList;

public class frontend_tao_ReferenceAssignment extends core_Variable, tao_Assignment {

    private String targetFeature;
    private boolean multivalued;



    public frontend_tao_ReferenceAssignment(
        String targetFeature,        boolean multivalued    ) {
        super(
        );
        this.targetFeature = targetFeature;
        this.multivalued = multivalued;
    }


    public String getTargetfeature() {
        return targetFeature;
    }

    public void setTargetfeature(String targetFeature) {
        this.targetFeature = targetFeature;
    }
    public boolean getMultivalued() {
        return multivalued;
    }

    public void setMultivalued(boolean multivalued) {
        this.multivalued = multivalued;
    }


}