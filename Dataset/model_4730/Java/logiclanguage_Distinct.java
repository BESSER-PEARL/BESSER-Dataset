





import java.util.List;
import java.util.ArrayList;

public class logiclanguage_Distinct extends PrimitiveRelation {






    private List<logiclanguage_Term> logiclanguage_terms;


    public logiclanguage_Distinct(
    ) {
        super(
        );
        this.logiclanguage_terms = new ArrayList<>();
    }

    public logiclanguage_Distinct(
        ArrayList<logiclanguage_Term> logiclanguage_terms    ) {
        this.logiclanguage_terms = logiclanguage_terms;
    }


    public List<logiclanguage_Term> getLogiclanguage_terms() {
        return logiclanguage_terms;
    }

    public void addLogiclanguage_term(Logiclanguage_term logiclanguage_term) {
        this.logiclanguage_terms.add(logiclanguage_term);
    }

}