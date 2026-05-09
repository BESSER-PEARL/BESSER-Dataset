





import java.util.List;
import java.util.ArrayList;

public class uma_TaskDescriptor extends WorkBreakdownElement {

    private String isSynchronizedWithSource;
    private String additionallyPerformedBy;
    private String assistedBy;
    private String externalInput;
    private String performedPrimarilyBy;
    private String output;
    private String group3;
    private String task;
    private String optionalInput;
    private String mandatoryInput;





    private List<uma_Section> uma_sections;


    public uma_TaskDescriptor(
        String isSynchronizedWithSource,        String additionallyPerformedBy,        String assistedBy,        String externalInput,        String performedPrimarilyBy,        String output,        String group3,        String task,        String optionalInput,        String mandatoryInput    ) {
        super(
        );
        this.isSynchronizedWithSource = isSynchronizedWithSource;
        this.additionallyPerformedBy = additionallyPerformedBy;
        this.assistedBy = assistedBy;
        this.externalInput = externalInput;
        this.performedPrimarilyBy = performedPrimarilyBy;
        this.output = output;
        this.group3 = group3;
        this.task = task;
        this.optionalInput = optionalInput;
        this.mandatoryInput = mandatoryInput;
        this.uma_sections = new ArrayList<>();
    }

    public uma_TaskDescriptor(
        String isSynchronizedWithSource,        String additionallyPerformedBy,        String assistedBy,        String externalInput,        String performedPrimarilyBy,        String output,        String group3,        String task,        String optionalInput,        String mandatoryInput        ArrayList<uma_Section> uma_sections    ) {
        this.isSynchronizedWithSource = isSynchronizedWithSource;
        this.additionallyPerformedBy = additionallyPerformedBy;
        this.assistedBy = assistedBy;
        this.externalInput = externalInput;
        this.performedPrimarilyBy = performedPrimarilyBy;
        this.output = output;
        this.group3 = group3;
        this.task = task;
        this.optionalInput = optionalInput;
        this.mandatoryInput = mandatoryInput;
        this.uma_sections = uma_sections;
    }

    public String getIssynchronizedwithsource() {
        return isSynchronizedWithSource;
    }

    public void setIssynchronizedwithsource(String isSynchronizedWithSource) {
        this.isSynchronizedWithSource = isSynchronizedWithSource;
    }
    public String getAdditionallyperformedby() {
        return additionallyPerformedBy;
    }

    public void setAdditionallyperformedby(String additionallyPerformedBy) {
        this.additionallyPerformedBy = additionallyPerformedBy;
    }
    public String getAssistedby() {
        return assistedBy;
    }

    public void setAssistedby(String assistedBy) {
        this.assistedBy = assistedBy;
    }
    public String getExternalinput() {
        return externalInput;
    }

    public void setExternalinput(String externalInput) {
        this.externalInput = externalInput;
    }
    public String getPerformedprimarilyby() {
        return performedPrimarilyBy;
    }

    public void setPerformedprimarilyby(String performedPrimarilyBy) {
        this.performedPrimarilyBy = performedPrimarilyBy;
    }
    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }
    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }
    public String getTask() {
        return task;
    }

    public void setTask(String task) {
        this.task = task;
    }
    public String getOptionalinput() {
        return optionalInput;
    }

    public void setOptionalinput(String optionalInput) {
        this.optionalInput = optionalInput;
    }
    public String getMandatoryinput() {
        return mandatoryInput;
    }

    public void setMandatoryinput(String mandatoryInput) {
        this.mandatoryInput = mandatoryInput;
    }

    public List<uma_Section> getUma_sections() {
        return uma_sections;
    }

    public void addUma_section(Uma_section uma_section) {
        this.uma_sections.add(uma_section);
    }

}