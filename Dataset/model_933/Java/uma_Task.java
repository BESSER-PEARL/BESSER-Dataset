





import java.util.List;
import java.util.ArrayList;

public class uma_Task extends ContentElement {

    private String group2;
    private String additionallyPerformedBy;
    private String mandatoryInput;
    private String precondition;
    private String estimationConsiderations;
    private String output;
    private String toolMentor;
    private String postcondition;
    private String performedBy;
    private String estimate;
    private String optionalInput;



    public uma_Task(
        String group2,        String additionallyPerformedBy,        String mandatoryInput,        String precondition,        String estimationConsiderations,        String output,        String toolMentor,        String postcondition,        String performedBy,        String estimate,        String optionalInput    ) {
        super(
        );
        this.group2 = group2;
        this.additionallyPerformedBy = additionallyPerformedBy;
        this.mandatoryInput = mandatoryInput;
        this.precondition = precondition;
        this.estimationConsiderations = estimationConsiderations;
        this.output = output;
        this.toolMentor = toolMentor;
        this.postcondition = postcondition;
        this.performedBy = performedBy;
        this.estimate = estimate;
        this.optionalInput = optionalInput;
    }


    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getAdditionallyperformedby() {
        return additionallyPerformedBy;
    }

    public void setAdditionallyperformedby(String additionallyPerformedBy) {
        this.additionallyPerformedBy = additionallyPerformedBy;
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
    public String getEstimationconsiderations() {
        return estimationConsiderations;
    }

    public void setEstimationconsiderations(String estimationConsiderations) {
        this.estimationConsiderations = estimationConsiderations;
    }
    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
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
    public String getPerformedby() {
        return performedBy;
    }

    public void setPerformedby(String performedBy) {
        this.performedBy = performedBy;
    }
    public String getEstimate() {
        return estimate;
    }

    public void setEstimate(String estimate) {
        this.estimate = estimate;
    }
    public String getOptionalinput() {
        return optionalInput;
    }

    public void setOptionalinput(String optionalInput) {
        this.optionalInput = optionalInput;
    }


}