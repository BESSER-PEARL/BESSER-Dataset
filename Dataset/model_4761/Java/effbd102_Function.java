





import java.util.List;
import java.util.ArrayList;

public class effbd102_Function extends SequenceNode, ProcessNode {

    private float minDuration;
    private String domain;
    private float maxDuration;





    private List<effbd102_Sequence> effbd102_sequences;




    private List<effbd102_InputPort> effbd102_inputports;




    private List<effbd102_Flow> effbd102_flows;




    private List<effbd102_OutputPort> effbd102_outputports;




    private effbd102_Function effbd102_function;


    public effbd102_Function(
        float minDuration,        String domain,        float maxDuration    ) {
        super(
        );
        this.minDuration = minDuration;
        this.domain = domain;
        this.maxDuration = maxDuration;
        this.effbd102_sequences = new ArrayList<>();
        this.effbd102_inputports = new ArrayList<>();
        this.effbd102_flows = new ArrayList<>();
        this.effbd102_outputports = new ArrayList<>();
    }

    public effbd102_Function(
        float minDuration,        String domain,        float maxDuration        ArrayList<effbd102_Sequence> effbd102_sequences,        ArrayList<effbd102_InputPort> effbd102_inputports,        ArrayList<effbd102_Flow> effbd102_flows,        ArrayList<effbd102_OutputPort> effbd102_outputports    ) {
        this.minDuration = minDuration;
        this.domain = domain;
        this.maxDuration = maxDuration;
        this.effbd102_sequences = effbd102_sequences;
        this.effbd102_inputports = effbd102_inputports;
        this.effbd102_flows = effbd102_flows;
        this.effbd102_outputports = effbd102_outputports;
    }

    public float getMinduration() {
        return minDuration;
    }

    public void setMinduration(float minDuration) {
        this.minDuration = minDuration;
    }
    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }
    public float getMaxduration() {
        return maxDuration;
    }

    public void setMaxduration(float maxDuration) {
        this.maxDuration = maxDuration;
    }

    public List<effbd102_Sequence> getEffbd102_sequences() {
        return effbd102_sequences;
    }

    public void addEffbd102_sequence(Effbd102_sequence effbd102_sequence) {
        this.effbd102_sequences.add(effbd102_sequence);
    }
    public List<effbd102_InputPort> getEffbd102_inputports() {
        return effbd102_inputports;
    }

    public void addEffbd102_inputport(Effbd102_inputport effbd102_inputport) {
        this.effbd102_inputports.add(effbd102_inputport);
    }
    public List<effbd102_Flow> getEffbd102_flows() {
        return effbd102_flows;
    }

    public void addEffbd102_flow(Effbd102_flow effbd102_flow) {
        this.effbd102_flows.add(effbd102_flow);
    }
    public List<effbd102_OutputPort> getEffbd102_outputports() {
        return effbd102_outputports;
    }

    public void addEffbd102_outputport(Effbd102_outputport effbd102_outputport) {
        this.effbd102_outputports.add(effbd102_outputport);
    }
    public effbd102_Function getEffbd102_function() {
        return effbd102_function;
    }

    public void setEffbd102_function(effbd102_Function effbd102_function) {
        this.effbd102_function = effbd102_function;
    }

}