





import java.util.List;
import java.util.ArrayList;

public class gama_EParameter extends EGamaObject {

    private String category;
    private String max;
    private String min;
    private String step;
    private String among;
    private String variable;
    private String init;



    public gama_EParameter(
        String category,        String max,        String min,        String step,        String among,        String variable,        String init    ) {
        super(
        );
        this.category = category;
        this.max = max;
        this.min = min;
        this.step = step;
        this.among = among;
        this.variable = variable;
        this.init = init;
    }


    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }
    public String getStep() {
        return step;
    }

    public void setStep(String step) {
        this.step = step;
    }
    public String getAmong() {
        return among;
    }

    public void setAmong(String among) {
        this.among = among;
    }
    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }
    public String getInit() {
        return init;
    }

    public void setInit(String init) {
        this.init = init;
    }


}