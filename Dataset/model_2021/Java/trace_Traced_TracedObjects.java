





import java.util.List;
import java.util.ArrayList;

public class trace_Traced_TracedObjects  {






    private List<activitydiagramConfiguration_TracedTrace> activitydiagramconfiguration_tracedtraces;




    private List<activitydiagram_TracedActivity> activitydiagram_tracedactivitys;




    private List<activitydiagram_TracedDecisionNode> activitydiagram_traceddecisionnodes;




    private List<activitydiagram_TracedOpaqueAction> activitydiagram_tracedopaqueactions;




    private List<activitydiagramConfiguration_TracedInputValue> activitydiagramconfiguration_tracedinputvalues;




    private List<activitydiagram_TracedBooleanVariable> activitydiagram_tracedbooleanvariables;




    private List<activitydiagram_TracedStringVariable> activitydiagram_tracedstringvariables;




    private List<activitydiagram_TracedMergeNode> activitydiagram_tracedmergenodes;




    private List<activitydiagramConfiguration_TracedOffer> activitydiagramconfiguration_tracedoffers;




    private List<activitydiagram_TracedActivityFinalNode> activitydiagram_tracedactivityfinalnodes;




    private List<activitydiagram_TracedForkNode> activitydiagram_tracedforknodes;




    private List<activitydiagramConfiguration_TracedForkedToken> activitydiagramconfiguration_tracedforkedtokens;




    private List<activitydiagram_TracedInitialNode> activitydiagram_tracedinitialnodes;




    private List<activitydiagramConfiguration_TracedInput> activitydiagramconfiguration_tracedinputs;




    private List<activitydiagram_TracedIntegerVariable> activitydiagram_tracedintegervariables;


    public trace_Traced_TracedObjects(
    ) {
        this.activitydiagramconfiguration_tracedtraces = new ArrayList<>();
        this.activitydiagram_tracedactivitys = new ArrayList<>();
        this.activitydiagram_traceddecisionnodes = new ArrayList<>();
        this.activitydiagram_tracedopaqueactions = new ArrayList<>();
        this.activitydiagramconfiguration_tracedinputvalues = new ArrayList<>();
        this.activitydiagram_tracedbooleanvariables = new ArrayList<>();
        this.activitydiagram_tracedstringvariables = new ArrayList<>();
        this.activitydiagram_tracedmergenodes = new ArrayList<>();
        this.activitydiagramconfiguration_tracedoffers = new ArrayList<>();
        this.activitydiagram_tracedactivityfinalnodes = new ArrayList<>();
        this.activitydiagram_tracedforknodes = new ArrayList<>();
        this.activitydiagramconfiguration_tracedforkedtokens = new ArrayList<>();
        this.activitydiagram_tracedinitialnodes = new ArrayList<>();
        this.activitydiagramconfiguration_tracedinputs = new ArrayList<>();
        this.activitydiagram_tracedintegervariables = new ArrayList<>();
    }

