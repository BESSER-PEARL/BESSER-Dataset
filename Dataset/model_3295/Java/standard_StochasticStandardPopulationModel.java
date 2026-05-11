





import java.util.List;
import java.util.ArrayList;

public class standard_StochasticStandardPopulationModel extends StandardPopulationModel {

    private float gain;



    public standard_StochasticStandardPopulationModel(
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