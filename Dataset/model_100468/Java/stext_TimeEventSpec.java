





import java.util.List;
import java.util.ArrayList;

public class stext_TimeEventSpec extends EventSpec {

    private int value;
    private String unit;



    public stext_TimeEventSpec(
        int value,        String unit    ) {
        super(
        );
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