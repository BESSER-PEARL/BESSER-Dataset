





import java.util.List;
import java.util.ArrayList;

public class asmeta_turbotransitionrules_TryCatchRule extends TurboRule {






    private List<basicterms_Term> basicterms_terms;


    public asmeta_turbotransitionrules_TryCatchRule(
    ) {
        super(
        );
        this.basicterms_terms = new ArrayList<>();
    }

    public asmeta_turbotransitionrules_TryCatchRule(
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