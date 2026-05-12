





import java.util.List;
import java.util.ArrayList;

public class stext_TimeEventSpec extends EventSpec {

    private String unit;
    private String type;
    private int value;



    public stext_TimeEventSpec(
        String unit,        String type,        int value    ) {
        super(
        );
        this.unit = unit;
        this.type = type;
        this.value = value;
    }


    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}