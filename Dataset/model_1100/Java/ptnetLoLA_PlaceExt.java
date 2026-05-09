





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_PlaceExt extends Place {

    private float probability;
    private boolean isStart;



    public ptnetLoLA_PlaceExt(
        float probability,        boolean isStart    ) {
        super(
        );
        this.probability = probability;
        this.isStart = isStart;
    }


    public float getProbability() {
        return probability;
    }

    public void setProbability(float probability) {
        this.probability = probability;
    }
    public boolean getIsstart() {
        return isStart;
    }

    public void setIsstart(boolean isStart) {
        this.isStart = isStart;
    }


}