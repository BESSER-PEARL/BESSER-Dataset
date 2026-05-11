





import java.util.List;
import java.util.ArrayList;

public class arduino_Delay extends Utilities {

    private String unit;
    private int value;



    public arduino_Delay(
        String unit,        int value    ) {
        super(
        );
        this.unit = unit;
        this.value = value;
    }


    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}