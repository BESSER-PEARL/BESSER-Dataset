





import java.util.List;
import java.util.ArrayList;

public class Petrinet_Transition extends Node {

    private float maxDelay;
    private float minDelay;





    private Petrinet_OutputArc petrinet_outputarc;




    private Petrinet_InputArc petrinet_inputarc;


    public Petrinet_Transition(
        float maxDelay,        float minDelay    ) {
        super(
        );
        this.maxDelay = maxDelay;
        this.minDelay = minDelay;
    }


    public float getMaxdelay() {
        return maxDelay;
    }

    public void setMaxdelay(float maxDelay) {
        this.maxDelay = maxDelay;
    }
    public float getMindelay() {
        return minDelay;
    }

    public void setMindelay(float minDelay) {
        this.minDelay = minDelay;
    }

    public Petrinet_OutputArc getPetrinet_outputarc() {
        return petrinet_outputarc;
    }

    public void setPetrinet_outputarc(Petrinet_OutputArc petrinet_outputarc) {
        this.petrinet_outputarc = petrinet_outputarc;
    }
    public Petrinet_InputArc getPetrinet_inputarc() {
        return petrinet_inputarc;
    }

    public void setPetrinet_inputarc(Petrinet_InputArc petrinet_inputarc) {
        this.petrinet_inputarc = petrinet_inputarc;
    }

}