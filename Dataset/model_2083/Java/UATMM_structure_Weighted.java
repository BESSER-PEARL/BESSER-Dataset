





import java.util.List;
import java.util.ArrayList;

public class UATMM_structure_Weighted extends Connector {

    private float Weights;
    private float Treshold;



    public UATMM_structure_Weighted(
        float Weights,        float Treshold    ) {
        super(
        );
        this.Weights = Weights;
        this.Treshold = Treshold;
    }


    public float getWeights() {
        return Weights;
    }

    public void setWeights(float Weights) {
        this.Weights = Weights;
    }
    public float getTreshold() {
        return Treshold;
    }

    public void setTreshold(float Treshold) {
        this.Treshold = Treshold;
    }


}