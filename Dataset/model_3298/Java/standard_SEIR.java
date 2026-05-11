





import java.util.List;
import java.util.ArrayList;

public class standard_SEIR extends SIR {

    private float incubationRate;



    public standard_SEIR(
        float incubationRate    ) {
        super(
        );
        this.incubationRate = incubationRate;
    }


    public float getIncubationrate() {
        return incubationRate;
    }

    public void setIncubationrate(float incubationRate) {
        this.incubationRate = incubationRate;
    }


}