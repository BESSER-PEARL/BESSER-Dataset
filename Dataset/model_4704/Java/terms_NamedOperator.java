





import java.util.List;
import java.util.ArrayList;

public class terms_NamedOperator extends OperatorDecl {






    private terms_Term terms_term;




    private terms_VariableDecl terms_variabledecl;




    private terms_Term terms_term;




    private List<terms_VariableDecl> terms_variabledecls;


    public terms_NamedOperator(
    ) {
        super(
        );
        this.terms_variabledecls = new ArrayList<>();
    }

    public terms_NamedOperator(
        ArrayList<terms_VariableDecl> terms_variabledecls    ) {
        this.terms_variabledecls = terms_variabledecls;
    }


    public terms_Term getTerms_term() {
        return terms_term;
    }

    public void setTerms_term(terms_Term terms_term) {
        this.terms_term = terms_term;
    }
    public terms_VariableDecl getTerms_variabledecl() {
        return terms_variabledecl;
    }

    public void setTerms_variabledecl(terms_VariableDecl terms_variabledecl) {
        this.terms_variabledecl = terms_variabledecl;
    }
    public terms_Term getTerms_term() {
        return terms_term;
    }

    public void setTerms_term(terms_Term terms_term) {
        this.terms_term = terms_term;
    }
    public List<terms_VariableDecl> getTerms_variabledecls() {
        return terms_variabledecls;
    }

    public void addTerms_variabledecl(Terms_variabledecl terms_variabledecl) {
        this.terms_variabledecls.add(terms_variabledecl);
    }

}