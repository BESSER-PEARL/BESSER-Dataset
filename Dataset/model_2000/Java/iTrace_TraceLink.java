





import java.util.List;
import java.util.ArrayList;

public class iTrace_TraceLink  {

    private String fromFileName;
    private String comment;
    private String mode;
    private String ruleName;
    private String type;
    private String createdOn;
    private String technicalBinding;
    private String createdBy;





    private iTrace_iTraceModel itrace_itracemodel;




    private iTrace_iTraceModel itrace_itracemodel;


    public iTrace_TraceLink(
        String fromFileName,        String comment,        String mode,        String ruleName,        String type,        String createdOn,        String technicalBinding,        String createdBy    ) {
        this.fromFileName = fromFileName;
        this.comment = comment;
        this.mode = mode;
        this.ruleName = ruleName;
        this.type = type;
        this.createdOn = createdOn;
        this.technicalBinding = technicalBinding;
        this.createdBy = createdBy;
    }


    public String getFromfilename() {
        return fromFileName;
    }

    public void setFromfilename(String fromFileName) {
        this.fromFileName = fromFileName;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }
    public String getRulename() {
        return ruleName;
    }

    public void setRulename(String ruleName) {
        this.ruleName = ruleName;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getCreatedon() {
        return createdOn;
    }

    public void setCreatedon(String createdOn) {
        this.createdOn = createdOn;
    }
    public String getTechnicalbinding() {
        return technicalBinding;
    }

    public void setTechnicalbinding(String technicalBinding) {
        this.technicalBinding = technicalBinding;
    }
    public String getCreatedby() {
        return createdBy;
    }

    public void setCreatedby(String createdBy) {
        this.createdBy = createdBy;
    }

    public iTrace_iTraceModel getItrace_itracemodel() {
        return itrace_itracemodel;
    }

    public void setItrace_itracemodel(iTrace_iTraceModel itrace_itracemodel) {
        this.itrace_itracemodel = itrace_itracemodel;
    }
    public iTrace_iTraceModel getItrace_itracemodel() {
        return itrace_itracemodel;
    }

    public void setItrace_itracemodel(iTrace_iTraceModel itrace_itracemodel) {
        this.itrace_itracemodel = itrace_itracemodel;
    }

}