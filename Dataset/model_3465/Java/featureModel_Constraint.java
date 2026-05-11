





import java.util.List;
import java.util.ArrayList;

public class featureModel_Constraint  {

    private String nameA;
    private String nameB;





    private featureModel_Constraints featuremodel_constraints;


    public featureModel_Constraint(
        String nameA,        String nameB    ) {
        this.nameA = nameA;
        this.nameB = nameB;
    }


    public String getNamea() {
        return nameA;
    }

    public void setNamea(String nameA) {
        this.nameA = nameA;
    }
    public String getNameb() {
        return nameB;
    }

    public void setNameb(String nameB) {
        this.nameB = nameB;
    }

    public featureModel_Constraints getFeaturemodel_constraints() {
        return featuremodel_constraints;
    }

    public void setFeaturemodel_constraints(featureModel_Constraints featuremodel_constraints) {
        this.featuremodel_constraints = featuremodel_constraints;
    }

}