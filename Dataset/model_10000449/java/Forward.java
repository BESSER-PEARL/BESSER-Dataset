





import java.util.List;
import java.util.ArrayList;

public class Forward  {

    private float BiasesWeigths;
    private float Input;
    private float Weights;



    public Forward(
        float BiasesWeigths,        float Input,        float Weights    ) {
        this.BiasesWeigths = BiasesWeigths;
        this.Input = Input;
        this.Weights = Weights;
    }


    public float getBiasesweigths() {
        return BiasesWeigths;
    }

    public void setBiasesweigths(float BiasesWeigths) {
        this.BiasesWeigths = BiasesWeigths;
    }
    public float getInput() {
        return Input;
    }

    public void setInput(float Input) {
        this.Input = Input;
    }
    public float getWeights() {
        return Weights;
    }

    public void setWeights(float Weights) {
        this.Weights = Weights;
    }


}