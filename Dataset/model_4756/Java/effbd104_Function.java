





import java.util.List;
import java.util.ArrayList;

public class effbd104_Function extends ProcessNode, SequenceNode {

    private String domain;





    private List<effbd104_Function> effbd104_functions;




    private List<effbd104_Sequence> effbd104_sequences;


    public effbd104_Function(
        String domain    ) {
        super(
        );
        this.domain = domain;
        this.effbd104_functions = new ArrayList<>();
        this.effbd104_sequences = new ArrayList<>();
    }

    public effbd104_Function(
        String domain        ArrayList<effbd104_Function> effbd104_functions,        ArrayList<effbd104_Sequence> effbd104_sequences    ) {
        this.domain = domain;
        this.effbd104_functions = effbd104_functions;
        this.effbd104_sequences = effbd104_sequences;
    }

    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }

    public List<effbd104_Function> getEffbd104_functions() {
        return effbd104_functions;
    }

    public void addEffbd104_function(Effbd104_function effbd104_function) {
        this.effbd104_functions.add(effbd104_function);
    }
    public List<effbd104_Sequence> getEffbd104_sequences() {
        return effbd104_sequences;
    }

    public void addEffbd104_sequence(Effbd104_sequence effbd104_sequence) {
        this.effbd104_sequences.add(effbd104_sequence);
    }

}