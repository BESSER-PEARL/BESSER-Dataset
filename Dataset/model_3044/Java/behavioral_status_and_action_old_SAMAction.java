





import java.util.List;
import java.util.ArrayList;

public class behavioral_status_and_action_old_SAMAction  {

    private boolean isAgentAction;
    private String name;





    private List<SAMSchemaAction> samschemaactions;




    private SapClass sapclass;


    public behavioral_status_and_action_old_SAMAction(
        boolean isAgentAction,        String name    ) {
        this.isAgentAction = isAgentAction;
        this.name = name;
        this.samschemaactions = new ArrayList<>();
    }

    public behavioral_status_and_action_old_SAMAction(
        boolean isAgentAction,        String name        ArrayList<SAMSchemaAction> samschemaactions    ) {
        this.isAgentAction = isAgentAction;
        this.name = name;
        this.samschemaactions = samschemaactions;
    }

    public boolean getIsagentaction() {
        return isAgentAction;
    }

    public void setIsagentaction(boolean isAgentAction) {
        this.isAgentAction = isAgentAction;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<SAMSchemaAction> getSamschemaactions() {
        return samschemaactions;
    }

    public void addSamschemaaction(Samschemaaction samschemaaction) {
        this.samschemaactions.add(samschemaaction);
    }
    public SapClass getSapclass() {
        return sapclass;
    }

    public void setSapclass(SapClass sapclass) {
        this.sapclass = sapclass;
    }

}