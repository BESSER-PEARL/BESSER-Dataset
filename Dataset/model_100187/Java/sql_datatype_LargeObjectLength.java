





import java.util.List;
import java.util.ArrayList;

public class sql_datatype_LargeObjectLength  {

    private String units;
    private String value;
    private String multiplier;



    public sql_datatype_LargeObjectLength(
        String units,        String value,        String multiplier    ) {
        this.units = units;
        this.value = value;
        this.multiplier = multiplier;
    }


    public String getUnits() {
        return units;
    }

    public void setUnits(String units) {
        this.units = units;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getMultiplier() {
        return multiplier;
    }

    public void setMultiplier(String multiplier) {
        this.multiplier = multiplier;
    }


}