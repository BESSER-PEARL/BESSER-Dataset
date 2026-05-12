





import java.util.List;
import java.util.ArrayList;

public class highlevelnets_npnets_NPnet extends IDiagramHolder {






    private List<Synchronization> synchronizations;




    private HighLevelPetriNet highlevelpetrinet;




    private List<TokenTypeElementNet> tokentypeelementnets;




    private TokenTypeAtomic tokentypeatomic;




    private List<NetConstant> netconstants;


    public highlevelnets_npnets_NPnet(
    ) {
        super(
        );
        this.synchronizations = new ArrayList<>();
        this.tokentypeelementnets = new ArrayList<>();
        this.netconstants = new ArrayList<>();
    }

    public highlevelnets_npnets_NPnet(
        ArrayList<Synchronization> synchronizations,        ArrayList<TokenTypeElementNet> tokentypeelementnets,        ArrayList<NetConstant> netconstants    ) {
        this.synchronizations = synchronizations;
        this.tokentypeelementnets = tokentypeelementnets;
        this.netconstants = netconstants;
    }


    public List<Synchronization> getSynchronizations() {
        return synchronizations;
    }

    public void addSynchronization(Synchronization synchronization) {
        this.synchronizations.add(synchronization);
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
    public TokenTypeAtomic getTokentypeatomic() {
        return tokentypeatomic;
    }

    public void setTokentypeatomic(TokenTypeAtomic tokentypeatomic) {
        this.tokentypeatomic = tokentypeatomic;
    }
    public List<NetConstant> getNetconstants() {
        return netconstants;
    }

    public void addNetconstant(Netconstant netconstant) {
        this.netconstants.add(netconstant);
    }

}