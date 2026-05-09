





import java.util.List;
import java.util.ArrayList;

public class graphpattern_Extendable  {






    private List<graphpattern_Stereotype> graphpattern_stereotypes;


    public graphpattern_Extendable(
    ) {
        this.graphpattern_stereotypes = new ArrayList<>();
    }

    public graphpattern_Extendable(
        ArrayList<graphpattern_Stereotype> graphpattern_stereotypes    ) {
        this.graphpattern_stereotypes = graphpattern_stereotypes;
    }


    public List<graphpattern_Stereotype> getGraphpattern_stereotypes() {
        return graphpattern_stereotypes;
    }

    public void addGraphpattern_stereotype(Graphpattern_stereotype graphpattern_stereotype) {
        this.graphpattern_stereotypes.add(graphpattern_stereotype);
    }

}