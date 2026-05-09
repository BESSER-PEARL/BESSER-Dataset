





import java.util.List;
import java.util.ArrayList;

public class problog_TermInstance extends Referable, Annotatable {






    private problog_Term problog_term;




    private List<problog_Referable> problog_referables;


    public problog_TermInstance(
    ) {
        super(
        );
        this.problog_referables = new ArrayList<>();
    }

    public problog_TermInstance(
        ArrayList<problog_Referable> problog_referables    ) {
        this.problog_referables = problog_referables;
    }


    public problog_Term getProblog_term() {
        return problog_term;
    }

    public void setProblog_term(problog_Term problog_term) {
        this.problog_term = problog_term;
    }
    public List<problog_Referable> getProblog_referables() {
        return problog_referables;
    }

    public void addProblog_referable(Problog_referable problog_referable) {
        this.problog_referables.add(problog_referable);
    }

}