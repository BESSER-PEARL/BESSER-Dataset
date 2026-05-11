





import java.util.List;
import java.util.ArrayList;

public class smalluml_Package extends NamedElement {






    private List<smalluml_Association> smalluml_associations;




    private List<smalluml_SuperType> smalluml_supertypes;


    public smalluml_Package(
    ) {
        super(
        );
        this.smalluml_associations = new ArrayList<>();
        this.smalluml_supertypes = new ArrayList<>();
    }

    public smalluml_Package(
        ArrayList<smalluml_Association> smalluml_associations,        ArrayList<smalluml_SuperType> smalluml_supertypes    ) {
        this.smalluml_associations = smalluml_associations;
        this.smalluml_supertypes = smalluml_supertypes;
    }


    public List<smalluml_Association> getSmalluml_associations() {
        return smalluml_associations;
    }

    public void addSmalluml_association(Smalluml_association smalluml_association) {
        this.smalluml_associations.add(smalluml_association);
    }
    public List<smalluml_SuperType> getSmalluml_supertypes() {
        return smalluml_supertypes;
    }

    public void addSmalluml_supertype(Smalluml_supertype smalluml_supertype) {
        this.smalluml_supertypes.add(smalluml_supertype);
    }

}