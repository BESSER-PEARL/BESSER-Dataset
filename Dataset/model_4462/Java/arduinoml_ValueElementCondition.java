





import java.util.List;
import java.util.ArrayList;

public class arduinoml_ValueElementCondition extends Condition {

    private float value;
    private String comparator;



    public arduinoml_ValueElementCondition(
        float value,        String comparator    ) {
        super(
        );
        this.value = value;
        this.comparator = comparator;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }
    public String getComparator() {
        return comparator;
    }

    public void setComparator(String comparator) {
        this.comparator = comparator;
    }


}