    public trace_Traced_TracedObjects(
        ArrayList<activitydiagramConfiguration_TracedTrace> activitydiagramconfiguration_tracedtraces,        ArrayList<activitydiagram_TracedActivity> activitydiagram_tracedactivitys,        ArrayList<activitydiagram_TracedDecisionNode> activitydiagram_traceddecisionnodes,        ArrayList<activitydiagram_TracedOpaqueAction> activitydiagram_tracedopaqueactions,        ArrayList<activitydiagramConfiguration_TracedInputValue> activitydiagramconfiguration_tracedinputvalues,        ArrayList<activitydiagram_TracedBooleanVariable> activitydiagram_tracedbooleanvariables,        ArrayList<activitydiagram_TracedStringVariable> activitydiagram_tracedstringvariables,        ArrayList<activitydiagram_TracedMergeNode> activitydiagram_tracedmergenodes,        ArrayList<activitydiagramConfiguration_TracedOffer> activitydiagramconfiguration_tracedoffers,        ArrayList<activitydiagram_TracedActivityFinalNode> activitydiagram_tracedactivityfinalnodes,        ArrayList<activitydiagram_TracedForkNode> activitydiagram_tracedforknodes,        ArrayList<activitydiagramConfiguration_TracedForkedToken> activitydiagramconfiguration_tracedforkedtokens,        ArrayList<activitydiagram_TracedInitialNode> activitydiagram_tracedinitialnodes,        ArrayList<activitydiagramConfiguration_TracedInput> activitydiagramconfiguration_tracedinputs,        ArrayList<activitydiagram_TracedIntegerVariable> activitydiagram_tracedintegervariables    ) {
        this.activitydiagramconfiguration_tracedtraces = activitydiagramconfiguration_tracedtraces;
        this.activitydiagram_tracedactivitys = activitydiagram_tracedactivitys;
        this.activitydiagram_traceddecisionnodes = activitydiagram_traceddecisionnodes;
        this.activitydiagram_tracedopaqueactions = activitydiagram_tracedopaqueactions;
        this.activitydiagramconfiguration_tracedinputvalues = activitydiagramconfiguration_tracedinputvalues;
        this.activitydiagram_tracedbooleanvariables = activitydiagram_tracedbooleanvariables;
        this.activitydiagram_tracedstringvariables = activitydiagram_tracedstringvariables;
        this.activitydiagram_tracedmergenodes = activitydiagram_tracedmergenodes;
        this.activitydiagramconfiguration_tracedoffers = activitydiagramconfiguration_tracedoffers;
        this.activitydiagram_tracedactivityfinalnodes = activitydiagram_tracedactivityfinalnodes;
        this.activitydiagram_tracedforknodes = activitydiagram_tracedforknodes;
        this.activitydiagramconfiguration_tracedforkedtokens = activitydiagramconfiguration_tracedforkedtokens;
        this.activitydiagram_tracedinitialnodes = activitydiagram_tracedinitialnodes;
        this.activitydiagramconfiguration_tracedinputs = activitydiagramconfiguration_tracedinputs;
        this.activitydiagram_tracedintegervariables = activitydiagram_tracedintegervariables;
    }


    public List<activitydiagramConfiguration_TracedTrace> getActivitydiagramconfiguration_tracedtraces() {
        return activitydiagramconfiguration_tracedtraces;
    }

    public void addActivitydiagramconfiguration_tracedtrace(Activitydiagramconfiguration_tracedtrace activitydiagramconfiguration_tracedtrace) {
        this.activitydiagramconfiguration_tracedtraces.add(activitydiagramconfiguration_tracedtrace);
    }
    public List<activitydiagram_TracedActivity> getActivitydiagram_tracedactivitys() {
        return activitydiagram_tracedactivitys;
    }

    public void addActivitydiagram_tracedactivity(Activitydiagram_tracedactivity activitydiagram_tracedactivity) {
        this.activitydiagram_tracedactivitys.add(activitydiagram_tracedactivity);
    }
    public List<activitydiagram_TracedDecisionNode> getActivitydiagram_traceddecisionnodes() {
        return activitydiagram_traceddecisionnodes;
    }

    public void addActivitydiagram_traceddecisionnode(Activitydiagram_traceddecisionnode activitydiagram_traceddecisionnode) {
        this.activitydiagram_traceddecisionnodes.add(activitydiagram_traceddecisionnode);
    }
    public List<activitydiagram_TracedOpaqueAction> getActivitydiagram_tracedopaqueactions() {
        return activitydiagram_tracedopaqueactions;
    }

    public void addActivitydiagram_tracedopaqueaction(Activitydiagram_tracedopaqueaction activitydiagram_tracedopaqueaction) {
        this.activitydiagram_tracedopaqueactions.add(activitydiagram_tracedopaqueaction);
    }
    public List<activitydiagramConfiguration_TracedInputValue> getActivitydiagramconfiguration_tracedinputvalues() {
        return activitydiagramconfiguration_tracedinputvalues;
    }

    public void addActivitydiagramconfiguration_tracedinputvalue(Activitydiagramconfiguration_tracedinputvalue activitydiagramconfiguration_tracedinputvalue) {
        this.activitydiagramconfiguration_tracedinputvalues.add(activitydiagramconfiguration_tracedinputvalue);
    }
    public List<activitydiagram_TracedBooleanVariable> getActivitydiagram_tracedbooleanvariables() {
        return activitydiagram_tracedbooleanvariables;
    }

