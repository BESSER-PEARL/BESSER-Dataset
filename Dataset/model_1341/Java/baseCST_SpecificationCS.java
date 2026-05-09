





import java.util.List;
import java.util.ArrayList;

public class baseCST_SpecificationCS extends ModelElementCS {

    private String exprString;





    private baseCST_StructuralFeatureCS basecst_structuralfeaturecs;




    private baseCST_OperationCS basecst_operationcs;




    private baseCST_ConstraintCS basecst_constraintcs;




    private baseCST_ConstraintCS basecst_constraintcs;


    public baseCST_SpecificationCS(
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

    public baseCST_StructuralFeatureCS getBasecst_structuralfeaturecs() {
        return basecst_structuralfeaturecs;
    }

    public void setBasecst_structuralfeaturecs(baseCST_StructuralFeatureCS basecst_structuralfeaturecs) {
        this.basecst_structuralfeaturecs = basecst_structuralfeaturecs;
    }
    public baseCST_OperationCS getBasecst_operationcs() {
        return basecst_operationcs;
    }

    public void setBasecst_operationcs(baseCST_OperationCS basecst_operationcs) {
        this.basecst_operationcs = basecst_operationcs;
    }
    public baseCST_ConstraintCS getBasecst_constraintcs() {
        return basecst_constraintcs;
    }

    public void setBasecst_constraintcs(baseCST_ConstraintCS basecst_constraintcs) {
        this.basecst_constraintcs = basecst_constraintcs;
    }
    public baseCST_ConstraintCS getBasecst_constraintcs() {
        return basecst_constraintcs;
    }

    public void setBasecst_constraintcs(baseCST_ConstraintCS basecst_constraintcs) {
        this.basecst_constraintcs = basecst_constraintcs;
    }

}