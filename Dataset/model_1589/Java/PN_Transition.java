





import java.util.List;
import java.util.ArrayList;

public class PN_Transition extends Node {

    private float maxDelay;
    private float minDelay;





    private PN_OutputArc pn_outputarc;




    private PN_InputArc pn_inputarc;


    public PN_Transition(
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

    public PN_OutputArc getPn_outputarc() {
        return pn_outputarc;
    }

    public void setPn_outputarc(PN_OutputArc pn_outputarc) {
        this.pn_outputarc = pn_outputarc;
    }
    public PN_InputArc getPn_inputarc() {
        return pn_inputarc;
    }

    public void setPn_inputarc(PN_InputArc pn_inputarc) {
        this.pn_inputarc = pn_inputarc;
    }

}