





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_QUDV_UnitFactor  {

    private String name;





    private Unit unit;




    private Rational rational;


    public SysML_ValueTypes_QUDV_QUDV_UnitFactor(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Unit getUnit() {
        return unit;
    }

    public void setUnit(Unit unit) {
        this.unit = unit;
    }
    public Rational getRational() {
        return rational;
    }

    public void setRational(Rational rational) {
        this.rational = rational;
    }

}