





import java.util.List;
import java.util.ArrayList;

public class asmeta_furtherterms_MapTerm extends CollectionTerm {






    private List<basicterms_TupleTerm> basicterms_tupleterms;


    public asmeta_furtherterms_MapTerm(
    ) {
        super(
        );
        this.basicterms_tupleterms = new ArrayList<>();
    }

    public asmeta_furtherterms_MapTerm(
        ArrayList<basicterms_TupleTerm> basicterms_tupleterms    ) {
        this.basicterms_tupleterms = basicterms_tupleterms;
    }


    public List<basicterms_TupleTerm> getBasicterms_tupleterms() {
        return basicterms_tupleterms;
    }

    public void addBasicterms_tupleterm(Basicterms_tupleterm basicterms_tupleterm) {
        this.basicterms_tupleterms.add(basicterms_tupleterm);
    }

}