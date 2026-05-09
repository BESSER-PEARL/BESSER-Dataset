





import java.util.List;
import java.util.ArrayList;

public class Core_IType extends IMember {

    private String fullyQualifiedParametrizedName;
    private String fullyQualifiedName;





    private List<IType> itypes;


    public Core_IType(
        String fullyQualifiedParametrizedName,        String fullyQualifiedName    ) {
        super(
        );
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
        this.fullyQualifiedName = fullyQualifiedName;
        this.itypes = new ArrayList<>();
    }

    public Core_IType(
        String fullyQualifiedParametrizedName,        String fullyQualifiedName        ArrayList<IType> itypes    ) {
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
        this.fullyQualifiedName = fullyQualifiedName;
        this.itypes = itypes;
    }

    public String getFullyqualifiedparametrizedname() {
        return fullyQualifiedParametrizedName;
    }

    public void setFullyqualifiedparametrizedname(String fullyQualifiedParametrizedName) {
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
    }
    public String getFullyqualifiedname() {
        return fullyQualifiedName;
    }

    public void setFullyqualifiedname(String fullyQualifiedName) {
        this.fullyQualifiedName = fullyQualifiedName;
    }

    public List<IType> getItypes() {
        return itypes;
    }

    public void addItype(Itype itype) {
        this.itypes.add(itype);
    }

}