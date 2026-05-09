





import java.util.List;
import java.util.ArrayList;

public class qvtrelationcs_PatternCS extends ModelElementCS {






    private List<qvtrelationcs_PredicateCS> qvtrelationcs_predicatecss;


    public qvtrelationcs_PatternCS(
    ) {
        super(
        );
        this.qvtrelationcs_predicatecss = new ArrayList<>();
    }

    public qvtrelationcs_PatternCS(
        ArrayList<qvtrelationcs_PredicateCS> qvtrelationcs_predicatecss    ) {
        this.qvtrelationcs_predicatecss = qvtrelationcs_predicatecss;
    }


    public List<qvtrelationcs_PredicateCS> getQvtrelationcs_predicatecss() {
        return qvtrelationcs_predicatecss;
    }

    public void addQvtrelationcs_predicatecs(Qvtrelationcs_predicatecs qvtrelationcs_predicatecs) {
        this.qvtrelationcs_predicatecss.add(qvtrelationcs_predicatecs);
    }

}