





import java.util.List;
import java.util.ArrayList;

public class units_Quantity  {

    private float value;





    private units_Unit units_unit;


    public units_Quantity(
        float value    ) {
        this.value = value;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }

    public units_Unit getUnits_unit() {
        return units_unit;
    }

    public void setUnits_unit(units_Unit units_unit) {
        this.units_unit = units_unit;
    }

}