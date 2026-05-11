





import java.util.List;
import java.util.ArrayList;

public class Model_Phase  {

    private String phaseID;
    private float timeAdvance;





    private Model_AtomicDEVS model_atomicdevs;


    public Model_Phase(
        String phaseID,        float timeAdvance    ) {
        this.phaseID = phaseID;
        this.timeAdvance = timeAdvance;
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

    public Model_AtomicDEVS getModel_atomicdevs() {
        return model_atomicdevs;
    }

    public void setModel_atomicdevs(Model_AtomicDEVS model_atomicdevs) {
        this.model_atomicdevs = model_atomicdevs;
    }

}