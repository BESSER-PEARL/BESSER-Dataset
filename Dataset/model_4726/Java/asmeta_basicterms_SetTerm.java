





import java.util.List;
import java.util.ArrayList;

public class asmeta_basicterms_SetTerm extends CollectionTerm {






    private List<basicterms_Term> basicterms_terms;


    public asmeta_basicterms_SetTerm(
    ) {
        super(
        );
        this.basicterms_terms = new ArrayList<>();
    }

    public asmeta_basicterms_SetTerm(
        ArrayList<basicterms_Term> basicterms_terms    ) {
        this.basicterms_terms = basicterms_terms;
    }


    public List<basicterms_Term> getBasicterms_terms() {
        return basicterms_terms;
    }

    public void addBasicterms_term(Basicterms_term basicterms_term) {
        this.basicterms_terms.add(basicterms_term);
    }

}