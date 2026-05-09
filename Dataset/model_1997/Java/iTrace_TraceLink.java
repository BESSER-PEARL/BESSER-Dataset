





import java.util.List;
import java.util.ArrayList;

public class iTrace_TraceLink  {

    private String technicalBinding;
    private String createdOn;
    private String createdBy;
    private String mode;
    private String fromFileName;
    private String ruleName;
    private String comment;
    private String type;



    public iTrace_TraceLink(
        String technicalBinding,        String createdOn,        String createdBy,        String mode,        String fromFileName,        String ruleName,        String comment,        String type    ) {
        this.technicalBinding = technicalBinding;
        this.createdOn = createdOn;
        this.createdBy = createdBy;
        this.mode = mode;
        this.fromFileName = fromFileName;
        this.ruleName = ruleName;
        this.comment = comment;
        this.type = type;
    }


    public String getTechnicalbinding() {
        return technicalBinding;
    }

    public void setTechnicalbinding(String technicalBinding) {
        this.technicalBinding = technicalBinding;
    }
    public String getCreatedon() {
        return createdOn;
    }

    public void setCreatedon(String createdOn) {
        this.createdOn = createdOn;
    }
    public String getCreatedby() {
        return createdBy;
    }

    public void setCreatedby(String createdBy) {
        this.createdBy = createdBy;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }
    public String getFromfilename() {
        return fromFileName;
    }

    public void setFromfilename(String fromFileName) {
        this.fromFileName = fromFileName;
    }
    public String getRulename() {
        return ruleName;
    }

    public void setRulename(String ruleName) {
        this.ruleName = ruleName;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}