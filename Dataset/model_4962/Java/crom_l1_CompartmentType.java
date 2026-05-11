





import java.util.List;
import java.util.ArrayList;

public class crom_l1_CompartmentType extends Player, RelationTarget, ModelElement {






    private List<crom_l1_CompartmentType> crom_l1_compartmenttypes;


    public crom_l1_CompartmentType(
    ) {
        super(
        );
        this.crom_l1_compartmenttypes = new ArrayList<>();
    }

    public crom_l1_CompartmentType(
        ArrayList<crom_l1_CompartmentType> crom_l1_compartmenttypes    ) {
        this.crom_l1_compartmenttypes = crom_l1_compartmenttypes;
    }


    public List<crom_l1_CompartmentType> getCrom_l1_compartmenttypes() {
        return crom_l1_compartmenttypes;
    }

    public void addCrom_l1_compartmenttype(Crom_l1_compartmenttype crom_l1_compartmenttype) {
        this.crom_l1_compartmenttypes.add(crom_l1_compartmenttype);
    }

}