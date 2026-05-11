





import java.util.List;
import java.util.ArrayList;

public class asmeta_basicterms_TupleTerm extends ExtendedTerm {

    private String terms;
    private String arity;



    public asmeta_basicterms_TupleTerm(
        String terms,        String arity    ) {
        super(
        );
        this.terms = terms;
        this.arity = arity;
    }


    public String getTerms() {
        return terms;
    }

    public void setTerms(String terms) {
        this.terms = terms;
    }
    public String getArity() {
        return arity;
    }

    public void setArity(String arity) {
        this.arity = arity;
    }


}