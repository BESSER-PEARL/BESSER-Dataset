





import java.util.List;
import java.util.ArrayList;

public class units_pc_UnitMultiplication extends Unit {






    private List<units_pc_Unit> units_pc_units;


    public units_pc_UnitMultiplication(
    ) {
        super(
        );
        this.units_pc_units = new ArrayList<>();
    }

    public units_pc_UnitMultiplication(
        ArrayList<units_pc_Unit> units_pc_units    ) {
        this.units_pc_units = units_pc_units;
    }


    public List<units_pc_Unit> getUnits_pc_units() {
        return units_pc_units;
    }

    public void addUnits_pc_unit(Units_pc_unit units_pc_unit) {
        this.units_pc_units.add(units_pc_unit);
    }

}