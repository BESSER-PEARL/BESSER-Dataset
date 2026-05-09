





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_RandomDoubleType extends DoubleType {

    private float min;
    private None allowsNull;
    private float max;



    public mutatorenvironment_RandomDoubleType(
        float min,        None allowsNull,        float max    ) {
        super(
        );
        this.min = min;
        this.allowsNull = allowsNull;
        this.max = max;
    }


    public float getMin() {
        return min;
    }

    public void setMin(float min) {
        this.min = min;
    }
    public None getAllowsnull() {
        return allowsNull;
    }

    public void setAllowsnull(None allowsNull) {
        this.allowsNull = allowsNull;
    }
    public float getMax() {
        return max;
    }

    public void setMax(float max) {
        this.max = max;
    }


}