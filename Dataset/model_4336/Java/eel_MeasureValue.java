





import java.util.List;
import java.util.ArrayList;

public class eel_MeasureValue extends TypedMeasure {

    private String value;



    public eel_MeasureValue(
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