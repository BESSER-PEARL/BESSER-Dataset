




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class BZ_BZIssue  {

    private String blocks;
    private int issueId;
    private String ccList;
    private String issueURL;
    private String status;
    private String versionFixedIn;
    private LocalDate lastModifiedOn;
    private String issueTitle;
    private String reportedByUsername;
    private String productName;
    private String latestCommit;
    private String componentName;
    private String keywords;
    private String importance;
    private String milestone;
    private String seeAlso;
    private String dependsOn;
    private String assignedTo;
    private String referenceURL;
    private String classification;
    private String platform;
    private String version;
    private String reportedBy;
    private LocalDate reportedOn;





    private BZ_BZComponent bz_bzcomponent;




    private BZ_BZRepo bz_bzrepo;




    private BZ_BZProduct bz_bzproduct;




    private BZ_BZComponent bz_bzcomponent;




    private BZ_BZRepo bz_bzrepo;




    private BZ_BZProduct bz_bzproduct;


    public BZ_BZIssue(
        String blocks,        int issueId,        String ccList,        String issueURL,        String status,        String versionFixedIn,        LocalDate lastModifiedOn,        String issueTitle,        String reportedByUsername,        String productName,        String latestCommit,        String componentName,        String keywords,        String importance,        String milestone,        String seeAlso,        String dependsOn,        String assignedTo,        String referenceURL,        String classification,        String platform,        String version,        String reportedBy,        LocalDate reportedOn    ) {
        this.blocks = blocks;
        this.issueId = issueId;
        this.ccList = ccList;
        this.issueURL = issueURL;
        this.status = status;
        this.versionFixedIn = versionFixedIn;
        this.lastModifiedOn = lastModifiedOn;
        this.issueTitle = issueTitle;
        this.reportedByUsername = reportedByUsername;
        this.productName = productName;
        this.latestCommit = latestCommit;
        this.componentName = componentName;
        this.keywords = keywords;
        this.importance = importance;
        this.milestone = milestone;
        this.seeAlso = seeAlso;
        this.dependsOn = dependsOn;
        this.assignedTo = assignedTo;
        this.referenceURL = referenceURL;
        this.classification = classification;
        this.platform = platform;
        this.version = version;
        this.reportedBy = reportedBy;
        this.reportedOn = reportedOn;
    }


    public String getBlocks() {
        return blocks;
    }

    public void setBlocks(String blocks) {
        this.blocks = blocks;
    }
    public int getIssueid() {
        return issueId;
    }

    public void setIssueid(int issueId) {
        this.issueId = issueId;
    }
    public String getCclist() {
        return ccList;
    }

    public void setCclist(String ccList) {
        this.ccList = ccList;
    }
    public String getIssueurl() {
        return issueURL;
    }

    public void setIssueurl(String issueURL) {
        this.issueURL = issueURL;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getVersionfixedin() {
        return versionFixedIn;
    }

    public void setVersionfixedin(String versionFixedIn) {
        this.versionFixedIn = versionFixedIn;
    }
    public LocalDate getLastmodifiedon() {
        return lastModifiedOn;
    }

    public void setLastmodifiedon(LocalDate lastModifiedOn) {
        this.lastModifiedOn = lastModifiedOn;
    }
    public String getIssuetitle() {
        return issueTitle;
    }

    public void setIssuetitle(String issueTitle) {
        this.issueTitle = issueTitle;
    }
    public String getReportedbyusername() {
        return reportedByUsername;
    }

    public void setReportedbyusername(String reportedByUsername) {
        this.reportedByUsername = reportedByUsername;
    }
    public String getProductname() {
        return productName;
    }

    public void setProductname(String productName) {
        this.productName = productName;
    }
    public String getLatestcommit() {
        return latestCommit;
    }

    public void setLatestcommit(String latestCommit) {
        this.latestCommit = latestCommit;
    }
    public String getComponentname() {
        return componentName;
    }

    public void setComponentname(String componentName) {
        this.componentName = componentName;
    }
    public String getKeywords() {
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }
    public String getImportance() {
        return importance;
    }

    public void setImportance(String importance) {
        this.importance = importance;
    }
    public String getMilestone() {
        return milestone;
    }

    public void setMilestone(String milestone) {
        this.milestone = milestone;
    }
    public String getSeealso() {
        return seeAlso;
    }

    public void setSeealso(String seeAlso) {
        this.seeAlso = seeAlso;
    }
    public String getDependson() {
        return dependsOn;
    }

    public void setDependson(String dependsOn) {
        this.dependsOn = dependsOn;
    }
    public String getAssignedto() {
        return assignedTo;
    }

    public void setAssignedto(String assignedTo) {
        this.assignedTo = assignedTo;
    }
    public String getReferenceurl() {
        return referenceURL;
    }

    public void setReferenceurl(String referenceURL) {
        this.referenceURL = referenceURL;
    }
    public String getClassification() {
        return classification;
    }

    public void setClassification(String classification) {
        this.classification = classification;
    }
    public String getPlatform() {
        return platform;
    }

    public void setPlatform(String platform) {
        this.platform = platform;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getReportedby() {
        return reportedBy;
    }

    public void setReportedby(String reportedBy) {
        this.reportedBy = reportedBy;
    }
    public LocalDate getReportedon() {
        return reportedOn;
    }

    public void setReportedon(LocalDate reportedOn) {
        this.reportedOn = reportedOn;
    }

    public BZ_BZComponent getBz_bzcomponent() {
        return bz_bzcomponent;
    }

    public void setBz_bzcomponent(BZ_BZComponent bz_bzcomponent) {
        this.bz_bzcomponent = bz_bzcomponent;
    }
    public BZ_BZRepo getBz_bzrepo() {
        return bz_bzrepo;
    }

    public void setBz_bzrepo(BZ_BZRepo bz_bzrepo) {
        this.bz_bzrepo = bz_bzrepo;
    }
    public BZ_BZProduct getBz_bzproduct() {
        return bz_bzproduct;
    }

    public void setBz_bzproduct(BZ_BZProduct bz_bzproduct) {
        this.bz_bzproduct = bz_bzproduct;
    }
    public BZ_BZComponent getBz_bzcomponent() {
        return bz_bzcomponent;
    }

    public void setBz_bzcomponent(BZ_BZComponent bz_bzcomponent) {
        this.bz_bzcomponent = bz_bzcomponent;
    }
    public BZ_BZRepo getBz_bzrepo() {
        return bz_bzrepo;
    }

    public void setBz_bzrepo(BZ_BZRepo bz_bzrepo) {
        this.bz_bzrepo = bz_bzrepo;
    }
    public BZ_BZProduct getBz_bzproduct() {
        return bz_bzproduct;
    }

    public void setBz_bzproduct(BZ_BZProduct bz_bzproduct) {
        this.bz_bzproduct = bz_bzproduct;
    }

}