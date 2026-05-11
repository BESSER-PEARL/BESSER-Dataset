





import java.util.List;
import java.util.ArrayList;

public class core_COREImpactNode extends COREModelElement {

    private float offset;
    private float scalingFactor;





    private core_COREImpactModel core_coreimpactmodel;


    public core_COREImpactNode(
        float offset,        float scalingFactor    ) {
        super(
        );
        this.offset = offset;
        this.scalingFactor = scalingFactor;
    }


    public float getOffset() {
        return offset;
    }

    public void setOffset(float offset) {
        this.offset = offset;
    }
    public float getScalingfactor() {
        return scalingFactor;
    }

    public void setScalingfactor(float scalingFactor) {
        this.scalingFactor = scalingFactor;
    }

    public core_COREImpactModel getCore_coreimpactmodel() {
        return core_coreimpactmodel;
    }

    public void setCore_coreimpactmodel(core_COREImpactModel core_coreimpactmodel) {
        this.core_coreimpactmodel = core_coreimpactmodel;
    }

}