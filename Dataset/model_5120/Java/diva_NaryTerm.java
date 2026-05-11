





import java.util.List;
import java.util.ArrayList;

public class diva_NaryTerm extends Term {






    private List<diva_Term> diva_terms;


    public diva_NaryTerm(
    ) {
        super(
        );
        this.diva_terms = new ArrayList<>();
    }

    public diva_NaryTerm(
        ArrayList<diva_Term> diva_terms    ) {
        this.diva_terms = diva_terms;
    }


    public List<diva_Term> getDiva_terms() {
        return diva_terms;
    }

    public void addDiva_term(Diva_term diva_term) {
        this.diva_terms.add(diva_term);
    }

}