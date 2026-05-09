





import java.util.List;
import java.util.ArrayList;

public class morel_Rule extends RuleElement {






    private List<morel_Pattern> morel_patterns;


    public morel_Rule(
    ) {
        super(
        );
        this.morel_patterns = new ArrayList<>();
    }

    public morel_Rule(
        ArrayList<morel_Pattern> morel_patterns    ) {
        this.morel_patterns = morel_patterns;
    }


    public List<morel_Pattern> getMorel_patterns() {
        return morel_patterns;
    }

    public void addMorel_pattern(Morel_pattern morel_pattern) {
        this.morel_patterns.add(morel_pattern);
    }

}