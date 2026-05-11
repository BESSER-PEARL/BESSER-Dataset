





import java.util.List;
import java.util.ArrayList;

public class units_UnitMultiplication extends Unit {






    private List<units_Unit> units_units;


    public units_UnitMultiplication(
    ) {
        super(
        );
        this.units_units = new ArrayList<>();
    }

    public units_UnitMultiplication(
        ArrayList<units_Unit> units_units    ) {
        this.units_units = units_units;
    }


    public List<units_Unit> getUnits_units() {
        return units_units;
    }

    public void addUnits_unit(Units_unit units_unit) {
        this.units_units.add(units_unit);
    }

}