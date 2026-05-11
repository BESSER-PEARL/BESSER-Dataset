





import java.util.List;
import java.util.ArrayList;

public class alf_SequentialClauses  {






    private alf_IfStatement alf_ifstatement;




    private List<alf_ConcurrentClauses> alf_concurrentclausess;


    public alf_SequentialClauses(
    ) {
        this.alf_concurrentclausess = new ArrayList<>();
    }

    public alf_SequentialClauses(
        ArrayList<alf_ConcurrentClauses> alf_concurrentclausess    ) {
        this.alf_concurrentclausess = alf_concurrentclausess;
    }


    public alf_IfStatement getAlf_ifstatement() {
        return alf_ifstatement;
    }

    public void setAlf_ifstatement(alf_IfStatement alf_ifstatement) {
        this.alf_ifstatement = alf_ifstatement;
    }
    public List<alf_ConcurrentClauses> getAlf_concurrentclausess() {
        return alf_concurrentclausess;
    }

    public void addAlf_concurrentclauses(Alf_concurrentclauses alf_concurrentclauses) {
        this.alf_concurrentclausess.add(alf_concurrentclauses);
    }

}