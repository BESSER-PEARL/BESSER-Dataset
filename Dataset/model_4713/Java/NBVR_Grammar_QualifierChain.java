





import java.util.List;
import java.util.ArrayList;

public class NBVR_Grammar_QualifierChain extends Qualifier {






    private List<SimpleQualifier> simplequalifiers;


    public NBVR_Grammar_QualifierChain(
    ) {
        super(
        );
        this.simplequalifiers = new ArrayList<>();
    }

    public NBVR_Grammar_QualifierChain(
        ArrayList<SimpleQualifier> simplequalifiers    ) {
        this.simplequalifiers = simplequalifiers;
    }


    public List<SimpleQualifier> getSimplequalifiers() {
        return simplequalifiers;
    }

    public void addSimplequalifier(Simplequalifier simplequalifier) {
        this.simplequalifiers.add(simplequalifier);
    }

}