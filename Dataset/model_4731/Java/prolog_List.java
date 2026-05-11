





import java.util.List;
import java.util.ArrayList;

public class prolog_List extends Term, Tail {






    private List<prolog_Term> prolog_terms;


    public prolog_List(
    ) {
        super(
        );
        this.prolog_terms = new ArrayList<>();
    }

    public prolog_List(
        ArrayList<prolog_Term> prolog_terms    ) {
        this.prolog_terms = prolog_terms;
    }


    public List<prolog_Term> getProlog_terms() {
        return prolog_terms;
    }

    public void addProlog_term(Prolog_term prolog_term) {
        this.prolog_terms.add(prolog_term);
    }

}