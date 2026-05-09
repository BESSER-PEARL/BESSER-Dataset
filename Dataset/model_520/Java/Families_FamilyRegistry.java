





import java.util.List;
import java.util.ArrayList;

public class Families_FamilyRegistry extends uncertainty_ModelElement, uncertainty_aFamilyRegistry {






    private List<aFamily> afamilys;


    public Families_FamilyRegistry(
    ) {
        super(
        );
        this.afamilys = new ArrayList<>();
    }

    public Families_FamilyRegistry(
        ArrayList<aFamily> afamilys    ) {
        this.afamilys = afamilys;
    }


    public List<aFamily> getAfamilys() {
        return afamilys;
    }

    public void addAfamily(Afamily afamily) {
        this.afamilys.add(afamily);
    }

}