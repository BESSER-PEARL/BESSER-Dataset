





import java.util.List;
import java.util.ArrayList;

public class uma_Task extends ContentElement {

    private String precondition;
    private String estimate;
    private String toolMentor;
    private String postcondition;
    private String estimationConsiderations;
    private String performedBy;
    private String optionalInput;
    private String mandatoryInput;
    private String additionallyPerformedBy;
    private String output;
    private String group2;



    public uma_Task(
        String precondition,        String estimate,        String toolMentor,        String postcondition,        String estimationConsiderations,        String performedBy,        String optionalInput,        String mandatoryInput,        String additionallyPerformedBy,        String output,        String group2    ) {
        super(
        );
        this.precondition = precondition;
        this.estimate = estimate;
        this.toolMentor = toolMentor;
        this.postcondition = postcondition;
        this.estimationConsiderations = estimationConsiderations;
        this.performedBy = performedBy;
        this.optionalInput = optionalInput;
        this.mandatoryInput = mandatoryInput;
        this.additionallyPerformedBy = additionallyPerformedBy;
        this.output = output;
        this.group2 = group2;
    }


    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }
    public String getEstimate() {
        return estimate;
    }

    public void setEstimate(String estimate) {
        this.estimate = estimate;
    }
    public String getToolmentor() {
        return toolMentor;
    }

    public void setToolmentor(String toolMentor) {
        this.toolMentor = toolMentor;
    }
    public String getPostcondition() {
        return postcondition;
    }

    public void setPostcondition(String postcondition) {
        this.postcondition = postcondition;
    }
    public String getEstimationconsiderations() {
        return estimationConsiderations;
    }

    public void setEstimationconsiderations(String estimationConsiderations) {
        this.estimationConsiderations = estimationConsiderations;
    }
    public String getPerformedby() {
        return performedBy;
    }

    public void setPerformedby(String performedBy) {
        this.performedBy = performedBy;
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
    public String getAdditionallyperformedby() {
        return additionallyPerformedBy;
    }

    public void setAdditionallyperformedby(String additionallyPerformedBy) {
        this.additionallyPerformedBy = additionallyPerformedBy;
    }
    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }


}