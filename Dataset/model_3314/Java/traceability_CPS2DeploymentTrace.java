





import java.util.List;
import java.util.ArrayList;

public class traceability_CPS2DeploymentTrace  {






    private traceability_CPSToDeployment traceability_cpstodeployment;




    private List<traceability_DeploymentElement> traceability_deploymentelements;


    public traceability_CPS2DeploymentTrace(
    ) {
        this.traceability_deploymentelements = new ArrayList<>();
    }

    public traceability_CPS2DeploymentTrace(
        ArrayList<traceability_DeploymentElement> traceability_deploymentelements    ) {
        this.traceability_deploymentelements = traceability_deploymentelements;
    }


    public traceability_CPSToDeployment getTraceability_cpstodeployment() {
        return traceability_cpstodeployment;
    }

    public void setTraceability_cpstodeployment(traceability_CPSToDeployment traceability_cpstodeployment) {
        this.traceability_cpstodeployment = traceability_cpstodeployment;
    }
    public List<traceability_DeploymentElement> getTraceability_deploymentelements() {
        return traceability_deploymentelements;
    }

    public void addTraceability_deploymentelement(Traceability_deploymentelement traceability_deploymentelement) {
        this.traceability_deploymentelements.add(traceability_deploymentelement);
    }

}