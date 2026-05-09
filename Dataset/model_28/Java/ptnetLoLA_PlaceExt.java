





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_PlaceExt extends Place {

    private boolean isStart;
    private float probability;



    public ptnetLoLA_PlaceExt(
        boolean isStart,        float probability    ) {
        super(
        );
        this.isStart = isStart;
        this.probability = probability;
    }


    public boolean getIsstart() {
        return isStart;
    }

    public void setIsstart(boolean isStart) {
        this.isStart = isStart;
    }
    public float getProbability() {
        return probability;
    }

    public void setProbability(float probability) {
        this.probability = probability;
    }


}