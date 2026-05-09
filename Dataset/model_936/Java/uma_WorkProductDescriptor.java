





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProductDescriptor extends Descriptor {

    private String activityEntryState;
    private String group2;
    private String deliverableParts;
    private String activityExitState;
    private String mandatoryInputTo;
    private String workProduct;
    private String externalInputTo;
    private String responsibleRole;
    private String optionalInputTo;
    private String impacts;
    private String outputFrom;
    private String impactedBy;





    private uma_ProcessComponentInterface uma_processcomponentinterface;


    public uma_WorkProductDescriptor(
        String activityEntryState,        String group2,        String deliverableParts,        String activityExitState,        String mandatoryInputTo,        String workProduct,        String externalInputTo,        String responsibleRole,        String optionalInputTo,        String impacts,        String outputFrom,        String impactedBy    ) {
        super(
        );
        this.activityEntryState = activityEntryState;
        this.group2 = group2;
        this.deliverableParts = deliverableParts;
        this.activityExitState = activityExitState;
        this.mandatoryInputTo = mandatoryInputTo;
        this.workProduct = workProduct;
        this.externalInputTo = externalInputTo;
        this.responsibleRole = responsibleRole;
        this.optionalInputTo = optionalInputTo;
        this.impacts = impacts;
        this.outputFrom = outputFrom;
        this.impactedBy = impactedBy;
    }


    public String getActivityentrystate() {
        return activityEntryState;
    }

    public void setActivityentrystate(String activityEntryState) {
        this.activityEntryState = activityEntryState;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getDeliverableparts() {
        return deliverableParts;
    }

    public void setDeliverableparts(String deliverableParts) {
        this.deliverableParts = deliverableParts;
    }
    public String getActivityexitstate() {
        return activityExitState;
    }

    public void setActivityexitstate(String activityExitState) {
        this.activityExitState = activityExitState;
    }
    public String getMandatoryinputto() {
        return mandatoryInputTo;
    }

    public void setMandatoryinputto(String mandatoryInputTo) {
        this.mandatoryInputTo = mandatoryInputTo;
    }
    public String getWorkproduct() {
        return workProduct;
    }

    public void setWorkproduct(String workProduct) {
        this.workProduct = workProduct;
    }
    public String getExternalinputto() {
        return externalInputTo;
    }

    public void setExternalinputto(String externalInputTo) {
        this.externalInputTo = externalInputTo;
    }
    public String getResponsiblerole() {
        return responsibleRole;
    }

    public void setResponsiblerole(String responsibleRole) {
        this.responsibleRole = responsibleRole;
    }
    public String getOptionalinputto() {
        return optionalInputTo;
    }

    public void setOptionalinputto(String optionalInputTo) {
        this.optionalInputTo = optionalInputTo;
    }
    public String getImpacts() {
        return impacts;
    }

    public void setImpacts(String impacts) {
        this.impacts = impacts;
    }
    public String getOutputfrom() {
        return outputFrom;
    }

    public void setOutputfrom(String outputFrom) {
        this.outputFrom = outputFrom;
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