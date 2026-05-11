





import java.util.List;
import java.util.ArrayList;

public class carnot_IModelParticipantSymbol extends IModelElementNodeSymbol {






    private carnot_PerformsConnectionType carnot_performsconnectiontype;




    private List<carnot_TriggersConnectionType> carnot_triggersconnectiontypes;




    private carnot_TriggersConnectionType carnot_triggersconnectiontype;




    private List<carnot_PerformsConnectionType> carnot_performsconnectiontypes;


    public carnot_IModelParticipantSymbol(
    ) {
        super(
        );
        this.carnot_triggersconnectiontypes = new ArrayList<>();
        this.carnot_performsconnectiontypes = new ArrayList<>();
    }

    public carnot_IModelParticipantSymbol(
        ArrayList<carnot_TriggersConnectionType> carnot_triggersconnectiontypes,        ArrayList<carnot_PerformsConnectionType> carnot_performsconnectiontypes    ) {
        this.carnot_triggersconnectiontypes = carnot_triggersconnectiontypes;
        this.carnot_performsconnectiontypes = carnot_performsconnectiontypes;
    }


    public carnot_PerformsConnectionType getCarnot_performsconnectiontype() {
        return carnot_performsconnectiontype;
    }

    public void setCarnot_performsconnectiontype(carnot_PerformsConnectionType carnot_performsconnectiontype) {
        this.carnot_performsconnectiontype = carnot_performsconnectiontype;
    }
    public List<carnot_TriggersConnectionType> getCarnot_triggersconnectiontypes() {
        return carnot_triggersconnectiontypes;
    }

    public void addCarnot_triggersconnectiontype(Carnot_triggersconnectiontype carnot_triggersconnectiontype) {
        this.carnot_triggersconnectiontypes.add(carnot_triggersconnectiontype);
    }
    public carnot_TriggersConnectionType getCarnot_triggersconnectiontype() {
        return carnot_triggersconnectiontype;
    }

    public void setCarnot_triggersconnectiontype(carnot_TriggersConnectionType carnot_triggersconnectiontype) {
        this.carnot_triggersconnectiontype = carnot_triggersconnectiontype;
    }
    public List<carnot_PerformsConnectionType> getCarnot_performsconnectiontypes() {
        return carnot_performsconnectiontypes;
    }

    public void addCarnot_performsconnectiontype(Carnot_performsconnectiontype carnot_performsconnectiontype) {
        this.carnot_performsconnectiontypes.add(carnot_performsconnectiontype);
    }

}