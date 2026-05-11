





import java.util.List;
import java.util.ArrayList;

public class crom_l1_composed_CompartmentType extends RigidType {






    private crom_l1_composed_CompartmentType crom_l1_composed_compartmenttype;




    private List<crom_l1_composed_Relationship> crom_l1_composed_relationships;




    private List<crom_l1_composed_CompartmentType> crom_l1_composed_compartmenttypes;


    public crom_l1_composed_CompartmentType(
    ) {
        super(
        );
        this.crom_l1_composed_relationships = new ArrayList<>();
        this.crom_l1_composed_compartmenttypes = new ArrayList<>();
    }

    public crom_l1_composed_CompartmentType(
        ArrayList<crom_l1_composed_Relationship> crom_l1_composed_relationships,        ArrayList<crom_l1_composed_CompartmentType> crom_l1_composed_compartmenttypes    ) {
        this.crom_l1_composed_relationships = crom_l1_composed_relationships;
        this.crom_l1_composed_compartmenttypes = crom_l1_composed_compartmenttypes;
    }


    public crom_l1_composed_CompartmentType getCrom_l1_composed_compartmenttype() {
        return crom_l1_composed_compartmenttype;
    }

    public void setCrom_l1_composed_compartmenttype(crom_l1_composed_CompartmentType crom_l1_composed_compartmenttype) {
        this.crom_l1_composed_compartmenttype = crom_l1_composed_compartmenttype;
    }
    public List<crom_l1_composed_Relationship> getCrom_l1_composed_relationships() {
        return crom_l1_composed_relationships;
    }

    public void addCrom_l1_composed_relationship(Crom_l1_composed_relationship crom_l1_composed_relationship) {
        this.crom_l1_composed_relationships.add(crom_l1_composed_relationship);
    }
    public List<crom_l1_composed_CompartmentType> getCrom_l1_composed_compartmenttypes() {
        return crom_l1_composed_compartmenttypes;
    }

    public void addCrom_l1_composed_compartmenttype(Crom_l1_composed_compartmenttype crom_l1_composed_compartmenttype) {
        this.crom_l1_composed_compartmenttypes.add(crom_l1_composed_compartmenttype);
    }

}