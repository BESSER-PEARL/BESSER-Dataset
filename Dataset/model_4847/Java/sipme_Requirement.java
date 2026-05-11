




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class sipme_Requirement extends SIPME_object {

    private String requirementStatement;
    private String requirementNature;
    private String requirementStatus;
    private LocalDate requirementDate;
    private String requirementVersion;
    private int requirementMaturity;
    private String requirementOrigin;
    private int requirementPriority;





    private sipme_Objective sipme_objective;




    private sipme_EnterpriseProcessor sipme_enterpriseprocessor;




    private sipme_Stakeholder sipme_stakeholder;




    private sipme_Objective sipme_objective;




    private sipme_Activity sipme_activity;




    private sipme_Requirement sipme_requirement;




    private List<sipme_Stakeholder> sipme_stakeholders;




    private List<sipme_EnterpriseResource> sipme_enterpriseresources;


    public sipme_Requirement(
        String requirementStatement,        String requirementNature,        String requirementStatus,        LocalDate requirementDate,        String requirementVersion,        int requirementMaturity,        String requirementOrigin,        int requirementPriority    ) {
        super(
        );
        this.requirementStatement = requirementStatement;
        this.requirementNature = requirementNature;
        this.requirementStatus = requirementStatus;
        this.requirementDate = requirementDate;
        this.requirementVersion = requirementVersion;
        this.requirementMaturity = requirementMaturity;
        this.requirementOrigin = requirementOrigin;
        this.requirementPriority = requirementPriority;
        this.sipme_stakeholders = new ArrayList<>();
        this.sipme_enterpriseresources = new ArrayList<>();
    }

    public sipme_Requirement(
        String requirementStatement,        String requirementNature,        String requirementStatus,        LocalDate requirementDate,        String requirementVersion,        int requirementMaturity,        String requirementOrigin,        int requirementPriority        ArrayList<sipme_Stakeholder> sipme_stakeholders,        ArrayList<sipme_EnterpriseResource> sipme_enterpriseresources    ) {
        this.requirementStatement = requirementStatement;
        this.requirementNature = requirementNature;
        this.requirementStatus = requirementStatus;
        this.requirementDate = requirementDate;
        this.requirementVersion = requirementVersion;
        this.requirementMaturity = requirementMaturity;
        this.requirementOrigin = requirementOrigin;
        this.requirementPriority = requirementPriority;
        this.sipme_stakeholders = sipme_stakeholders;
        this.sipme_enterpriseresources = sipme_enterpriseresources;
    }

    public String getRequirementstatement() {
        return requirementStatement;
    }

    public void setRequirementstatement(String requirementStatement) {
        this.requirementStatement = requirementStatement;
    }
    public String getRequirementnature() {
        return requirementNature;
    }

    public void setRequirementnature(String requirementNature) {
        this.requirementNature = requirementNature;
    }
    public String getRequirementstatus() {
        return requirementStatus;
    }

    public void setRequirementstatus(String requirementStatus) {
        this.requirementStatus = requirementStatus;
    }
    public LocalDate getRequirementdate() {
        return requirementDate;
    }

    public void setRequirementdate(LocalDate requirementDate) {
        this.requirementDate = requirementDate;
    }
    public String getRequirementversion() {
        return requirementVersion;
    }

    public void setRequirementversion(String requirementVersion) {
        this.requirementVersion = requirementVersion;
    }
    public int getRequirementmaturity() {
        return requirementMaturity;
    }

    public void setRequirementmaturity(int requirementMaturity) {
        this.requirementMaturity = requirementMaturity;
    }
    public String getRequirementorigin() {
        return requirementOrigin;
    }

    public void setRequirementorigin(String requirementOrigin) {
        this.requirementOrigin = requirementOrigin;
    }
    public int getRequirementpriority() {
        return requirementPriority;
    }

    public void setRequirementpriority(int requirementPriority) {
        this.requirementPriority = requirementPriority;
    }

    public sipme_Objective getSipme_objective() {
        return sipme_objective;
    }

    public void setSipme_objective(sipme_Objective sipme_objective) {
        this.sipme_objective = sipme_objective;
    }
    public sipme_EnterpriseProcessor getSipme_enterpriseprocessor() {
        return sipme_enterpriseprocessor;
    }

    public void setSipme_enterpriseprocessor(sipme_EnterpriseProcessor sipme_enterpriseprocessor) {
        this.sipme_enterpriseprocessor = sipme_enterpriseprocessor;
    }
    public sipme_Stakeholder getSipme_stakeholder() {
        return sipme_stakeholder;
    }

    public void setSipme_stakeholder(sipme_Stakeholder sipme_stakeholder) {
        this.sipme_stakeholder = sipme_stakeholder;
    }
    public sipme_Objective getSipme_objective() {
        return sipme_objective;
    }

    public void setSipme_objective(sipme_Objective sipme_objective) {
        this.sipme_objective = sipme_objective;
    }
    public sipme_Activity getSipme_activity() {
        return sipme_activity;
    }

    public void setSipme_activity(sipme_Activity sipme_activity) {
        this.sipme_activity = sipme_activity;
    }
    public sipme_Requirement getSipme_requirement() {
        return sipme_requirement;
    }

    public void setSipme_requirement(sipme_Requirement sipme_requirement) {
        this.sipme_requirement = sipme_requirement;
    }
    public List<sipme_Stakeholder> getSipme_stakeholders() {
        return sipme_stakeholders;
    }

    public void addSipme_stakeholder(Sipme_stakeholder sipme_stakeholder) {
        this.sipme_stakeholders.add(sipme_stakeholder);
    }
    public List<sipme_EnterpriseResource> getSipme_enterpriseresources() {
        return sipme_enterpriseresources;
    }

    public void addSipme_enterpriseresource(Sipme_enterpriseresource sipme_enterpriseresource) {
        this.sipme_enterpriseresources.add(sipme_enterpriseresource);
    }

}