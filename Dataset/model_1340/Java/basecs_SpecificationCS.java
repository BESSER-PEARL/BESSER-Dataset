





import java.util.List;
import java.util.ArrayList;

public class basecs_SpecificationCS extends ModelElementCS {

    private String exprString;





    private basecs_StructuralFeatureCS basecs_structuralfeaturecs;




    private basecs_ConstraintCS basecs_constraintcs;




    private basecs_OperationCS basecs_operationcs;




    private basecs_ConstraintCS basecs_constraintcs;


    public basecs_SpecificationCS(
        String exprString    ) {
        super(
        );
        this.exprString = exprString;
    }


    public String getExprstring() {
        return exprString;
    }

    public void setExprstring(String exprString) {
        this.exprString = exprString;
    }

    public basecs_StructuralFeatureCS getBasecs_structuralfeaturecs() {
        return basecs_structuralfeaturecs;
    }

    public void setBasecs_structuralfeaturecs(basecs_StructuralFeatureCS basecs_structuralfeaturecs) {
        this.basecs_structuralfeaturecs = basecs_structuralfeaturecs;
    }
    public basecs_ConstraintCS getBasecs_constraintcs() {
        return basecs_constraintcs;
    }

    public void setBasecs_constraintcs(basecs_ConstraintCS basecs_constraintcs) {
        this.basecs_constraintcs = basecs_constraintcs;
    }
    public basecs_OperationCS getBasecs_operationcs() {
        return basecs_operationcs;
    }

    public void setBasecs_operationcs(basecs_OperationCS basecs_operationcs) {
        this.basecs_operationcs = basecs_operationcs;
    }
    public basecs_ConstraintCS getBasecs_constraintcs() {
        return basecs_constraintcs;
    }

    public void setBasecs_constraintcs(basecs_ConstraintCS basecs_constraintcs) {
        this.basecs_constraintcs = basecs_constraintcs;
    }

}