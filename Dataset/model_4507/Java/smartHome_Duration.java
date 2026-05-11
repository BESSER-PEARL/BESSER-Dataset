





import java.util.List;
import java.util.ArrayList;

public class smartHome_Duration  {

    private int value;
    private String unit;



    public smartHome_Duration(
        int value,        String unit    ) {
        this.value = value;
        this.unit = unit;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }


}