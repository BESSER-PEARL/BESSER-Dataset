





import java.util.List;
import java.util.ArrayList;

public class units_av_pc_UnitPower extends Unit {

    private int exponent;





    private units_av_pc_Unit units_av_pc_unit;


    public units_av_pc_UnitPower(
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

    public units_av_pc_Unit getUnits_av_pc_unit() {
        return units_av_pc_unit;
    }

    public void setUnits_av_pc_unit(units_av_pc_Unit units_av_pc_unit) {
        this.units_av_pc_unit = units_av_pc_unit;
    }

}