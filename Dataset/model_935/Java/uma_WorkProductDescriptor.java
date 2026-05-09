





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProductDescriptor extends Descriptor {

    private String optionalInputTo;
    private String workProduct;
    private String group2;
    private String responsibleRole;
    private String impactedBy;
    private String externalInputTo;
    private String activityEntryState;
    private String activityExitState;
    private String impacts;
    private String mandatoryInputTo;
    private String deliverableParts;
    private String outputFrom;



    public uma_WorkProductDescriptor(
        String optionalInputTo,        String workProduct,        String group2,        String responsibleRole,        String impactedBy,        String externalInputTo,        String activityEntryState,        String activityExitState,        String impacts,        String mandatoryInputTo,        String deliverableParts,        String outputFrom    ) {
        super(
        );
        this.optionalInputTo = optionalInputTo;
        this.workProduct = workProduct;
        this.group2 = group2;
        this.responsibleRole = responsibleRole;
        this.impactedBy = impactedBy;
        this.externalInputTo = externalInputTo;
        this.activityEntryState = activityEntryState;
        this.activityExitState = activityExitState;
        this.impacts = impacts;
        this.mandatoryInputTo = mandatoryInputTo;
        this.deliverableParts = deliverableParts;
        this.outputFrom = outputFrom;
    }


    public String getOptionalinputto() {
        return optionalInputTo;
    }

    public void setOptionalinputto(String optionalInputTo) {
        this.optionalInputTo = optionalInputTo;
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
    public String getResponsiblerole() {
        return responsibleRole;
    }

    public void setResponsiblerole(String responsibleRole) {
        this.responsibleRole = responsibleRole;
    }
    public String getImpactedby() {
        return impactedBy;
    }

    public void setImpactedby(String impactedBy) {
        this.impactedBy = impactedBy;
    }
    public String getExternalinputto() {
        return externalInputTo;
    }

    public void setExternalinputto(String externalInputTo) {
        this.externalInputTo = externalInputTo;
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
    public String getImpacts() {
        return impacts;
    }

    public void setImpacts(String impacts) {
        this.impacts = impacts;
    }
    public String getMandatoryinputto() {
        return mandatoryInputTo;
    }

    public void setMandatoryinputto(String mandatoryInputTo) {
        this.mandatoryInputTo = mandatoryInputTo;
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


}