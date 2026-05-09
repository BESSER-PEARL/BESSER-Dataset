





import java.util.List;
import java.util.ArrayList;

public class henshin_MultiUnit extends Unit {






    private List<henshin_Unit> henshin_units;


    public henshin_MultiUnit(
    ) {
        super(
        );
        this.henshin_units = new ArrayList<>();
    }

    public henshin_MultiUnit(
        ArrayList<henshin_Unit> henshin_units    ) {
        this.henshin_units = henshin_units;
    }


    public List<henshin_Unit> getHenshin_units() {
        return henshin_units;
    }

    public void addHenshin_unit(Henshin_unit henshin_unit) {
        this.henshin_units.add(henshin_unit);
    }

}