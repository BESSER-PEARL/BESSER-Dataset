





import java.util.List;
import java.util.ArrayList;

public class ryz_ModelAssociation extends NamedElement {

    private String principalRoleName;
    private boolean isRequired;
    private String cardinality;
    private String dependentRoleName;



    public ryz_ModelAssociation(
        String principalRoleName,        boolean isRequired,        String cardinality,        String dependentRoleName    ) {
        super(
        );
        this.principalRoleName = principalRoleName;
        this.isRequired = isRequired;
        this.cardinality = cardinality;
        this.dependentRoleName = dependentRoleName;
    }


    public String getPrincipalrolename() {
        return principalRoleName;
    }

    public void setPrincipalrolename(String principalRoleName) {
        this.principalRoleName = principalRoleName;
    }
    public boolean getIsrequired() {
        return isRequired;
    }

    public void setIsrequired(boolean isRequired) {
        this.isRequired = isRequired;
    }
    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }
    public String getDependentrolename() {
        return dependentRoleName;
    }

    public void setDependentrolename(String dependentRoleName) {
        this.dependentRoleName = dependentRoleName;
    }


}