





import java.util.List;
import java.util.ArrayList;

public class graphpattern_Bundle extends Pattern {






    private graphpattern_Pattern graphpattern_pattern;




    private List<graphpattern_EPackage> graphpattern_epackages;


    public graphpattern_Bundle(
    ) {
        super(
        );
        this.graphpattern_epackages = new ArrayList<>();
    }

    public graphpattern_Bundle(
        ArrayList<graphpattern_EPackage> graphpattern_epackages    ) {
        this.graphpattern_epackages = graphpattern_epackages;
    }


    public graphpattern_Pattern getGraphpattern_pattern() {
        return graphpattern_pattern;
    }

    public void setGraphpattern_pattern(graphpattern_Pattern graphpattern_pattern) {
        this.graphpattern_pattern = graphpattern_pattern;
    }
    public List<graphpattern_EPackage> getGraphpattern_epackages() {
        return graphpattern_epackages;
    }

    public void addGraphpattern_epackage(Graphpattern_epackage graphpattern_epackage) {
        this.graphpattern_epackages.add(graphpattern_epackage);
    }

}