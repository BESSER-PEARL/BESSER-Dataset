





import java.util.List;
import java.util.ArrayList;

public class units_av_av_UnitPower extends Unit {

    private int exponent;





    private units_av_av_Unit units_av_av_unit;


    public units_av_av_UnitPower(
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

    public units_av_av_Unit getUnits_av_av_unit() {
        return units_av_av_unit;
    }

    public void setUnits_av_av_unit(units_av_av_Unit units_av_av_unit) {
        this.units_av_av_unit = units_av_av_unit;
    }

}