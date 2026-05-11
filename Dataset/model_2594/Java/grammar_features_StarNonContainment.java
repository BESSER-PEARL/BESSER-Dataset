





import java.util.List;
import java.util.ArrayList;

public class grammar_features_StarNonContainment extends Child {






    private List<grammar_features_X> grammar_features_xs;


    public grammar_features_StarNonContainment(
    ) {
        super(
        );
        this.grammar_features_xs = new ArrayList<>();
    }

    public grammar_features_StarNonContainment(
        ArrayList<grammar_features_X> grammar_features_xs    ) {
        this.grammar_features_xs = grammar_features_xs;
    }


    public List<grammar_features_X> getGrammar_features_xs() {
        return grammar_features_xs;
    }

    public void addGrammar_features_x(Grammar_features_x grammar_features_x) {
        this.grammar_features_xs.add(grammar_features_x);
    }

}