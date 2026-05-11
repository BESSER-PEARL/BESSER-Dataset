





import java.util.List;
import java.util.ArrayList;

public class traceSystem_Traced_TracedObjects  {






    private List<activitydiagramConfiguration_TracedForkedToken> activitydiagramconfiguration_tracedforkedtokens;




    private List<activitydiagramConfiguration_TracedControlToken> activitydiagramconfiguration_tracedcontroltokens;




    private List<activitydiagramConfiguration_TracedTrace> activitydiagramconfiguration_tracedtraces;




    private List<activitydiagramConfiguration_TracedInput> activitydiagramconfiguration_tracedinputs;




    private List<activitydiagram_TracedControlFlow> activitydiagram_tracedcontrolflows;




    private List<activitydiagram_TracedJoinNode> activitydiagram_tracedjoinnodes;




    private List<activitydiagram_TracedActivity> activitydiagram_tracedactivitys;




    private List<activitydiagramConfiguration_TracedInputValue> activitydiagramconfiguration_tracedinputvalues;


    public traceSystem_Traced_TracedObjects(
    ) {
        this.activitydiagramconfiguration_tracedforkedtokens = new ArrayList<>();
        this.activitydiagramconfiguration_tracedcontroltokens = new ArrayList<>();
        this.activitydiagramconfiguration_tracedtraces = new ArrayList<>();
        this.activitydiagramconfiguration_tracedinputs = new ArrayList<>();
        this.activitydiagram_tracedcontrolflows = new ArrayList<>();
        this.activitydiagram_tracedjoinnodes = new ArrayList<>();
        this.activitydiagram_tracedactivitys = new ArrayList<>();
        this.activitydiagramconfiguration_tracedinputvalues = new ArrayList<>();
    }

    public traceSystem_Traced_TracedObjects(
        ArrayList<activitydiagramConfiguration_TracedForkedToken> activitydiagramconfiguration_tracedforkedtokens,        ArrayList<activitydiagramConfiguration_TracedControlToken> activitydiagramconfiguration_tracedcontroltokens,        ArrayList<activitydiagramConfiguration_TracedTrace> activitydiagramconfiguration_tracedtraces,        ArrayList<activitydiagramConfiguration_TracedInput> activitydiagramconfiguration_tracedinputs,        ArrayList<activitydiagram_TracedControlFlow> activitydiagram_tracedcontrolflows,        ArrayList<activitydiagram_TracedJoinNode> activitydiagram_tracedjoinnodes,        ArrayList<activitydiagram_TracedActivity> activitydiagram_tracedactivitys,        ArrayList<activitydiagramConfiguration_TracedInputValue> activitydiagramconfiguration_tracedinputvalues    ) {
        this.activitydiagramconfiguration_tracedforkedtokens = activitydiagramconfiguration_tracedforkedtokens;
        this.activitydiagramconfiguration_tracedcontroltokens = activitydiagramconfiguration_tracedcontroltokens;
        this.activitydiagramconfiguration_tracedtraces = activitydiagramconfiguration_tracedtraces;
        this.activitydiagramconfiguration_tracedinputs = activitydiagramconfiguration_tracedinputs;
        this.activitydiagram_tracedcontrolflows = activitydiagram_tracedcontrolflows;
        this.activitydiagram_tracedjoinnodes = activitydiagram_tracedjoinnodes;
        this.activitydiagram_tracedactivitys = activitydiagram_tracedactivitys;
        this.activitydiagramconfiguration_tracedinputvalues = activitydiagramconfiguration_tracedinputvalues;
    }


    public List<activitydiagramConfiguration_TracedForkedToken> getActivitydiagramconfiguration_tracedforkedtokens() {
        return activitydiagramconfiguration_tracedforkedtokens;
    }

    public void addActivitydiagramconfiguration_tracedforkedtoken(Activitydiagramconfiguration_tracedforkedtoken activitydiagramconfiguration_tracedforkedtoken) {
        this.activitydiagramconfiguration_tracedforkedtokens.add(activitydiagramconfiguration_tracedforkedtoken);
    }
    public List<activitydiagramConfiguration_TracedControlToken> getActivitydiagramconfiguration_tracedcontroltokens() {
        return activitydiagramconfiguration_tracedcontroltokens;
    }

    public void addActivitydiagramconfiguration_tracedcontroltoken(Activitydiagramconfiguration_tracedcontroltoken activitydiagramconfiguration_tracedcontroltoken) {
        this.activitydiagramconfiguration_tracedcontroltokens.add(activitydiagramconfiguration_tracedcontroltoken);
    }
    public List<activitydiagramConfiguration_TracedTrace> getActivitydiagramconfiguration_tracedtraces() {
        return activitydiagramconfiguration_tracedtraces;
    }

    public void addActivitydiagramconfiguration_tracedtrace(Activitydiagramconfiguration_tracedtrace activitydiagramconfiguration_tracedtrace) {
        this.activitydiagramconfiguration_tracedtraces.add(activitydiagramconfiguration_tracedtrace);
    }
    public List<activitydiagramConfiguration_TracedInput> getActivitydiagramconfiguration_tracedinputs() {
        return activitydiagramconfiguration_tracedinputs;
    }

    public void addActivitydiagramconfiguration_tracedinput(Activitydiagramconfiguration_tracedinput activitydiagramconfiguration_tracedinput) {
        this.activitydiagramconfiguration_tracedinputs.add(activitydiagramconfiguration_tracedinput);
    }
    public List<activitydiagram_TracedControlFlow> getActivitydiagram_tracedcontrolflows() {
        return activitydiagram_tracedcontrolflows;
    }

    public void addActivitydiagram_tracedcontrolflow(Activitydiagram_tracedcontrolflow activitydiagram_tracedcontrolflow) {
        this.activitydiagram_tracedcontrolflows.add(activitydiagram_tracedcontrolflow);
    }
    public List<activitydiagram_TracedJoinNode> getActivitydiagram_tracedjoinnodes() {
        return activitydiagram_tracedjoinnodes;
    }

    public void addActivitydiagram_tracedjoinnode(Activitydiagram_tracedjoinnode activitydiagram_tracedjoinnode) {
        this.activitydiagram_tracedjoinnodes.add(activitydiagram_tracedjoinnode);
    }
    public List<activitydiagram_TracedActivity> getActivitydiagram_tracedactivitys() {
        return activitydiagram_tracedactivitys;
    }

    public void addActivitydiagram_tracedactivity(Activitydiagram_tracedactivity activitydiagram_tracedactivity) {
        this.activitydiagram_tracedactivitys.add(activitydiagram_tracedactivity);
    }
    public List<activitydiagramConfiguration_TracedInputValue> getActivitydiagramconfiguration_tracedinputvalues() {
        return activitydiagramconfiguration_tracedinputvalues;
    }

    public void addActivitydiagramconfiguration_tracedinputvalue(Activitydiagramconfiguration_tracedinputvalue activitydiagramconfiguration_tracedinputvalue) {
        this.activitydiagramconfiguration_tracedinputvalues.add(activitydiagramconfiguration_tracedinputvalue);
    }

}