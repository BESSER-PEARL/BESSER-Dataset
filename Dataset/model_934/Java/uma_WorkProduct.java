





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProduct extends ContentElement {

    private String estimate;
    private String group2;
    private String report;
    private String estimationConsiderations;
    private String toolMentor;
    private String template;



    public uma_WorkProduct(
        String estimate,        String group2,        String report,        String estimationConsiderations,        String toolMentor,        String template    ) {
        super(
        );
        this.estimate = estimate;
        this.group2 = group2;
        this.report = report;
        this.estimationConsiderations = estimationConsiderations;
        this.toolMentor = toolMentor;
        this.template = template;
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
    public String getReport() {
        return report;
    }

    public void setReport(String report) {
        this.report = report;
    }
    public String getEstimationconsiderations() {
        return estimationConsiderations;
    }

    public void setEstimationconsiderations(String estimationConsiderations) {
        this.estimationConsiderations = estimationConsiderations;
    }
    public String getToolmentor() {
        return toolMentor;
    }

    public void setToolmentor(String toolMentor) {
        this.toolMentor = toolMentor;
    }
    public String getTemplate() {
        return template;
    }

    public void setTemplate(String template) {
        this.template = template;
    }


}