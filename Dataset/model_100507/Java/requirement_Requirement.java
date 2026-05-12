




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class requirement_Requirement extends NamedElement {

    private String status;
    private String type;
    private String rationale;
    private String subtype;
    private LocalDate createdOn;
    private String acceptanceCriteria;
    private int version;
    private String id;
    private String statement;
    private LocalDate modifiedOn;



    public requirement_Requirement(
        String status,        String type,        String rationale,        String subtype,        LocalDate createdOn,        String acceptanceCriteria,        int version,        String id,        String statement,        LocalDate modifiedOn    ) {
        super(
        );
        this.status = status;
        this.type = type;
        this.rationale = rationale;
        this.subtype = subtype;
        this.createdOn = createdOn;
        this.acceptanceCriteria = acceptanceCriteria;
        this.version = version;
        this.id = id;
        this.statement = statement;
        this.modifiedOn = modifiedOn;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getRationale() {
        return rationale;
    }

    public void setRationale(String rationale) {
        this.rationale = rationale;
    }
    public String getSubtype() {
        return subtype;
    }

    public void setSubtype(String subtype) {
        this.subtype = subtype;
    }
    public LocalDate getCreatedon() {
        return createdOn;
    }

    public void setCreatedon(LocalDate createdOn) {
        this.createdOn = createdOn;
    }
    public String getAcceptancecriteria() {
        return acceptanceCriteria;
    }

    public void setAcceptancecriteria(String acceptanceCriteria) {
        this.acceptanceCriteria = acceptanceCriteria;
    }
    public int getVersion() {
        return version;
    }

    public void setVersion(int version) {
        this.version = version;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getStatement() {
        return statement;
    }

    public void setStatement(String statement) {
        this.statement = statement;
    }
    public LocalDate getModifiedon() {
        return modifiedOn;
    }

    public void setModifiedon(LocalDate modifiedOn) {
        this.modifiedOn = modifiedOn;
    }


}