    public void addActivitydiagram_tracedbooleanvariable(Activitydiagram_tracedbooleanvariable activitydiagram_tracedbooleanvariable) {
        this.activitydiagram_tracedbooleanvariables.add(activitydiagram_tracedbooleanvariable);
    }
    public List<activitydiagram_TracedStringVariable> getActivitydiagram_tracedstringvariables() {
        return activitydiagram_tracedstringvariables;
    }

    public void addActivitydiagram_tracedstringvariable(Activitydiagram_tracedstringvariable activitydiagram_tracedstringvariable) {
        this.activitydiagram_tracedstringvariables.add(activitydiagram_tracedstringvariable);
    }
    public List<activitydiagram_TracedMergeNode> getActivitydiagram_tracedmergenodes() {
        return activitydiagram_tracedmergenodes;
    }

    public void addActivitydiagram_tracedmergenode(Activitydiagram_tracedmergenode activitydiagram_tracedmergenode) {
        this.activitydiagram_tracedmergenodes.add(activitydiagram_tracedmergenode);
    }
    public List<activitydiagramConfiguration_TracedOffer> getActivitydiagramconfiguration_tracedoffers() {
        return activitydiagramconfiguration_tracedoffers;
    }

    public void addActivitydiagramconfiguration_tracedoffer(Activitydiagramconfiguration_tracedoffer activitydiagramconfiguration_tracedoffer) {
        this.activitydiagramconfiguration_tracedoffers.add(activitydiagramconfiguration_tracedoffer);
    }
    public List<activitydiagram_TracedActivityFinalNode> getActivitydiagram_tracedactivityfinalnodes() {
        return activitydiagram_tracedactivityfinalnodes;
    }

    public void addActivitydiagram_tracedactivityfinalnode(Activitydiagram_tracedactivityfinalnode activitydiagram_tracedactivityfinalnode) {
        this.activitydiagram_tracedactivityfinalnodes.add(activitydiagram_tracedactivityfinalnode);
    }
    public List<activitydiagram_TracedForkNode> getActivitydiagram_tracedforknodes() {
        return activitydiagram_tracedforknodes;
    }

    public void addActivitydiagram_tracedforknode(Activitydiagram_tracedforknode activitydiagram_tracedforknode) {
        this.activitydiagram_tracedforknodes.add(activitydiagram_tracedforknode);
    }
    public List<activitydiagramConfiguration_TracedForkedToken> getActivitydiagramconfiguration_tracedforkedtokens() {
        return activitydiagramconfiguration_tracedforkedtokens;
    }

    public void addActivitydiagramconfiguration_tracedforkedtoken(Activitydiagramconfiguration_tracedforkedtoken activitydiagramconfiguration_tracedforkedtoken) {
        this.activitydiagramconfiguration_tracedforkedtokens.add(activitydiagramconfiguration_tracedforkedtoken);
    }
    public List<activitydiagram_TracedInitialNode> getActivitydiagram_tracedinitialnodes() {
        return activitydiagram_tracedinitialnodes;
    }

    public void addActivitydiagram_tracedinitialnode(Activitydiagram_tracedinitialnode activitydiagram_tracedinitialnode) {
        this.activitydiagram_tracedinitialnodes.add(activitydiagram_tracedinitialnode);
    }
    public List<activitydiagramConfiguration_TracedInput> getActivitydiagramconfiguration_tracedinputs() {
        return activitydiagramconfiguration_tracedinputs;
    }

    public void addActivitydiagramconfiguration_tracedinput(Activitydiagramconfiguration_tracedinput activitydiagramconfiguration_tracedinput) {
        this.activitydiagramconfiguration_tracedinputs.add(activitydiagramconfiguration_tracedinput);
    }
    public List<activitydiagram_TracedIntegerVariable> getActivitydiagram_tracedintegervariables() {
        return activitydiagram_tracedintegervariables;
    }

    public void addActivitydiagram_tracedintegervariable(Activitydiagram_tracedintegervariable activitydiagram_tracedintegervariable) {
        this.activitydiagram_tracedintegervariables.add(activitydiagram_tracedintegervariable);
    }

}