





import java.util.List;
import java.util.ArrayList;

public class sPLOT2CoCo_OrAlternativeTreeConstraint extends TreeConstraint {

    private int max;
    private int min;





    private List<sPLOT2CoCo_Feature> splot2coco_features;


    public sPLOT2CoCo_OrAlternativeTreeConstraint(
        int max,        int min    ) {
        super(
        );
        this.max = max;
        this.min = min;
        this.splot2coco_features = new ArrayList<>();
    }

    public sPLOT2CoCo_OrAlternativeTreeConstraint(
        int max,        int min        ArrayList<sPLOT2CoCo_Feature> splot2coco_features    ) {
        this.max = max;
        this.min = min;
        this.splot2coco_features = splot2coco_features;
    }

    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }

    public List<sPLOT2CoCo_Feature> getSplot2coco_features() {
        return splot2coco_features;
    }

    public void addSplot2coco_feature(Splot2coco_feature splot2coco_feature) {
        this.splot2coco_features.add(splot2coco_feature);
    }

}