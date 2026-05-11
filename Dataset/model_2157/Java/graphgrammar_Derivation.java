





import java.util.List;
import java.util.ArrayList;

public class graphgrammar_Derivation  {






    private List<graphgrammar_DerivationStep> graphgrammar_derivationsteps;


    public graphgrammar_Derivation(
    ) {
        this.graphgrammar_derivationsteps = new ArrayList<>();
    }

    public graphgrammar_Derivation(
        ArrayList<graphgrammar_DerivationStep> graphgrammar_derivationsteps    ) {
        this.graphgrammar_derivationsteps = graphgrammar_derivationsteps;
    }


    public List<graphgrammar_DerivationStep> getGraphgrammar_derivationsteps() {
        return graphgrammar_derivationsteps;
    }

    public void addGraphgrammar_derivationstep(Graphgrammar_derivationstep graphgrammar_derivationstep) {
        this.graphgrammar_derivationsteps.add(graphgrammar_derivationstep);
    }

}