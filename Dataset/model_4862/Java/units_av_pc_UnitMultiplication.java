





import java.util.List;
import java.util.ArrayList;

public class units_av_pc_UnitMultiplication extends Unit {






    private List<units_av_pc_Unit> units_av_pc_units;


    public units_av_pc_UnitMultiplication(
    ) {
        super(
        );
        this.units_av_pc_units = new ArrayList<>();
    }

    public units_av_pc_UnitMultiplication(
        ArrayList<units_av_pc_Unit> units_av_pc_units    ) {
        this.units_av_pc_units = units_av_pc_units;
    }


    public List<units_av_pc_Unit> getUnits_av_pc_units() {
        return units_av_pc_units;
    }

    public void addUnits_av_pc_unit(Units_av_pc_unit units_av_pc_unit) {
        this.units_av_pc_units.add(units_av_pc_unit);
    }

}