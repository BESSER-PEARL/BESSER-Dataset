





import java.util.List;
import java.util.ArrayList;

public class units_av_av_UnitMultiplication extends Unit {






    private List<units_av_av_Unit> units_av_av_units;


    public units_av_av_UnitMultiplication(
    ) {
        super(
        );
        this.units_av_av_units = new ArrayList<>();
    }

    public units_av_av_UnitMultiplication(
        ArrayList<units_av_av_Unit> units_av_av_units    ) {
        this.units_av_av_units = units_av_av_units;
    }


    public List<units_av_av_Unit> getUnits_av_av_units() {
        return units_av_av_units;
    }

    public void addUnits_av_av_unit(Units_av_av_unit units_av_av_unit) {
        this.units_av_av_units.add(units_av_av_unit);
    }

}