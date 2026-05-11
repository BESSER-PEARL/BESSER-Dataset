





import java.util.List;
import java.util.ArrayList;

public class smif_constraints_UniquenessConstraint extends TypeConstraint {

    private String isPrimaryIdentity;





    private List<PropertyType> propertytypes;


    public smif_constraints_UniquenessConstraint(
        String isPrimaryIdentity    ) {
        super(
        );
        this.isPrimaryIdentity = isPrimaryIdentity;
        this.propertytypes = new ArrayList<>();
    }

    public smif_constraints_UniquenessConstraint(
        String isPrimaryIdentity        ArrayList<PropertyType> propertytypes    ) {
        this.isPrimaryIdentity = isPrimaryIdentity;
        this.propertytypes = propertytypes;
    }

    public String getIsprimaryidentity() {
        return isPrimaryIdentity;
    }

    public void setIsprimaryidentity(String isPrimaryIdentity) {
        this.isPrimaryIdentity = isPrimaryIdentity;
    }

    public List<PropertyType> getPropertytypes() {
        return propertytypes;
    }

    public void addPropertytype(Propertytype propertytype) {
        this.propertytypes.add(propertytype);
    }

}