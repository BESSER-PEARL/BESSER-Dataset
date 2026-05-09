





import java.util.List;
import java.util.ArrayList;

public class uma_Task extends ContentElement {

    private String mandatoryInput;
    private String toolMentor;
    private String estimate;
    private String group2;
    private String postcondition;
    private String performedBy;
    private String optionalInput;
    private String estimationConsiderations;
    private String output;
    private String additionallyPerformedBy;
    private String precondition;



    public uma_Task(
        String mandatoryInput,        String toolMentor,        String estimate,        String group2,        String postcondition,        String performedBy,        String optionalInput,        String estimationConsiderations,        String output,        String additionallyPerformedBy,        String precondition    ) {
        super(
        );
        this.mandatoryInput = mandatoryInput;
        this.toolMentor = toolMentor;
        this.estimate = estimate;
        this.group2 = group2;
        this.postcondition = postcondition;
        this.performedBy = performedBy;
        this.optionalInput = optionalInput;
        this.estimationConsiderations = estimationConsiderations;
        this.output = output;
        this.additionallyPerformedBy = additionallyPerformedBy;
        this.precondition = precondition;
    }


    public String getMandatoryinput() {
        return mandatoryInput;
    }

    public void setMandatoryinput(String mandatoryInput) {
        this.mandatoryInput = mandatoryInput;
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
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
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
    public String getOptionalinput() {
        return optionalInput;
    }

    public void setOptionalinput(String optionalInput) {
        this.optionalInput = optionalInput;
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
    public String getAdditionallyperformedby() {
        return additionallyPerformedBy;
    }

    public void setAdditionallyperformedby(String additionallyPerformedBy) {
        this.additionallyPerformedBy = additionallyPerformedBy;
    }
    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }


}