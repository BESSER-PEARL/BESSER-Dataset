





import java.util.List;
import java.util.ArrayList;

public class Model_Phase  {

    private String phaseID;
    private float timeAdvance;





    private List<Model_Variable> model_variables;




    private Model_AtomicDEVS model_atomicdevs;


    public Model_Phase(
        String phaseID,        float timeAdvance    ) {
        this.phaseID = phaseID;
        this.timeAdvance = timeAdvance;
        this.model_variables = new ArrayList<>();
    }

    public Model_Phase(
        String phaseID,        float timeAdvance        ArrayList<Model_Variable> model_variables    ) {
        this.phaseID = phaseID;
        this.timeAdvance = timeAdvance;
        this.model_variables = model_variables;
    }

    public String getPhaseid() {
        return phaseID;
    }

    public void setPhaseid(String phaseID) {
        this.phaseID = phaseID;
    }
    public float getTimeadvance() {
        return timeAdvance;
    }

    public void setTimeadvance(float timeAdvance) {
        this.timeAdvance = timeAdvance;
    }

    public List<Model_Variable> getModel_variables() {
        return model_variables;
    }

    public void addModel_variable(Model_variable model_variable) {
        this.model_variables.add(model_variable);
    }
    public Model_AtomicDEVS getModel_atomicdevs() {
        return model_atomicdevs;
    }

    public void setModel_atomicdevs(Model_AtomicDEVS model_atomicdevs) {
        this.model_atomicdevs = model_atomicdevs;
    }

}