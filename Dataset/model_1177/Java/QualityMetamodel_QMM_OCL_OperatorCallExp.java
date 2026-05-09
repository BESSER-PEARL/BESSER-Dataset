





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_QMM_OCL_OperatorCallExp extends OclExpression {

    private String operationName;



    public QualityMetamodel_QMM_OCL_OperatorCallExp(
        String operationName    ) {
        super(
        );
        this.operationName = operationName;
    }


    public String getOperationname() {
        return operationName;
    }

    public void setOperationname(String operationName) {
        this.operationName = operationName;
    }


}