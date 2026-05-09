





import java.util.List;
import java.util.ArrayList;

public class Core_IType extends IMember {

    private String fullyQualifiedName;
    private String fullyQualifiedParametrizedName;





    private List<ITypeParameter> itypeparameters;


    public Core_IType(
        String fullyQualifiedName,        String fullyQualifiedParametrizedName    ) {
        super(
        );
        this.fullyQualifiedName = fullyQualifiedName;
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
        this.itypeparameters = new ArrayList<>();
    }

    public Core_IType(
        String fullyQualifiedName,        String fullyQualifiedParametrizedName        ArrayList<ITypeParameter> itypeparameters    ) {
        this.fullyQualifiedName = fullyQualifiedName;
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
        this.itypeparameters = itypeparameters;
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

    public List<ITypeParameter> getItypeparameters() {
        return itypeparameters;
    }

    public void addItypeparameter(Itypeparameter itypeparameter) {
        this.itypeparameters.add(itypeparameter);
    }

}