





import java.util.List;
import java.util.ArrayList;

public class spem_TaskUse extends MethodContentUse, WorkBreakdownElement {

    private String postCondition;
    private String preCondition;





    private spem_ProcessPerformer spem_processperformer;




    private List<spem_ProcessParameter> spem_processparameters;


    public spem_TaskUse(
        String postCondition,        String preCondition    ) {
        super(
        );
        this.postCondition = postCondition;
        this.preCondition = preCondition;
        this.spem_processparameters = new ArrayList<>();
    }

    public spem_TaskUse(
        String postCondition,        String preCondition        ArrayList<spem_ProcessParameter> spem_processparameters    ) {
        this.postCondition = postCondition;
        this.preCondition = preCondition;
        this.spem_processparameters = spem_processparameters;
    }

    public String getPostcondition() {
        return postCondition;
    }

    public void setPostcondition(String postCondition) {
        this.postCondition = postCondition;
    }
    public String getPrecondition() {
        return preCondition;
    }

    public void setPrecondition(String preCondition) {
        this.preCondition = preCondition;
    }

    public spem_ProcessPerformer getSpem_processperformer() {
        return spem_processperformer;
    }

    public void setSpem_processperformer(spem_ProcessPerformer spem_processperformer) {
        this.spem_processperformer = spem_processperformer;
    }
    public List<spem_ProcessParameter> getSpem_processparameters() {
        return spem_processparameters;
    }

    public void addSpem_processparameter(Spem_processparameter spem_processparameter) {
        this.spem_processparameters.add(spem_processparameter);
    }

}