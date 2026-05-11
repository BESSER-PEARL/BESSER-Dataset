





import java.util.List;
import java.util.ArrayList;

public class prolog_Predicate extends Term, Part {

    private String name;





    private List<prolog_Term> prolog_terms;


    public prolog_Predicate(
        String name    ) {
        super(
        );
        this.name = name;
        this.prolog_terms = new ArrayList<>();
    }

    public prolog_Predicate(
        String name        ArrayList<prolog_Term> prolog_terms    ) {
        this.name = name;
        this.prolog_terms = prolog_terms;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<prolog_Term> getProlog_terms() {
        return prolog_terms;
    }

    public void addProlog_term(Prolog_term prolog_term) {
        this.prolog_terms.add(prolog_term);
    }

}