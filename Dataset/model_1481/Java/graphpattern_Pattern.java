





import java.util.List;
import java.util.ArrayList;

public class graphpattern_Pattern extends PatternElement {






    private List<graphpattern_GraphPattern> graphpattern_graphpatterns;




    private List<graphpattern_Pattern> graphpattern_patterns;




    private graphpattern_GraphPattern graphpattern_graphpattern;


    public graphpattern_Pattern(
    ) {
        super(
        );
        this.graphpattern_graphpatterns = new ArrayList<>();
        this.graphpattern_patterns = new ArrayList<>();
    }

    public graphpattern_Pattern(
        ArrayList<graphpattern_GraphPattern> graphpattern_graphpatterns,        ArrayList<graphpattern_Pattern> graphpattern_patterns    ) {
        this.graphpattern_graphpatterns = graphpattern_graphpatterns;
        this.graphpattern_patterns = graphpattern_patterns;
    }


    public List<graphpattern_GraphPattern> getGraphpattern_graphpatterns() {
        return graphpattern_graphpatterns;
    }

    public void addGraphpattern_graphpattern(Graphpattern_graphpattern graphpattern_graphpattern) {
        this.graphpattern_graphpatterns.add(graphpattern_graphpattern);
    }
    public List<graphpattern_Pattern> getGraphpattern_patterns() {
        return graphpattern_patterns;
    }

    public void addGraphpattern_pattern(Graphpattern_pattern graphpattern_pattern) {
        this.graphpattern_patterns.add(graphpattern_pattern);
    }
    public graphpattern_GraphPattern getGraphpattern_graphpattern() {
        return graphpattern_graphpattern;
    }

    public void setGraphpattern_graphpattern(graphpattern_GraphPattern graphpattern_graphpattern) {
        this.graphpattern_graphpattern = graphpattern_graphpattern;
    }

}