





import java.util.List;
import java.util.ArrayList;

public class uma_TaskDescriptor extends WorkBreakdownElement {

    private String task;
    private String isSynchronizedWithSource;
    private String output;
    private String assistedBy;
    private String optionalInput;
    private String group3;
    private String performedPrimarilyBy;
    private String externalInput;
    private String mandatoryInput;
    private String additionallyPerformedBy;





    private List<uma_Section> uma_sections;


    public uma_TaskDescriptor(
        String task,        String isSynchronizedWithSource,        String output,        String assistedBy,        String optionalInput,        String group3,        String performedPrimarilyBy,        String externalInput,        String mandatoryInput,        String additionallyPerformedBy    ) {
        super(
        );
        this.task = task;
        this.isSynchronizedWithSource = isSynchronizedWithSource;
        this.output = output;
        this.assistedBy = assistedBy;
        this.optionalInput = optionalInput;
        this.group3 = group3;
        this.performedPrimarilyBy = performedPrimarilyBy;
        this.externalInput = externalInput;
        this.mandatoryInput = mandatoryInput;
        this.additionallyPerformedBy = additionallyPerformedBy;
        this.uma_sections = new ArrayList<>();
    }

    public uma_TaskDescriptor(
        String task,        String isSynchronizedWithSource,        String output,        String assistedBy,        String optionalInput,        String group3,        String performedPrimarilyBy,        String externalInput,        String mandatoryInput,        String additionallyPerformedBy        ArrayList<uma_Section> uma_sections    ) {
        this.task = task;
        this.isSynchronizedWithSource = isSynchronizedWithSource;
        this.output = output;
        this.assistedBy = assistedBy;
        this.optionalInput = optionalInput;
        this.group3 = group3;
        this.performedPrimarilyBy = performedPrimarilyBy;
        this.externalInput = externalInput;
        this.mandatoryInput = mandatoryInput;
        this.additionallyPerformedBy = additionallyPerformedBy;
        this.uma_sections = uma_sections;
    }

    public String getTask() {
        return task;
    }

    public void setTask(String task) {
        this.task = task;
    }
    public String getIssynchronizedwithsource() {
        return isSynchronizedWithSource;
    }

    public void setIssynchronizedwithsource(String isSynchronizedWithSource) {
        this.isSynchronizedWithSource = isSynchronizedWithSource;
    }
    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }
    public String getAssistedby() {
        return assistedBy;
    }

    public void setAssistedby(String assistedBy) {
        this.assistedBy = assistedBy;
    }
    public String getOptionalinput() {
        return optionalInput;
    }

    public void setOptionalinput(String optionalInput) {
        this.optionalInput = optionalInput;
    }
    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }
    public String getPerformedprimarilyby() {
        return performedPrimarilyBy;
    }

    public void setPerformedprimarilyby(String performedPrimarilyBy) {
        this.performedPrimarilyBy = performedPrimarilyBy;
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
    public String getAdditionallyperformedby() {
        return additionallyPerformedBy;
    }

    public void setAdditionallyperformedby(String additionallyPerformedBy) {
        this.additionallyPerformedBy = additionallyPerformedBy;
    }

    public List<uma_Section> getUma_sections() {
        return uma_sections;
    }

    public void addUma_section(Uma_section uma_section) {
        this.uma_sections.add(uma_section);
    }

}