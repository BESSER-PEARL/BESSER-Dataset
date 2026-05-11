





import java.util.List;
import java.util.ArrayList;

public class effbd201_Function extends ProcessNode, SequenceNode {

    private String domain;





    private List<effbd201_InputPort> effbd201_inputports;




    private effbd201_Function effbd201_function;




    private List<effbd201_OutputPort> effbd201_outputports;


    public effbd201_Function(
        String domain    ) {
        super(
        );
        this.domain = domain;
        this.effbd201_inputports = new ArrayList<>();
        this.effbd201_outputports = new ArrayList<>();
    }

    public effbd201_Function(
        String domain        ArrayList<effbd201_InputPort> effbd201_inputports,        ArrayList<effbd201_OutputPort> effbd201_outputports    ) {
        this.domain = domain;
        this.effbd201_inputports = effbd201_inputports;
        this.effbd201_outputports = effbd201_outputports;
    }

    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }

    public List<effbd201_InputPort> getEffbd201_inputports() {
        return effbd201_inputports;
    }

    public void addEffbd201_inputport(Effbd201_inputport effbd201_inputport) {
        this.effbd201_inputports.add(effbd201_inputport);
    }
    public effbd201_Function getEffbd201_function() {
        return effbd201_function;
    }

    public void setEffbd201_function(effbd201_Function effbd201_function) {
        this.effbd201_function = effbd201_function;
    }
    public List<effbd201_OutputPort> getEffbd201_outputports() {
        return effbd201_outputports;
    }

    public void addEffbd201_outputport(Effbd201_outputport effbd201_outputport) {
        this.effbd201_outputports.add(effbd201_outputport);
    }

}