





import java.util.List;
import java.util.ArrayList;

public class units_UnitRepository  {






    private List<units_BaseUnit> units_baseunits;


    public units_UnitRepository(
    ) {
        this.units_baseunits = new ArrayList<>();
    }

    public units_UnitRepository(
        ArrayList<units_BaseUnit> units_baseunits    ) {
        this.units_baseunits = units_baseunits;
    }


    public List<units_BaseUnit> getUnits_baseunits() {
        return units_baseunits;
    }

    public void addUnits_baseunit(Units_baseunit units_baseunit) {
        this.units_baseunits.add(units_baseunit);
    }

}