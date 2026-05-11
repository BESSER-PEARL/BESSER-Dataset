





import java.util.List;
import java.util.ArrayList;

public class units_UnitPower extends Unit {

    private int exponent;





    private units_Unit units_unit;


    public units_UnitPower(
        int exponent    ) {
        super(
        );
        this.exponent = exponent;
    }


    public int getExponent() {
        return exponent;
    }

    public void setExponent(int exponent) {
        this.exponent = exponent;
    }

    public units_Unit getUnits_unit() {
        return units_unit;
    }

    public void setUnits_unit(units_Unit units_unit) {
        this.units_unit = units_unit;
    }

}