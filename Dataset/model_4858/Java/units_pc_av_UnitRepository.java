





import java.util.List;
import java.util.ArrayList;

public class units_pc_av_UnitRepository  {






    private List<units_pc_av_BaseUnit> units_pc_av_baseunits;


    public units_pc_av_UnitRepository(
    ) {
        this.units_pc_av_baseunits = new ArrayList<>();
    }

    public units_pc_av_UnitRepository(
        ArrayList<units_pc_av_BaseUnit> units_pc_av_baseunits    ) {
        this.units_pc_av_baseunits = units_pc_av_baseunits;
    }


    public List<units_pc_av_BaseUnit> getUnits_pc_av_baseunits() {
        return units_pc_av_baseunits;
    }

    public void addUnits_pc_av_baseunit(Units_pc_av_baseunit units_pc_av_baseunit) {
        this.units_pc_av_baseunits.add(units_pc_av_baseunit);
    }

}