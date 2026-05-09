





import java.util.List;
import java.util.ArrayList;

public class Core_IType extends IMember {

    private String fullyQualifiedName;
    private String fullyQualifiedParametrizedName;





    private List<IType> itypes;


    public Core_IType(
        String fullyQualifiedName,        String fullyQualifiedParametrizedName    ) {
        super(
        );
        this.fullyQualifiedName = fullyQualifiedName;
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
        this.itypes = new ArrayList<>();
    }

    public Core_IType(
        String fullyQualifiedName,        String fullyQualifiedParametrizedName        ArrayList<IType> itypes    ) {
        this.fullyQualifiedName = fullyQualifiedName;
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
        this.itypes = itypes;
    }

    public String getFullyqualifiedname() {
        return fullyQualifiedName;
    }

    public void setFullyqualifiedname(String fullyQualifiedName) {
        this.fullyQualifiedName = fullyQualifiedName;
    }
    public String getFullyqualifiedparametrizedname() {
        return fullyQualifiedParametrizedName;
    }

    public void setFullyqualifiedparametrizedname(String fullyQualifiedParametrizedName) {
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
    }

    public List<IType> getItypes() {
        return itypes;
    }

    public void addItype(Itype itype) {
        this.itypes.add(itype);
    }

}