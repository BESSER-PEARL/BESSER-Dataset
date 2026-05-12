





import java.util.List;
import java.util.ArrayList;

public class AsmL_EnumerateSequence extends SequenceTerm {






    private List<Term> terms;


    public AsmL_EnumerateSequence(
    ) {
        super(
        );
        this.terms = new ArrayList<>();
    }

    public AsmL_EnumerateSequence(
        ArrayList<Term> terms    ) {
        this.terms = terms;
    }


    public List<Term> getTerms() {
        return terms;
    }

    public void addTerm(Term term) {
        this.terms.add(term);
    }

}