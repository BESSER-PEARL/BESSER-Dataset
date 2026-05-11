





import java.util.List;
import java.util.ArrayList;

public class effbd103_Function extends SequenceNode, ProcessNode {

    private String domain;





    private List<effbd103_Flow> effbd103_flows;




    private List<effbd103_Function> effbd103_functions;




    private List<effbd103_Token> effbd103_tokens;




    private List<effbd103_Sequence> effbd103_sequences;




    private List<effbd103_InputPort> effbd103_inputports;




    private List<effbd103_OutputPort> effbd103_outputports;




    private List<effbd103_Description> effbd103_descriptions;


    public effbd103_Function(
        String domain    ) {
        super(
        );
        this.domain = domain;
        this.effbd103_flows = new ArrayList<>();
        this.effbd103_functions = new ArrayList<>();
        this.effbd103_tokens = new ArrayList<>();
        this.effbd103_sequences = new ArrayList<>();
        this.effbd103_inputports = new ArrayList<>();
        this.effbd103_outputports = new ArrayList<>();
        this.effbd103_descriptions = new ArrayList<>();
    }

    public effbd103_Function(
        String domain        ArrayList<effbd103_Flow> effbd103_flows,        ArrayList<effbd103_Function> effbd103_functions,        ArrayList<effbd103_Token> effbd103_tokens,        ArrayList<effbd103_Sequence> effbd103_sequences,        ArrayList<effbd103_InputPort> effbd103_inputports,        ArrayList<effbd103_OutputPort> effbd103_outputports,        ArrayList<effbd103_Description> effbd103_descriptions    ) {
        this.domain = domain;
        this.effbd103_flows = effbd103_flows;
        this.effbd103_functions = effbd103_functions;
        this.effbd103_tokens = effbd103_tokens;
        this.effbd103_sequences = effbd103_sequences;
        this.effbd103_inputports = effbd103_inputports;
        this.effbd103_outputports = effbd103_outputports;
        this.effbd103_descriptions = effbd103_descriptions;
    }

    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }

    public List<effbd103_Flow> getEffbd103_flows() {
        return effbd103_flows;
    }

    public void addEffbd103_flow(Effbd103_flow effbd103_flow) {
        this.effbd103_flows.add(effbd103_flow);
    }
    public List<effbd103_Function> getEffbd103_functions() {
        return effbd103_functions;
    }

    public void addEffbd103_function(Effbd103_function effbd103_function) {
        this.effbd103_functions.add(effbd103_function);
    }
    public List<effbd103_Token> getEffbd103_tokens() {
        return effbd103_tokens;
    }

    public void addEffbd103_token(Effbd103_token effbd103_token) {
        this.effbd103_tokens.add(effbd103_token);
    }
    public List<effbd103_Sequence> getEffbd103_sequences() {
        return effbd103_sequences;
    }

    public void addEffbd103_sequence(Effbd103_sequence effbd103_sequence) {
        this.effbd103_sequences.add(effbd103_sequence);
    }
    public List<effbd103_InputPort> getEffbd103_inputports() {
        return effbd103_inputports;
    }

    public void addEffbd103_inputport(Effbd103_inputport effbd103_inputport) {
        this.effbd103_inputports.add(effbd103_inputport);
    }
    public List<effbd103_OutputPort> getEffbd103_outputports() {
        return effbd103_outputports;
    }

    public void addEffbd103_outputport(Effbd103_outputport effbd103_outputport) {
        this.effbd103_outputports.add(effbd103_outputport);
    }
    public List<effbd103_Description> getEffbd103_descriptions() {
        return effbd103_descriptions;
    }

    public void addEffbd103_description(Effbd103_description effbd103_description) {
        this.effbd103_descriptions.add(effbd103_description);
    }

}