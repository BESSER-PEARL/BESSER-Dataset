





import java.util.List;
import java.util.ArrayList;

public class ale_ClassifierSetType extends typeLiteral {






    private List<ale_classifierTypeRule> ale_classifiertyperules;


    public ale_ClassifierSetType(
    ) {
        super(
        );
        this.ale_classifiertyperules = new ArrayList<>();
    }

    public ale_ClassifierSetType(
        ArrayList<ale_classifierTypeRule> ale_classifiertyperules    ) {
        this.ale_classifiertyperules = ale_classifiertyperules;
    }


    public List<ale_classifierTypeRule> getAle_classifiertyperules() {
        return ale_classifiertyperules;
    }

    public void addAle_classifiertyperule(Ale_classifiertyperule ale_classifiertyperule) {
        this.ale_classifiertyperules.add(ale_classifiertyperule);
    }

}