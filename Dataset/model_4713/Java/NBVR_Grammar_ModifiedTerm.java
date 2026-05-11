





import java.util.List;
import java.util.ArrayList;

public class NBVR_Grammar_ModifiedTerm extends SimpleNounPhrase {






    private List<Qualifier> qualifiers;


    public NBVR_Grammar_ModifiedTerm(
    ) {
        super(
        );
        this.qualifiers = new ArrayList<>();
    }

    public NBVR_Grammar_ModifiedTerm(
        ArrayList<Qualifier> qualifiers    ) {
        this.qualifiers = qualifiers;
    }


    public List<Qualifier> getQualifiers() {
        return qualifiers;
    }

    public void addQualifier(Qualifier qualifier) {
        this.qualifiers.add(qualifier);
    }

}