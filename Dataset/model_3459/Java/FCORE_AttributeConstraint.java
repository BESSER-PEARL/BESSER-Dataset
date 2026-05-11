





import java.util.List;
import java.util.ArrayList;

public class FCORE_AttributeConstraint  {

    private String equation;





    private FCORE_AttributeConstraintConnection fcore_attributeconstraintconnection;




    private FCORE_AttributeConstraintConnection fcore_attributeconstraintconnection;




    private FCORE_FeatureModel fcore_featuremodel;


    public FCORE_AttributeConstraint(
        String equation    ) {
        this.equation = equation;
    }


    public String getEquation() {
        return equation;
    }

    public void setEquation(String equation) {
        this.equation = equation;
    }

    public FCORE_AttributeConstraintConnection getFcore_attributeconstraintconnection() {
        return fcore_attributeconstraintconnection;
    }

    public void setFcore_attributeconstraintconnection(FCORE_AttributeConstraintConnection fcore_attributeconstraintconnection) {
        this.fcore_attributeconstraintconnection = fcore_attributeconstraintconnection;
    }
    public FCORE_AttributeConstraintConnection getFcore_attributeconstraintconnection() {
        return fcore_attributeconstraintconnection;
    }

    public void setFcore_attributeconstraintconnection(FCORE_AttributeConstraintConnection fcore_attributeconstraintconnection) {
        this.fcore_attributeconstraintconnection = fcore_attributeconstraintconnection;
    }
    public FCORE_FeatureModel getFcore_featuremodel() {
        return fcore_featuremodel;
    }

    public void setFcore_featuremodel(FCORE_FeatureModel fcore_featuremodel) {
        this.fcore_featuremodel = fcore_featuremodel;
    }

}