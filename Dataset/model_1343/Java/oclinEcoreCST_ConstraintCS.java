





import java.util.List;
import java.util.ArrayList;

public class oclinEcoreCST_ConstraintCS extends NamedElementCS {

    private String stereotype;





    private oclinEcoreCST_ClassifierCS oclinecorecst_classifiercs;




    private oclinEcoreCST_OperationCS oclinecorecst_operationcs;




    private oclinEcoreCST_StructuralFeatureCS oclinecorecst_structuralfeaturecs;


    public oclinEcoreCST_ConstraintCS(
        String stereotype    ) {
        super(
        );
        this.stereotype = stereotype;
    }


    public String getStereotype() {
        return stereotype;
    }

    public void setStereotype(String stereotype) {
        this.stereotype = stereotype;
    }

    public oclinEcoreCST_ClassifierCS getOclinecorecst_classifiercs() {
        return oclinecorecst_classifiercs;
    }

    public void setOclinecorecst_classifiercs(oclinEcoreCST_ClassifierCS oclinecorecst_classifiercs) {
        this.oclinecorecst_classifiercs = oclinecorecst_classifiercs;
    }
    public oclinEcoreCST_OperationCS getOclinecorecst_operationcs() {
        return oclinecorecst_operationcs;
    }

    public void setOclinecorecst_operationcs(oclinEcoreCST_OperationCS oclinecorecst_operationcs) {
        this.oclinecorecst_operationcs = oclinecorecst_operationcs;
    }
    public oclinEcoreCST_StructuralFeatureCS getOclinecorecst_structuralfeaturecs() {
        return oclinecorecst_structuralfeaturecs;
    }

    public void setOclinecorecst_structuralfeaturecs(oclinEcoreCST_StructuralFeatureCS oclinecorecst_structuralfeaturecs) {
        this.oclinecorecst_structuralfeaturecs = oclinecorecst_structuralfeaturecs;
    }

}