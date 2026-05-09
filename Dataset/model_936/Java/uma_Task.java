





import java.util.List;
import java.util.ArrayList;

public class uma_Task extends ContentElement {

    private String group2;
    private String optionalInput;
    private String toolMentor;
    private String estimate;
    private String output;
    private String mandatoryInput;
    private String precondition;
    private String additionallyPerformedBy;
    private String postcondition;
    private String estimationConsiderations;
    private String performedBy;



    public uma_Task(
        String group2,        String optionalInput,        String toolMentor,        String estimate,        String output,        String mandatoryInput,        String precondition,        String additionallyPerformedBy,        String postcondition,        String estimationConsiderations,        String performedBy    ) {
        super(
        );
        this.group2 = group2;
        this.optionalInput = optionalInput;
        this.toolMentor = toolMentor;
        this.estimate = estimate;
        this.output = output;
        this.mandatoryInput = mandatoryInput;
        this.precondition = precondition;
        this.additionallyPerformedBy = additionallyPerformedBy;
        this.postcondition = postcondition;
        this.estimationConsiderations = estimationConsiderations;
        this.performedBy = performedBy;
    }


    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getOptionalinput() {
        return optionalInput;
    }

    public void setOptionalinput(String optionalInput) {
        this.optionalInput = optionalInput;
    }
    public String getToolmentor() {
        return toolMentor;
    }

    public void setToolmentor(String toolMentor) {
        this.toolMentor = toolMentor;
    }
    public String getEstimate() {
        return estimate;
    }

    public void setEstimate(String estimate) {
        this.estimate = estimate;
    }
    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }
    public String getMandatoryinput() {
        return mandatoryInput;
    }

    public void setMandatoryinput(String mandatoryInput) {
        this.mandatoryInput = mandatoryInput;
    }
    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }
    public String getAdditionallyperformedby() {
        return additionallyPerformedBy;
    }

    public void setAdditionallyperformedby(String additionallyPerformedBy) {
        this.additionallyPerformedBy = additionallyPerformedBy;
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


}