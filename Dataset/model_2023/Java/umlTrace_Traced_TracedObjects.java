





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Traced_TracedObjects  {






    private List<IntermediateActivities_TracedOffer> intermediateactivities_tracedoffers;




    private List<Loci_TracedExecutionEnvironment> loci_tracedexecutionenvironments;




    private List<IntermediateActivities_TracedActivityEdgeInstance> intermediateactivities_tracedactivityedgeinstances;




    private List<Kernel_TracedBooleanValue> kernel_tracedbooleanvalues;




    private List<IntermediateActivities_TracedObjectToken> intermediateactivities_tracedobjecttokens;




    private List<uml_TracedArtifact> uml_tracedartifacts;




    private List<Input_TracedInputParameterValues> input_tracedinputparametervaluess;




    private List<IntermediateActivities_TracedActivityExecution> intermediateactivities_tracedactivityexecutions;




    private List<uml_TracedOpaqueBehavior> uml_tracedopaquebehaviors;


    public umlTrace_Traced_TracedObjects(
    ) {
        this.intermediateactivities_tracedoffers = new ArrayList<>();
        this.loci_tracedexecutionenvironments = new ArrayList<>();
        this.intermediateactivities_tracedactivityedgeinstances = new ArrayList<>();
        this.kernel_tracedbooleanvalues = new ArrayList<>();
        this.intermediateactivities_tracedobjecttokens = new ArrayList<>();
        this.uml_tracedartifacts = new ArrayList<>();
        this.input_tracedinputparametervaluess = new ArrayList<>();
        this.intermediateactivities_tracedactivityexecutions = new ArrayList<>();
        this.uml_tracedopaquebehaviors = new ArrayList<>();
    }

    public umlTrace_Traced_TracedObjects(
        ArrayList<IntermediateActivities_TracedOffer> intermediateactivities_tracedoffers,        ArrayList<Loci_TracedExecutionEnvironment> loci_tracedexecutionenvironments,        ArrayList<IntermediateActivities_TracedActivityEdgeInstance> intermediateactivities_tracedactivityedgeinstances,        ArrayList<Kernel_TracedBooleanValue> kernel_tracedbooleanvalues,        ArrayList<IntermediateActivities_TracedObjectToken> intermediateactivities_tracedobjecttokens,        ArrayList<uml_TracedArtifact> uml_tracedartifacts,        ArrayList<Input_TracedInputParameterValues> input_tracedinputparametervaluess,        ArrayList<IntermediateActivities_TracedActivityExecution> intermediateactivities_tracedactivityexecutions,        ArrayList<uml_TracedOpaqueBehavior> uml_tracedopaquebehaviors    ) {
        this.intermediateactivities_tracedoffers = intermediateactivities_tracedoffers;
        this.loci_tracedexecutionenvironments = loci_tracedexecutionenvironments;
        this.intermediateactivities_tracedactivityedgeinstances = intermediateactivities_tracedactivityedgeinstances;
        this.kernel_tracedbooleanvalues = kernel_tracedbooleanvalues;
        this.intermediateactivities_tracedobjecttokens = intermediateactivities_tracedobjecttokens;
        this.uml_tracedartifacts = uml_tracedartifacts;
        this.input_tracedinputparametervaluess = input_tracedinputparametervaluess;
        this.intermediateactivities_tracedactivityexecutions = intermediateactivities_tracedactivityexecutions;
        this.uml_tracedopaquebehaviors = uml_tracedopaquebehaviors;
    }


    public List<IntermediateActivities_TracedOffer> getIntermediateactivities_tracedoffers() {
        return intermediateactivities_tracedoffers;
    }

    public void addIntermediateactivities_tracedoffer(Intermediateactivities_tracedoffer intermediateactivities_tracedoffer) {
        this.intermediateactivities_tracedoffers.add(intermediateactivities_tracedoffer);
    }
    public List<Loci_TracedExecutionEnvironment> getLoci_tracedexecutionenvironments() {
        return loci_tracedexecutionenvironments;
    }

    public void addLoci_tracedexecutionenvironment(Loci_tracedexecutionenvironment loci_tracedexecutionenvironment) {
        this.loci_tracedexecutionenvironments.add(loci_tracedexecutionenvironment);
    }
    public List<IntermediateActivities_TracedActivityEdgeInstance> getIntermediateactivities_tracedactivityedgeinstances() {
        return intermediateactivities_tracedactivityedgeinstances;
    }

    public void addIntermediateactivities_tracedactivityedgeinstance(Intermediateactivities_tracedactivityedgeinstance intermediateactivities_tracedactivityedgeinstance) {
        this.intermediateactivities_tracedactivityedgeinstances.add(intermediateactivities_tracedactivityedgeinstance);
    }
    public List<Kernel_TracedBooleanValue> getKernel_tracedbooleanvalues() {
        return kernel_tracedbooleanvalues;
    }

    public void addKernel_tracedbooleanvalue(Kernel_tracedbooleanvalue kernel_tracedbooleanvalue) {
        this.kernel_tracedbooleanvalues.add(kernel_tracedbooleanvalue);
    }
    public List<IntermediateActivities_TracedObjectToken> getIntermediateactivities_tracedobjecttokens() {
        return intermediateactivities_tracedobjecttokens;
    }

    public void addIntermediateactivities_tracedobjecttoken(Intermediateactivities_tracedobjecttoken intermediateactivities_tracedobjecttoken) {
        this.intermediateactivities_tracedobjecttokens.add(intermediateactivities_tracedobjecttoken);
    }
    public List<uml_TracedArtifact> getUml_tracedartifacts() {
        return uml_tracedartifacts;
    }

    public void addUml_tracedartifact(Uml_tracedartifact uml_tracedartifact) {
        this.uml_tracedartifacts.add(uml_tracedartifact);
    }
    public List<Input_TracedInputParameterValues> getInput_tracedinputparametervaluess() {
        return input_tracedinputparametervaluess;
    }

    public void addInput_tracedinputparametervalues(Input_tracedinputparametervalues input_tracedinputparametervalues) {
        this.input_tracedinputparametervaluess.add(input_tracedinputparametervalues);
    }
    public List<IntermediateActivities_TracedActivityExecution> getIntermediateactivities_tracedactivityexecutions() {
        return intermediateactivities_tracedactivityexecutions;
    }

    public void addIntermediateactivities_tracedactivityexecution(Intermediateactivities_tracedactivityexecution intermediateactivities_tracedactivityexecution) {
        this.intermediateactivities_tracedactivityexecutions.add(intermediateactivities_tracedactivityexecution);
    }
    public List<uml_TracedOpaqueBehavior> getUml_tracedopaquebehaviors() {
        return uml_tracedopaquebehaviors;
    }

    public void addUml_tracedopaquebehavior(Uml_tracedopaquebehavior uml_tracedopaquebehavior) {
        this.uml_tracedopaquebehaviors.add(uml_tracedopaquebehavior);
    }

}