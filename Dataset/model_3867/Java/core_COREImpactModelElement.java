





import java.util.List;
import java.util.ArrayList;

public class core_COREImpactModelElement extends COREModelElement {

    private float scalingFactor;
    private float offset;





    private core_COREImpactModel core_coreimpactmodel;


    public core_COREImpactModelElement(
        float scalingFactor,        float offset    ) {
        super(
        );
        this.scalingFactor = scalingFactor;
        this.offset = offset;
    }


    public float getScalingfactor() {
        return scalingFactor;
    }

    public void setScalingfactor(float scalingFactor) {
        this.scalingFactor = scalingFactor;
    }
    public float getOffset() {
        return offset;
    }

    public void setOffset(float offset) {
        this.offset = offset;
    }

    public core_COREImpactModel getCore_coreimpactmodel() {
        return core_coreimpactmodel;
    }

    public void setCore_coreimpactmodel(core_COREImpactModel core_coreimpactmodel) {
        this.core_coreimpactmodel = core_coreimpactmodel;
    }

}