





import java.util.List;
import java.util.ArrayList;

public class Backpropagation  {

    private float BiasesWeigths;
    private float output;
    private float Weigths;
    private float target;





    private Forward forward;


    public Backpropagation(
        float BiasesWeigths,        float output,        float Weigths,        float target    ) {
        this.BiasesWeigths = BiasesWeigths;
        this.output = output;
        this.Weigths = Weigths;
        this.target = target;
    }


    public float getBiasesweigths() {
        return BiasesWeigths;
    }

    public void setBiasesweigths(float BiasesWeigths) {
        this.BiasesWeigths = BiasesWeigths;
    }
    public float getOutput() {
        return output;
    }

    public void setOutput(float output) {
        this.output = output;
    }
    public float getWeigths() {
        return Weigths;
    }

    public void setWeigths(float Weigths) {
        this.Weigths = Weigths;
    }
    public float getTarget() {
        return target;
    }

    public void setTarget(float target) {
        this.target = target;
    }

    public Forward getForward() {
        return forward;
    }

    public void setForward(Forward forward) {
        this.forward = forward;
    }

}