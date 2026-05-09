





import java.util.List;
import java.util.ArrayList;

public class Core_IType extends IMember {

    private String fullyQualifiedParametrizedName;
    private String fullyQualifiedName;



    public Core_IType(
        String fullyQualifiedParametrizedName,        String fullyQualifiedName    ) {
        super(
        );
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
        this.fullyQualifiedName = fullyQualifiedName;
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


}