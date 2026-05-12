





import java.util.List;
import java.util.ArrayList;

public class AsmL_EnumerateSet extends SetTerm {






    private List<Term> terms;


    public AsmL_EnumerateSet(
    ) {
        super(
        );
        this.terms = new ArrayList<>();
    }

    public AsmL_EnumerateSet(
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