





import java.util.List;
import java.util.ArrayList;

public class terms_Operator extends Term {






    private List<terms_Term> terms_terms;




    private List<terms_Sort> terms_sorts;




    private terms_Sort terms_sort;




    private terms_Term terms_term;


    public terms_Operator(
    ) {
        super(
        );
        this.terms_terms = new ArrayList<>();
        this.terms_sorts = new ArrayList<>();
    }

    public terms_Operator(
        ArrayList<terms_Term> terms_terms,        ArrayList<terms_Sort> terms_sorts    ) {
        this.terms_terms = terms_terms;
        this.terms_sorts = terms_sorts;
    }


    public List<terms_Term> getTerms_terms() {
        return terms_terms;
    }

    public void addTerms_term(Terms_term terms_term) {
        this.terms_terms.add(terms_term);
    }
    public List<terms_Sort> getTerms_sorts() {
        return terms_sorts;
    }

    public void addTerms_sort(Terms_sort terms_sort) {
        this.terms_sorts.add(terms_sort);
    }
    public terms_Sort getTerms_sort() {
        return terms_sort;
    }

    public void setTerms_sort(terms_Sort terms_sort) {
        this.terms_sort = terms_sort;
    }
    public terms_Term getTerms_term() {
        return terms_term;
    }

    public void setTerms_term(terms_Term terms_term) {
        this.terms_term = terms_term;
    }

}