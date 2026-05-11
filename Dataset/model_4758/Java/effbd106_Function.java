





import java.util.List;
import java.util.ArrayList;

public class effbd106_Function extends ProcessNode, SequenceNode {

    private String domain;





    private List<effbd106_OutputPort> effbd106_outputports;




    private List<effbd106_Sequence> effbd106_sequences;




    private List<effbd106_Function> effbd106_functions;




    private List<effbd106_Flow> effbd106_flows;


    public effbd106_Function(
        String domain    ) {
        super(
        );
        this.domain = domain;
        this.effbd106_outputports = new ArrayList<>();
        this.effbd106_sequences = new ArrayList<>();
        this.effbd106_functions = new ArrayList<>();
        this.effbd106_flows = new ArrayList<>();
    }

    public effbd106_Function(
        String domain        ArrayList<effbd106_OutputPort> effbd106_outputports,        ArrayList<effbd106_Sequence> effbd106_sequences,        ArrayList<effbd106_Function> effbd106_functions,        ArrayList<effbd106_Flow> effbd106_flows    ) {
        this.domain = domain;
        this.effbd106_outputports = effbd106_outputports;
        this.effbd106_sequences = effbd106_sequences;
        this.effbd106_functions = effbd106_functions;
        this.effbd106_flows = effbd106_flows;
    }

    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }

    public List<effbd106_OutputPort> getEffbd106_outputports() {
        return effbd106_outputports;
    }

    public void addEffbd106_outputport(Effbd106_outputport effbd106_outputport) {
        this.effbd106_outputports.add(effbd106_outputport);
    }
    public List<effbd106_Sequence> getEffbd106_sequences() {
        return effbd106_sequences;
    }

    public void addEffbd106_sequence(Effbd106_sequence effbd106_sequence) {
        this.effbd106_sequences.add(effbd106_sequence);
    }
    public List<effbd106_Function> getEffbd106_functions() {
        return effbd106_functions;
    }

    public void addEffbd106_function(Effbd106_function effbd106_function) {
        this.effbd106_functions.add(effbd106_function);
    }
    public List<effbd106_Flow> getEffbd106_flows() {
        return effbd106_flows;
    }

    public void addEffbd106_flow(Effbd106_flow effbd106_flow) {
        this.effbd106_flows.add(effbd106_flow);
    }

}