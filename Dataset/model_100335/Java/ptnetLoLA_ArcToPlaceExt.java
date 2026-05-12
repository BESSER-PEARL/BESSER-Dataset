





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_ArcToPlaceExt extends ArcToPlace {

    private float probability;



    public ptnetLoLA_ArcToPlaceExt(
        float probability    ) {
        super(
        );
        this.probability = probability;
    }


    public float getProbability() {
        return probability;
    }

    public void setProbability(float probability) {
        this.probability = probability;
    }


}