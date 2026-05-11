





import java.util.List;
import java.util.ArrayList;

public class asmeta_basicterms_TupleTerm extends ExtendedTerm {

    private String arity;
    private String terms;



    public asmeta_basicterms_TupleTerm(
        String arity,        String terms    ) {
        super(
        );
        this.arity = arity;
        this.terms = terms;
    }


    public String getArity() {
        return arity;
    }

    public void setArity(String arity) {
        this.arity = arity;
    }
    public String getTerms() {
        return terms;
    }

    public void setTerms(String terms) {
        this.terms = terms;
    }


}