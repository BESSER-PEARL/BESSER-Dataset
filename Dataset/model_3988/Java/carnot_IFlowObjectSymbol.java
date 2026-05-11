





import java.util.List;
import java.util.ArrayList;

public class carnot_IFlowObjectSymbol extends INodeSymbol {






    private carnot_TransitionConnectionType carnot_transitionconnectiontype;




    private carnot_TransitionConnectionType carnot_transitionconnectiontype;




    private List<carnot_TransitionConnectionType> carnot_transitionconnectiontypes;




    private List<carnot_TransitionConnectionType> carnot_transitionconnectiontypes;


    public carnot_IFlowObjectSymbol(
    ) {
        super(
        );
        this.carnot_transitionconnectiontypes = new ArrayList<>();
        this.carnot_transitionconnectiontypes = new ArrayList<>();
    }

    public carnot_IFlowObjectSymbol(
        ArrayList<carnot_TransitionConnectionType> carnot_transitionconnectiontypes,        ArrayList<carnot_TransitionConnectionType> carnot_transitionconnectiontypes    ) {
        this.carnot_transitionconnectiontypes = carnot_transitionconnectiontypes;
        this.carnot_transitionconnectiontypes = carnot_transitionconnectiontypes;
    }


    public carnot_TransitionConnectionType getCarnot_transitionconnectiontype() {
        return carnot_transitionconnectiontype;
    }

    public void setCarnot_transitionconnectiontype(carnot_TransitionConnectionType carnot_transitionconnectiontype) {
        this.carnot_transitionconnectiontype = carnot_transitionconnectiontype;
    }
    public carnot_TransitionConnectionType getCarnot_transitionconnectiontype() {
        return carnot_transitionconnectiontype;
    }

    public void setCarnot_transitionconnectiontype(carnot_TransitionConnectionType carnot_transitionconnectiontype) {
        this.carnot_transitionconnectiontype = carnot_transitionconnectiontype;
    }
    public List<carnot_TransitionConnectionType> getCarnot_transitionconnectiontypes() {
        return carnot_transitionconnectiontypes;
    }

    public void addCarnot_transitionconnectiontype(Carnot_transitionconnectiontype carnot_transitionconnectiontype) {
        this.carnot_transitionconnectiontypes.add(carnot_transitionconnectiontype);
    }
    public List<carnot_TransitionConnectionType> getCarnot_transitionconnectiontypes() {
        return carnot_transitionconnectiontypes;
    }

    public void addCarnot_transitionconnectiontype(Carnot_transitionconnectiontype carnot_transitionconnectiontype) {
        this.carnot_transitionconnectiontypes.add(carnot_transitionconnectiontype);
    }

}