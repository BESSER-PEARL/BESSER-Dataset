




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class requirement_Requirement extends NamedElement {

    private LocalDate createdOn;
    private String id;
    private String subtype;
    private String statement;
    private String rationale;
    private String status;
    private LocalDate modifiedOn;
    private int version;
    private String type;
    private String acceptanceCriteria;





    private requirement_Category requirement_category;




    private requirement_Category requirement_category;


    public requirement_Requirement(
        LocalDate createdOn,        String id,        String subtype,        String statement,        String rationale,        String status,        LocalDate modifiedOn,        int version,        String type,        String acceptanceCriteria    ) {
        super(
        );
        this.createdOn = createdOn;
        this.id = id;
        this.subtype = subtype;
        this.statement = statement;
        this.rationale = rationale;
        this.status = status;
        this.modifiedOn = modifiedOn;
        this.version = version;
        this.type = type;
        this.acceptanceCriteria = acceptanceCriteria;
    }


    public LocalDate getCreatedon() {
        return createdOn;
    }

    public void setCreatedon(LocalDate createdOn) {
        this.createdOn = createdOn;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSubtype() {
        return subtype;
    }

    public void setSubtype(String subtype) {
        this.subtype = subtype;
    }
    public String getStatement() {
        return statement;
    }

    public void setStatement(String statement) {
        this.statement = statement;
    }
    public String getRationale() {
        return rationale;
    }

    public void setRationale(String rationale) {
        this.rationale = rationale;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public LocalDate getModifiedon() {
        return modifiedOn;
    }

    public void setModifiedon(LocalDate modifiedOn) {
        this.modifiedOn = modifiedOn;
    }
    public int getVersion() {
        return version;
    }

    public void setVersion(int version) {
        this.version = version;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAcceptancecriteria() {
        return acceptanceCriteria;
    }

    public void setAcceptancecriteria(String acceptanceCriteria) {
        this.acceptanceCriteria = acceptanceCriteria;
    }

    public requirement_Category getRequirement_category() {
        return requirement_category;
    }

    public void setRequirement_category(requirement_Category requirement_category) {
        this.requirement_category = requirement_category;
    }
    public requirement_Category getRequirement_category() {
        return requirement_category;
    }

    public void setRequirement_category(requirement_Category requirement_category) {
        this.requirement_category = requirement_category;
    }

}