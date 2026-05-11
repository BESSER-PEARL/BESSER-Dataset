





import java.util.List;
import java.util.ArrayList;

public class vM_Feature extends FeatureDefinition {

    private boolean notDecidable;
    private boolean notTranslatable;
    private String name;
    private String min;
    private boolean optional;
    private String max;
    private boolean runTime;





    private vM_FeatureHierarchy vm_featurehierarchy;


    public vM_Feature(
        boolean notDecidable,        boolean notTranslatable,        String name,        String min,        boolean optional,        String max,        boolean runTime    ) {
        super(
        );
        this.notDecidable = notDecidable;
        this.notTranslatable = notTranslatable;
        this.name = name;
        this.min = min;
        this.optional = optional;
        this.max = max;
        this.runTime = runTime;
    }


    public boolean getNotdecidable() {
        return notDecidable;
    }

    public void setNotdecidable(boolean notDecidable) {
        this.notDecidable = notDecidable;
    }
    public boolean getNottranslatable() {
        return notTranslatable;
    }

    public void setNottranslatable(boolean notTranslatable) {
        this.notTranslatable = notTranslatable;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }
    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }
    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }
    public boolean getRuntime() {
        return runTime;
    }

    public void setRuntime(boolean runTime) {
        this.runTime = runTime;
    }

    public vM_FeatureHierarchy getVm_featurehierarchy() {
        return vm_featurehierarchy;
    }

    public void setVm_featurehierarchy(vM_FeatureHierarchy vm_featurehierarchy) {
        this.vm_featurehierarchy = vm_featurehierarchy;
    }

}