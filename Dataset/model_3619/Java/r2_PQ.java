





import java.util.List;
import java.util.ArrayList;

public class r2_PQ extends QTY {

    private String value;
    private String unit;



    public r2_PQ(
        String value,        String unit    ) {
        super(
        );
        this.value = value;
        this.unit = unit;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }


}