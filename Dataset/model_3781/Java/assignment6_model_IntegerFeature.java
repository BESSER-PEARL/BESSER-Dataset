





import java.util.List;
import java.util.ArrayList;

public class assignment6_model_IntegerFeature extends Feature {

    private int step;
    private int value;
    private int maxValue;
    private int minValue;



    public assignment6_model_IntegerFeature(
        int step,        int value,        int maxValue,        int minValue    ) {
        super(
        );
        this.step = step;
        this.value = value;
        this.maxValue = maxValue;
        this.minValue = minValue;
    }


    public int getStep() {
        return step;
    }

    public void setStep(int step) {
        this.step = step;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public int getMaxvalue() {
        return maxValue;
    }

    public void setMaxvalue(int maxValue) {
        this.maxValue = maxValue;
    }
    public int getMinvalue() {
        return minValue;
    }

    public void setMinvalue(int minValue) {
        this.minValue = minValue;
    }


}