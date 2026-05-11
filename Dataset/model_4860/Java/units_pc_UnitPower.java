





import java.util.List;
import java.util.ArrayList;

public class units_pc_UnitPower extends Unit {

    private int exponent;





    private units_pc_Unit units_pc_unit;


    public units_pc_UnitPower(
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

    public units_pc_Unit getUnits_pc_unit() {
        return units_pc_unit;
    }

    public void setUnits_pc_unit(units_pc_Unit units_pc_unit) {
        this.units_pc_unit = units_pc_unit;
    }

}