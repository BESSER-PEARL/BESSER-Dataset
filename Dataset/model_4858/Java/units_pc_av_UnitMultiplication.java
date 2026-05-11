





import java.util.List;
import java.util.ArrayList;

public class units_pc_av_UnitMultiplication extends Unit {






    private List<units_pc_av_Unit> units_pc_av_units;


    public units_pc_av_UnitMultiplication(
    ) {
        super(
        );
        this.units_pc_av_units = new ArrayList<>();
    }

    public units_pc_av_UnitMultiplication(
        ArrayList<units_pc_av_Unit> units_pc_av_units    ) {
        this.units_pc_av_units = units_pc_av_units;
    }


    public List<units_pc_av_Unit> getUnits_pc_av_units() {
        return units_pc_av_units;
    }

    public void addUnits_pc_av_unit(Units_pc_av_unit units_pc_av_unit) {
        this.units_pc_av_units.add(units_pc_av_unit);
    }

}