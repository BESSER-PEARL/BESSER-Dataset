





import java.util.List;
import java.util.ArrayList;

public class units_av_pc_UnitRepository  {






    private List<units_av_pc_BaseUnit> units_av_pc_baseunits;


    public units_av_pc_UnitRepository(
    ) {
        this.units_av_pc_baseunits = new ArrayList<>();
    }

    public units_av_pc_UnitRepository(
        ArrayList<units_av_pc_BaseUnit> units_av_pc_baseunits    ) {
        this.units_av_pc_baseunits = units_av_pc_baseunits;
    }


    public List<units_av_pc_BaseUnit> getUnits_av_pc_baseunits() {
        return units_av_pc_baseunits;
    }

    public void addUnits_av_pc_baseunit(Units_av_pc_baseunit units_av_pc_baseunit) {
        this.units_av_pc_baseunits.add(units_av_pc_baseunit);
    }

}