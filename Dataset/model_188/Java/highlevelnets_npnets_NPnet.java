





import java.util.List;
import java.util.ArrayList;

public class highlevelnets_npnets_NPnet extends IDiagramHolder {






    private TokenTypeAtomic tokentypeatomic;




    private HighLevelPetriNet highlevelpetrinet;




    private List<TokenTypeElementNet> tokentypeelementnets;


    public highlevelnets_npnets_NPnet(
    ) {
        super(
        );
        this.tokentypeelementnets = new ArrayList<>();
    }

    public highlevelnets_npnets_NPnet(
        ArrayList<TokenTypeElementNet> tokentypeelementnets    ) {
        this.tokentypeelementnets = tokentypeelementnets;
    }


    public TokenTypeAtomic getTokentypeatomic() {
        return tokentypeatomic;
    }

    public void setTokentypeatomic(TokenTypeAtomic tokentypeatomic) {
        this.tokentypeatomic = tokentypeatomic;
    }
    public HighLevelPetriNet getHighlevelpetrinet() {
        return highlevelpetrinet;
    }

    public void setHighlevelpetrinet(HighLevelPetriNet highlevelpetrinet) {
        this.highlevelpetrinet = highlevelpetrinet;
    }
    public List<TokenTypeElementNet> getTokentypeelementnets() {
        return tokentypeelementnets;
    }

    public void addTokentypeelementnet(Tokentypeelementnet tokentypeelementnet) {
        this.tokentypeelementnets.add(tokentypeelementnet);
    }

}