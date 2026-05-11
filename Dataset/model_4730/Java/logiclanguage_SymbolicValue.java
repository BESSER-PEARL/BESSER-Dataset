





import java.util.List;
import java.util.ArrayList;

public class logiclanguage_SymbolicValue extends Term {






    private List<logiclanguage_Term> logiclanguage_terms;




    private logiclanguage_SymbolicDeclaration logiclanguage_symbolicdeclaration;


    public logiclanguage_SymbolicValue(
    ) {
        super(
        );
        this.logiclanguage_terms = new ArrayList<>();
    }

    public logiclanguage_SymbolicValue(
        ArrayList<logiclanguage_Term> logiclanguage_terms    ) {
        this.logiclanguage_terms = logiclanguage_terms;
    }


    public List<logiclanguage_Term> getLogiclanguage_terms() {
        return logiclanguage_terms;
    }

    public void addLogiclanguage_term(Logiclanguage_term logiclanguage_term) {
        this.logiclanguage_terms.add(logiclanguage_term);
    }
    public logiclanguage_SymbolicDeclaration getLogiclanguage_symbolicdeclaration() {
        return logiclanguage_symbolicdeclaration;
    }

    public void setLogiclanguage_symbolicdeclaration(logiclanguage_SymbolicDeclaration logiclanguage_symbolicdeclaration) {
        this.logiclanguage_symbolicdeclaration = logiclanguage_symbolicdeclaration;
    }

}