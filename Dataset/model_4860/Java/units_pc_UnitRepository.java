





import java.util.List;
import java.util.ArrayList;

public class units_pc_UnitRepository  {






    private List<units_pc_BaseUnit> units_pc_baseunits;


    public units_pc_UnitRepository(
    ) {
        this.units_pc_baseunits = new ArrayList<>();
    }

    public units_pc_UnitRepository(
        ArrayList<units_pc_BaseUnit> units_pc_baseunits    ) {
        this.units_pc_baseunits = units_pc_baseunits;
    }


    public List<units_pc_BaseUnit> getUnits_pc_baseunits() {
        return units_pc_baseunits;
    }

    public void addUnits_pc_baseunit(Units_pc_baseunit units_pc_baseunit) {
        this.units_pc_baseunits.add(units_pc_baseunit);
    }

}