





import java.util.List;
import java.util.ArrayList;

public class Measure_IntegerMeasure extends Measure {

    private String value;



    public Measure_IntegerMeasure(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}