





import java.util.List;
import java.util.ArrayList;

public class asmeta_furtherterms_CaseTerm extends ExtendedTerm {

    private String resultTerms;





    private basicterms_Term basicterms_term;




    private List<basicterms_Term> basicterms_terms;




    private basicterms_Term basicterms_term;


    public asmeta_furtherterms_CaseTerm(
        String resultTerms    ) {
        super(
        );
        this.resultTerms = resultTerms;
        this.basicterms_terms = new ArrayList<>();
    }

    public asmeta_furtherterms_CaseTerm(
        String resultTerms        ArrayList<basicterms_Term> basicterms_terms    ) {
        this.resultTerms = resultTerms;
        this.basicterms_terms = basicterms_terms;
    }

    public String getResultterms() {
        return resultTerms;
    }

    public void setResultterms(String resultTerms) {
        this.resultTerms = resultTerms;
    }

    public basicterms_Term getBasicterms_term() {
        return basicterms_term;
    }

    public void setBasicterms_term(basicterms_Term basicterms_term) {
        this.basicterms_term = basicterms_term;
    }
    public List<basicterms_Term> getBasicterms_terms() {
        return basicterms_terms;
    }

    public void addBasicterms_term(Basicterms_term basicterms_term) {
        this.basicterms_terms.add(basicterms_term);
    }
    public basicterms_Term getBasicterms_term() {
        return basicterms_term;
    }

    public void setBasicterms_term(basicterms_Term basicterms_term) {
        this.basicterms_term = basicterms_term;
    }

}