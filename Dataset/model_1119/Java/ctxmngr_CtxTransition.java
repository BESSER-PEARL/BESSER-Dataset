





import java.util.List;
import java.util.ArrayList;

public class ctxmngr_CtxTransition extends NamedElement {

    private float transProb;
    private String output;
    private boolean isRemote;
    private String input;
    private float transRate;
    private String Condition;
    private String Action;
    private String Event;





    private ctxmngr_RemoteFiringDependency ctxmngr_remotefiringdependency;


    public ctxmngr_CtxTransition(
        float transProb,        String output,        boolean isRemote,        String input,        float transRate,        String Condition,        String Action,        String Event    ) {
        super(
        );
        this.transProb = transProb;
        this.output = output;
        this.isRemote = isRemote;
        this.input = input;
        this.transRate = transRate;
        this.Condition = Condition;
        this.Action = Action;
        this.Event = Event;
    }


    public float getTransprob() {
        return transProb;
    }

    public void setTransprob(float transProb) {
        this.transProb = transProb;
    }
    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }
    public boolean getIsremote() {
        return isRemote;
    }

    public void setIsremote(boolean isRemote) {
        this.isRemote = isRemote;
    }
    public String getInput() {
        return input;
    }

    public void setInput(String input) {
        this.input = input;
    }
    public float getTransrate() {
        return transRate;
    }

    public void setTransrate(float transRate) {
        this.transRate = transRate;
    }
    public String getCondition() {
        return Condition;
    }

    public void setCondition(String Condition) {
        this.Condition = Condition;
    }
    public String getAction() {
        return Action;
    }

    public void setAction(String Action) {
        this.Action = Action;
    }
    public String getEvent() {
        return Event;
    }

    public void setEvent(String Event) {
        this.Event = Event;
    }

    public ctxmngr_RemoteFiringDependency getCtxmngr_remotefiringdependency() {
        return ctxmngr_remotefiringdependency;
    }

    public void setCtxmngr_remotefiringdependency(ctxmngr_RemoteFiringDependency ctxmngr_remotefiringdependency) {
        this.ctxmngr_remotefiringdependency = ctxmngr_remotefiringdependency;
    }

}