





import java.util.List;
import java.util.ArrayList;

public class sql_datatype_LargeObjectLength  {

    private String value;
    private String multiplier;
    private String units;



    public sql_datatype_LargeObjectLength(
        String value,        String multiplier,        String units    ) {
        this.value = value;
        this.multiplier = multiplier;
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
    public String getUnits() {
        return units;
    }

    public void setUnits(String units) {
        this.units = units;
    }


}