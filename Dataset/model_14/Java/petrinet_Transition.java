





import java.util.List;
import java.util.ArrayList;

public class petrinet_Transition extends Node {

    private float maxDelay;
    private float minDelay;





    private petrinet_OutputArc petrinet_outputarc;




    private petrinet_InputArc petrinet_inputarc;


    public petrinet_Transition(
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

    public petrinet_OutputArc getPetrinet_outputarc() {
        return petrinet_outputarc;
    }

    public void setPetrinet_outputarc(petrinet_OutputArc petrinet_outputarc) {
        this.petrinet_outputarc = petrinet_outputarc;
    }
    public petrinet_InputArc getPetrinet_inputarc() {
        return petrinet_inputarc;
    }

    public void setPetrinet_inputarc(petrinet_InputArc petrinet_inputarc) {
        this.petrinet_inputarc = petrinet_inputarc;
    }

}