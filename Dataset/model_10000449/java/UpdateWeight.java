





import java.util.List;
import java.util.ArrayList;

public class UpdateWeight  {

    private float Weights;
    private float BiasesWeigths;





    private Backpropagation backpropagation;


    public UpdateWeight(
        float Weights,        float BiasesWeigths    ) {
        this.Weights = Weights;
        this.BiasesWeigths = BiasesWeigths;
    }


    public float getWeights() {
        return Weights;
    }

    public void setWeights(float Weights) {
        this.Weights = Weights;
    }
    public float getBiasesweigths() {
        return BiasesWeigths;
    }

    public void setBiasesweigths(float BiasesWeigths) {
        this.BiasesWeigths = BiasesWeigths;
    }

    public Backpropagation getBackpropagation() {
        return backpropagation;
    }

    public void setBackpropagation(Backpropagation backpropagation) {
        this.backpropagation = backpropagation;
    }

}