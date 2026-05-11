





import java.util.List;
import java.util.ArrayList;

public class vM_Feature extends FeatureDefinition {

    private String name;
    private String max;
    private boolean notTranslatable;
    private String min;
    private boolean runTime;
    private boolean notDecidable;
    private boolean optional;





    private vM_FeatureHierarchy vm_featurehierarchy;


    public vM_Feature(
        String name,        String max,        boolean notTranslatable,        String min,        boolean runTime,        boolean notDecidable,        boolean optional    ) {
        super(
        );
        this.name = name;
        this.max = max;
        this.notTranslatable = notTranslatable;
        this.min = min;
        this.runTime = runTime;
        this.notDecidable = notDecidable;
        this.optional = optional;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }
    public boolean getNottranslatable() {
        return notTranslatable;
    }

    public void setNottranslatable(boolean notTranslatable) {
        this.notTranslatable = notTranslatable;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }
    public boolean getRuntime() {
        return runTime;
    }

    public void setRuntime(boolean runTime) {
        this.runTime = runTime;
    }
    public boolean getNotdecidable() {
        return notDecidable;
    }

    public void setNotdecidable(boolean notDecidable) {
        this.notDecidable = notDecidable;
    }
    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }

    public vM_FeatureHierarchy getVm_featurehierarchy() {
        return vm_featurehierarchy;
    }

    public void setVm_featurehierarchy(vM_FeatureHierarchy vm_featurehierarchy) {
        this.vm_featurehierarchy = vm_featurehierarchy;
    }

}