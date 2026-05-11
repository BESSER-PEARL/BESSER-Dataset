





import java.util.List;
import java.util.ArrayList;

public class graphgrammar_Resolution  {






    private List<graphgrammar_ResolutionStep> graphgrammar_resolutionsteps;


    public graphgrammar_Resolution(
    ) {
        this.graphgrammar_resolutionsteps = new ArrayList<>();
    }

    public graphgrammar_Resolution(
        ArrayList<graphgrammar_ResolutionStep> graphgrammar_resolutionsteps    ) {
        this.graphgrammar_resolutionsteps = graphgrammar_resolutionsteps;
    }


    public List<graphgrammar_ResolutionStep> getGraphgrammar_resolutionsteps() {
        return graphgrammar_resolutionsteps;
    }

    public void addGraphgrammar_resolutionstep(Graphgrammar_resolutionstep graphgrammar_resolutionstep) {
        this.graphgrammar_resolutionsteps.add(graphgrammar_resolutionstep);
    }

}