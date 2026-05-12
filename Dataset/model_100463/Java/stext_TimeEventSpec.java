





import java.util.List;
import java.util.ArrayList;

public class stext_TimeEventSpec extends EventSpec {

    private int value;
    private String unit;
    private String type;



    public stext_TimeEventSpec(
        int value,        String unit,        String type    ) {
        super(
        );
        this.value = value;
        this.unit = unit;
        this.type = type;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}