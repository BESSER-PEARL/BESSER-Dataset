





import java.util.List;
import java.util.ArrayList;

public class terms_Operator extends Term {






    private List<terms_Term> terms_terms;




    private terms_Term terms_term;


    public terms_Operator(
    ) {
        super(
        );
        this.terms_terms = new ArrayList<>();
    }

    public terms_Operator(
        ArrayList<terms_Term> terms_terms    ) {
        this.terms_terms = terms_terms;
    }


    public List<terms_Term> getTerms_terms() {
        return terms_terms;
    }

    public void addTerms_term(Terms_term terms_term) {
        this.terms_terms.add(terms_term);
    }
    public terms_Term getTerms_term() {
        return terms_term;
    }

    public void setTerms_term(terms_Term terms_term) {
        this.terms_term = terms_term;
    }

}