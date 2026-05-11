





import java.util.List;
import java.util.ArrayList;

public class traceability_CPSToDeployment  {






    private traceability_Deployment traceability_deployment;




    private List<traceability_CPS2DeplyomentTrace> traceability_cps2deplyomenttraces;


    public traceability_CPSToDeployment(
    ) {
        this.traceability_cps2deplyomenttraces = new ArrayList<>();
    }

    public traceability_CPSToDeployment(
        ArrayList<traceability_CPS2DeplyomentTrace> traceability_cps2deplyomenttraces    ) {
        this.traceability_cps2deplyomenttraces = traceability_cps2deplyomenttraces;
    }


    public traceability_Deployment getTraceability_deployment() {
        return traceability_deployment;
    }

    public void setTraceability_deployment(traceability_Deployment traceability_deployment) {
        this.traceability_deployment = traceability_deployment;
    }
    public List<traceability_CPS2DeplyomentTrace> getTraceability_cps2deplyomenttraces() {
        return traceability_cps2deplyomenttraces;
    }

    public void addTraceability_cps2deplyomenttrace(Traceability_cps2deplyomenttrace traceability_cps2deplyomenttrace) {
        this.traceability_cps2deplyomenttraces.add(traceability_cps2deplyomenttrace);
    }

}