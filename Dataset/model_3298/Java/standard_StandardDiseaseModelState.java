





import java.util.List;
import java.util.ArrayList;

public class standard_StandardDiseaseModelState extends DiseaseModelState {

    private float areaRatio;



    public standard_StandardDiseaseModelState(
        float areaRatio    ) {
        super(
        );
        this.areaRatio = areaRatio;
    }


    public float getArearatio() {
        return areaRatio;
    }

    public void setArearatio(float areaRatio) {
        this.areaRatio = areaRatio;
    }


}