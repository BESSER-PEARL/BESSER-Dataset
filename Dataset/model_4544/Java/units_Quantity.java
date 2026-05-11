





import java.util.List;
import java.util.ArrayList;

public class units_Quantity  {

    private String value;





    private units_Unit units_unit;


    public units_Quantity(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public units_Unit getUnits_unit() {
        return units_unit;
    }

    public void setUnits_unit(units_Unit units_unit) {
        this.units_unit = units_unit;
    }

}