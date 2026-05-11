





import java.util.List;
import java.util.ArrayList;

public class standard_StandardStochasticDiseaseModel extends StochasticDiseaseModel {

    private float gain;



    public standard_StandardStochasticDiseaseModel(
        float gain    ) {
        super(
        );
        this.gain = gain;
    }


    public float getGain() {
        return gain;
    }

    public void setGain(float gain) {
        this.gain = gain;
    }


}