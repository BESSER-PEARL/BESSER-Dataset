





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProductDescriptor extends Descriptor {

    private String impacts;
    private String activityExitState;
    private String optionalInputTo;
    private String externalInputTo;
    private String deliverableParts;
    private String outputFrom;
    private String mandatoryInputTo;
    private String responsibleRole;
    private String activityEntryState;
    private String workProduct;
    private String group2;
    private String impactedBy;





    private uma_ProcessComponentInterface uma_processcomponentinterface;


    public uma_WorkProductDescriptor(
        String impacts,        String activityExitState,        String optionalInputTo,        String externalInputTo,        String deliverableParts,        String outputFrom,        String mandatoryInputTo,        String responsibleRole,        String activityEntryState,        String workProduct,        String group2,        String impactedBy    ) {
        super(
        );
        this.impacts = impacts;
        this.activityExitState = activityExitState;
        this.optionalInputTo = optionalInputTo;
        this.externalInputTo = externalInputTo;
        this.deliverableParts = deliverableParts;
        this.outputFrom = outputFrom;
        this.mandatoryInputTo = mandatoryInputTo;
        this.responsibleRole = responsibleRole;
        this.activityEntryState = activityEntryState;
        this.workProduct = workProduct;
        this.group2 = group2;
        this.impactedBy = impactedBy;
    }


    public String getImpacts() {
        return impacts;
    }

    public void setImpacts(String impacts) {
        this.impacts = impacts;
    }
    public String getActivityexitstate() {
        return activityExitState;
    }

    public void setActivityexitstate(String activityExitState) {
        this.activityExitState = activityExitState;
    }
    public String getOptionalinputto() {
        return optionalInputTo;
    }

    public void setOptionalinputto(String optionalInputTo) {
        this.optionalInputTo = optionalInputTo;
    }
    public String getExternalinputto() {
        return externalInputTo;
    }

    public void setExternalinputto(String externalInputTo) {
        this.externalInputTo = externalInputTo;
    }
    public String getDeliverableparts() {
        return deliverableParts;
    }

    public void setDeliverableparts(String deliverableParts) {
        this.deliverableParts = deliverableParts;
    }
    public String getOutputfrom() {
        return outputFrom;
    }

    public void setOutputfrom(String outputFrom) {
        this.outputFrom = outputFrom;
    }
    public String getMandatoryinputto() {
        return mandatoryInputTo;
    }

    public void setMandatoryinputto(String mandatoryInputTo) {
        this.mandatoryInputTo = mandatoryInputTo;
    }
    public String getResponsiblerole() {
        return responsibleRole;
    }

    public void setResponsiblerole(String responsibleRole) {
        this.responsibleRole = responsibleRole;
    }
    public String getActivityentrystate() {
        return activityEntryState;
    }

    public void setActivityentrystate(String activityEntryState) {
        this.activityEntryState = activityEntryState;
    }
    public String getWorkproduct() {
        return workProduct;
    }

    public void setWorkproduct(String workProduct) {
        this.workProduct = workProduct;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getImpactedby() {
        return impactedBy;
    }

    public void setImpactedby(String impactedBy) {
        this.impactedBy = impactedBy;
    }

    public uma_ProcessComponentInterface getUma_processcomponentinterface() {
        return uma_processcomponentinterface;
    }

    public void setUma_processcomponentinterface(uma_ProcessComponentInterface uma_processcomponentinterface) {
        this.uma_processcomponentinterface = uma_processcomponentinterface;
    }

}