





import java.util.List;
import java.util.ArrayList;

public class stext_TimeEventSpec extends EventSpec {

    private String unit;
    private int value;
    private String type;



    public stext_TimeEventSpec(
        String unit,        int value,        String type    ) {
        super(
        );
        this.unit = unit;
        this.value = value;
        this.type = type;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}