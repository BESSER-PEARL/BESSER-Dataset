





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_RandomDoubleNumberType extends RandomNumberType {

    private float min;



    public mutatorenvironment_RandomDoubleNumberType(
        float min    ) {
        super(
        );
        this.min = min;
    }


    public float getMin() {
        return min;
    }

    public void setMin(float min) {
        this.min = min;
    }


}