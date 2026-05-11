





import java.util.List;
import java.util.ArrayList;

public class edges_MixingEdgeLabelValue extends LabelValue {

    private float mixingRate;



    public edges_MixingEdgeLabelValue(
        float mixingRate    ) {
        super(
        );
        this.mixingRate = mixingRate;
    }


    public float getMixingrate() {
        return mixingRate;
    }

    public void setMixingrate(float mixingRate) {
        this.mixingRate = mixingRate;
    }


}