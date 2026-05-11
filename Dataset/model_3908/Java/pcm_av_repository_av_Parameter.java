





import java.util.List;
import java.util.ArrayList;

public class pcm_av_repository_av_Parameter  {

    private String parameterName;
    private String modifier__Parameter;





    private InfrastructureSignature infrastructuresignature;




    private OperationSignature operationsignature;


    public pcm_av_repository_av_Parameter(
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

    public InfrastructureSignature getInfrastructuresignature() {
        return infrastructuresignature;
    }

    public void setInfrastructuresignature(InfrastructureSignature infrastructuresignature) {
        this.infrastructuresignature = infrastructuresignature;
    }
    public OperationSignature getOperationsignature() {
        return operationsignature;
    }

    public void setOperationsignature(OperationSignature operationsignature) {
        this.operationsignature = operationsignature;
    }

}