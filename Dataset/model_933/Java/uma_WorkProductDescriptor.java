





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProductDescriptor extends Descriptor {

    private String optionalInputTo;
    private String responsibleRole;
    private String activityEntryState;
    private String activityExitState;
    private String workProduct;
    private String group2;
    private String mandatoryInputTo;
    private String externalInputTo;
    private String impactedBy;
    private String deliverableParts;
    private String outputFrom;
    private String impacts;





    private uma_ProcessComponentInterface uma_processcomponentinterface;


    public uma_WorkProductDescriptor(
        String optionalInputTo,        String responsibleRole,        String activityEntryState,        String activityExitState,        String workProduct,        String group2,        String mandatoryInputTo,        String externalInputTo,        String impactedBy,        String deliverableParts,        String outputFrom,        String impacts    ) {
        super(
        );
        this.optionalInputTo = optionalInputTo;
        this.responsibleRole = responsibleRole;
        this.activityEntryState = activityEntryState;
        this.activityExitState = activityExitState;
        this.workProduct = workProduct;
        this.group2 = group2;
        this.mandatoryInputTo = mandatoryInputTo;
        this.externalInputTo = externalInputTo;
        this.impactedBy = impactedBy;
        this.deliverableParts = deliverableParts;
        this.outputFrom = outputFrom;
        this.impacts = impacts;
    }


    public String getOptionalinputto() {
        return optionalInputTo;
    }

    public void setOptionalinputto(String optionalInputTo) {
        this.optionalInputTo = optionalInputTo;
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
    public String getActivityexitstate() {
        return activityExitState;
    }

    public void setActivityexitstate(String activityExitState) {
        this.activityExitState = activityExitState;
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
    public String getMandatoryinputto() {
        return mandatoryInputTo;
    }

    public void setMandatoryinputto(String mandatoryInputTo) {
        this.mandatoryInputTo = mandatoryInputTo;
    }
    public String getExternalinputto() {
        return externalInputTo;
    }

    public void setExternalinputto(String externalInputTo) {
        this.externalInputTo = externalInputTo;
    }
    public String getImpactedby() {
        return impactedBy;
    }

    public void setImpactedby(String impactedBy) {
        this.impactedBy = impactedBy;
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
    public String getImpacts() {
        return impacts;
    }

    public void setImpacts(String impacts) {
        this.impacts = impacts;
    }

    public uma_ProcessComponentInterface getUma_processcomponentinterface() {
        return uma_processcomponentinterface;
    }

    public void setUma_processcomponentinterface(uma_ProcessComponentInterface uma_processcomponentinterface) {
        this.uma_processcomponentinterface = uma_processcomponentinterface;
    }

}