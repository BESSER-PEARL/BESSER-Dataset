





import java.util.List;
import java.util.ArrayList;

public class units_UnitCarryingElement  {

    private String unitSpecification;





    private units_Unit units_unit;


    public units_UnitCarryingElement(
        String unitSpecification    ) {
        this.unitSpecification = unitSpecification;
    }


    public String getUnitspecification() {
        return unitSpecification;
    }

    public void setUnitspecification(String unitSpecification) {
        this.unitSpecification = unitSpecification;
    }

    public units_Unit getUnits_unit() {
        return units_unit;
    }

    public void setUnits_unit(units_Unit units_unit) {
        this.units_unit = units_unit;
    }

}