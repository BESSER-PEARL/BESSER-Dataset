





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_repository_pc_Parameter  {

    private String parameterName;
    private String modifier__Parameter;





    private OperationSignature operationsignature;


    public pcm_pc_repository_pc_Parameter(
        String parameterName,        String modifier__Parameter    ) {
        this.parameterName = parameterName;
        this.modifier__Parameter = modifier__Parameter;
    }


    public String getParametername() {
        return parameterName;
    }

    public void setParametername(String parameterName) {
        this.parameterName = parameterName;
    }
    public String getModifier__parameter() {
        return modifier__Parameter;
    }

    public void setModifier__parameter(String modifier__Parameter) {
        this.modifier__Parameter = modifier__Parameter;
    }

    public OperationSignature getOperationsignature() {
        return operationsignature;
    }

    public void setOperationsignature(OperationSignature operationsignature) {
        this.operationsignature = operationsignature;
    }

}