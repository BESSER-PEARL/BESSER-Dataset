





import java.util.List;
import java.util.ArrayList;

public class Maude_RecTerm extends Term {

    private String op;





    private List<Maude_Term> maude_terms;


    public Maude_RecTerm(
        String op    ) {
        super(
        );
        this.op = op;
        this.maude_terms = new ArrayList<>();
    }

    public Maude_RecTerm(
        String op        ArrayList<Maude_Term> maude_terms    ) {
        this.op = op;
        this.maude_terms = maude_terms;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public List<Maude_Term> getMaude_terms() {
        return maude_terms;
    }

    public void addMaude_term(Maude_term maude_term) {
        this.maude_terms.add(maude_term);
    }

}