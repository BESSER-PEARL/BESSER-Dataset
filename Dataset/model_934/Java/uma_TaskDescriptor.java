





import java.util.List;
import java.util.ArrayList;

public class uma_TaskDescriptor extends WorkBreakdownElement {

    private String task;
    private String externalInput;
    private String mandatoryInput;
    private String output;
    private String performedPrimarilyBy;
    private String group3;
    private String additionallyPerformedBy;
    private String isSynchronizedWithSource;
    private String optionalInput;
    private String assistedBy;



    public uma_TaskDescriptor(
        String task,        String externalInput,        String mandatoryInput,        String output,        String performedPrimarilyBy,        String group3,        String additionallyPerformedBy,        String isSynchronizedWithSource,        String optionalInput,        String assistedBy    ) {
        super(
        );
        this.task = task;
        this.externalInput = externalInput;
        this.mandatoryInput = mandatoryInput;
        this.output = output;
        this.performedPrimarilyBy = performedPrimarilyBy;
        this.group3 = group3;
        this.additionallyPerformedBy = additionallyPerformedBy;
        this.isSynchronizedWithSource = isSynchronizedWithSource;
        this.optionalInput = optionalInput;
        this.assistedBy = assistedBy;
    }


    public String getTask() {
        return task;
    }

    public void setTask(String task) {
        this.task = task;
    }
    public String getExternalinput() {
        return externalInput;
    }

    public void setExternalinput(String externalInput) {
        this.externalInput = externalInput;
    }
    public String getMandatoryinput() {
        return mandatoryInput;
    }

    public void setMandatoryinput(String mandatoryInput) {
        this.mandatoryInput = mandatoryInput;
    }
    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }
    public String getPerformedprimarilyby() {
        return performedPrimarilyBy;
    }

    public void setPerformedprimarilyby(String performedPrimarilyBy) {
        this.performedPrimarilyBy = performedPrimarilyBy;
    }
    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }
    public String getAdditionallyperformedby() {
        return additionallyPerformedBy;
    }

    public void setAdditionallyperformedby(String additionallyPerformedBy) {
        this.additionallyPerformedBy = additionallyPerformedBy;
    }
    public String getIssynchronizedwithsource() {
        return isSynchronizedWithSource;
    }

    public void setIssynchronizedwithsource(String isSynchronizedWithSource) {
        this.isSynchronizedWithSource = isSynchronizedWithSource;
    }
    public String getOptionalinput() {
        return optionalInput;
    }

    public void setOptionalinput(String optionalInput) {
        this.optionalInput = optionalInput;
    }
    public String getAssistedby() {
        return assistedBy;
    }

    public void setAssistedby(String assistedBy) {
        this.assistedBy = assistedBy;
    }


}